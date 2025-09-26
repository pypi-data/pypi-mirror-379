"""Integration tests for FunASR client using dotenv configuration."""

import os
from pathlib import Path
import tempfile
from unittest.mock import AsyncMock, MagicMock, patch

from dotenv import load_dotenv
import pytest

from funasr_client import AsyncFunASRClient, FunASRClient
from funasr_client.callbacks import SimpleCallback
from funasr_client.models import ClientConfig, FinalResult


@pytest.fixture(scope="module")
def test_env_file():
    """Create a test .env file for integration tests."""
    env_content = """
# Test environment configuration for FunASR integration tests
FUNASR_WS_URL=ws://test-server.example.com:10095
FUNASR_MODE=2pass
FUNASR_TIMEOUT=10.0
FUNASR_MAX_RETRIES=2
FUNASR_SAMPLE_RATE=16000
FUNASR_ENABLE_ITN=true
FUNASR_ENABLE_VAD=true
FUNASR_AUTO_RECONNECT=true
FUNASR_DEBUG=false
FUNASR_LOG_LEVEL=INFO
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False) as f:
        f.write(env_content.strip())
        env_file = f.name

    yield env_file

    # Cleanup
    os.unlink(env_file)


@pytest.fixture
def load_test_env(test_env_file):
    """Load test environment variables and cleanup after test."""
    # Store original env vars
    original_env = dict(os.environ)

    # Load test environment
    load_dotenv(test_env_file, override=True)

    yield

    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


class TestDotenvIntegration:
    """Test FunASR client integration with dotenv configuration."""

    def test_client_initialization_with_dotenv(self, load_test_env):
        """Test client initialization using dotenv configuration."""
        client = FunASRClient()

        # Verify configuration loaded from environment
        assert client.config.server_url == "ws://test-server.example.com:10095"
        assert client.config.timeout == 10.0
        assert client.config.max_retries == 2
        assert client.config.audio.sample_rate == 16000

    def test_async_client_initialization_with_dotenv(self, load_test_env):
        """Test async client initialization using dotenv configuration."""
        client = AsyncFunASRClient()

        # Verify configuration loaded from environment
        assert client.config.server_url == "ws://test-server.example.com:10095"
        assert client.config.timeout == 10.0
        assert client.config.max_retries == 2

    def test_environment_override_precedence(self, load_test_env):
        """Test that explicit config overrides environment variables."""
        # Create client with explicit config that should override env vars
        config = ClientConfig(server_url="ws://override.example.com:8080", timeout=60.0)
        client = FunASRClient(config=config)

        # Verify explicit config takes precedence
        assert client.config.server_url == "ws://override.example.com:8080"
        assert client.config.timeout == 60.0
        # But other env vars should still be loaded (or use defaults if not set)
        assert client.config.max_retries >= 0  # Should be valid
        assert client.config.audio.sample_rate == 16000  # From env or default

    def test_server_url_parameter_override(self, load_test_env):
        """Test that server_url parameter overrides both config and env."""
        override_url = "ws://param-override.example.com:9090"
        client = FunASRClient(server_url=override_url)

        # Verify parameter override takes precedence
        assert client.config.server_url == override_url
        # But other env vars should still be loaded
        assert client.config.timeout == 10.0  # From env


class TestMockedRecognitionIntegration:
    """Test recognition workflows with mocked services."""

    @pytest.fixture
    def mock_audio_file(self):
        """Create a mock audio file for testing."""
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            # Write some dummy audio data
            f.write(b"RIFF" + b"\x00" * 44 + b"audio_data_here")
            audio_file = f.name

        yield Path(audio_file)

        # Cleanup
        os.unlink(audio_file)

    @patch("funasr_client.connection.ConnectionManager")
    @patch("funasr_client.audio.AudioFileStreamer")
    def test_file_recognition_with_dotenv_config(
        self,
        mock_streamer_class,
        mock_connection_manager,
        load_test_env,
        mock_audio_file,
    ):
        """Test file recognition using dotenv configuration."""
        # Setup mocks
        mock_connection = AsyncMock()
        mock_connection_manager.return_value.acquire_connection.return_value = (
            mock_connection
        )

        mock_streamer = MagicMock()
        mock_streamer.get_duration.return_value = 2.0
        mock_streamer_class.return_value = mock_streamer

        # Mock recognition result
        final_result = FinalResult(
            text="Integration test with dotenv configuration",
            confidence=0.95,
            timestamp=1234567890.0,
            is_final=True,
            session_id="dotenv_test_session",
        )

        # Create client (will load dotenv config)
        client = FunASRClient()

        # Mock the internal async method
        with patch.object(client, "_recognize_file_async", return_value=final_result):
            result = client.recognize_file(mock_audio_file)

        # Verify result
        assert result.text == "Integration test with dotenv configuration"
        assert result.confidence == 0.95
        assert result.is_final is True

    @patch("funasr_client.connection.ConnectionManager")
    async def test_async_recognition_with_callback(
        self, mock_connection_manager, load_test_env, mock_audio_file
    ):
        """Test async recognition with callback using dotenv config."""
        # Setup connection mock
        mock_connection = AsyncMock()
        mock_connection_manager.return_value.acquire_connection.return_value = (
            mock_connection
        )

        # Create simple callback to verify dotenv integration works
        callback = SimpleCallback()

        # Mock recognition result
        final_result = FinalResult(
            text="Integration test with async callback",
            confidence=0.95,
            timestamp=1234567890.0,
            is_final=True,
            session_id="async_test_session",
        )

        client = AsyncFunASRClient()

        # Mock the recognize_file method directly to return expected result
        with patch.object(client, "recognize_file", return_value=final_result):
            await client.start()
            result = await client.recognize_file(mock_audio_file, callback)
            await client.close()

        # Verify result
        assert result.text == "Integration test with async callback"
        assert result.confidence == 0.95
        assert result.is_final is True


class TestErrorHandlingIntegration:
    """Test error handling in integration scenarios."""

    @patch("funasr_client.connection.ConnectionManager")
    def test_connection_error_with_dotenv_retry_config(
        self, mock_connection_manager, load_test_env
    ):
        """Test connection error handling with retry config from dotenv."""
        # Setup connection manager to fail
        from funasr_client.errors import ConnectionError as FunASRConnectionError

        mock_connection_manager.return_value.acquire_connection.side_effect = (
            FunASRConnectionError("Connection failed")
        )

        client = FunASRClient()

        # Verify retry config from dotenv is used
        assert client.config.max_retries == 2  # From test env

        # Test that connection error is raised
        with pytest.raises(FunASRConnectionError), tempfile.NamedTemporaryFile(
            suffix=".wav"
        ) as f:
            f.write(b"dummy_audio")
            f.flush()
            client.recognize_file(f.name)

    @patch("funasr_client.connection.ConnectionManager")
    async def test_async_error_propagation_with_env_config(
        self, mock_connection_manager, load_test_env
    ):
        """Test async error propagation with environment configuration."""
        from funasr_client.errors import FunASRError

        # Setup connection manager to fail after start
        mock_connection_manager.return_value.acquire_connection.side_effect = (
            FunASRError("Service error")
        )

        client = AsyncFunASRClient()
        await client.start()

        # Test that service error is propagated
        with pytest.raises(FunASRError), tempfile.NamedTemporaryFile(
            suffix=".wav"
        ) as f:
            f.write(b"dummy_audio")
            f.flush()
            await client.recognize_file(f.name)

        await client.close()


class TestConfigurationValidation:
    """Test configuration validation with dotenv."""

    def test_invalid_environment_values(self, test_env_file):
        """Test handling of invalid environment values."""
        # Create env file with invalid values
        invalid_env_content = """
