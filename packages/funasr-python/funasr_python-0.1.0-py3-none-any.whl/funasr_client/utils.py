"""Utility functions for FunASR client."""

from __future__ import annotations

import asyncio
import json
import logging
from pathlib import Path
import time
from typing import Any, Dict, List, Optional, Union
from urllib.parse import urlparse


def setup_logging(
    level: str = "INFO",
    format_string: Optional[str] = None,
    filename: Optional[str] = None,
) -> None:
    """Set up logging configuration for FunASR client.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format_string: Custom format string for log messages
        filename: Optional filename to write logs to
    """
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    logging_config = {
        "level": getattr(logging, level.upper()),
        "format": format_string,
        "datefmt": "%Y-%m-%d %H:%M:%S",
    }

    if filename:
        logging_config["filename"] = filename

    logging.basicConfig(**logging_config)


def validate_server_url(url: str) -> bool:
    """Validate WebSocket server URL format.

    Args:
        url: Server URL to validate

    Returns:
        True if URL is valid WebSocket URL

    Raises:
        ValueError: If URL is invalid
    """
    if not url:
        raise ValueError("Server URL cannot be empty")

    parsed = urlparse(url)

    if parsed.scheme not in ("ws", "wss"):
        raise ValueError(f"Invalid scheme '{parsed.scheme}'. Must be 'ws' or 'wss'")

    if not parsed.hostname:
        raise ValueError("Server URL must include hostname")

    if parsed.port and not (1 <= parsed.port <= 65535):
        raise ValueError(f"Invalid port {parsed.port}. Must be between 1-65535")

    return True


def parse_timestamp_string(timestamp_str: str) -> List[List[float]]:
    """Parse timestamp string from FunASR response.

    Args:
        timestamp_str: Timestamp string in format "[[start, end], ...]"

    Returns:
        List of [start_time, end_time] pairs

    Raises:
        ValueError: If timestamp string is invalid
    """
    if not timestamp_str or timestamp_str == "[]":
        return []

    try:
        timestamps = json.loads(timestamp_str)
        if not isinstance(timestamps, list):
            raise ValueError("Timestamps must be a list")

        parsed_timestamps = []
        for ts in timestamps:
            if not isinstance(ts, list) or len(ts) != 2:
                raise ValueError("Each timestamp must be [start, end]")

            start_time, end_time = float(ts[0]), float(ts[1])
            if start_time < 0 or end_time < 0 or end_time < start_time:
                raise ValueError(f"Invalid timestamp range: [{start_time}, {end_time}]")

            parsed_timestamps.append([start_time, end_time])

        return parsed_timestamps

    except (json.JSONDecodeError, TypeError, ValueError) as e:
        raise ValueError(f"Invalid timestamp format: {e}") from e


def format_duration(seconds: float) -> str:
    """Format duration in seconds to human-readable string.

    Args:
        seconds: Duration in seconds

    Returns:
        Formatted duration string (e.g., "1m 23.45s", "45.67s", "2h 15m 30s")
    """
    if seconds < 0:
        return "0s"

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining_seconds = seconds % 60

    parts = []
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if remaining_seconds > 0 or not parts:
        parts.append(f"{remaining_seconds:.2f}s")

    return " ".join(parts)


def calculate_real_time_factor(processing_time: float, audio_duration: float) -> float:
    """Calculate real-time factor (RTF) for audio processing.

    Args:
        processing_time: Time taken to process audio (seconds)
        audio_duration: Duration of processed audio (seconds)

    Returns:
        Real-time factor (processing_time / audio_duration)
        - RTF < 1.0: Faster than real-time
        - RTF = 1.0: Real-time processing
        - RTF > 1.0: Slower than real-time
    """
    if audio_duration <= 0:
        return 0.0
    return processing_time / audio_duration


def estimate_audio_size(
    duration: float,
    sample_rate: int = 16000,
    channels: int = 1,
    sample_width: int = 2,
) -> int:
    """Estimate audio data size in bytes.

    Args:
        duration: Audio duration in seconds
        sample_rate: Sample rate in Hz
        channels: Number of audio channels
        sample_width: Sample width in bytes (1=8bit, 2=16bit, etc.)

    Returns:
        Estimated size in bytes
    """
    return int(duration * sample_rate * channels * sample_width)


def calculate_bitrate(
    size_bytes: int,
    duration: float,
) -> float:
    """Calculate audio bitrate in bits per second.

    Args:
        size_bytes: Audio data size in bytes
        duration: Audio duration in seconds

    Returns:
        Bitrate in bits per second
    """
    if duration <= 0:
        return 0.0
    return (size_bytes * 8) / duration


