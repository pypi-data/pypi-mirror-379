"""Error classes and exception hierarchy for FunASR client."""

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Optional


class ErrorCategory(str, Enum):
    """Categories of errors that can occur."""

    CONNECTION = "connection"
    AUTHENTICATION = "authentication"
    PROTOCOL = "protocol"
    AUDIO = "audio"
    SERVICE = "service"
    CLIENT = "client"
    NETWORK = "network"
    TIMEOUT = "timeout"


class ErrorSeverity(str, Enum):
    """Severity levels for errors."""

    LOW = "low"  # Minor errors that can be ignored
    MEDIUM = "medium"  # Moderate errors that need handling
    HIGH = "high"  # Serious errors affecting functionality
    CRITICAL = "critical"  # Critical errors making system unusable


class RecoveryAction(str, Enum):
    """Recommended recovery actions for errors."""

    IGNORE = "ignore"  # Ignore the error
    RETRY = "retry"  # Retry the operation
    RECONNECT = "reconnect"  # Reconnect to the server
    FALLBACK = "fallback"  # Use fallback processing
    ABORT = "abort"  # Abort the operation


class FunASRError(Exception):
    """Base exception class for all FunASR client errors."""

    def __init__(
        self,
        message: str,
        code: str = "UNKNOWN_ERROR",
        category: ErrorCategory = ErrorCategory.CLIENT,
        severity: ErrorSeverity = ErrorSeverity.MEDIUM,
        recovery_action: RecoveryAction = RecoveryAction.RETRY,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize FunASR error.

        Args:
            message: Human-readable error message
            code: Error code for programmatic handling
            category: Error category
            severity: Error severity level
            recovery_action: Recommended recovery action
            details: Additional error details
        """
        super().__init__(message)
        self.message = message
        self.code = code
        self.category = category
        self.severity = severity
        self.recovery_action = recovery_action
        self.details = details or {}

    def __str__(self) -> str:
        """Return string representation of the error."""
        return f"[{self.code}] {self.message}"

    def __repr__(self) -> str:
        """Return detailed representation of the error."""
        return (
            f"{self.__class__.__name__}("
            f"code='{self.code}', "
            f"category='{self.category.value}', "
            f"severity='{self.severity.value}', "
            f"message='{self.message}')"
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert error to dictionary format."""
        return {
            "error": {
                "code": self.code,
                "category": self.category.value,
                "severity": self.severity.value,
                "message": self.message,
                "recovery_action": self.recovery_action.value,
                "details": self.details,
            }
        }


# Connection-related errors
class ConnectionError(FunASRError):
    """Base class for connection-related errors."""

    def __init__(self, message: str, code: str = "CONNECTION_ERROR", **kwargs) -> None:
        super().__init__(
            message,
            code=code,
            category=ErrorCategory.CONNECTION,
            severity=ErrorSeverity.HIGH,
            recovery_action=RecoveryAction.RECONNECT,
            **kwargs,
        )


class ConnectionTimeoutError(ConnectionError):
    """Connection timeout error."""

    def __init__(self, timeout: float, **kwargs) -> None:
        message = f"Connection timed out after {timeout} seconds"
        super().__init__(
            message,
            code="CONNECTION_TIMEOUT",
            details={"timeout": timeout},
            **kwargs,
        )


class ConnectionRefusedError(ConnectionError):
    """Connection refused error."""

    def __init__(self, server_url: str, **kwargs) -> None:
        message = f"Connection refused to server: {server_url}"
        super().__init__(
            message,
            code="CONNECTION_REFUSED",
            details={"server_url": server_url},
            **kwargs,
        )


class ConnectionLostError(ConnectionError):
    """Connection lost error."""

    def __init__(self, reason: Optional[str] = None, **kwargs) -> None:
        message = "WebSocket connection was lost"
        if reason:
            message += f": {reason}"
        super().__init__(
            message,
            code="CONNECTION_LOST",
            details={"reason": reason},
            **kwargs,
        )


# Authentication errors
class AuthenticationError(FunASRError):
    """Base class for authentication errors."""

    def __init__(
        self, message: str, code: str = "AUTHENTICATION_ERROR", **kwargs
    ) -> None:
        # Set default recovery_action only if not provided
        if "recovery_action" not in kwargs:
            kwargs["recovery_action"] = RecoveryAction.ABORT

        super().__init__(
            message,
            code=code,
            category=ErrorCategory.AUTHENTICATION,
            severity=ErrorSeverity.CRITICAL,
            **kwargs,
        )


class InvalidCredentialsError(AuthenticationError):
    """Invalid credentials error."""

    def __init__(self, **kwargs) -> None:
        super().__init__(
            "Invalid authentication credentials",
            code="INVALID_CREDENTIALS",
            **kwargs,
        )


class TokenExpiredError(AuthenticationError):
    """Token expired error."""

    def __init__(self, **kwargs) -> None:
        # Override the default ABORT recovery action with RETRY
        kwargs["recovery_action"] = RecoveryAction.RETRY
        super().__init__(
            "Authentication token has expired",
            code="TOKEN_EXPIRED",
            **kwargs,
        )


# Protocol errors
class ProtocolError(FunASRError):
    """Base class for protocol-related errors."""

    def __init__(self, message: str, code: str = "PROTOCOL_ERROR", **kwargs) -> None:
        # Set default recovery_action only if not provided
        if "recovery_action" not in kwargs:
            kwargs["recovery_action"] = RecoveryAction.RETRY

        super().__init__(
            message,
            code=code,
            category=ErrorCategory.PROTOCOL,
            severity=ErrorSeverity.MEDIUM,
            **kwargs,
        )


class InvalidMessageFormatError(ProtocolError):
    """Invalid message format error."""

    def __init__(self, raw_message: str, **kwargs) -> None:
        message = "Invalid message format received from server"
        # Override the default RETRY recovery action with IGNORE
        kwargs["recovery_action"] = RecoveryAction.IGNORE
        kwargs["details"] = {"raw_message": raw_message[:200]}  # Truncate long messages
        super().__init__(
            message,
            code="INVALID_MESSAGE_FORMAT",
            **kwargs,
        )


class ProtocolVersionMismatchError(ProtocolError):
    """Protocol version mismatch error."""

    def __init__(self, client_version: str, server_version: str, **kwargs) -> None:
        message = f"Protocol version mismatch: client={client_version}, server={server_version}"
        super().__init__(
            message,
            code="PROTOCOL_VERSION_MISMATCH",
            severity=ErrorSeverity.HIGH,
            recovery_action=RecoveryAction.ABORT,
            details={
                "client_version": client_version,
                "server_version": server_version,
            },
            **kwargs,
        )


# Audio-related errors
class AudioError(FunASRError):
    """Base class for audio-related errors."""

    def __init__(self, message: str, code: str = "AUDIO_ERROR", **kwargs) -> None:
        # Set default recovery_action only if not provided
        if "recovery_action" not in kwargs:
            kwargs["recovery_action"] = RecoveryAction.FALLBACK

        # Set default severity only if not provided
        if "severity" not in kwargs:
            kwargs["severity"] = ErrorSeverity.MEDIUM

        super().__init__(
            message,
            code=code,
            category=ErrorCategory.AUDIO,
            **kwargs,
        )


class UnsupportedAudioFormatError(AudioError):
    """Unsupported audio format error."""

    def __init__(self, format_name: str, **kwargs) -> None:
        message = f"Unsupported audio format: {format_name}"
        super().__init__(
            message,
            code="UNSUPPORTED_AUDIO_FORMAT",
            details={"format": format_name},
            **kwargs,
        )


class InvalidSampleRateError(AudioError):
    """Invalid sample rate error."""

    def __init__(self, sample_rate: int, supported_rates: list[int], **kwargs) -> None:
        message = f"Invalid sample rate {sample_rate}Hz. Supported: {supported_rates}"
        super().__init__(
            message,
            code="INVALID_SAMPLE_RATE",
            details={
                "sample_rate": sample_rate,
                "supported_rates": supported_rates,
            },
            **kwargs,
        )


class AudioDataCorruptedError(AudioError):
    """Audio data corrupted error."""

    def __init__(self, reason: Optional[str] = None, **kwargs) -> None:
        message = "Audio data is corrupted or invalid"
        if reason:
            message += f": {reason}"

        super().__init__(
            message,
            code="AUDIO_DATA_CORRUPTED",
            recovery_action=RecoveryAction.IGNORE,
            details={"reason": reason},
            **kwargs,
        )


class AudioFileNotFoundError(AudioError):
    """Audio file not found error."""

    def __init__(self, file_path: str, **kwargs) -> None:
        message = f"Audio file not found: {file_path}"
        super().__init__(
            message,
            code="AUDIO_FILE_NOT_FOUND",
            severity=ErrorSeverity.HIGH,
            recovery_action=RecoveryAction.ABORT,
            details={"file_path": file_path},
            **kwargs,
        )


# Service errors
class ServiceError(FunASRError):
    """Base class for service-related errors."""

    def __init__(self, message: str, code: str = "SERVICE_ERROR", **kwargs) -> None:
        super().__init__(
            message,
            code=code,
            category=ErrorCategory.SERVICE,
            severity=ErrorSeverity.HIGH,
            recovery_action=RecoveryAction.RETRY,
            **kwargs,
        )


class ServiceUnavailableError(ServiceError):
    """Service unavailable error."""

    def __init__(self, **kwargs) -> None:
        super().__init__(
            "FunASR service is currently unavailable",
            code="SERVICE_UNAVAILABLE",
            **kwargs,
        )


class ServiceOverloadedError(ServiceError):
    """Service overloaded error."""

    def __init__(self, **kwargs) -> None:
        super().__init__(
            "FunASR service is currently overloaded",
            code="SERVICE_OVERLOADED",
            severity=ErrorSeverity.MEDIUM,
            **kwargs,
        )


class InternalServerError(ServiceError):
    """Internal server error."""

    def __init__(self, server_message: Optional[str] = None, **kwargs) -> None:
        message = "Internal server error occurred"
        if server_message:
            message += f": {server_message}"
        super().__init__(
            message,
            code="INTERNAL_SERVER_ERROR",
            details={"server_message": server_message},
            **kwargs,
        )


# Client errors
class ClientError(FunASRError):
    """Base class for client-side errors."""

    def __init__(self, message: str, code: str = "CLIENT_ERROR", **kwargs) -> None:
        super().__init__(
            message,
            code=code,
            category=ErrorCategory.CLIENT,
            severity=ErrorSeverity.HIGH,
            recovery_action=RecoveryAction.ABORT,
            **kwargs,
        )


class InvalidConfigurationError(ClientError):
    """Invalid configuration error."""

    def __init__(
        self, config_key: str, config_value: Any, reason: str, **kwargs
    ) -> None:
        message = f"Invalid configuration for '{config_key}': {reason}"
        super().__init__(
            message,
            code="INVALID_CONFIGURATION",
            details={
                "config_key": config_key,
                "config_value": str(config_value),
                "reason": reason,
            },
            **kwargs,
        )


class ResourceExhaustedError(ClientError):
    """Resource exhausted error."""

    def __init__(self, resource_type: str, **kwargs) -> None:
        message = f"Client resource exhausted: {resource_type}"
        super().__init__(
            message,
            code="RESOURCE_EXHAUSTED",
            recovery_action=RecoveryAction.FALLBACK,
            details={"resource_type": resource_type},
            **kwargs,
        )


# Network errors
class NetworkError(FunASRError):
    """Base class for network-related errors."""

    def __init__(self, message: str, code: str = "NETWORK_ERROR", **kwargs) -> None:
        super().__init__(
            message,
            code=code,
            category=ErrorCategory.NETWORK,
            severity=ErrorSeverity.HIGH,
            recovery_action=RecoveryAction.RETRY,
            **kwargs,
        )


class NetworkUnreachableError(NetworkError):
    """Network unreachable error."""

    def __init__(self, host: str, **kwargs) -> None:
        message = f"Network unreachable: {host}"
        super().__init__(
            message,
            code="NETWORK_UNREACHABLE",
            details={"host": host},
            **kwargs,
        )


class DNSResolutionError(NetworkError):
    """DNS resolution error."""

    def __init__(self, hostname: str, **kwargs) -> None:
        message = f"DNS resolution failed for hostname: {hostname}"
        super().__init__(
            message,
            code="DNS_RESOLUTION_FAILED",
            details={"hostname": hostname},
            **kwargs,
        )


# Timeout errors
class TimeoutError(FunASRError):
    """Base class for timeout-related errors."""

    def __init__(
        self, message: str, timeout: float, code: str = "TIMEOUT_ERROR", **kwargs
    ) -> None:
        super().__init__(
            message,
            code=code,
            category=ErrorCategory.TIMEOUT,
            severity=ErrorSeverity.MEDIUM,
            recovery_action=RecoveryAction.RETRY,
            details={"timeout": timeout},
            **kwargs,
        )


class ResponseTimeoutError(TimeoutError):
    """Response timeout error."""

    def __init__(self, timeout: float, **kwargs) -> None:
        message = f"No response received within {timeout} seconds"
        super().__init__(
            message,
            timeout,
            code="RESPONSE_TIMEOUT",
            **kwargs,
        )


class RecognitionTimeoutError(TimeoutError):
    """Recognition timeout error."""

    def __init__(self, timeout: float, **kwargs) -> None:
        message = f"Recognition did not complete within {timeout} seconds"
        super().__init__(
            message,
            timeout,
            code="RECOGNITION_TIMEOUT",
            **kwargs,
        )


# Error mapping utilities
def map_server_error(error_data: Dict[str, Any]) -> FunASRError:
    """Map server error response to appropriate exception.

    Args:
        error_data: Error data from server response

    Returns:
        Appropriate FunASRError subclass instance
    """
    error_code = error_data.get("code", "UNKNOWN_ERROR")
    error_message = error_data.get("message", "Unknown error occurred")
    error_details = error_data.get("details", {})

    # Connection errors
    if error_code in ("CONNECTION_FAILED", "CONNECTION_TIMEOUT", "CONNECTION_REFUSED"):
        return ConnectionError(error_message, code=error_code, details=error_details)

    # Authentication errors
    if error_code in ("AUTHENTICATION_FAILED", "INVALID_CREDENTIALS", "TOKEN_EXPIRED"):
        return AuthenticationError(
            error_message, code=error_code, details=error_details
        )

    # Audio errors
    if error_code in (
        "AUDIO_FORMAT_ERROR",
        "UNSUPPORTED_AUDIO_FORMAT",
        "INVALID_SAMPLE_RATE",
        "AUDIO_DATA_CORRUPTED",
    ):
        return AudioError(error_message, code=error_code, details=error_details)

    # Service errors
    if error_code in (
        "SERVICE_UNAVAILABLE",
        "SERVICE_OVERLOADED",
        "INTERNAL_SERVER_ERROR",
    ):
        return ServiceError(error_message, code=error_code, details=error_details)

    # Protocol errors
    if error_code in (
        "PROTOCOL_ERROR",
        "INVALID_MESSAGE_FORMAT",
        "PROTOCOL_VERSION_MISMATCH",
    ):
        return ProtocolError(error_message, code=error_code, details=error_details)

    # Default to generic FunASR error
    return FunASRError(error_message, code=error_code, details=error_details)


def is_recoverable_error(error: FunASRError) -> bool:
    """Check if an error is recoverable.

    Args:
        error: The error to check

    Returns:
        True if the error is potentially recoverable
    """
    return error.recovery_action in (
        RecoveryAction.RETRY,
        RecoveryAction.RECONNECT,
        RecoveryAction.FALLBACK,
    )


def should_retry_error(error: FunASRError) -> bool:
    """Check if an error should trigger a retry.

    Args:
        error: The error to check

    Returns:
        True if the operation should be retried
    """
    return error.recovery_action in (
        RecoveryAction.RETRY,
        RecoveryAction.RECONNECT,
    )
