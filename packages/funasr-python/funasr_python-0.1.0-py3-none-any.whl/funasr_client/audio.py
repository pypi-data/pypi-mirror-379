"""Audio processing utilities for FunASR client."""

from __future__ import annotations

import asyncio
import logging
from pathlib import Path
import struct
from typing import Any, AsyncIterator, Dict, Iterator, Optional, Tuple, Union

import librosa
import numpy as np

from .errors import (
    AudioDataCorruptedError,
    AudioFileNotFoundError,
    InvalidSampleRateError,
    UnsupportedAudioFormatError,
)
from .models import AudioConfig, AudioFormat


class AudioProcessor:
    """Handles audio format conversion and preprocessing."""

    def __init__(self, target_config: Optional[AudioConfig] = None) -> None:
        """Initialize audio processor.

        Args:
            target_config: Target audio configuration (default: 16kHz, mono, 16-bit)
        """
        self.target_config = target_config or AudioConfig()
        self.logger = logging.getLogger(__name__)

    def load_audio_file(self, file_path: Union[str, Path]) -> Tuple[np.ndarray, int]:
        """Load audio file and return audio data and sample rate.

        Args:
            file_path: Path to audio file

        Returns:
            Tuple of (audio_data, sample_rate)

        Raises:
            AudioFileNotFoundError: If file doesn't exist
            UnsupportedAudioFormatError: If format is not supported
            AudioDataCorruptedError: If file is corrupted
        """
        file_path = Path(file_path)

        if not file_path.exists():
            raise AudioFileNotFoundError(str(file_path))

        try:
            # Use librosa for robust audio loading
            audio_data, sample_rate = librosa.load(
                str(file_path),
                sr=None,  # Keep original sample rate
                mono=False,  # Keep original channels
                dtype=np.float32,
            )

            self.logger.debug(
                f"Loaded audio file: {file_path.name}, "
                f"shape: {audio_data.shape}, "
                f"sample_rate: {sample_rate}"
            )

            return audio_data, sample_rate

        except Exception as e:
            if "format not recognized" in str(e).lower():
                raise UnsupportedAudioFormatError(file_path.suffix) from e
            else:
                raise AudioDataCorruptedError(f"Failed to load audio file: {e}") from e

    def convert_to_target_format(
        self,
        audio_data: np.ndarray,
        source_sample_rate: int,
        source_channels: Optional[int] = None,
    ) -> bytes:
        """Convert audio data to target format.

        Args:
            audio_data: Input audio data (float32)
            source_sample_rate: Source sample rate
            source_channels: Number of source channels (inferred if None)

        Returns:
            Audio data in target format (PCM bytes)

        Raises:
            InvalidSampleRateError: If sample rate conversion fails
        """
        # Infer channels if not provided
        if source_channels is None:
            source_channels = 1 if audio_data.ndim == 1 else audio_data.shape[0]

        try:
            # Convert to mono if needed
            if source_channels > 1 and self.target_config.channels == 1:
                audio_data = self._stereo_to_mono(audio_data)
            elif source_channels == 1 and self.target_config.channels == 2:
                audio_data = self._mono_to_stereo(audio_data)

            # Resample if needed
            if source_sample_rate != self.target_config.sample_rate:
                audio_data = self._resample_audio(
                    audio_data, source_sample_rate, self.target_config.sample_rate
                )

            # Convert to target bit depth
            pcm_data = self._float_to_pcm(audio_data, self.target_config.sample_width)

            return pcm_data

        except Exception as e:
            raise AudioDataCorruptedError(f"Audio format conversion failed: {e}") from e

    def validate_audio_data(self, audio_data: bytes) -> bool:
        """Validate audio data integrity.

        Args:
            audio_data: Audio data to validate

        Returns:
            True if audio data is valid

        Raises:
            AudioDataCorruptedError: If audio data is invalid
        """
        if not audio_data:
            raise AudioDataCorruptedError("Empty audio data")

        # Check if length is compatible with sample width
        expected_sample_size = (
            self.target_config.sample_width * self.target_config.channels
        )
        if len(audio_data) % expected_sample_size != 0:
            raise AudioDataCorruptedError(
                f"Audio data length {len(audio_data)} is not compatible with "
                f"sample size {expected_sample_size}"
            )

        # Convert to samples and check for valid range
        try:
            if self.target_config.sample_width == 2:  # 16-bit
                samples = struct.unpack(f"<{len(audio_data) // 2}h", audio_data)
                # Check for reasonable amplitude range
                max_sample = max(abs(s) for s in samples)
                if max_sample > 32767:
                    raise AudioDataCorruptedError(
                        f"Sample amplitude {max_sample} exceeds 16-bit range"
                    )

        except struct.error as e:
            raise AudioDataCorruptedError(f"Invalid audio data format: {e}") from e

        return True

    def create_wav_header(self, data_size: int) -> bytes:
        """Create WAV file header.

        Args:
            data_size: Size of audio data in bytes

        Returns:
            WAV header bytes
        """
        # WAV header format
        sample_rate = self.target_config.sample_rate
        channels = self.target_config.channels
        sample_width = self.target_config.sample_width

        byte_rate = sample_rate * channels * sample_width
        block_align = channels * sample_width

        header = struct.pack(
            "<4sL4s4sLHHLLHH4sL",
            b"RIFF",
            36 + data_size,  # File size - 8 bytes
            b"WAVE",
            b"fmt ",
            16,  # Subchunk1Size (PCM)
            1,  # AudioFormat (PCM)
            channels,
            sample_rate,
            byte_rate,
            block_align,
            sample_width * 8,  # BitsPerSample
            b"data",
            data_size,
        )

        return header

    def _stereo_to_mono(self, stereo_audio: np.ndarray) -> np.ndarray:
        """Convert stereo to mono audio.

        Args:
            stereo_audio: Stereo audio data

        Returns:
            Mono audio data
        """
        if stereo_audio.ndim == 1:
            return stereo_audio

        # Average the channels
        return np.mean(stereo_audio, axis=0 if stereo_audio.shape[0] == 2 else 1)

    def _mono_to_stereo(self, mono_audio: np.ndarray) -> np.ndarray:
        """Convert mono to stereo audio.

        Args:
            mono_audio: Mono audio data

        Returns:
            Stereo audio data
        """
        if mono_audio.ndim == 2:
            return mono_audio

        # Duplicate the channel
        return np.stack([mono_audio, mono_audio], axis=0)

    def _resample_audio(
        self, audio_data: np.ndarray, source_sr: int, target_sr: int
    ) -> np.ndarray:
        """Resample audio data.

        Args:
            audio_data: Input audio data
            source_sr: Source sample rate
            target_sr: Target sample rate

        Returns:
            Resampled audio data
        """
        if source_sr == target_sr:
            return audio_data

        try:
            return librosa.resample(audio_data, orig_sr=source_sr, target_sr=target_sr)
        except Exception as e:
            raise InvalidSampleRateError(
                target_sr, [8000, 16000, 22050, 44100, 48000], details={"error": str(e)}
            ) from e

    def _float_to_pcm(self, audio_data: np.ndarray, sample_width: int) -> bytes:
        """Convert float audio data to PCM bytes.

        Args:
            audio_data: Float audio data (-1.0 to 1.0)
            sample_width: Target sample width in bytes

        Returns:
            PCM audio data as bytes
        """
        # Clip to valid range
        audio_data = np.clip(audio_data, -1.0, 1.0)

        if sample_width == 1:  # 8-bit unsigned
            pcm_data = ((audio_data + 1.0) * 127.5).astype(np.uint8)
            return pcm_data.tobytes()
        elif sample_width == 2:  # 16-bit signed
            pcm_data = (audio_data * 32767).astype(np.int16)
            return pcm_data.tobytes()
        elif sample_width == 3:  # 24-bit signed
            pcm_data = (audio_data * 8388607).astype(np.int32)
            # Convert to 24-bit (3 bytes per sample)
            bytes_data = []
            for sample in pcm_data.flatten():  # Flatten to ensure 1-dimensional
                # Convert numpy scalar to Python int before calling to_bytes
                sample_int = int(sample.item())  # Use .item() to extract scalar
                bytes_data.extend(
                    sample_int.to_bytes(3, byteorder="little", signed=True)
                )
            return bytes(bytes_data)
        elif sample_width == 4:  # 32-bit signed
            pcm_data = (audio_data * 2147483647).astype(np.int32)
            return pcm_data.tobytes()
        else:
            raise ValueError(f"Unsupported sample width: {sample_width}")

    def resample_audio(
        self, audio_data: np.ndarray, source_rate: int, target_rate: int
    ) -> np.ndarray:
        """Public wrapper for resampling audio."""
        return self._resample_audio(audio_data, source_rate, target_rate)

    def convert_to_mono(self, audio_data: np.ndarray) -> np.ndarray:
        """Public wrapper for converting stereo to mono."""
        if len(audio_data.shape) == 1:
            return audio_data  # Already mono
        return self._stereo_to_mono(audio_data)

    def normalize_audio(self, audio_data: np.ndarray) -> np.ndarray:
        """Normalize audio data to [-1, 1] range."""
        if np.max(np.abs(audio_data)) == 0:
            return audio_data  # Avoid division by zero
        return audio_data / np.max(np.abs(audio_data))

    def bytes_to_numpy(self, audio_bytes: bytes, sample_width: int = 2) -> np.ndarray:
        """Convert audio bytes to numpy array."""
        if sample_width == 1:
            dtype = np.uint8
            normalization = 128.0
        elif sample_width == 2:
            dtype = np.int16
            normalization = 32768.0
        elif sample_width == 4:
            dtype = np.int32
            normalization = 2147483648.0
        else:
            raise ValueError(f"Unsupported sample width: {sample_width}")

        audio_array = np.frombuffer(audio_bytes, dtype=dtype)
        return audio_array.astype(np.float32) / normalization

    def numpy_to_bytes(self, audio_data: np.ndarray, sample_width: int = 2) -> bytes:
        """Convert numpy array to audio bytes."""
        return self._float_to_pcm(audio_data, sample_width)

    def apply_gain(self, audio_data: np.ndarray, gain_db: float) -> np.ndarray:
        """Apply gain to audio data."""
        gain_linear = 10 ** (gain_db / 20.0)
        return audio_data * gain_linear

    def detect_clipping(self, audio_data: np.ndarray, threshold: float = 0.99) -> bool:
        """Detect if audio data is clipped."""
        return np.any(np.abs(audio_data) >= threshold)