def safe_filename(text: str, max_length: int = 255) -> str:
    """Convert text to safe filename.

    Args:
        text: Input text
        max_length: Maximum filename length

    Returns:
        Safe filename string
    """
    import re

    # Replace invalid characters with underscore
    safe_text = re.sub(r'[<>:"/\\|?*]', "_", text)

    # Remove multiple consecutive underscores
    safe_text = re.sub(r"_{2,}", "_", safe_text)

    # Remove leading/trailing underscores and whitespace
    safe_text = safe_text.strip("_ ")

    # Truncate to maximum length
    if len(safe_text) > max_length:
        safe_text = safe_text[:max_length]

    # Ensure filename is not empty
    if not safe_text:
        safe_text = "untitled"

    return safe_text


def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split list into chunks of specified size.

    Args:
        items: List to chunk
        chunk_size: Maximum size of each chunk

    Returns:
        List of chunked lists

    Raises:
        ValueError: If chunk_size <= 0
    """
    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive")

    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def retry_with_backoff(
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    backoff_multiplier: float = 2.0,
    jitter: bool = True,
):
    """Decorator for retrying functions with exponential backoff.

    Args:
        max_retries: Maximum number of retry attempts
        base_delay: Base delay between retries in seconds
        max_delay: Maximum delay between retries in seconds
        backoff_multiplier: Multiplier for exponential backoff
        jitter: Whether to add random jitter to delays

    Returns:
        Decorator function
    """

    def decorator(func):
        async def async_wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    if asyncio.iscoroutinefunction(func):
                        return await func(*args, **kwargs)
                    else:
                        return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_retries:
                        delay = min(
                            base_delay * (backoff_multiplier**attempt), max_delay
                        )
                        if jitter:
                            import random

                            delay *= random.uniform(0.8, 1.2)
                        await asyncio.sleep(delay)

            raise last_exception

        def sync_wrapper(*args, **kwargs):
            import time

            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_retries:
                        delay = min(
                            base_delay * (backoff_multiplier**attempt), max_delay
                        )
                        if jitter:
                            import random

                            delay *= random.uniform(0.8, 1.2)
                        time.sleep(delay)

            raise last_exception

        # Return appropriate wrapper based on function type
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper

    return decorator


def measure_execution_time(func):
    """Decorator to measure function execution time.

    Args:
        func: Function to measure

    Returns:
        Decorated function that logs execution time
    """
    import functools

    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            result = await func(*args, **kwargs)
            execution_time = time.perf_counter() - start_time
            logger = logging.getLogger(func.__module__)
            logger.debug(f"{func.__name__} executed in {execution_time:.4f} seconds")
            return result
        except Exception:
            execution_time = time.perf_counter() - start_time
            logger = logging.getLogger(func.__module__)
            logger.debug(f"{func.__name__} failed after {execution_time:.4f} seconds")
            raise

    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            execution_time = time.perf_counter() - start_time
            logger = logging.getLogger(func.__module__)
            logger.debug(f"{func.__name__} executed in {execution_time:.4f} seconds")
            return result
        except Exception:
            execution_time = time.perf_counter() - start_time
            logger = logging.getLogger(func.__module__)
            logger.debug(f"{func.__name__} failed after {execution_time:.4f} seconds")
            raise

    # Return appropriate wrapper
    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper


def deep_merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Deep merge two dictionaries.

    Args:
        dict1: Base dictionary
        dict2: Dictionary to merge into dict1

    Returns:
        Merged dictionary
    """
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value

    return result


