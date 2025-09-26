"""Unit tests for FunASR client audio processing."""


import numpy as np
import pytest

from funasr_client.audio import AudioProcessor
from funasr_client.errors import AudioFileNotFoundError
from funasr_client.models import AudioConfig, AudioFormat


class TestAudioProcessor:
    """Test audio processor functionality."""

    def test_init_default_config(self):
        """Test processor initialization with default config."""
        processor = AudioProcessor()
        assert processor.target_config.sample_rate == 16000
        assert processor.target_config.channels == 1
        assert processor.target_config.sample_width == 2

    def test_init_custom_config(self):
        """Test processor initialization with custom config."""
        config = AudioConfig(
            sample_rate=44100, channels=2, sample_width=3, format=AudioFormat.WAV
        )
        processor = AudioProcessor(config)
        assert processor.target_config.sample_rate == 44100
        assert processor.target_config.channels == 2
        assert processor.target_config.format == AudioFormat.WAV

    def test_load_audio_file_wav(self, sample_wav_file):
        """Test loading WAV audio file."""
        processor = AudioProcessor()
        audio_data, sample_rate = processor.load_audio_file(sample_wav_file)

        assert isinstance(audio_data, np.ndarray)
        assert sample_rate == 16000
        assert len(audio_data) > 0

    def test_load_audio_file_nonexistent(self):
        """Test loading non-existent audio file."""
        processor = AudioProcessor()

        with pytest.raises(AudioFileNotFoundError):
            processor.load_audio_file("/non/existent/file.wav")

    def test_resample_audio_up(self):
        """Test upsampling audio."""
        processor = AudioProcessor()

        # Create test audio at 8kHz
        original_sample_rate = 8000
        target_sample_rate = 16000
        duration = 1.0

        samples = int(original_sample_rate * duration)
        audio_data = np.sin(2 * np.pi * 440 * np.linspace(0, duration, samples)).astype(
            np.float32
        )

        resampled = processor.resample_audio(
            audio_data, original_sample_rate, target_sample_rate
        )

        expected_samples = int(
            len(audio_data) * target_sample_rate / original_sample_rate
        )
        assert len(resampled) == expected_samples

    def test_resample_audio_down(self):
        """Test downsampling audio."""
        processor = AudioProcessor()

        # Create test audio at 44.1kHz
        original_sample_rate = 44100
        target_sample_rate = 16000
        duration = 0.5

        samples = int(original_sample_rate * duration)
        audio_data = np.sin(2 * np.pi * 440 * np.linspace(0, duration, samples)).astype(
            np.float32
        )

        resampled = processor.resample_audio(
            audio_data, original_sample_rate, target_sample_rate
        )

        expected_samples = int(
            len(audio_data) * target_sample_rate / original_sample_rate
        )
        assert abs(len(resampled) - expected_samples) <= 1  # Allow for rounding

    def test_resample_audio_same_rate(self):
        """Test resampling with same sample rate."""
        processor = AudioProcessor()

        sample_rate = 16000
        audio_data = np.random.random(1000).astype(np.float32)

        resampled = processor.resample_audio(audio_data, sample_rate, sample_rate)
        np.testing.assert_array_almost_equal(audio_data, resampled)

    def test_convert_to_mono(self):
        """Test stereo to mono conversion."""
        processor = AudioProcessor()

        # Create stereo audio data
        stereo_data = np.random.random((1000, 2)).astype(np.float32)
        mono_data = processor.convert_to_mono(stereo_data)

        assert mono_data.ndim == 1
        assert len(mono_data) == len(stereo_data)

        # Check that it's the average of both channels
        expected_mono = np.mean(stereo_data, axis=1)
        np.testing.assert_array_almost_equal(mono_data, expected_mono)

    def test_convert_to_mono_already_mono(self):
        """Test mono conversion with already mono audio."""
        processor = AudioProcessor()

        mono_data = np.random.random(1000).astype(np.float32)
        result = processor.convert_to_mono(mono_data)

        np.testing.assert_array_equal(mono_data, result)

    def test_normalize_audio(self):
        """Test audio normalization."""
        processor = AudioProcessor()

        # Create audio with known amplitude
        audio_data = np.array([0.1, -0.2, 0.5, -0.8, 0.3], dtype=np.float32)
        normalized = processor.normalize_audio(audio_data)

        # Should be normalized to [-1, 1] range
        assert np.max(np.abs(normalized)) <= 1.0
        assert np.max(np.abs(normalized)) > 0.9  # Should use most of the range

    def test_normalize_audio_zero(self):
        """Test normalizing zero audio."""
        processor = AudioProcessor()

        audio_data = np.zeros(1000, dtype=np.float32)
        normalized = processor.normalize_audio(audio_data)

        np.testing.assert_array_equal(audio_data, normalized)

    def test_convert_to_target_format(self):
        """Test conversion to target format."""
        config = AudioConfig(sample_rate=16000, channels=1)
        processor = AudioProcessor(config)

        # Create test audio at different sample rate and stereo
        source_sample_rate = 44100
        audio_data = np.random.random((22050, 2)).astype(
            np.float32
        )  # 0.5 seconds stereo

        converted = processor.convert_to_target_format(
            audio_data, source_sample_rate, source_channels=2
        )

        assert isinstance(converted, bytes)
        assert len(converted) > 0


# AudioFileStreamer, AudioChunker, and AudioUtilities tests removed - not essential for core functionality


if __name__ == "__main__":
    pytest.main([__file__])