class AudioChunker:
    """Splits audio data into chunks for streaming."""

    def __init__(
        self,
        chunk_size: int = 3200,  # bytes (100ms at 16kHz, 16-bit, mono)
        overlap: int = 0,  # bytes of overlap between chunks
    ) -> None:
        """Initialize audio chunker.

        Args:
            chunk_size: Size of each chunk in bytes
            overlap: Overlap between consecutive chunks in bytes
        """
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.remainder = b""

    def chunk_audio(self, audio_data: bytes) -> Iterator[bytes]:
        """Split audio data into chunks.

        Args:
            audio_data: Input audio data

        Yields:
            Audio chunks
        """
        # Combine with remainder from previous call
        audio_data = self.remainder + audio_data

        step_size = self.chunk_size - self.overlap
        offset = 0

        while offset + self.chunk_size <= len(audio_data):
            chunk = audio_data[offset : offset + self.chunk_size]
            yield chunk
            offset += step_size

        # Store remainder for next call
        self.remainder = audio_data[offset:]

    def get_remainder(self) -> bytes:
        """Get remaining audio data.

        Returns:
            Remaining audio data that didn't fill a complete chunk
        """
        remainder = self.remainder
        self.remainder = b""
        return remainder

    async def chunk_audio_async(
        self, audio_stream: AsyncIterator[bytes]
    ) -> AsyncIterator[bytes]:
        """Asynchronously chunk audio stream.

        Args:
            audio_stream: Async audio data stream

        Yields:
            Audio chunks
        """
        async for audio_data in audio_stream:
            for chunk in self.chunk_audio(audio_data):
                yield chunk

        # Yield final remainder if exists
        remainder = self.get_remainder()
        if remainder:
            yield remainder


