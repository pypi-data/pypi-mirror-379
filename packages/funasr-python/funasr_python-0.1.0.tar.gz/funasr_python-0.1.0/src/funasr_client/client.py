"""Main FunASR client classes."""

from __future__ import annotations

import asyncio
import contextlib
import logging
from pathlib import Path
import time
from typing import Any, AsyncIterator, Dict, Iterator, List, Optional, Union
import uuid

from .audio import AudioFileStreamer, AudioProcessor, AudioRecorder
from .callbacks import AsyncRecognitionCallback, CallbackAdapter, RecognitionCallback
from .config import config_manager
from .connection import Connection, ConnectionManager
from .errors import (
    ConnectionError,
    FunASRError,
    map_server_error,
)
from .models import (
    ClientConfig,
    ConnectionMetrics,
    FinalResult,
    FunASRResponse,
    PartialResult,
    RealtimeSession,
    RecognitionMode,
)
from .models import (
    FunASRError as FunASRErrorModel,
)
from .protocols import StreamingProtocol


class FunASRClient:
    """Synchronous FunASR client for speech recognition."""

    def __init__(
        self,
        server_url: Optional[str] = None,
        config: Optional[Union[ClientConfig, Dict[str, Any], str, Path]] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize FunASR client.

        Args:
            server_url: WebSocket server URL (overrides config)
            config: Client configuration
            **kwargs: Additional configuration overrides

        Raises:
            InvalidConfigurationError: If configuration is invalid
        """
        # Load and validate configuration
        self.config = config_manager.load_config(config, **kwargs)
        if server_url:
            self.config.server_url = server_url

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(getattr(logging, self.config.log_level))

        # Initialize components
        self.audio_processor = AudioProcessor(self.config.audio)
        self._connection: Optional[Connection] = None
        self._session_id: Optional[str] = None

        # Metrics
        self.metrics = ConnectionMetrics()

    def recognize_file(
        self,
        audio_path: Union[str, Path],
        callback: Optional[RecognitionCallback] = None,
    ) -> FinalResult:
        """Recognize audio file synchronously.

        Args:
            audio_path: Path to audio file
            callback: Optional callback for receiving intermediate results

        Returns:
            Final recognition result

        Raises:
            AudioError: If audio file processing fails
            ConnectionError: If connection fails
            FunASRError: If recognition fails
        """
        return asyncio.run(self._recognize_file_async(audio_path, callback))

    def recognize_stream(
        self,
        audio_stream: Iterator[bytes],
        callback: RecognitionCallback,
    ) -> None:
        """Recognize audio stream synchronously.

        Args:
            audio_stream: Iterator of audio data chunks
            callback: Callback for receiving results

        Raises:
            AudioError: If audio processing fails
            ConnectionError: If connection fails
            FunASRError: If recognition fails
        """
        asyncio.run(self._recognize_stream_async(audio_stream, callback))

    def start_realtime(self, callback: RecognitionCallback) -> RealtimeSession:
        """Start real-time speech recognition synchronously.

        Args:
            callback: Callback for receiving results

        Returns:
            Real-time session object

        Raises:
            AudioError: If microphone access fails
            ConnectionError: If connection fails
        """
        return asyncio.run(self._start_realtime_async(callback))

    async def _recognize_file_async(
        self,
        audio_path: Union[str, Path],
        callback: Optional[RecognitionCallback],
    ) -> FinalResult:
        """Recognize audio file asynchronously."""
        async_client = AsyncFunASRClient(config=self.config)
        try:
            if callback:
                return await async_client.recognize_file(
                    audio_path, CallbackAdapter(callback)
                )
            else:
                return await async_client.recognize_file(audio_path)
        finally:
            await async_client.close()

    async def _recognize_stream_async(
        self,
        audio_stream: Iterator[bytes],
        callback: RecognitionCallback,
    ) -> None:
        """Recognize audio stream asynchronously."""
        async_client = AsyncFunASRClient(config=self.config)
        try:
            # Convert sync iterator to async iterator
            async def async_stream():
                for chunk in audio_stream:
                    yield chunk

            await async_client.recognize_stream(
                async_stream(), CallbackAdapter(callback)
            )
        finally:
            await async_client.close()

    async def _start_realtime_async(
        self, callback: RecognitionCallback
    ) -> RealtimeSession:
        """Start real-time recognition asynchronously."""
        async_client = AsyncFunASRClient(config=self.config)
        # Note: This is a simplified version - real implementation would need
        # to handle the lifecycle of the async client properly
        return await async_client.start_realtime(CallbackAdapter(callback))

    def close(self) -> None:
        """Close the client and clean up resources."""
        # Sync client doesn't maintain persistent connections, so nothing to close

    def get_stats(self) -> Dict[str, Any]:
        """Get client statistics.

        Returns:
            Dictionary with client statistics
        """
        return {
            "config": {
                "server_url": self.config.server_url,
                "mode": self.config.mode.value,
                "sample_rate": self.config.audio.sample_rate,
            },
            "metrics": {
                "total_files_processed": 0,  # Would track in real implementation
                "total_duration_processed": 0.0,
                "average_processing_time": 0.0,
            },
        }


class AsyncFunASRClient:
    """Asynchronous FunASR client for speech recognition."""

    def __init__(
        self,
        server_url: Optional[str] = None,
        config: Optional[Union[ClientConfig, Dict[str, Any], str, Path]] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize async FunASR client.

        Args:
            server_url: WebSocket server URL (overrides config)
            config: Client configuration
            **kwargs: Additional configuration overrides

        Raises:
            InvalidConfigurationError: If configuration is invalid
        """
        # Load and validate configuration
        self.config = config_manager.load_config(config, **kwargs)
        if server_url:
            self.config.server_url = server_url

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(getattr(logging, self.config.log_level))

        # Initialize components
        self.audio_processor = AudioProcessor(self.config.audio)
        self.connection_manager = ConnectionManager(self.config)

        # Session management
        self.active_sessions: Dict[str, RealtimeSession] = {}
        self._is_started = False

        # Metrics
        self.metrics = ConnectionMetrics()

    async def start(self) -> None:
        """Start the async client."""
        if not self._is_started:
            await self.connection_manager.start()
            self._is_started = True
            self.logger.info("AsyncFunASRClient started")

    async def close(self) -> None:
        """Close the client and clean up resources."""
        if self._is_started:
            # End all active sessions
            for session in list(self.active_sessions.values()):
                session.end_session()

            # Close connection manager
            await self.connection_manager.stop()
            self._is_started = False
            self.logger.info("AsyncFunASRClient closed")

    async def recognize_file(
        self,
        audio_path: Union[str, Path],
        callback: Optional[Union[RecognitionCallback, AsyncRecognitionCallback]] = None,
    ) -> FinalResult:
        """Recognize audio file asynchronously.

        Args:
            audio_path: Path to audio file
            callback: Optional callback for receiving intermediate results

        Returns:
            Final recognition result

        Raises:
            AudioError: If audio file processing fails
            ConnectionError: If connection fails
            FunASRError: If recognition fails
        """
        if not self._is_started:
            await self.start()

        session_id = str(uuid.uuid4())
        start_time = time.time()

        try:
            # Create audio streamer
            streamer = AudioFileStreamer(
                audio_path,
                chunk_duration=self.config.chunk_interval
                / 1000,  # Convert ms to seconds
                target_config=self.config.audio,
            )

            # Stream the file
            final_result = None
            adapter = CallbackAdapter(callback) if callback else None

            async def result_handler(
                result: Union[PartialResult, FinalResult, FunASRError],
            ):
                nonlocal final_result
                if isinstance(result, FinalResult):
                    final_result = result
                    if adapter:
                        await adapter.call_final_result(result)
                elif isinstance(result, PartialResult) and adapter:
                    await adapter.call_partial_result(result)
                elif isinstance(result, FunASRError) and adapter:
                    await adapter.call_error(result)

            await self._recognize_stream_internal(
                session_id,
                streamer.stream_audio(),
                result_handler,
            )

            if final_result is None:
                raise FunASRError("No final result received")

            # Update metrics
            processing_time = time.time() - start_time
            self.metrics.total_processing_time += processing_time
            self.metrics.message_count += 1

            return final_result

        except Exception as e:
            self.metrics.error_count += 1
            if isinstance(e, FunASRError):
                raise
            raise FunASRError(f"File recognition failed: {e}") from e

    async def recognize_stream(
        self,
        audio_stream: AsyncIterator[bytes],
        callback: Union[RecognitionCallback, AsyncRecognitionCallback],
    ) -> None:
        """Recognize audio stream asynchronously.

        Args:
            audio_stream: Async iterator of audio data chunks
            callback: Callback for receiving results

        Raises:
            AudioError: If audio processing fails
            ConnectionError: If connection fails
            FunASRError: If recognition fails
        """
        if not self._is_started:
            await self.start()

        session_id = str(uuid.uuid4())
        adapter = CallbackAdapter(callback)

        async def result_handler(
            result: Union[PartialResult, FinalResult, FunASRError],
        ):
            if isinstance(result, PartialResult):
                await adapter.call_partial_result(result)
            elif isinstance(result, FinalResult):
                await adapter.call_final_result(result)
            elif isinstance(result, FunASRError):
                await adapter.call_error(result)

        await self._recognize_stream_internal(session_id, audio_stream, result_handler)

    async def start_realtime(
        self,
        callback: Union[RecognitionCallback, AsyncRecognitionCallback],
    ) -> RealtimeSession:
        """Start real-time speech recognition.

        Args:
            callback: Callback for receiving results

        Returns:
            Real-time session object

        Raises:
            AudioError: If microphone access fails
            ConnectionError: If connection fails
        """
        if not self._is_started:
            await self.start()

        session_id = str(uuid.uuid4())
        session = RealtimeSession(session_id=session_id)
        self.active_sessions[session_id] = session

        try:
            # Start audio recording
            recorder = AudioRecorder(
                audio_config=self.config.audio,
                chunk_duration=self.config.chunk_interval / 1000,
            )

            adapter = CallbackAdapter(callback)

            async def result_handler(
                result: Union[PartialResult, FinalResult, FunASRError],
            ):
                if isinstance(result, PartialResult):
                    await adapter.call_partial_result(result)
                elif isinstance(result, FinalResult):
                    await adapter.call_final_result(result)
                elif isinstance(result, FunASRError):
                    await adapter.call_error(result)

            # Start recognition with microphone stream
            recognition_task = asyncio.create_task(
                self._recognize_stream_internal(
                    session_id,
                    recorder.start_recording(),
                    result_handler,
                )
            )

            # Store the task for cleanup
            session.recognition_task = recognition_task  # type: ignore

            return session

        except Exception as e:
            # Clean up session on error
            self.active_sessions.pop(session_id, None)
            session.end_session()
            raise FunASRError(f"Failed to start real-time recognition: {e}") from e

    async def end_realtime_session(self, session: RealtimeSession) -> None:
        """End a real-time recognition session.

        Args:
            session: Session to end
        """
        session_id = session.session_id
        if session_id in self.active_sessions:
            session.end_session()
            del self.active_sessions[session_id]

            # Cancel recognition task if exists
            if hasattr(session, "recognition_task"):
                task = session.recognition_task
                if not task.done():
                    task.cancel()
                    with contextlib.suppress(asyncio.CancelledError):
                        await task

            self.logger.info(f"Ended real-time session {session_id}")

    async def _recognize_stream_internal(
        self,
        session_id: str,
        audio_stream: AsyncIterator[bytes],
        result_handler: Any,
    ) -> None:
        """Internal method for stream recognition."""
        connection = None
        try:
            # Acquire connection
            connection = await self.connection_manager.acquire_connection(session_id)

            # Create streaming protocol
            protocol = StreamingProtocol(
                self.config.server_url,
                timeout=self.config.timeout,
            )

            # Initialize protocol connection (reuse existing connection)
            protocol.websocket = connection.protocol.websocket
            protocol.state = connection.protocol.state

            # Prepare initialization message
            init_message = self.config.to_init_message(session_id)

            # Set up message handler
            results: List[Union[PartialResult, FinalResult]] = []
            final_received = False

            async def message_handler(message):
                nonlocal final_received
                try:
                    if isinstance(message, FunASRErrorModel):
                        error = map_server_error(message.error)
                        await result_handler(error)
                        return

                    if isinstance(message, FunASRResponse):
                        # Convert to appropriate result type
                        if message.is_final:
                            result = FinalResult(
                                text=self._clean_text(message.text),
                                confidence=message.confidence or 0.0,
                                timestamp=time.time(),
                                is_final=True,
                                session_id=session_id,
                                alternatives=[],  # Could parse from response
                            )
                            results.append(result)
                            await result_handler(result)
                            final_received = True
                        else:
                            result = PartialResult(
                                text=self._clean_text(message.text),
                                confidence=message.confidence or 0.0,
                                timestamp=time.time(),
                                is_final=False,
                                session_id=session_id,
                                start_time=0.0,  # Could parse from timestamp
                                end_time=0.0,
                            )
                            results.append(result)
                            await result_handler(result)

                except Exception as e:
                    error = FunASRError(f"Error processing server message: {e}")
                    await result_handler(error)

            # Start streaming recognition
            await protocol.start_streaming(init_message, audio_stream, message_handler)

            # Wait for final result in non-offline modes
            if self.config.mode != RecognitionMode.OFFLINE:
                timeout = self.config.timeout
                start_wait = time.time()
                while not final_received and (time.time() - start_wait) < timeout:
                    await asyncio.sleep(0.1)

        except Exception as e:
            if isinstance(e, FunASRError):
                raise
            raise ConnectionError(f"Stream recognition failed: {e}") from e

        finally:
            # Release connection
            if connection:
                await self.connection_manager.release_connection(connection, session_id)

    def _clean_text(self, text: str) -> str:
        """Clean recognition text by removing language tags and special markers.

        Args:
            text: Raw text from server

        Returns:
            Cleaned text
        """
        if not text:
            return ""

        # Remove language tags like <|zh|>, <|en|>
        import re

        text = re.sub(r"<\|[^|]+\|>", "", text)

        # Remove other special markers
        text = re.sub(r"<[^>]*>", "", text)

        # Clean up whitespace
        text = text.strip()

        return text

    async def get_connection_stats(self) -> Dict[str, Any]:
        """Get connection statistics.

        Returns:
            Dictionary with connection statistics
        """
        stats = self.connection_manager.get_stats()
        stats.update(
            {
                "client": {
                    "active_sessions": len(self.active_sessions),
                    "is_started": self._is_started,
                    "metrics": {
                        "connection_time": self.metrics.connection_time,
                        "message_count": self.metrics.message_count,
                        "error_count": self.metrics.error_count,
                        "total_processing_time": self.metrics.total_processing_time,
                        "real_time_factor": self.metrics.real_time_factor,
                    },
                }
            }
        )
        return stats

    def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()


# Convenience functions for quick usage
def recognize_file(
    audio_path: Union[str, Path],
    server_url: str = "ws://localhost:10095",
    **config_kwargs,
) -> str:
    """Recognize audio file with minimal configuration.

    Args:
        audio_path: Path to audio file
        server_url: FunASR server URL
        **config_kwargs: Additional configuration options

    Returns:
        Recognition text

    Raises:
        FunASRError: If recognition fails
    """
    client = FunASRClient(server_url=server_url, **config_kwargs)
    try:
        result = client.recognize_file(audio_path)
        return result.text
    finally:
        client.close()


async def recognize_file_async(
    audio_path: Union[str, Path],
    server_url: str = "ws://localhost:10095",
    **config_kwargs,
) -> str:
    """Recognize audio file asynchronously with minimal configuration.

    Args:
        audio_path: Path to audio file
        server_url: FunASR server URL
        **config_kwargs: Additional configuration options

    Returns:
        Recognition text

    Raises:
        FunASRError: If recognition fails
    """
    async with AsyncFunASRClient(server_url=server_url, **config_kwargs) as client:
        result = await client.recognize_file(audio_path)
        return result.text


def create_client(
    server_url: Optional[str] = None,
    preset: Optional[str] = None,
    **config_kwargs,
) -> FunASRClient:
    """Create a FunASR client with preset configuration.

    Args:
        server_url: WebSocket server URL
        preset: Configuration preset ('low_latency', 'high_accuracy', 'balanced')
        **config_kwargs: Additional configuration overrides

    Returns:
        Configured FunASR client

    Raises:
        InvalidConfigurationError: If configuration is invalid
    """
    # Extract config from kwargs if present to avoid parameter conflicts
    base_config = config_kwargs.pop("config", None)

    if preset:
        config = config_manager.get_preset(preset, **config_kwargs)
    else:
        config = config_manager.load_config(base_config, **config_kwargs)

    if server_url:
        config.server_url = server_url

    return FunASRClient(config=config)


def create_async_client(
    server_url: Optional[str] = None,
    preset: Optional[str] = None,
    **config_kwargs,
) -> AsyncFunASRClient:
    """Create an async FunASR client with preset configuration.

    Args:
        server_url: WebSocket server URL
        preset: Configuration preset ('low_latency', 'high_accuracy', 'balanced')
        **config_kwargs: Additional configuration overrides

    Returns:
        Configured async FunASR client

    Raises:
        InvalidConfigurationError: If configuration is invalid
    """
    # Extract config from kwargs if present to avoid parameter conflicts
    base_config = config_kwargs.pop("config", None)

    if preset:
        config = config_manager.get_preset(preset, **config_kwargs)
    else:
        config = config_manager.load_config(base_config, **config_kwargs)

    if server_url:
        config.server_url = server_url

    return AsyncFunASRClient(config=config)