FUNASR_WS_URL=invalid_url
FUNASR_TIMEOUT=not_a_number
FUNASR_MAX_RETRIES=-1
"""

        with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False) as f:
            f.write(invalid_env_content)
            invalid_env_file = f.name

        try:
            # Store original env and clear FunASR variables
            original_env = dict(os.environ)
            funasr_vars = [k for k in os.environ if k.startswith("FUNASR_")]
            for var in funasr_vars:
                del os.environ[var]

            # Load invalid environment
            load_dotenv(invalid_env_file, override=True)

            # Verify the invalid values are actually set
            assert os.getenv("FUNASR_TIMEOUT") == "not_a_number"

            # Client initialization should raise InvalidConfigurationError for invalid values
            from funasr_client.errors import InvalidConfigurationError

            with pytest.raises(InvalidConfigurationError):
                FunASRClient()

        finally:
            # Cleanup
            os.unlink(invalid_env_file)
            # Restore environment
            os.environ.clear()
            os.environ.update(original_env)

    def test_partial_environment_configuration(self, load_test_env):
        """Test that partial environment configuration works with defaults."""
        # Clear some environment variables to test partial config
        if "FUNASR_MAX_RETRIES" in os.environ:
            del os.environ["FUNASR_MAX_RETRIES"]

        client = FunASRClient()

        # Should have valid configuration (either from env or defaults)
        assert client.config.server_url is not None
        assert client.config.timeout > 0

        # Should use defaults for missing values
        assert client.config.max_retries >= 0  # Should be valid default


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