def get_file_size_mb(file_path: Union[str, Path]) -> float:
    """Get file size in megabytes.

    Args:
        file_path: Path to file

    Returns:
        File size in MB

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return path.stat().st_size / (1024 * 1024)


def normalize_text_for_comparison(text: str) -> str:
    """Normalize text for comparison purposes.

    Args:
        text: Input text

    Returns:
        Normalized text (lowercase, no extra whitespace)
    """
    import re

    if not text:
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text


def extract_numbers_from_text(text: str) -> List[float]:
    """Extract all numbers from text.

    Args:
        text: Input text

    Returns:
        List of extracted numbers
    """
    import re

    if not text:
        return []

    # Pattern to match integers and floats (including negative)
    pattern = r"-?\d+\.?\d*"
    matches = re.findall(pattern, text)

    numbers = []
    for match in matches:
        try:
            if "." in match:
                numbers.append(float(match))
            else:
                numbers.append(float(int(match)))
        except ValueError:
            continue

    return numbers


def create_progress_bar(
    current: int,
    total: int,
    width: int = 50,
    fill_char: str = "█",
    empty_char: str = "░",
) -> str:
    """Create a text-based progress bar.

    Args:
        current: Current progress value
        total: Total progress value
        width: Width of progress bar in characters
        fill_char: Character for filled portion
        empty_char: Character for empty portion

    Returns:
        Progress bar string
    """
    if total <= 0:
        return f"[{empty_char * width}] 0%"

    percentage = min(100, max(0, (current / total) * 100))
    filled_width = int((current / total) * width)
    empty_width = width - filled_width

    bar = fill_char * filled_width + empty_char * empty_width
    return f"[{bar}] {percentage:.1f}%"


def human_readable_size(size_bytes: int) -> str:
    """Convert bytes to human-readable size string.

    Args:
        size_bytes: Size in bytes

    Returns:
        Human-readable size string (e.g., "1.5 MB", "256 KB")
    """
    if size_bytes < 0:
        return "0 B"

    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(size_bytes)

    for unit in units:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0

    return f"{size:.1f} PB"


async def wait_for_condition(
    condition_func: callable,
    timeout: float = 30.0,
    check_interval: float = 0.1,
) -> bool:
    """Wait for a condition to become true.

    Args:
        condition_func: Function that returns True when condition is met
        timeout: Maximum time to wait in seconds
        check_interval: Time between condition checks in seconds

    Returns:
        True if condition was met, False if timeout occurred
    """
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            if condition_func():
                return True
        except Exception:
            pass

        await asyncio.sleep(check_interval)

    return False


def is_audio_file(file_path: Union[str, Path]) -> bool:
    """Check if file is a supported audio file.

    Args:
        file_path: Path to file

    Returns:
        True if file appears to be a supported audio file
    """
    audio_extensions = {
        ".wav",
        ".mp3",
        ".m4a",
        ".aac",
        ".flac",
        ".ogg",
        ".pcm",
        ".raw",
    }

    path = Path(file_path)
    return path.suffix.lower() in audio_extensions


def get_system_info() -> Dict[str, Any]:
    """Get system information for debugging.

    Returns:
        Dictionary with system information
    """
    import platform
    import sys

    info = {
        "python_version": sys.version,
        "platform": platform.platform(),
        "architecture": platform.architecture(),
        "processor": platform.processor(),
        "system": platform.system(),
        "release": platform.release(),
    }

    # Add memory info if available
    try:
        import psutil

        memory = psutil.virtual_memory()
        info["memory"] = {
            "total": memory.total,
            "available": memory.available,
            "percent_used": memory.percent,
        }
    except ImportError:
        pass

    return info


# Context managers
class Timer:
    """Context manager for measuring execution time."""

    def __init__(
        self, name: str = "Operation", logger: Optional[logging.Logger] = None
    ):
        """Initialize timer.

        Args:
            name: Name of the operation being timed
            logger: Logger to use for output (creates new one if None)
        """
        self.name = name
        self.logger = logger or logging.getLogger(__name__)
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None

    def __enter__(self):
        """Start timing."""
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """End timing and log result."""
        self.end_time = time.perf_counter()
        duration = self.elapsed
        self.logger.info(f"{self.name} completed in {duration:.4f} seconds")

    @property
    def elapsed(self) -> float:
        """Get elapsed time in seconds."""
        if self.start_time is None:
            return 0.0
        end_time = self.end_time or time.perf_counter()
        return end_time - self.start_time


class TemporaryConfig:
    """Context manager for temporarily modifying configuration."""

    def __init__(self, config: Any, **overrides):
        """Initialize temporary config.

        Args:
            config: Configuration object to modify
            **overrides: Configuration values to temporarily set
        """
        self.config = config
        self.overrides = overrides
        self.original_values = {}

    def __enter__(self):
        """Apply temporary configuration."""
        for key, value in self.overrides.items():
            if hasattr(self.config, key):
                self.original_values[key] = getattr(self.config, key)
                setattr(self.config, key, value)
        return self.config

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Restore original configuration."""
        for key, value in self.original_values.items():
            setattr(self.config, key, value)


# Export commonly used functions
__all__ = [
    "TemporaryConfig",
    "Timer",
    "calculate_bitrate",
    "calculate_real_time_factor",
    "chunk_list",
    "create_progress_bar",
    "deep_merge_dicts",
    "estimate_audio_size",
    "extract_numbers_from_text",
    "format_duration",
    "get_file_size_mb",
    "get_system_info",
    "human_readable_size",
    "is_audio_file",
    "measure_execution_time",
    "normalize_text_for_comparison",
    "parse_timestamp_string",
    "retry_with_backoff",
    "safe_filename",
    "setup_logging",
    "validate_server_url",
    "wait_for_condition",
]
