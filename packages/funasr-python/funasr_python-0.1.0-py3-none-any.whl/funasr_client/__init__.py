"""FunASR Python Client - High-performance client for FunASR WebSocket speech recognition service."""

from __future__ import annotations

__version__ = "0.1.0"
__author__ = "FunASR Team"
__email__ = ""

# Core client classes
# Audio processing
from .audio import (
    AudioChunker,
    AudioFileStreamer,
    AudioProcessor,
    AudioRecorder,
    calculate_audio_duration,
    create_silence,
    detect_audio_format,
)

# Callbacks
from .callbacks import (
    AsyncRecognitionCallback,
    AsyncSimpleCallback,
    LoggingCallback,
    MultiCallback,
    RecognitionCallback,
    SimpleCallback,
    create_logging_callback,
    create_simple_callback,
)
from .client import (
    AsyncFunASRClient,
    FunASRClient,
    create_async_client,
    create_client,
    recognize_file,
    recognize_file_async,
)

# Configuration and models
from .config import ConfigManager, config_manager

# Errors
from .errors import (
    AudioError,
    AuthenticationError,
    ClientError,
    ConnectionError,
    FunASRError,
    NetworkError,
    ProtocolError,
    ServiceError,
    TimeoutError,
)
from .models import (
    AudioConfig,
    AudioFormat,
    ClientConfig,
    ConfigPresets,
    ConnectionState,
    FinalResult,
    PartialResult,
    RealtimeSession,
    RecognitionMode,
    RecognitionResult,
    SentenceResult,
    WordResult,
)

# Utilities
from .utils import (
    Timer,
    calculate_real_time_factor,
    format_duration,
    human_readable_size,
    is_audio_file,
    normalize_text_for_comparison,
    setup_logging,
    validate_server_url,
)

# Public API
__all__ = [
    "AsyncFunASRClient",
    "AsyncRecognitionCallback",
    "AsyncSimpleCallback",
    "AudioChunker",
    "AudioConfig",
    "AudioError",
    "AudioFileStreamer",
    "AudioFormat",
    # Audio processing
    "AudioProcessor",
    "AudioRecorder",
    "AuthenticationError",
    # Configuration
    "ClientConfig",
    "ClientError",
    "ConfigManager",
    "ConfigPresets",
    "ConnectionError",
    "ConnectionState",
    "FinalResult",
    # Core clients
    "FunASRClient",
    # Errors
    "FunASRError",
    "LoggingCallback",
    "MultiCallback",
    "NetworkError",
    "PartialResult",
    "ProtocolError",
    "RealtimeSession",
    # Callbacks
    "RecognitionCallback",
    # Models and enums
    "RecognitionMode",
    "RecognitionResult",
    "SentenceResult",
    "ServiceError",
    "SimpleCallback",
    "TimeoutError",
    "Timer",
    "WordResult",
    "__author__",
    "__email__",
    # Version info
    "__version__",
    "calculate_audio_duration",
    "calculate_real_time_factor",
    "config_manager",
    "create_async_client",
    "create_client",
    "create_logging_callback",
    "create_silence",
    "create_simple_callback",
    "detect_audio_format",
    "format_duration",
    "human_readable_size",
    "is_audio_file",
    "normalize_text_for_comparison",
    "recognize_file",
    "recognize_file_async",
    # Utilities
    "setup_logging",
    "validate_server_url",
]


def get_version() -> str:
    """Get the package version.

    Returns:
        Package version string
    """
    return __version__


def get_client_info() -> dict:
    """Get client information.

    Returns:
        Dictionary with client information
    """
    return {
        "name": "funasr-python",
        "version": __version__,
        "author": __author__,
        "email": __email__,
        "description": "High-performance Python client for FunASR WebSocket speech recognition service",
        "supported_python": ">=3.8",
        "supported_audio_formats": [fmt.value for fmt in AudioFormat],
        "supported_recognition_modes": [mode.value for mode in RecognitionMode],
    }


# Setup package-level configuration
def configure(
    log_level: str = "INFO",
    **config_kwargs,
) -> None:
    """Configure package-level settings.

    Args:
        log_level: Default logging level
        **config_kwargs: Additional configuration options (unused, kept for backwards compatibility)
    """
    setup_logging(level=log_level)
