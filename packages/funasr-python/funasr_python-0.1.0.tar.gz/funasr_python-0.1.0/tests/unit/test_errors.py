"""Unit tests for FunASR client error classes."""

import pytest

from funasr_client.errors import (
    AudioError,
    AuthenticationError,
    ClientError,
    ConnectionError,
    ConnectionTimeoutError,
    ErrorCategory,
    ErrorSeverity,
    FunASRError,
    InvalidConfigurationError,
    InvalidCredentialsError,
    InvalidMessageFormatError,
    InvalidSampleRateError,
    NetworkError,
    ProtocolError,
    RecoveryAction,
    ServiceError,
    TimeoutError,
    TokenExpiredError,
    UnsupportedAudioFormatError,
    is_recoverable_error,
    map_server_error,
    should_retry_error,
)


class TestFunASRError:
    """Test base FunASR error class."""

    def test_default_values(self):
        """Test default error values."""
        error = FunASRError("Test error")
        assert error.message == "Test error"
        assert error.code == "UNKNOWN_ERROR"
        assert error.category == ErrorCategory.CLIENT
        assert error.severity == ErrorSeverity.MEDIUM
        assert error.recovery_action == RecoveryAction.RETRY
        assert error.details == {}

    def test_custom_values(self):
        """Test custom error values."""
        details = {"key": "value"}
        error = FunASRError(
            message="Custom error",
            code="CUSTOM_ERROR",
            category=ErrorCategory.SERVICE,
            severity=ErrorSeverity.HIGH,
            recovery_action=RecoveryAction.RECONNECT,
            details=details,
        )

        assert error.message == "Custom error"
        assert error.code == "CUSTOM_ERROR"
        assert error.category == ErrorCategory.SERVICE
        assert error.severity == ErrorSeverity.HIGH
        assert error.recovery_action == RecoveryAction.RECONNECT
        assert error.details == details

    def test_string_representation(self):
        """Test string representation."""
        error = FunASRError("Test error", code="TEST_ERROR")
        assert str(error) == "[TEST_ERROR] Test error"

    def test_repr_representation(self):
        """Test repr representation."""
        error = FunASRError("Test error", code="TEST_ERROR")
        expected = "FunASRError(code='TEST_ERROR', category='client', severity='medium', message='Test error')"
        assert repr(error) == expected

    def test_to_dict(self):
        """Test dictionary conversion."""
        details = {"key": "value"}
        error = FunASRError(
            message="Test error",
            code="TEST_ERROR",
            details=details,
        )

        error_dict = error.to_dict()
        expected = {
            "error": {
                "code": "TEST_ERROR",
                "category": "client",
                "severity": "medium",
                "message": "Test error",
                "recovery_action": "retry",
                "details": details,
            }
        }
        assert error_dict == expected


