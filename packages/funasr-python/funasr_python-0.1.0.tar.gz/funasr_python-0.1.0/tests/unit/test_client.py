"""Unit tests for FunASR client classes - simplified version."""

import pytest

from funasr_client.client import AsyncFunASRClient, FunASRClient
from funasr_client.models import ClientConfig


class TestFunASRClient:
    """Test synchronous FunASR client."""

    def test_init_default(self):
        """Test client initialization with defaults."""
        client = FunASRClient()
        assert hasattr(client, "config")
        assert hasattr(client, "audio_processor")

    def test_init_custom_config(self):
        """Test client initialization with custom config."""
        config = ClientConfig(server_url="ws://test.example.com:8080", timeout=60.0)
        client = FunASRClient(config=config)
        assert client.config.server_url == "ws://test.example.com:8080"
        assert client.config.timeout == 60.0


class TestAsyncFunASRClient:
    """Test asynchronous FunASR client."""

    def test_init_custom_config(self):
        """Test async client initialization with custom config."""
        config = ClientConfig(server_url="ws://async.example.com:8080", timeout=45.0)
        client = AsyncFunASRClient(config=config)
        assert client.config.server_url == "ws://async.example.com:8080"
        assert client.config.timeout == 45.0


class TestClientErrorHandling:
    """Test client error handling."""

    def test_recognition_error_handling(self):
        """Test recognition error handling."""
        from funasr_client.errors import FunASRError

        error = FunASRError("Recognition failed", severity="high")
        assert error.message == "Recognition failed"
        assert error.severity == "high"

    def test_audio_error_handling(self):
        """Test audio error handling."""
        from funasr_client.errors import AudioError

        error = AudioError("Audio processing failed")
        assert error.message == "Audio processing failed"


if __name__ == "__main__":
    pytest.main([__file__])