class AudioFileStreamer:
    """Streams audio file data in chunks."""

    def __init__(
        self,
        file_path: Union[str, Path],
        chunk_duration: float = 0.1,  # seconds
        simulate_realtime: bool = False,
        target_config: Optional[AudioConfig] = None,
    ) -> None:
        """Initialize audio file streamer.

        Args:
            file_path: Path to audio file
            chunk_duration: Duration of each chunk in seconds
            simulate_realtime: Whether to simulate real-time playback speed
            target_config: Target audio configuration
        """
        self.file_path = Path(file_path)
        self.chunk_duration = chunk_duration
        self.simulate_realtime = simulate_realtime
        self.target_config = target_config or AudioConfig()

        self.processor = AudioProcessor(self.target_config)
        self.total_duration: Optional[float] = None
        self.processed_audio: Optional[bytes] = None

    async def stream_audio(self) -> AsyncIterator[bytes]:
        """Stream audio file data in chunks.

        Yields:
            Audio data chunks

        Raises:
            AudioFileNotFoundError: If file doesn't exist
            AudioDataCorruptedError: If file is corrupted
        """
        # Load and convert audio file
        if self.processed_audio is None:
            await self._prepare_audio()

        chunk_size_bytes = int(
            self.chunk_duration
            * self.target_config.sample_rate
            * self.target_config.channels
            * self.target_config.sample_width
        )

        offset = 0

        while offset < len(self.processed_audio):
            chunk_end = min(offset + chunk_size_bytes, len(self.processed_audio))
            chunk = self.processed_audio[offset:chunk_end]

            yield chunk

            # Simulate real-time playback if requested
            if self.simulate_realtime:
                await asyncio.sleep(self.chunk_duration)

            offset = chunk_end

    def stream_audio_sync(self) -> Iterator[bytes]:
        """Synchronously stream audio file data in chunks.

        Yields:
            Audio data chunks
        """
        # Load and convert audio file synchronously
        if self.processed_audio is None:
            self._prepare_audio_sync()

        chunk_size_bytes = int(
            self.chunk_duration
            * self.target_config.sample_rate
            * self.target_config.channels
            * self.target_config.sample_width
        )

        offset = 0

        while offset < len(self.processed_audio):
            chunk_end = min(offset + chunk_size_bytes, len(self.processed_audio))
            chunk = self.processed_audio[offset:chunk_end]

            yield chunk
            offset = chunk_end

    async def _prepare_audio(self) -> None:
        """Prepare audio data asynchronously."""
        loop = asyncio.get_event_loop()
        self.processed_audio, self.total_duration = await loop.run_in_executor(
            None, self._load_and_convert_audio
        )

    def _prepare_audio_sync(self) -> None:
        """Prepare audio data synchronously."""
        self.processed_audio, self.total_duration = self._load_and_convert_audio()

    def _load_and_convert_audio(self) -> Tuple[bytes, float]:
        """Load and convert audio file.

        Returns:
            Tuple of (converted_audio_bytes, duration_seconds)
        """
        # Load audio file
        audio_data, source_sample_rate = self.processor.load_audio_file(self.file_path)

        # Calculate duration
        if audio_data.ndim == 1:
            duration = len(audio_data) / source_sample_rate
        else:
            duration = audio_data.shape[1] / source_sample_rate

        # Convert to target format
        converted_audio = self.processor.convert_to_target_format(
            audio_data, source_sample_rate
        )

        return converted_audio, duration

    def get_file_info(self) -> Dict[str, Any]:
        """Get audio file information.

        Returns:
            Dictionary with file information
        """
        if self.processed_audio is None:
            self._prepare_audio_sync()

        return {
            "file_path": str(self.file_path),
            "duration": self.total_duration,
            "size_bytes": len(self.processed_audio) if self.processed_audio else 0,
            "sample_rate": self.target_config.sample_rate,
            "channels": self.target_config.channels,
            "sample_width": self.target_config.sample_width,
            "format": self.target_config.format.value,
        }


