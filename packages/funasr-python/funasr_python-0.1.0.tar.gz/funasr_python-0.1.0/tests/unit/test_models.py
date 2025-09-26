"""Unit tests for FunASR client models."""

import json

import pytest

from funasr_client.models import (
    AudioConfig,
    AudioFormat,
    ClientConfig,
    ConfigPresets,
    ConnectionMetrics,
    ConnectionState,
    FinalResult,
    FunASRInitMessage,
    FunASRResponse,
    PartialResult,
    RealtimeSession,
    RecognitionMode,
    SentenceResult,
    WordResult,
)


class TestAudioConfig:
    """Test AudioConfig class."""

    def test_default_values(self):
        """Test default audio configuration values."""
        config = AudioConfig()
        assert config.sample_rate == 16000
        assert config.channels == 1
        assert config.sample_width == 2
        assert config.format == AudioFormat.PCM

    def test_custom_values(self):
        """Test custom audio configuration values."""
        config = AudioConfig(
            sample_rate=44100, channels=2, sample_width=3, format=AudioFormat.WAV
        )
        assert config.sample_rate == 44100
        assert config.channels == 2
        assert config.sample_width == 3
        assert config.format == AudioFormat.WAV


class TestClientConfig:
    """Test ClientConfig class."""

    def test_default_values(self):
        """Test default client configuration values."""
        config = ClientConfig()
        assert config.server_url == "ws://localhost:10095"
        assert config.timeout == 30.0
        assert config.max_retries == 3
        assert config.mode == RecognitionMode.TWO_PASS
        assert config.enable_itn is True
        assert config.auto_reconnect is True

    def test_to_init_message(self):
        """Test conversion to FunASR init message."""
        config = ClientConfig()
        init_msg = config.to_init_message("test_session")

        assert init_msg.mode == RecognitionMode.TWO_PASS
        assert init_msg.wav_name == "test_session"
        assert init_msg.audio_fs == 16000
        assert init_msg.is_speaking is True
        assert init_msg.itn is True

    def test_hotwords_conversion(self):
        """Test hotwords dictionary conversion."""
        config = ClientConfig(hotwords={"hello": 10, "world": 5})
        init_msg = config.to_init_message()

        hotwords_dict = json.loads(init_msg.hotwords)
        assert hotwords_dict == {"hello": 10, "world": 5}


class TestConfigPresets:
    """Test configuration presets."""

    def test_low_latency_preset(self):
        """Test low latency preset configuration."""
        config = ConfigPresets.low_latency()
        assert config.mode == RecognitionMode.ONLINE
        assert config.chunk_size == [1, 6, 1]
        assert config.chunk_interval == 5
        assert config.enable_vad is True
        assert config.timeout == 10.0

    def test_high_accuracy_preset(self):
        """Test high accuracy preset configuration."""
        config = ConfigPresets.high_accuracy()
        assert config.mode == RecognitionMode.TWO_PASS
        assert config.chunk_size == [5, 10, 5]
        assert config.enable_itn is True
        assert config.enable_punctuation is True
        assert config.timeout == 60.0

    def test_balanced_preset(self):
        """Test balanced preset configuration."""
        config = ConfigPresets.balanced()
        assert config.mode == RecognitionMode.TWO_PASS
        assert config.chunk_size == [3, 8, 3]
        assert config.chunk_interval == 8
        assert config.timeout == 30.0


class TestFunASRInitMessage:
    """Test FunASR initialization message."""

    def test_default_values(self):
        """Test default initialization message values."""
        msg = FunASRInitMessage()
        assert msg.mode == RecognitionMode.TWO_PASS
        assert msg.chunk_size == [5, 10, 5]
        assert msg.chunk_interval == 10
        assert msg.wav_format == AudioFormat.PCM
        assert msg.audio_fs == 16000
        assert msg.is_speaking is True

    def test_model_dump(self):
        """Test model serialization."""
        msg = FunASRInitMessage(
            wav_name="test_audio", mode=RecognitionMode.ONLINE, hotwords='{"test": 15}'
        )
        data = msg.model_dump()

        assert data["wav_name"] == "test_audio"
        assert data["mode"] == "online"
        assert data["hotwords"] == '{"test": 15}'
        assert data["is_speaking"] is True

    def test_validation(self):
        """Test field validation."""
        # Test valid values
        msg = FunASRInitMessage(
            chunk_interval=50, audio_fs=44100, encoder_chunk_look_back=8
        )
        assert msg.chunk_interval == 50
        assert msg.audio_fs == 44100
        assert msg.encoder_chunk_look_back == 8


class TestFunASRResponse:
    """Test FunASR response message."""

    def test_default_values(self):
        """Test default response values."""
        response = FunASRResponse()
        assert response.text == ""
        assert response.timestamp == "[]"
        assert response.is_final is False
        assert response.confidence is None

    def test_with_data(self):
        """Test response with actual data."""
        response = FunASRResponse(
            mode="2pass",
            text="<|zh|>你好世界",
            timestamp="[[0.0, 1.2]]",
            is_final=True,
            confidence=0.95,
            wav_name="test_audio",
        )

        assert response.mode == "2pass"
        assert response.text == "<|zh|>你好世界"
        assert response.timestamp == "[[0.0, 1.2]]"
        assert response.is_final is True
        assert response.confidence == 0.95
        assert response.wav_name == "test_audio"


