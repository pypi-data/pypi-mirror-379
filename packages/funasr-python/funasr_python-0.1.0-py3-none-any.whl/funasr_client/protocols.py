"""WebSocket protocol implementation for FunASR communication."""

from __future__ import annotations

import asyncio
import json
import logging
import time
from typing import Any, AsyncIterator, Callable, Dict, Optional, Union

import websockets
from websockets.exceptions import ConnectionClosed, WebSocketException
from websockets.protocol import State as WebSocketState

from .errors import (
    ConnectionError,
    ConnectionLostError,
    ConnectionRefusedError,
    ConnectionTimeoutError,
    InvalidMessageFormatError,
    ProtocolError,
)
from .models import (
    ConnectionState,
    FunASREndMessage,
    FunASRError,
    FunASRInitMessage,
    FunASRResponse,
)


class WebSocketProtocol:
    """Handles WebSocket communication with FunASR server."""

    def __init__(
        self,
        server_url: str,
        timeout: float = 30.0,
        ping_interval: Optional[float] = None,
        ping_timeout: float = 10.0,
        close_timeout: float = 10.0,
        max_size: Optional[int] = 10 * 1024 * 1024,  # 10MB
        compression: Optional[str] = None,
        subprotocols: Optional[list[str]] = None,
    ) -> None:
        """Initialize WebSocket protocol.

        Args:
            server_url: WebSocket server URL
            timeout: Connection timeout in seconds
            ping_interval: Ping interval for keepalive (None to disable)
            ping_timeout: Timeout for ping response
            close_timeout: Timeout for connection close
            max_size: Maximum message size in bytes
            compression: Compression method ('deflate' or None)
        """
        self.server_url = server_url
        self.timeout = timeout
        self.ping_interval = ping_interval
        self.ping_timeout = ping_timeout
        self.close_timeout = close_timeout
        self.max_size = max_size
        self.compression = compression
        self.subprotocols = subprotocols or ["binary"]

        # websockets client protocol type
        self.websocket: Optional[websockets.WebSocketClientProtocol] = None
        self.state = ConnectionState.DISCONNECTED
        self.logger = logging.getLogger(__name__)

        # Connection metrics
        self.connection_start_time: Optional[float] = None
        self.last_ping_time: Optional[float] = None
        self.message_count = 0
        self.error_count = 0

    async def connect(self) -> None:
        """Establish WebSocket connection.

        Raises:
            ConnectionTimeoutError: If connection times out
            ConnectionRefusedError: If connection is refused
            ConnectionError: For other connection errors
        """
        if self.state != ConnectionState.DISCONNECTED:
            raise ConnectionError(f"Cannot connect from state: {self.state}")

        self.state = ConnectionState.CONNECTING
        self.connection_start_time = time.time()

        try:
            # Prepare connection parameters
            connect_kwargs = {
                "ping_interval": self.ping_interval,
                "ping_timeout": self.ping_timeout,
                "close_timeout": self.close_timeout,
                "max_size": self.max_size,
            }

            # Add compression if specified
            if self.compression:
                connect_kwargs["compression"] = self.compression

            # Add SSL context for secure connections
            if self.server_url.startswith("wss://"):
                import ssl

                ssl_context = ssl.create_default_context()
                # For development/testing, you might want to disable certificate verification
                # ssl_context.check_hostname = False
                # ssl_context.verify_mode = ssl.CERT_NONE
                connect_kwargs["ssl"] = ssl_context

            # Establish connection with timeout
            self.websocket = await asyncio.wait_for(
                websockets.connect(
                    self.server_url, subprotocols=self.subprotocols, **connect_kwargs
                ),
                timeout=self.timeout,
            )

            self.state = ConnectionState.CONNECTED
            self.logger.info(f"Connected to FunASR server: {self.server_url}")

        except asyncio.TimeoutError as e:
            self.state = ConnectionState.ERROR
            raise ConnectionTimeoutError(self.timeout) from e

        except ConnectionRefusedError as e:
            self.state = ConnectionState.ERROR
            raise ConnectionRefusedError(self.server_url) from e

        except (OSError, WebSocketException) as e:
            self.state = ConnectionState.ERROR
            raise ConnectionError(f"Failed to connect to {self.server_url}: {e}") from e

    async def disconnect(self) -> None:
        """Close WebSocket connection gracefully."""
        if self.websocket and self.websocket.state == WebSocketState.OPEN:
            try:
                await asyncio.wait_for(
                    self.websocket.close(),
                    timeout=self.close_timeout,
                )
            except asyncio.TimeoutError:
                self.logger.warning("WebSocket close timed out")
            except Exception as e:
                self.logger.warning(f"Error during WebSocket close: {e}")

        self.websocket = None
        self.state = ConnectionState.DISCONNECTED
        self.logger.info("Disconnected from FunASR server")

    async def send_init_message(self, init_message: FunASRInitMessage) -> None:
        """Send initialization message to server.

        Args:
            init_message: Initialization message

        Raises:
            ConnectionError: If not connected
            ProtocolError: If message cannot be sent
        """
        await self._send_json(init_message.model_dump())
        self.state = ConnectionState.RECOGNIZING

    async def send_audio_data(self, audio_data: bytes) -> None:
        """Send audio data to server.

        Args:
            audio_data: Raw audio data

        Raises:
            ConnectionError: If not connected
            ProtocolError: If data cannot be sent
        """
        await self._send_binary(audio_data)

    async def send_end_message(self) -> None:
        """Send end-of-speech message to server.

        Raises:
            ConnectionError: If not connected
            ProtocolError: If message cannot be sent
        """
        end_message = FunASREndMessage()
        await self._send_json(end_message.model_dump())
        self.state = ConnectionState.FINALIZING

    async def receive_messages(
        self,
        message_handler: Callable[[Union[FunASRResponse, FunASRError]], None],
    ) -> None:
        """Receive and process messages from server.

        Args:
            message_handler: Callback function to handle received messages

        Raises:
            ConnectionLostError: If connection is lost
            InvalidMessageFormatError: If message format is invalid
        """
        if not self.websocket:
            raise ConnectionError("Not connected to server")

        try:
            async for raw_message in self.websocket:
                try:
                    # Parse message
                    if isinstance(raw_message, str):
                        message_data = json.loads(raw_message)
                        message = self._parse_text_message(message_data)
                        if asyncio.iscoroutinefunction(message_handler):
                            await message_handler(message)
                        else:
                            message_handler(message)
                        self.message_count += 1
                    else:
                        # Binary messages are not expected from FunASR server
                        self.logger.warning(
                            f"Unexpected binary message: {len(raw_message)} bytes"
                        )

                except json.JSONDecodeError as e:
                    self.error_count += 1
                    error = InvalidMessageFormatError(raw_message)
                    self.logger.error(f"Invalid JSON message: {e}")
                    if asyncio.iscoroutinefunction(message_handler):
                        await message_handler(error)
                    else:
                        message_handler(error)

                except Exception as e:
                    self.error_count += 1
                    self.logger.error(f"Error processing message: {e}")

        except ConnectionClosed as e:
            self.state = ConnectionState.ERROR
            raise ConnectionLostError(f"WebSocket connection closed: {e}") from e

        except WebSocketException as e:
            self.state = ConnectionState.ERROR
            raise ConnectionLostError(f"WebSocket error: {e}") from e

    async def _send_json(self, data: Dict[str, Any]) -> None:
        """Send JSON message to server.

        Args:
            data: Data to send as JSON

        Raises:
            ConnectionError: If not connected
            ProtocolError: If message cannot be sent
        """
        if not self.is_connected:
            raise ConnectionError("WebSocket is not connected")

        try:
            message = json.dumps(data, ensure_ascii=False)
            await self.websocket.send(message)
            self.logger.debug(f"Sent JSON message: {message[:200]}...")

        except (ConnectionClosed, WebSocketException) as e:
            self.state = ConnectionState.ERROR
            raise ConnectionLostError(
                f"Connection lost while sending message: {e}"
            ) from e

        except Exception as e:
            raise ProtocolError(f"Failed to send JSON message: {e}") from e

    async def _send_binary(self, data: bytes) -> None:
        """Send binary message to server.

        Args:
            data: Binary data to send

        Raises:
            ConnectionError: If not connected
            ProtocolError: If data cannot be sent
        """
        if not self.is_connected:
            raise ConnectionError("WebSocket is not connected")

        try:
            await self.websocket.send(data)
            self.logger.debug(f"Sent binary data: {len(data)} bytes")

        except (ConnectionClosed, WebSocketException) as e:
            self.state = ConnectionState.ERROR
            raise ConnectionLostError(f"Connection lost while sending data: {e}") from e

        except Exception as e:
            raise ProtocolError(f"Failed to send binary data: {e}") from e

    def _parse_text_message(
        self, message_data: Dict[str, Any]
    ) -> Union[FunASRResponse, FunASRError]:
        """Parse text message from server.

        Args:
            message_data: Raw message data

        Returns:
            Parsed message object

        Raises:
            InvalidMessageFormatError: If message format is invalid
        """
        try:
            # Check if this is an error message
            if "error" in message_data:
                return FunASRError(**message_data)

            # Parse as response message
            return FunASRResponse(**message_data)

        except Exception as e:
            raise InvalidMessageFormatError(json.dumps(message_data)) from e

    @property
    def is_connected(self) -> bool:
        """Check if WebSocket is connected."""
        return (
            self.websocket is not None and self.websocket.state == WebSocketState.OPEN
        )

    @property
    def connection_time(self) -> float:
        """Get connection duration in seconds."""
        if self.connection_start_time is None:
            return 0.0
        return time.time() - self.connection_start_time

    def get_connection_stats(self) -> Dict[str, Any]:
        """Get connection statistics.

        Returns:
            Dictionary with connection statistics
        """
        return {
            "state": self.state.value,
            "server_url": self.server_url,
            "connection_time": self.connection_time,
            "message_count": self.message_count,
            "error_count": self.error_count,
            "is_connected": self.is_connected,
            "last_ping_time": self.last_ping_time,
        }


