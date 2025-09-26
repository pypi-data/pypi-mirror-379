"""Test configuration and fixtures for FunASR client."""

import asyncio
import os
from pathlib import Path
import tempfile
from typing import Any, Dict, Generator
from unittest.mock import AsyncMock, MagicMock

import numpy as np
import pytest

from funasr_client import (
    AudioConfig,
    ClientConfig,
    ConfigPresets,
)


@pytest.fixture
def event_loop():
    """Create an event loop for async tests."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def basic_config() -> ClientConfig:
    """Basic client configuration for testing."""
    return ClientConfig(
        server_url="ws://localhost:10095",
        timeout=10.0,
        max_retries=2,
        auto_reconnect=False,
        debug=True,
    )


@pytest.fixture
def audio_config() -> AudioConfig:
    """Basic audio configuration for testing."""
    return AudioConfig(
        sample_rate=16000,
        channels=1,
        sample_width=2,
    )


@pytest.fixture
def mock_websocket():
    """Mock WebSocket connection."""
    mock = AsyncMock()
    mock.closed = False
    mock.close = AsyncMock()
    mock.send = AsyncMock()
    mock.recv = AsyncMock()
    return mock


@pytest.fixture
def sample_audio_data() -> bytes:
    """Generate sample 16-bit PCM audio data."""
    # Generate 1 second of sine wave at 440Hz, 16kHz sample rate
    sample_rate = 16000
    duration = 1.0
    frequency = 440.0

    samples = int(sample_rate * duration)
    t = np.linspace(0, duration, samples, dtype=np.float32)
    audio = np.sin(2 * np.pi * frequency * t) * 0.5

    # Convert to 16-bit PCM
    audio_int16 = (audio * 32767).astype(np.int16)
    return audio_int16.tobytes()


@pytest.fixture
def sample_audio_file(sample_audio_data: bytes) -> Generator[Path, None, None]:
    """Create a temporary audio file for testing."""
    with tempfile.NamedTemporaryFile(suffix=".pcm", delete=False) as f:
        f.write(sample_audio_data)
        temp_path = Path(f.name)

    yield temp_path

    # Clean up
    if temp_path.exists():
        temp_path.unlink()


@pytest.fixture
def sample_wav_file(sample_audio_data: bytes) -> Generator[Path, None, None]:
    """Create a temporary WAV file for testing."""
    import wave

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        temp_path = Path(f.name)

    # Write WAV file
    with wave.open(str(temp_path), "wb") as wav_file:
        wav_file.setnchannels(1)  # mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(16000)  # 16kHz
        wav_file.writeframes(sample_audio_data)

    yield temp_path

    # Clean up
    if temp_path.exists():
        temp_path.unlink()


@pytest.fixture
def mock_server_response() -> Dict[str, Any]:
    """Mock server response message."""
    return {
        "mode": "2pass",
        "text": "<|zh|>你好世界",
        "timestamp": "[[0.0, 1.2]]",
        "is_final": False,
        "wav_name": "test_audio",
        "confidence": 0.95,
    }


@pytest.fixture
def mock_final_response() -> Dict[str, Any]:
    """Mock final server response message."""
    return {
        "mode": "2pass",
        "text": "<|zh|>你好世界",
        "timestamp": "[[0.0, 1.2]]",
        "is_final": True,
        "wav_name": "test_audio",
        "confidence": 0.98,
    }


@pytest.fixture
def mock_error_response() -> Dict[str, Any]:
    """Mock server error response."""
    return {
        "error": {
            "code": "AUDIO_FORMAT_ERROR",
            "message": "Unsupported audio format",
            "details": {"expected_format": "pcm", "received_format": "unknown"},
        }
    }


@pytest.fixture(params=["low_latency", "high_accuracy", "balanced"])
def config_preset(request) -> ClientConfig:
    """Parametrized fixture for different configuration presets."""
    preset_name = request.param
    return getattr(ConfigPresets, preset_name)()


@pytest.fixture
def temp_config_file() -> Generator[Path, None, None]:
    """Create a temporary configuration file."""
    config_data = {
        "server_url": "ws://test.example.com:8080",
        "timeout": 15.0,
        "mode": "online",
        "audio": {"sample_rate": 44100, "channels": 2},
    }

    import json

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(config_data, f)
        temp_path = Path(f.name)

    yield temp_path

    # Clean up
    if temp_path.exists():
        temp_path.unlink()


@pytest.fixture
def mock_connection():
    """Mock connection object."""
    from funasr_client.connection import Connection

    mock_protocol = MagicMock()
    mock_protocol.is_connected = True
    mock_protocol.get_connection_stats.return_value = {
        "state": "connected",
        "message_count": 10,
        "error_count": 0,
    }

    connection = Connection("test_conn_1", mock_protocol)
    return connection


class MockRecognitionCallback:
    """Mock callback for testing recognition events."""

    def __init__(self):
        self.partial_results = []
        self.final_results = []
        self.sentence_results = []
        self.errors = []
        self.status_changes = []

    def on_partial_result(self, result):
        self.partial_results.append(result)

    def on_final_result(self, result):
        self.final_results.append(result)

    def on_sentence_end(self, result):
        self.sentence_results.append(result)

    def on_error(self, error):
        self.errors.append(error)

    def on_connection_status(self, status):
        self.status_changes.append(status)


@pytest.fixture
def mock_callback():
    """Mock callback instance for testing."""
    return MockRecognitionCallback()


# Skip tests that require external dependencies
def skip_if_no_pyaudio():
    """Skip test if PyAudio is not available."""
    try:
        import pyaudio  # noqa: F401

        return False
    except ImportError:
        return True


def skip_if_no_server():
    """Skip test if FunASR server is not available."""
    # In a real implementation, you might ping the server
    # For now, just check if we're in CI or have the env var set
    return os.environ.get("FUNASR_TEST_SERVER_AVAILABLE", "").lower() not in (
        "1",
        "true",
        "yes",
    )


# Markers for test categorization
pytestmark = [
    pytest.mark.asyncio,
]


# Test data directories
FIXTURES_DIR = Path(__file__).parent / "fixtures"
AUDIO_FIXTURES_DIR = FIXTURES_DIR / "audio"
CONFIG_FIXTURES_DIR = FIXTURES_DIR / "config"

# Ensure fixture directories exist
FIXTURES_DIR.mkdir(exist_ok=True)
AUDIO_FIXTURES_DIR.mkdir(exist_ok=True)
CONFIG_FIXTURES_DIR.mkdir(exist_ok=True)
