"""Callback interfaces for FunASR client."""

from __future__ import annotations

from abc import ABC, abstractmethod
import asyncio
from typing import Any, Awaitable, Callable, List, Optional, Union

from .errors import FunASRError
from .models import (
    ConnectionState,
    FinalResult,
    PartialResult,
    SentenceResult,
)


class RecognitionCallback(ABC):
    """Abstract base class for recognition result callbacks."""

    @abstractmethod
    def on_partial_result(self, result: PartialResult) -> None:
        """Handle partial recognition result (streaming).

        Args:
            result: Partial recognition result with temporary text and timing
        """

    @abstractmethod
    def on_final_result(self, result: FinalResult) -> None:
        """Handle final recognition result (2-pass optimized).

        Args:
            result: Final recognition result with optimized text and confidence
        """

    @abstractmethod
    def on_sentence_end(self, result: SentenceResult) -> None:
        """Handle sentence completion event.

        Args:
            result: Complete sentence recognition result with word-level details
        """

    @abstractmethod
    def on_error(self, error: FunASRError) -> None:
        """Handle recognition error.

        Args:
            error: Error that occurred during recognition
        """

    @abstractmethod
    def on_connection_status(self, status: ConnectionState) -> None:
        """Handle connection status change.

        Args:
            status: New connection status
        """


class AsyncRecognitionCallback(ABC):
    """Abstract base class for async recognition result callbacks."""

    @abstractmethod
    async def on_partial_result(self, result: PartialResult) -> None:
        """Handle partial recognition result (streaming).

        Args:
            result: Partial recognition result with temporary text and timing
        """

    @abstractmethod
    async def on_final_result(self, result: FinalResult) -> None:
        """Handle final recognition result (2-pass optimized).

        Args:
            result: Final recognition result with optimized text and confidence
        """

    @abstractmethod
    async def on_sentence_end(self, result: SentenceResult) -> None:
        """Handle sentence completion event.

        Args:
            result: Complete sentence recognition result with word-level details
        """

    @abstractmethod
    async def on_error(self, error: FunASRError) -> None:
        """Handle recognition error.

        Args:
            error: Error that occurred during recognition
        """

    @abstractmethod
    async def on_connection_status(self, status: ConnectionState) -> None:
        """Handle connection status change.

        Args:
            status: New connection status
        """


# Type aliases for functional callbacks
PartialResultCallback = Callable[[PartialResult], None]
FinalResultCallback = Callable[[FinalResult], None]
SentenceEndCallback = Callable[[SentenceResult], None]
ErrorCallback = Callable[[FunASRError], None]
ConnectionStatusCallback = Callable[[ConnectionState], None]

# Async versions
AsyncPartialResultCallback = Callable[[PartialResult], Awaitable[None]]
AsyncFinalResultCallback = Callable[[FinalResult], Awaitable[None]]
AsyncSentenceEndCallback = Callable[[SentenceResult], Awaitable[None]]
AsyncErrorCallback = Callable[[FunASRError], Awaitable[None]]
AsyncConnectionStatusCallback = Callable[[ConnectionState], Awaitable[None]]


class SimpleCallback(RecognitionCallback):
    """Simple callback implementation using functional callbacks."""

    def __init__(
        self,
        on_partial: Optional[PartialResultCallback] = None,
        on_final: Optional[FinalResultCallback] = None,
        on_sentence: Optional[SentenceEndCallback] = None,
        on_error: Optional[ErrorCallback] = None,
        on_status: Optional[ConnectionStatusCallback] = None,
    ) -> None:
        """Initialize simple callback.

        Args:
            on_partial: Callback for partial results
            on_final: Callback for final results
            on_sentence: Callback for sentence completion
            on_error: Callback for errors
            on_status: Callback for connection status changes
        """
        self._on_partial = on_partial
        self._on_final = on_final
        self._on_sentence = on_sentence
        self._on_error = on_error
        self._on_status = on_status

    def on_partial_result(self, result: PartialResult) -> None:
        """Handle partial recognition result."""
        if self._on_partial:
            self._on_partial(result)

    def on_final_result(self, result: FinalResult) -> None:
        """Handle final recognition result."""
        if self._on_final:
            self._on_final(result)

    def on_sentence_end(self, result: SentenceResult) -> None:
        """Handle sentence completion event."""
        if self._on_sentence:
            self._on_sentence(result)

    def on_error(self, error: FunASRError) -> None:
        """Handle recognition error."""
        if self._on_error:
            self._on_error(error)

    def on_connection_status(self, status: ConnectionState) -> None:
        """Handle connection status change."""
        if self._on_status:
            self._on_status(status)