class StreamingProtocol(WebSocketProtocol):
    """Enhanced protocol for streaming audio recognition."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize streaming protocol."""
        super().__init__(*args, **kwargs)
        self._audio_queue: Optional[asyncio.Queue] = None
        self._streaming_task: Optional[asyncio.Task] = None
        self._background_tasks: set = set()

    async def start_streaming(
        self,
        init_message: FunASRInitMessage,
        audio_stream: AsyncIterator[bytes],
        message_handler: Callable[[Union[FunASRResponse, FunASRError]], None],
    ) -> None:
        """Start streaming audio recognition.

        Args:
            init_message: Initialization message
            audio_stream: Async iterator of audio data
            message_handler: Callback for received messages

        Raises:
            ConnectionError: If not connected
        """
        if self.state != ConnectionState.CONNECTED:
            raise ConnectionError(f"Cannot start streaming from state: {self.state}")

        # Send initialization message
        await self.send_init_message(init_message)

        final_event = asyncio.Event()

        async def _wrapped_handler(msg: Union[FunASRResponse, FunASRError]):
            try:
                if isinstance(msg, FunASRResponse) and msg.is_final:
                    final_event.set()
                # Use non-blocking callback execution to prevent message loop blocking
                if asyncio.iscoroutinefunction(message_handler):
                    # Execute callback asynchronously without blocking message processing
                    task = asyncio.create_task(message_handler(msg))
                    self._background_tasks.add(task)
                    task.add_done_callback(self._background_tasks.discard)
                else:
                    message_handler(msg)
                    message_handler(msg)
            except Exception:
                # Do not break receiving loop on handler error
                self.logger.exception("Error in message handler")

        receive_task = asyncio.create_task(self.receive_messages(_wrapped_handler))
        send_task = asyncio.create_task(self._stream_audio(audio_stream))

        try:
            # Wait until all audio sent
            await send_task
            # For offline and 2pass scenarios, wait for final or timeout
            try:
                await asyncio.wait_for(final_event.wait(), timeout=self.timeout)
            except asyncio.TimeoutError:
                # It's acceptable if server doesn't send explicit final in some modes
                self.logger.debug("Final event wait timed out")
        finally:
            if not receive_task.done():
                receive_task.cancel()
                import contextlib

                with contextlib.suppress(asyncio.CancelledError):
                    await receive_task

    async def _stream_audio(self, audio_stream: AsyncIterator[bytes]) -> None:
        """Stream audio data to server.

        Args:
            audio_stream: Async iterator of audio data
        """
        try:
            async for audio_chunk in audio_stream:
                # Check connection before sending each chunk
                if not self.is_connected:
                    raise ConnectionLostError("Connection lost during audio streaming")

                await self.send_audio_data(audio_chunk)
                # Small delay to prevent overwhelming the server
                await asyncio.sleep(0.001)

            # Send end-of-speech message
            if self.is_connected:
                await self.send_end_message()

        except (ConnectionClosed, ConnectionLostError) as e:
            self.state = ConnectionState.ERROR
            self.logger.error(f"Connection lost while streaming audio: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Error streaming audio: {e}")
            raise