class TestRecognitionResults:
    """Test recognition result classes."""

    def test_partial_result(self):
        """Test partial result creation."""
        result = PartialResult(
            text="Hello",
            confidence=0.8,
            timestamp=1234567890.0,
            is_final=False,
            session_id="session_1",
            start_time=0.0,
            end_time=1.5,
        )

        assert result.text == "Hello"
        assert result.confidence == 0.8
        assert result.is_final is False
        assert result.session_id == "session_1"
        assert result.start_time == 0.0
        assert result.end_time == 1.5

    def test_final_result(self):
        """Test final result creation."""
        result = FinalResult(
            text="Hello world",
            confidence=0.95,
            timestamp=1234567890.0,
            is_final=True,
            session_id="session_1",
            alternatives=["Hi world", "Hello world!"],
            speaker_id="speaker_001",
        )

        assert result.text == "Hello world"
        assert result.confidence == 0.95
        assert result.is_final is True
        assert result.alternatives == ["Hi world", "Hello world!"]
        assert result.speaker_id == "speaker_001"

    def test_sentence_result(self):
        """Test sentence result creation."""
        words = [
            WordResult("Hello", 0.0, 0.5, 0.9),
            WordResult("world", 0.6, 1.0, 0.85),
        ]

        result = SentenceResult(
            text="Hello world",
            confidence=0.88,
            timestamp=1234567890.0,
            is_final=True,
            session_id="session_1",
            sentence_id=1,
            words=words,
        )

        assert result.text == "Hello world"
        assert result.sentence_id == 1
        assert len(result.words) == 2
        assert result.words[0].word == "Hello"
        assert result.words[1].confidence == 0.85

    def test_word_result(self):
        """Test word result creation."""
        word = WordResult(word="test", start_time=1.0, end_time=1.5, confidence=0.92)

        assert word.word == "test"
        assert word.start_time == 1.0
        assert word.end_time == 1.5
        assert word.confidence == 0.92


class TestConnectionMetrics:
    """Test connection metrics."""

    def test_default_values(self):
        """Test default metrics values."""
        metrics = ConnectionMetrics()
        assert metrics.connection_time == 0.0
        assert metrics.message_count == 0
        assert metrics.error_count == 0
        assert metrics.reconnection_count == 0

    def test_real_time_factor_calculation(self):
        """Test real-time factor calculation."""
        metrics = ConnectionMetrics(total_processing_time=1.5, total_audio_duration=3.0)
        assert metrics.real_time_factor == 0.5

    def test_real_time_factor_zero_duration(self):
        """Test real-time factor with zero duration."""
        metrics = ConnectionMetrics(total_processing_time=1.0, total_audio_duration=0.0)
        assert metrics.real_time_factor == 0.0

    def test_success_rate_calculation(self):
        """Test success rate calculation."""
        metrics = ConnectionMetrics(message_count=8, error_count=2)
        assert metrics.success_rate == 80.0

    def test_success_rate_no_requests(self):
        """Test success rate with no requests."""
        metrics = ConnectionMetrics(message_count=0, error_count=0)
        assert metrics.success_rate == 1.0


class TestRealtimeSession:
    """Test real-time session."""

    def test_session_creation(self):
        """Test session creation."""
        session = RealtimeSession(session_id="test_session")
        assert session.session_id == "test_session"
        assert session.is_active is True
        assert isinstance(session.metrics, ConnectionMetrics)

    def test_end_session(self):
        """Test ending a session."""
        session = RealtimeSession(session_id="test_session")
        assert session.is_active is True

        session.end_session()
        assert session.is_active is False


class TestEnums:
    """Test enum classes."""

    def test_recognition_mode_values(self):
        """Test recognition mode enum values."""
        assert RecognitionMode.OFFLINE == "offline"
        assert RecognitionMode.ONLINE == "online"
        assert RecognitionMode.TWO_PASS == "2pass"

    def test_connection_state_values(self):
        """Test connection state enum values."""
        assert ConnectionState.DISCONNECTED == "disconnected"
        assert ConnectionState.CONNECTING == "connecting"
        assert ConnectionState.CONNECTED == "connected"
        assert ConnectionState.RECOGNIZING == "recognizing"
        assert ConnectionState.FINALIZING == "finalizing"
        assert ConnectionState.ERROR == "error"

    def test_audio_format_values(self):
        """Test audio format enum values."""
        assert AudioFormat.PCM == "pcm"
        assert AudioFormat.WAV == "wav"
        assert AudioFormat.MP3 == "mp3"
        assert AudioFormat.M4A == "m4a"
        assert AudioFormat.FLAC == "flac"
        assert AudioFormat.OGG == "ogg"


if __name__ == "__main__":
    pytest.main([__file__])