class AsyncSimpleCallback(AsyncRecognitionCallback):
    """Simple async callback implementation using functional callbacks."""

    def __init__(
        self,
        on_partial: Optional[AsyncPartialResultCallback] = None,
        on_final: Optional[AsyncFinalResultCallback] = None,
        on_sentence: Optional[AsyncSentenceEndCallback] = None,
        on_error: Optional[AsyncErrorCallback] = None,
        on_status: Optional[AsyncConnectionStatusCallback] = None,
    ) -> None:
        """Initialize async simple callback.

        Args:
            on_partial: Async callback for partial results
            on_final: Async callback for final results
            on_sentence: Async callback for sentence completion
            on_error: Async callback for errors
            on_status: Async callback for connection status changes
        """
        self._on_partial = on_partial
        self._on_final = on_final
        self._on_sentence = on_sentence
        self._on_error = on_error
        self._on_status = on_status

    async def on_partial_result(self, result: PartialResult) -> None:
        """Handle partial recognition result."""
        if self._on_partial:
            await self._on_partial(result)

    async def on_final_result(self, result: FinalResult) -> None:
        """Handle final recognition result."""
        if self._on_final:
            await self._on_final(result)

    async def on_sentence_end(self, result: SentenceResult) -> None:
        """Handle sentence completion event."""
        if self._on_sentence:
            await self._on_sentence(result)

    async def on_error(self, error: FunASRError) -> None:
        """Handle recognition error."""
        if self._on_error:
            await self._on_error(error)

    async def on_connection_status(self, status: ConnectionState) -> None:
        """Handle connection status change."""
        if self._on_status:
            await self._on_status(status)


class CallbackAdapter:
    """Adapts between sync and async callbacks."""

    def __init__(
        self, callback: Union[RecognitionCallback, AsyncRecognitionCallback]
    ) -> None:
        """Initialize callback adapter.

        Args:
            callback: Callback instance to adapt
        """
        self.callback = callback
        self.is_async = isinstance(callback, AsyncRecognitionCallback)

    async def call_partial_result(self, result: PartialResult) -> None:
        """Call partial result callback."""
        if self.is_async:
            await self.callback.on_partial_result(result)  # type: ignore
        else:
            self.callback.on_partial_result(result)  # type: ignore

    async def call_final_result(self, result: FinalResult) -> None:
        """Call final result callback."""
        if self.is_async:
            await self.callback.on_final_result(result)  # type: ignore
        else:
            self.callback.on_final_result(result)  # type: ignore

    async def call_sentence_end(self, result: SentenceResult) -> None:
        """Call sentence end callback."""
        if self.is_async:
            await self.callback.on_sentence_end(result)  # type: ignore
        else:
            self.callback.on_sentence_end(result)  # type: ignore

    async def call_error(self, error: FunASRError) -> None:
        """Call error callback."""
        if self.is_async:
            await self.callback.on_error(error)  # type: ignore
        else:
            self.callback.on_error(error)  # type: ignore

    async def call_connection_status(self, status: ConnectionState) -> None:
        """Call connection status callback."""
        if self.is_async:
            await self.callback.on_connection_status(status)  # type: ignore
        else:
            self.callback.on_connection_status(status)  # type: ignore