class TestSpecificErrors:
    """Test specific error classes."""

    def test_connection_error(self):
        """Test ConnectionError class."""
        error = ConnectionError("Connection failed")
        assert error.category == ErrorCategory.CONNECTION
        assert error.recovery_action == RecoveryAction.RECONNECT
        assert error.severity == ErrorSeverity.HIGH
        assert error.code == "CONNECTION_ERROR"

    def test_connection_timeout_error(self):
        """Test ConnectionTimeoutError class."""
        error = ConnectionTimeoutError(30.0)
        assert error.category == ErrorCategory.CONNECTION
        assert error.recovery_action == RecoveryAction.RECONNECT
        assert error.code == "CONNECTION_TIMEOUT"
        assert error.details["timeout"] == 30.0
        assert "30.0 seconds" in error.message

    def test_timeout_error(self):
        """Test TimeoutError class."""
        error = TimeoutError("Operation timed out", 15.0)
        assert error.category == ErrorCategory.TIMEOUT
        assert error.recovery_action == RecoveryAction.RETRY
        assert error.severity == ErrorSeverity.MEDIUM
        assert error.details["timeout"] == 15.0

    def test_audio_error(self):
        """Test AudioError class."""
        error = AudioError("Invalid audio format")
        assert error.category == ErrorCategory.AUDIO
        assert error.recovery_action == RecoveryAction.FALLBACK
        assert error.severity == ErrorSeverity.MEDIUM
        assert error.code == "AUDIO_ERROR"

    def test_unsupported_audio_format_error(self):
        """Test UnsupportedAudioFormatError class."""
        error = UnsupportedAudioFormatError("mp3")
        assert isinstance(error, AudioError)
        assert error.code == "UNSUPPORTED_AUDIO_FORMAT"
        assert error.details["format"] == "mp3"
        assert "mp3" in error.message

    def test_invalid_sample_rate_error(self):
        """Test InvalidSampleRateError class."""
        error = InvalidSampleRateError(22050, [16000, 8000])
        assert isinstance(error, AudioError)
        assert error.code == "INVALID_SAMPLE_RATE"
        assert error.details["sample_rate"] == 22050
        assert error.details["supported_rates"] == [16000, 8000]

    def test_authentication_error(self):
        """Test AuthenticationError class."""
        error = AuthenticationError("Invalid credentials")
        assert error.category == ErrorCategory.AUTHENTICATION
        assert error.recovery_action == RecoveryAction.ABORT
        assert error.severity == ErrorSeverity.CRITICAL
        assert error.code == "AUTHENTICATION_ERROR"

    def test_invalid_credentials_error(self):
        """Test InvalidCredentialsError class."""
        error = InvalidCredentialsError()
        assert isinstance(error, AuthenticationError)
        assert error.code == "INVALID_CREDENTIALS"

    def test_token_expired_error(self):
        """Test TokenExpiredError class."""
        error = TokenExpiredError()
        assert isinstance(error, AuthenticationError)
        assert error.code == "TOKEN_EXPIRED"
        assert error.recovery_action == RecoveryAction.RETRY  # Override from base

    def test_protocol_error(self):
        """Test ProtocolError class."""
        error = ProtocolError("Invalid message format")
        assert error.category == ErrorCategory.PROTOCOL
        assert error.recovery_action == RecoveryAction.RETRY
        assert error.severity == ErrorSeverity.MEDIUM
        assert error.code == "PROTOCOL_ERROR"

    def test_invalid_message_format_error(self):
        """Test InvalidMessageFormatError class."""
        error = InvalidMessageFormatError("invalid json")
        assert isinstance(error, ProtocolError)
        assert error.code == "INVALID_MESSAGE_FORMAT"
        assert error.recovery_action == RecoveryAction.IGNORE

    def test_service_error(self):
        """Test ServiceError class."""
        error = ServiceError("Server error")
        assert error.category == ErrorCategory.SERVICE
        assert error.recovery_action == RecoveryAction.RETRY
        assert error.severity == ErrorSeverity.HIGH
        assert error.code == "SERVICE_ERROR"

    def test_network_error(self):
        """Test NetworkError class."""
        error = NetworkError("Network unavailable")
        assert error.category == ErrorCategory.NETWORK
        assert error.recovery_action == RecoveryAction.RETRY
        assert error.severity == ErrorSeverity.HIGH
        assert error.code == "NETWORK_ERROR"

    def test_client_error(self):
        """Test ClientError class."""
        error = ClientError("Client configuration error")
        assert error.category == ErrorCategory.CLIENT
        assert error.recovery_action == RecoveryAction.ABORT
        assert error.severity == ErrorSeverity.HIGH
        assert error.code == "CLIENT_ERROR"

    def test_invalid_configuration_error(self):
        """Test InvalidConfigurationError class."""
        error = InvalidConfigurationError("timeout", -1, "Timeout cannot be negative")
        assert isinstance(error, ClientError)
        assert error.code == "INVALID_CONFIGURATION"
        assert error.details["config_key"] == "timeout"
        assert error.details["config_value"] == "-1"
        assert error.details["reason"] == "Timeout cannot be negative"


