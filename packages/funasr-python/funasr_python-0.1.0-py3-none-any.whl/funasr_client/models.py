"""Core data models for FunASR client."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import time
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class RecognitionMode(str, Enum):
    """Recognition modes supported by FunASR."""

    OFFLINE = "offline"  # Process audio after it's fully received
    ONLINE = "online"  # Real-time streaming recognition
    TWO_PASS = "2pass"  # Combines online and offline for better accuracy


class ConnectionState(str, Enum):
    """WebSocket connection states."""

    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    RECOGNIZING = "recognizing"
    FINALIZING = "finalizing"
    ERROR = "error"


class AudioFormat(str, Enum):
    """Supported audio formats."""

    PCM = "pcm"
    WAV = "wav"
    MP3 = "mp3"
    M4A = "m4a"
    FLAC = "flac"
    OGG = "ogg"


@dataclass
class AudioConfig:
    """Audio configuration for recognition."""

    sample_rate: int = 16000
    channels: int = 1
    sample_width: int = 2  # bytes per sample (16-bit = 2 bytes)
    format: AudioFormat = AudioFormat.PCM


class FunASRInitMessage(BaseModel):
    """Initialization message sent to FunASR server."""

    mode: RecognitionMode = RecognitionMode.TWO_PASS
    chunk_size: List[int] = Field(default=[5, 10, 5])
    chunk_interval: int = Field(default=10, ge=1, le=100)
    wav_name: str = Field(default="audio_stream")
    wav_format: AudioFormat = AudioFormat.PCM
    audio_fs: int = Field(default=16000, ge=8000, le=48000)
    is_speaking: bool = True
    itn: bool = True  # Inverse text normalization
    svs_itn: bool = True  # Punctuation restoration
    hotwords: str = Field(default="")
    encoder_chunk_look_back: int = Field(default=4, ge=0)
    decoder_chunk_look_back: int = Field(default=0, ge=0)

    class Config:
        """Pydantic model configuration."""

        use_enum_values = True


class FunASREndMessage(BaseModel):
    """Message to indicate end of speech."""

    is_speaking: bool = False


class FunASRResponse(BaseModel):
    """Response message from FunASR server."""

    mode: Optional[str] = None
    text: str = ""
    timestamp: str = Field(default="[]")
    is_final: bool = False
    wav_name: str = ""
    confidence: Optional[float] = Field(default=None, ge=0.0, le=1.0)
    sentence_id: Optional[int] = None
    speaker_id: Optional[str] = None


class FunASRError(BaseModel):
    """Error message from FunASR server."""

    error: Dict[str, Any]

    @property
    def code(self) -> str:
        """Get error code."""
        return self.error.get("code", "UNKNOWN_ERROR")

    @property
    def message(self) -> str:
        """Get error message."""
        return self.error.get("message", "Unknown error occurred")

    @property
    def details(self) -> Dict[str, Any]:
        """Get error details."""
        return self.error.get("details", {})


@dataclass
class WordResult:
    """Word-level recognition result."""

    word: str
    start_time: float
    end_time: float
    confidence: float


@dataclass
class RecognitionResult:
    """Base class for recognition results."""

    text: str
    confidence: float
    timestamp: float
    is_final: bool
    session_id: str


@dataclass
class PartialResult(RecognitionResult):
    """Partial recognition result for streaming."""

    start_time: float = 0.0
    end_time: float = 0.0


@dataclass
class FinalResult(RecognitionResult):
    """Final optimized recognition result."""

    alternatives: List[str] = field(default_factory=list)
    speaker_id: Optional[str] = None
    emotion: Optional[str] = None


@dataclass
class SentenceResult(RecognitionResult):
    """Sentence-level recognition result."""

    sentence_id: int = 0
    words: List[WordResult] = field(default_factory=list)


@dataclass
class ConnectionMetrics:
    """Connection performance metrics."""

    connection_time: float = 0.0
    first_response_time: float = 0.0
    final_processing_time: float = 0.0
    total_audio_duration: float = 0.0
    total_processing_time: float = 0.0
    message_count: int = 0
    error_count: int = 0
    reconnection_count: int = 0

    @property
    def real_time_factor(self) -> float:
        """Calculate real-time factor (processing_time / audio_duration)."""
        if self.total_audio_duration <= 0:
            return 0.0
        return self.total_processing_time / self.total_audio_duration

    @property
    def success_rate(self) -> float:
        """Calculate success rate."""
        total_requests = self.message_count + self.error_count
        if total_requests <= 0:
            return 1.0
        return (self.message_count / total_requests) * 100


@dataclass
class ClientConfig:
    """Client configuration."""

    # Connection settings
    server_url: str = "ws://localhost:10095"
    timeout: float = 30.0
    max_retries: int = 3
    retry_delay: float = 1.0
    use_ssl: bool = False

    # Audio settings
    audio: AudioConfig = field(default_factory=AudioConfig)

    # Recognition settings
    mode: RecognitionMode = RecognitionMode.TWO_PASS
    chunk_size: List[int] = field(default_factory=lambda: [5, 10, 5])
    chunk_interval: int = 10
    enable_itn: bool = True
    enable_punctuation: bool = True
    hotwords: Dict[str, int] = field(default_factory=dict)

    # Performance settings
    enable_vad: bool = True
    auto_reconnect: bool = True
    connection_pool_size: int = 5
    buffer_size: int = 8192

    # WebSocket settings
    ping_interval: Optional[float] = None
    ping_timeout: float = 10.0
    close_timeout: float = 10.0
    max_message_size: Optional[int] = 10 * 1024 * 1024
    compression: Optional[str] = None  # e.g., 'deflate' or None
    subprotocols: Optional[List[str]] = field(default_factory=lambda: ["binary"])

    # Debug settings
    debug: bool = False
    log_level: str = "INFO"

    def to_init_message(self, wav_name: str = "audio_stream") -> FunASRInitMessage:
        """Convert config to FunASR initialization message."""
        hotwords_str = ""
        if self.hotwords:
            import json

            hotwords_str = json.dumps(self.hotwords)

        return FunASRInitMessage(
            mode=self.mode,
            chunk_size=self.chunk_size,
            chunk_interval=self.chunk_interval,
            wav_name=wav_name,
            wav_format=self.audio.format,
            audio_fs=self.audio.sample_rate,
            is_speaking=True,
            itn=self.enable_itn,
            svs_itn=self.enable_punctuation,
            hotwords=hotwords_str,
        )


@dataclass
class RealtimeSession:
    """Real-time recognition session."""

    session_id: str
    start_time: float = field(default_factory=time.time)
    is_active: bool = True
    metrics: ConnectionMetrics = field(default_factory=ConnectionMetrics)

    def end_session(self) -> None:
        """End the real-time session."""
        self.is_active = False


# Preset configurations
class ConfigPresets:
    """Predefined configuration presets."""

    @staticmethod
    def low_latency() -> ClientConfig:
        """Low latency mode for real-time interaction."""
        return ClientConfig(
            mode=RecognitionMode.ONLINE,
            chunk_size=[1, 6, 1],
            chunk_interval=5,
            enable_vad=True,
            timeout=10.0,
        )

    @staticmethod
    def high_accuracy() -> ClientConfig:
        """High accuracy mode for transcription scenarios."""
        return ClientConfig(
            mode=RecognitionMode.TWO_PASS,
            chunk_size=[5, 10, 5],
            chunk_interval=10,
            enable_itn=True,
            enable_punctuation=True,
            timeout=60.0,
        )

    @staticmethod
    def balanced() -> ClientConfig:
        """Balanced mode for general purpose usage."""
        return ClientConfig(
            mode=RecognitionMode.TWO_PASS,
            chunk_size=[3, 8, 3],
            chunk_interval=8,
            timeout=30.0,
        )