class LoggingCallback(RecognitionCallback):
    """Callback that logs all recognition events."""

    def __init__(self, logger_name: str = __name__, log_level: str = "INFO") -> None:
        """Initialize logging callback.

        Args:
            logger_name: Name for the logger
            log_level: Logging level for recognition events
        """
        import logging

        self.logger = logging.getLogger(logger_name)
        self.log_level = getattr(logging, log_level.upper())

    def on_partial_result(self, result: PartialResult) -> None:
        """Log partial recognition result."""
        self.logger.log(
            self.log_level,
            f"Partial result: '{result.text}' (confidence: {result.confidence:.2f}, "
            f"time: {result.start_time:.2f}-{result.end_time:.2f}s)",
        )

    def on_final_result(self, result: FinalResult) -> None:
        """Log final recognition result."""
        self.logger.log(
            self.log_level,
            f"Final result: '{result.text}' (confidence: {result.confidence:.2f})",
        )
        if result.alternatives:
            self.logger.log(self.log_level, f"Alternatives: {result.alternatives}")

    def on_sentence_end(self, result: SentenceResult) -> None:
        """Log sentence completion event."""
        self.logger.log(
            self.log_level,
            f"Sentence #{result.sentence_id}: '{result.text}' "
            f"({len(result.words)} words, confidence: {result.confidence:.2f})",
        )

    def on_error(self, error: FunASRError) -> None:
        """Log recognition error."""
        self.logger.error(f"Recognition error: {error}")

    def on_connection_status(self, status: ConnectionState) -> None:
        """Log connection status change."""
        self.logger.info(f"Connection status: {status.value}")


class MultiCallback(RecognitionCallback):
    """Callback that dispatches to multiple callbacks."""

    def __init__(self, callbacks: List[RecognitionCallback]) -> None:
        """Initialize multi-callback.

        Args:
            callbacks: List of callbacks to dispatch to
        """
        self.callbacks = callbacks

    def add_callback(self, callback: RecognitionCallback) -> None:
        """Add a callback to the dispatcher.

        Args:
            callback: Callback to add
        """
        self.callbacks.append(callback)

    def remove_callback(self, callback: RecognitionCallback) -> None:
        """Remove a callback from the dispatcher.

        Args:
            callback: Callback to remove
        """
        if callback in self.callbacks:
            self.callbacks.remove(callback)

    def on_partial_result(self, result: PartialResult) -> None:
        """Dispatch partial result to all callbacks."""
        for callback in self.callbacks:
            try:
                callback.on_partial_result(result)
            except Exception as e:
                self._handle_callback_error(callback, "on_partial_result", e)

    def on_final_result(self, result: FinalResult) -> None:
        """Dispatch final result to all callbacks."""
        for callback in self.callbacks:
            try:
                callback.on_final_result(result)
            except Exception as e:
                self._handle_callback_error(callback, "on_final_result", e)

    def on_sentence_end(self, result: SentenceResult) -> None:
        """Dispatch sentence end to all callbacks."""
        for callback in self.callbacks:
            try:
                callback.on_sentence_end(result)
            except Exception as e:
                self._handle_callback_error(callback, "on_sentence_end", e)

    def on_error(self, error: FunASRError) -> None:
        """Dispatch error to all callbacks."""
        for callback in self.callbacks:
            try:
                callback.on_error(error)
            except Exception as e:
                self._handle_callback_error(callback, "on_error", e)

    def on_connection_status(self, status: ConnectionState) -> None:
        """Dispatch connection status to all callbacks."""
        for callback in self.callbacks:
            try:
                callback.on_connection_status(status)
            except Exception as e:
                self._handle_callback_error(callback, "on_connection_status", e)

    def _handle_callback_error(
        self, callback: RecognitionCallback, method: str, error: Exception
    ) -> None:
        """Handle callback execution error.

        Args:
            callback: Callback that failed
            method: Method that failed
            error: Exception that occurred
        """
        import logging

        logger = logging.getLogger(__name__)
        logger.error(
            f"Error in callback {callback.__class__.__name__}.{method}: {error}",
            exc_info=True,
        )