class AudioRecorder:
    """Records audio from microphone with optional real-time processing."""

    def __init__(
        self,
        audio_config: Optional[AudioConfig] = None,
        chunk_duration: float = 0.1,  # seconds
        buffer_size: Optional[int] = None,
    ) -> None:
        """Initialize audio recorder.

        Args:
            audio_config: Audio configuration
            chunk_duration: Duration of each recorded chunk
            buffer_size: Audio buffer size (auto-calculated if None)
        """
        self.audio_config = audio_config or AudioConfig()
        self.chunk_duration = chunk_duration

        if buffer_size is None:
            # Calculate buffer size for the specified chunk duration
            self.buffer_size = int(
                chunk_duration
                * self.audio_config.sample_rate
                * self.audio_config.channels
            )
        else:
            self.buffer_size = buffer_size

        self.is_recording = False
        self.logger = logging.getLogger(__name__)

        # Audio recording attributes (initialized on demand)
        self._audio_interface = None
        self._stream = None

    async def start_recording(self) -> AsyncIterator[bytes]:
        """Start recording audio from microphone.

        Yields:
            Audio data chunks

        Raises:
            AudioError: If recording fails to start
        """
        try:
            import pyaudio
        except ImportError as e:
            raise UnsupportedAudioFormatError(
                "pyaudio",
                details={"error": "PyAudio is required for microphone recording"},
            ) from e

        self._audio_interface = pyaudio.PyAudio()

        try:
            # Configure audio stream
            self._stream = self._audio_interface.open(
                format=self._get_pyaudio_format(),
                channels=self.audio_config.channels,
                rate=self.audio_config.sample_rate,
                input=True,
                frames_per_buffer=self.buffer_size,
            )

            self.is_recording = True
            self.logger.info("Started audio recording")

            # Record audio chunks
            while self.is_recording:
                try:
                    audio_data = self._stream.read(
                        self.buffer_size, exception_on_overflow=False
                    )
                    yield audio_data
                    await asyncio.sleep(0.01)  # Small delay to prevent busy waiting

                except Exception as e:
                    self.logger.error(f"Error reading audio data: {e}")
                    break

        finally:
            await self.stop_recording()

    async def stop_recording(self) -> None:
        """Stop audio recording."""
        self.is_recording = False

        if self._stream:
            try:
                self._stream.stop_stream()
                self._stream.close()
            except Exception as e:
                self.logger.warning(f"Error stopping audio stream: {e}")
            self._stream = None

        if self._audio_interface:
            try:
                self._audio_interface.terminate()
            except Exception as e:
                self.logger.warning(f"Error terminating audio interface: {e}")
            self._audio_interface = None

        self.logger.info("Stopped audio recording")

    def _get_pyaudio_format(self) -> int:
        """Get PyAudio format constant.

        Returns:
            PyAudio format constant
        """
        import pyaudio

        if self.audio_config.sample_width == 1:
            return pyaudio.paUInt8
        elif self.audio_config.sample_width == 2:
            return pyaudio.paInt16
        elif self.audio_config.sample_width == 3:
            return pyaudio.paInt24
        elif self.audio_config.sample_width == 4:
            return pyaudio.paInt32
        else:
            raise ValueError(
                f"Unsupported sample width: {self.audio_config.sample_width}"
            )