class ReconnectingProtocol:
    """WebSocket protocol with automatic reconnection capability."""

    def __init__(
        self,
        server_url: str,
        max_retries: int = 5,
        base_delay: float = 1.0,
        max_delay: float = 60.0,
        backoff_multiplier: float = 2.0,
        **protocol_kwargs,
    ) -> None:
        """Initialize reconnecting protocol.

        Args:
            server_url: WebSocket server URL
            max_retries: Maximum number of reconnection attempts
            base_delay: Base delay between reconnection attempts
            max_delay: Maximum delay between attempts
            backoff_multiplier: Backoff multiplier for exponential backoff
            **protocol_kwargs: Additional arguments for WebSocketProtocol
        """
        self.server_url = server_url
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.backoff_multiplier = backoff_multiplier
        self.protocol_kwargs = protocol_kwargs

        self.protocol: Optional[WebSocketProtocol] = None
        self.reconnect_attempts = 0
        self.logger = logging.getLogger(__name__)

    async def connect(self) -> WebSocketProtocol:
        """Connect with automatic reconnection.

        Returns:
            Connected WebSocket protocol instance

        Raises:
            ConnectionError: If all reconnection attempts fail
        """
        for attempt in range(self.max_retries + 1):
            try:
                self.protocol = WebSocketProtocol(
                    self.server_url, **self.protocol_kwargs
                )
                await self.protocol.connect()
                self.reconnect_attempts = 0
                return self.protocol

            except Exception as e:
                self.reconnect_attempts = attempt + 1
                self.logger.warning(
                    f"Connection attempt {attempt + 1}/{self.max_retries + 1} failed: {e}"
                )

                if attempt < self.max_retries:
                    # Calculate delay with exponential backoff
                    delay = min(
                        self.base_delay * (self.backoff_multiplier**attempt),
                        self.max_delay,
                    )

                    # Add jitter to avoid thundering herd
                    import random

                    jitter = random.uniform(0.8, 1.2)
                    delay *= jitter

                    self.logger.info(f"Retrying connection in {delay:.2f} seconds...")
                    await asyncio.sleep(delay)
                else:
                    raise ConnectionError(
                        f"Failed to connect after {self.max_retries + 1} attempts: {e}"
                    ) from e

        # This should never be reached, but satisfy type checker
        raise ConnectionError("Unexpected error in connection loop")

    async def disconnect(self) -> None:
        """Disconnect from server."""
        if self.protocol:
            await self.protocol.disconnect()
            self.protocol = None

    def get_reconnection_stats(self) -> Dict[str, Any]:
        """Get reconnection statistics.

        Returns:
            Dictionary with reconnection statistics
        """
        stats = {
            "reconnect_attempts": self.reconnect_attempts,
            "max_retries": self.max_retries,
        }

        if self.protocol:
            stats.update(self.protocol.get_connection_stats())

        return stats