class BufferingCallback(RecognitionCallback):
    """Callback that buffers results for batch processing."""

    def __init__(
        self,
        target_callback: RecognitionCallback,
        buffer_size: int = 10,
        flush_timeout: float = 1.0,
    ) -> None:
        """Initialize buffering callback.

        Args:
            target_callback: Target callback to buffer results for
            buffer_size: Maximum number of results to buffer
            flush_timeout: Maximum time to wait before flushing buffer
        """
        self.target_callback = target_callback
        self.buffer_size = buffer_size
        self.flush_timeout = flush_timeout

        self.partial_results: List[PartialResult] = []
        self.final_results: List[FinalResult] = []
        self.sentence_results: List[SentenceResult] = []
        self.errors: List[FunASRError] = []

        self._flush_task: Optional[asyncio.Task] = None
        self._last_activity = 0.0

    def on_partial_result(self, result: PartialResult) -> None:
        """Buffer partial recognition result."""
        self.partial_results.append(result)
        self._schedule_flush()

    def on_final_result(self, result: FinalResult) -> None:
        """Buffer final recognition result."""
        self.final_results.append(result)
        self._schedule_flush()

    def on_sentence_end(self, result: SentenceResult) -> None:
        """Buffer sentence completion event."""
        self.sentence_results.append(result)
        self._schedule_flush()

    def on_error(self, error: FunASRError) -> None:
        """Buffer recognition error."""
        self.errors.append(error)
        self._schedule_flush()

    def on_connection_status(self, status: ConnectionState) -> None:
        """Pass through connection status immediately."""
        self.target_callback.on_connection_status(status)

    def flush(self) -> None:
        """Flush all buffered results."""
        # Process all buffered results
        for result in self.partial_results:
            self.target_callback.on_partial_result(result)

        for result in self.final_results:
            self.target_callback.on_final_result(result)

        for result in self.sentence_results:
            self.target_callback.on_sentence_end(result)

        for error in self.errors:
            self.target_callback.on_error(error)

        # Clear buffers
        self.partial_results.clear()
        self.final_results.clear()
        self.sentence_results.clear()
        self.errors.clear()

    def _schedule_flush(self) -> None:
        """Schedule buffer flush if needed."""
        import time

        self._last_activity = time.time()

        # Check if buffer is full
        total_buffered = (
            len(self.partial_results)
            + len(self.final_results)
            + len(self.sentence_results)
            + len(self.errors)
        )

        if total_buffered >= self.buffer_size:
            self.flush()
            return

        # Schedule timeout-based flush
        if self._flush_task is None or self._flush_task.done():
            self._flush_task = asyncio.create_task(self._flush_after_timeout())

    async def _flush_after_timeout(self) -> None:
        """Flush buffer after timeout."""
        await asyncio.sleep(self.flush_timeout)

        # Only flush if no recent activity
        import time

        if time.time() - self._last_activity >= self.flush_timeout:
            self.flush()


# Utility functions for creating common callback patterns
def create_simple_callback(
    on_final: Optional[Callable[[str, float], None]] = None,
    on_error: Optional[Callable[[str], None]] = None,
    **kwargs: Any,
) -> SimpleCallback:
    """Create a simple callback with common function signatures.

    Args:
        on_final: Function to call with final text and confidence
        on_error: Function to call with error message
        **kwargs: Additional callback functions

    Returns:
        SimpleCallback instance
    """

    def final_wrapper(result: FinalResult) -> None:
        if on_final:
            on_final(result.text, result.confidence)

    def error_wrapper(error: FunASRError) -> None:
        if on_error:
            on_error(str(error))

    return SimpleCallback(
        on_final=final_wrapper,
        on_error=error_wrapper,
        **kwargs,
    )


def create_logging_callback(
    logger_name: Optional[str] = None,
    log_partial: bool = True,
    log_final: bool = True,
    log_errors: bool = True,
) -> LoggingCallback:
    """Create a logging callback with customizable options.

    Args:
        logger_name: Logger name (uses default if None)
        log_partial: Whether to log partial results
        log_final: Whether to log final results
        log_errors: Whether to log errors

    Returns:
        LoggingCallback instance
    """
    callback = LoggingCallback(logger_name or __name__)

    if not log_partial:
        callback.on_partial_result = lambda result: None  # type: ignore

    if not log_final:
        callback.on_final_result = lambda result: None  # type: ignore

    if not log_errors:
        callback.on_error = lambda error: None  # type: ignore

    return callback