class TestErrorUtilities:
    """Test error utility functions."""

    def test_is_recoverable_error(self):
        """Test recoverable error detection."""
        # Recoverable errors
        assert is_recoverable_error(NetworkError("Network error"))
        assert is_recoverable_error(ConnectionError("Connection failed"))
        assert is_recoverable_error(ServiceError("Server error"))
        assert is_recoverable_error(AudioError("Audio error"))  # Has FALLBACK action

        # Non-recoverable errors
        assert not is_recoverable_error(AuthenticationError("Invalid auth"))
        assert not is_recoverable_error(ClientError("Client error"))

        # Custom recovery actions
        custom_error = FunASRError("Test", recovery_action=RecoveryAction.RETRY)
        assert is_recoverable_error(custom_error)

        custom_error = FunASRError("Test", recovery_action=RecoveryAction.ABORT)
        assert not is_recoverable_error(custom_error)

    def test_should_retry_error(self):
        """Test retry detection."""
        # Retryable errors
        assert should_retry_error(NetworkError("Network error"))
        assert should_retry_error(ServiceError("Server error"))
        assert should_retry_error(ConnectionError("Connection failed"))

        # Non-retryable errors
        assert not should_retry_error(AudioError("Audio error"))  # FALLBACK action
        assert not should_retry_error(AuthenticationError("Invalid auth"))
        assert not should_retry_error(ClientError("Client error"))

        # Custom recovery actions
        custom_error = FunASRError("Test", recovery_action=RecoveryAction.RETRY)
        assert should_retry_error(custom_error)

        custom_error = FunASRError("Test", recovery_action=RecoveryAction.FALLBACK)
        assert not should_retry_error(custom_error)

    def test_map_server_error_with_error_dict(self):
        """Test error creation from server response with error dict."""
        response = {
            "code": "AUDIO_FORMAT_ERROR",
            "message": "Unsupported audio format",
            "details": {"expected_format": "pcm", "received_format": "unknown"},
        }

        error = map_server_error(response)
        assert isinstance(error, AudioError)
        assert error.code == "AUDIO_FORMAT_ERROR"
        assert error.message == "Unsupported audio format"
        assert error.details["expected_format"] == "pcm"

    def test_map_server_error_connection_errors(self):
        """Test mapping of connection errors."""
        response = {
            "code": "CONNECTION_TIMEOUT",
            "message": "Connection timed out",
        }
        error = map_server_error(response)
        assert isinstance(error, ConnectionError)
        assert error.code == "CONNECTION_TIMEOUT"

    def test_map_server_error_authentication_errors(self):
        """Test mapping of authentication errors."""
        response = {
            "code": "INVALID_CREDENTIALS",
            "message": "Invalid credentials provided",
        }
        error = map_server_error(response)
        assert isinstance(error, AuthenticationError)
        assert error.code == "INVALID_CREDENTIALS"

    def test_map_server_error_service_errors(self):
        """Test mapping of service errors."""
        response = {
            "code": "SERVICE_UNAVAILABLE",
            "message": "Service is temporarily unavailable",
        }
        error = map_server_error(response)
        assert isinstance(error, ServiceError)
        assert error.code == "SERVICE_UNAVAILABLE"

    def test_map_server_error_protocol_errors(self):
        """Test mapping of protocol errors."""
        response = {
            "code": "INVALID_MESSAGE_FORMAT",
            "message": "Message format is invalid",
        }
        error = map_server_error(response)
        assert isinstance(error, ProtocolError)
        assert error.code == "INVALID_MESSAGE_FORMAT"

    def test_map_server_error_unknown_error(self):
        """Test mapping of unknown errors."""
        response = {
            "code": "UNKNOWN_CUSTOM_ERROR",
            "message": "Something went wrong",
        }
        error = map_server_error(response)
        assert isinstance(error, FunASRError)
        assert error.code == "UNKNOWN_CUSTOM_ERROR"
        assert error.message == "Something went wrong"

    def test_map_server_error_missing_fields(self):
        """Test error creation with missing fields."""
        # Missing message
        response = {"code": "TEST_ERROR"}
        error = map_server_error(response)
        assert error.code == "TEST_ERROR"
        assert error.message == "Unknown error occurred"

        # Missing code
        response = {"message": "Test message"}
        error = map_server_error(response)
        assert error.code == "UNKNOWN_ERROR"
        assert error.message == "Test message"

        # Empty response
        response = {}
        error = map_server_error(response)
        assert error.code == "UNKNOWN_ERROR"
        assert error.message == "Unknown error occurred"


class TestErrorEnums:
    """Test error enum classes."""

    def test_error_category_values(self):
        """Test error category enum values."""
        assert ErrorCategory.CLIENT == "client"
        assert ErrorCategory.SERVICE == "service"
        assert ErrorCategory.NETWORK == "network"
        assert ErrorCategory.PROTOCOL == "protocol"
        assert ErrorCategory.CONNECTION == "connection"
        assert ErrorCategory.AUTHENTICATION == "authentication"
        assert ErrorCategory.AUDIO == "audio"
        assert ErrorCategory.TIMEOUT == "timeout"

    def test_error_severity_values(self):
        """Test error severity enum values."""
        assert ErrorSeverity.LOW == "low"
        assert ErrorSeverity.MEDIUM == "medium"
        assert ErrorSeverity.HIGH == "high"
        assert ErrorSeverity.CRITICAL == "critical"

    def test_recovery_action_values(self):
        """Test recovery action enum values."""
        assert RecoveryAction.RETRY == "retry"
        assert RecoveryAction.RECONNECT == "reconnect"
        assert RecoveryAction.FALLBACK == "fallback"
        assert RecoveryAction.ABORT == "abort"
        assert RecoveryAction.IGNORE == "ignore"


if __name__ == "__main__":
    pytest.main([__file__])