# Utility functions
def detect_audio_format(file_path: Union[str, Path]) -> AudioFormat:
    """Detect audio format from file extension.

    Args:
        file_path: Path to audio file

    Returns:
        Detected audio format

    Raises:
        UnsupportedAudioFormatError: If format is not supported
    """
    file_path = Path(file_path)
    extension = file_path.suffix.lower()

    format_mapping = {
        ".pcm": AudioFormat.PCM,
        ".wav": AudioFormat.WAV,
        ".mp3": AudioFormat.MP3,
        ".m4a": AudioFormat.M4A,
        ".aac": AudioFormat.M4A,  # AAC files often have .m4a extension
        ".flac": AudioFormat.FLAC,
        ".ogg": AudioFormat.OGG,
    }

    if extension in format_mapping:
        return format_mapping[extension]
    else:
        raise UnsupportedAudioFormatError(extension)


def calculate_audio_duration(audio_data: bytes, audio_config: AudioConfig) -> float:
    """Calculate audio duration from data size and configuration.

    Args:
        audio_data: Audio data bytes
        audio_config: Audio configuration

    Returns:
        Duration in seconds
    """
    bytes_per_sample = audio_config.sample_width * audio_config.channels
    total_samples = len(audio_data) // bytes_per_sample
    return total_samples / audio_config.sample_rate


def create_silence(duration: float, audio_config: AudioConfig) -> bytes:
    """Create silence audio data.

    Args:
        duration: Duration in seconds
        audio_config: Audio configuration

    Returns:
        Silence audio data as bytes
    """
    total_samples = int(duration * audio_config.sample_rate * audio_config.channels)

    if audio_config.sample_width == 1:  # 8-bit unsigned
        silence_data = np.full(total_samples, 128, dtype=np.uint8)
    else:  # 16-bit, 24-bit, or 32-bit signed
        silence_data = np.zeros(
            total_samples,
            dtype=np.int16 if audio_config.sample_width == 2 else np.int32,
        )

    return silence_data.tobytes()
