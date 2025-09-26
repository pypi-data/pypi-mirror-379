# FunASR Python Client

[![PyPI version](https://badge.fury.io/py/funasr-python.svg)](https://badge.fury.io/py/funasr-python)
[![Python versions](https://img.shields.io/pypi/pyversions/funasr-python.svg)](https://pypi.org/project/funasr-python)
[![License](https://img.shields.io/pypi/l/funasr-python.svg)](https://pypi.org/project/funasr-python)
[![Tests](https://github.com/your-org/funasr-python/workflows/Tests/badge.svg)](https://github.com/your-org/funasr-python/actions)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

A high-performance, enterprise-grade Python client for FunASR WebSocket speech recognition service. Built for production use with comprehensive error handling, automatic reconnection, and extensive customization options.

## Features

### 🚀 **High Performance**
- **Asynchronous I/O**: Built on asyncio for maximum concurrency
- **Connection Pooling**: Efficient WebSocket connection management
- **Streaming Recognition**: Real-time speech recognition with minimal latency
- **Memory Efficient**: Optimized audio processing with configurable buffering

### 🔧 **Production Ready**
- **Robust Error Handling**: Comprehensive exception handling and recovery
- **Automatic Reconnection**: Smart reconnection with exponential backoff
- **Health Monitoring**: Built-in connection health checks
- **Resource Management**: Automatic cleanup and resource deallocation

### 📊 **Recognition Modes for Different Scenarios**
- **Offline Mode**: Best for complete audio files, highest accuracy
- **Online Mode**: Ultra-low latency streaming, suitable for interactive applications
- **Two-Pass Mode** ⭐: **Recommended for real-time scenarios** - combines streaming speed with offline accuracy

### 🎯 **Enterprise Features**
- **Configuration Management**: Flexible configuration with .env support
- **Comprehensive Logging**: Structured logging with configurable levels
- **Metrics & Monitoring**: Built-in performance metrics
- **Type Safety**: Full type hints for better IDE support

### 🎵 **Audio Processing**
- **Multiple Formats**: Support for WAV, FLAC, MP3, and more
- **Automatic Resampling**: Smart audio format conversion
- **Voice Activity Detection**: Optional VAD for improved efficiency
- **Microphone Integration**: Real-time microphone recording support

## Installation

### Basic Installation

```bash
pip install funasr-python
```

### With Optional Dependencies

```bash
# Audio processing capabilities
pip install funasr-python[audio]

# Performance optimizations
pip install funasr-python[performance]

# Development tools
pip install funasr-python[dev]

# Everything
pip install funasr-python[all]
```

### From Source

```bash
git clone https://github.com/alibaba-damo-academy/FunASR.git
cd FunASR/clients/funasr-python
pip install -e .
```

## Quick Start

### Basic Usage

```python
import asyncio
from funasr_client import AsyncFunASRClient

async def main():
    client = AsyncFunASRClient()

    # Recognize an audio file
    result = await client.recognize_file("examples/audio/asr_example.wav")
    print(f"Recognition result: {result.text}")

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### Real-time Recognition (Recommended)

For real-time applications, we recommend **Two-Pass Mode** which provides the best balance of speed and accuracy:

```python
import asyncio
from funasr_client import AsyncFunASRClient
from funasr_client.models import RecognitionMode, ClientConfig

async def realtime_recognition():
    # Two-Pass Mode: Optimal for real-time scenarios
    config = ClientConfig(
        server_url="ws://localhost:10095",
        mode=RecognitionMode.TWO_PASS,  # Recommended for real-time
        enable_vad=True,  # Voice activity detection
        chunk_interval=10  # Balanced latency/accuracy
    )

    client = AsyncFunASRClient(config=config)

    def on_partial_result(result):
        print(f"Partial: {result.text}")

    def on_final_result(result):
        print(f"Final: {result.text} (confidence: {result.confidence:.2f})")

    from funasr_client.callbacks import SimpleCallback
    callback = SimpleCallback(
        on_partial=on_partial_result,
        on_final=on_final_result
    )

    await client.start()

    # Start real-time session
    session = await client.start_realtime(callback)

    # Your audio streaming logic here
    # In practice, you would stream from microphone or audio source

    await client.close()

if __name__ == "__main__":
    asyncio.run(realtime_recognition())
```

### Ultra-Low Latency (Interactive Applications)

For scenarios requiring minimal latency (e.g., voice assistants):

```python
async def ultra_low_latency():
    config = ClientConfig(
        mode=RecognitionMode.ONLINE,  # Ultra-low latency
        chunk_interval=5,  # Faster processing
        enable_vad=True
    )

    client = AsyncFunASRClient(config=config)
    # Implementation similar to above
```

### Configuration with Environment Variables

Create a `.env` file:

```env
FUNASR_WS_URL=ws://localhost:10095
FUNASR_MODE=2pass  # Recommended: Two-Pass Mode for optimal real-time performance
FUNASR_SAMPLE_RATE=16000
FUNASR_ENABLE_ITN=true
FUNASR_ENABLE_VAD=true  # Recommended for real-time scenarios
```

```python
from funasr_client import create_async_client

# Configuration loaded automatically from .env
client = await create_async_client()
result = await client.recognize_file("examples/audio/asr_example.wav")
print(result.text)
```

## Advanced Usage

### Custom Configuration

```python
from funasr_client import AsyncFunASRClient, ClientConfig, AudioConfig
from funasr_client.models import RecognitionMode, AudioFormat

config = ClientConfig(
    server_url="ws://your-server:10095",
    mode=RecognitionMode.TWO_PASS,
    timeout=30.0,
    max_retries=3,
    audio=AudioConfig(
        sample_rate=16000,
        format=AudioFormat.PCM,
        channels=1
    )
)

client = AsyncFunASRClient(config=config)
```

### Callback Handlers

```python
from funasr_client.callbacks import SimpleCallback

def on_result(result):
    print(f"Received: {result.text}")

def on_error(error):
    print(f"Error: {error}")

callback = SimpleCallback(
    on_result=on_result,
    on_error=on_error
)

client = AsyncFunASRClient(callback=callback)
```

### Multiple Recognition Sessions

```python
async def recognize_multiple():
    # Use Two-Pass Mode for optimal performance
    client = AsyncFunASRClient(
        mode=RecognitionMode.TWO_PASS  # ⭐ Recommended
    )

    # Process multiple files concurrently
    tasks = [
        client.recognize_file("examples/audio/asr_example.wav"),
        client.recognize_file("examples/audio/61-70970-0001.wav"),
        client.recognize_file("examples/audio/61-70970-0016.wav")
    ]

    results = await asyncio.gather(*tasks)
    for i, result in enumerate(results, 1):
        print(f"File {i}: {result.text}")
```

### Real-time Applications Examples

#### Live Streaming Transcription

```python
async def live_transcription():
    """Real-time transcription for live streams."""
    config = ClientConfig(
        mode=RecognitionMode.TWO_PASS,  # ⭐ Optimal for live streaming
        enable_vad=True,                # Filter silence
        chunk_interval=8,               # Balanced performance
        auto_reconnect=True             # Handle network issues
    )

    client = AsyncFunASRClient(config=config)

    def on_result(result):
        if result.is_final:
            # Send to subtitle system
            send_subtitle(result.text, result.confidence)
        else:
            # Show live preview
            show_live_text(result.text)

    from funasr_client.callbacks import SimpleCallback
    callback = SimpleCallback(on_final=on_result, on_partial=on_result)

    await client.start()
    session = await client.start_realtime(callback)

    # Your audio streaming implementation here
    await stream_audio_to_session(session)
```

#### Voice Assistant Integration

```python
async def voice_assistant():
    """Voice assistant with Two-Pass optimization."""
    config = ClientConfig(
        mode=RecognitionMode.TWO_PASS,  # ⭐ Best for voice assistants
        enable_vad=True,                # Automatic speech detection
        chunk_interval=10               # Good responsiveness
    )

    client = AsyncFunASRClient(config=config)

    async def process_command(result):
        if result.is_final and result.confidence > 0.8:
            # Process voice command
            response = await process_voice_command(result.text)
            await speak_response(response)

    from funasr_client.callbacks import AsyncSimpleCallback
    callback = AsyncSimpleCallback(on_final=process_command)

    await client.start()
    session = await client.start_realtime(callback)

    print("🎤 Voice assistant ready. Speak now...")
    # Your microphone streaming logic here
```

## Command Line Interface

The package includes a full-featured CLI:

```bash
# Basic recognition
funasr-client recognize examples/audio/asr_example.wav

# Real-time recognition from microphone
funasr-client stream --source microphone

# Batch processing
funasr-client batch examples/audio/*.wav --output results.jsonl

# Server configuration
funasr-client configure --server-url ws://localhost:10095

# Test connection
funasr-client test-connection
```

## Recognition Mode Selection Guide

Choose the optimal recognition mode for your use case:

| Mode | Latency | Accuracy | Best For | Use Cases |
|------|---------|----------|----------|-----------|
| **Two-Pass** ⭐ | Medium | **High** | **Real-time applications** | Live streaming, real-time subtitles, voice assistants |
| **Online** | **Low** | Medium | Interactive apps | Voice commands, quick responses |
| **Offline** | High | **Highest** | File processing | Transcription services, post-processing |

### Two-Pass Mode Advantages ⭐

**Recommended for real-time scenarios** because it:

- ✅ **Fast partial results** for immediate user feedback
- ✅ **High-accuracy final results** using 2-pass optimization
- ✅ **Balanced resource usage** with smart buffering
- ✅ **Production-ready** with robust error handling

```python
# Recommended configuration for real-time applications
config = ClientConfig(
    mode=RecognitionMode.TWO_PASS,  # Best balance
    enable_vad=True,                # Improves efficiency
    chunk_interval=10,              # Optimal for most cases
    auto_reconnect=True             # Production reliability
)
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FUNASR_WS_URL` | WebSocket server URL | `ws://localhost:10095` |
| `FUNASR_MODE` | Recognition mode (`offline`, `online`, `2pass`) | `2pass` ⭐ |
| `FUNASR_TIMEOUT` | Connection timeout | `30.0` |
| `FUNASR_MAX_RETRIES` | Max retry attempts | `3` |
| `FUNASR_SAMPLE_RATE` | Audio sample rate | `16000` |
| `FUNASR_ENABLE_ITN` | Enable inverse text normalization | `true` |
| `FUNASR_ENABLE_VAD` | Enable voice activity detection | `true` |
| `FUNASR_DEBUG` | Enable debug logging | `false` |

> 💡 **Tip**: Two-Pass Mode (`2pass`) is recommended for most real-time applications as it provides the best balance between latency and accuracy.

### Configuration File

```python
from funasr_client import ConfigManager

# Load from custom config file
config = ConfigManager.from_file("my_config.json")
client = AsyncFunASRClient(config=config.client_config)
```

## Error Handling

```python
from funasr_client.errors import (
    FunASRError,
    ConnectionError,
    AudioError,
    TimeoutError
)

try:
    result = await client.recognize_file("examples/audio/asr_example.wav")
except ConnectionError:
    print("Failed to connect to server")
except AudioError:
    print("Audio processing failed")
except TimeoutError:
    print("Request timed out")
except FunASRError as e:
    print(f"Recognition error: {e}")
```

## Performance Optimization

### Real-time Performance Best Practices

For optimal real-time performance, follow these recommendations:

```python
from funasr_client import AsyncFunASRClient, ClientConfig
from funasr_client.models import RecognitionMode, AudioConfig

# Optimized configuration for real-time scenarios
config = ClientConfig(
    # Core settings
    mode=RecognitionMode.TWO_PASS,  # ⭐ Best balance for real-time
    enable_vad=True,                # Reduces processing load
    chunk_interval=10,              # Optimal latency/accuracy trade-off

    # Performance settings
    auto_reconnect=True,            # Production reliability
    connection_pool_size=5,         # Connection reuse
    buffer_size=8192,               # Optimal buffer size

    # Audio optimization
    audio=AudioConfig(
        sample_rate=16000,          # Standard ASR rate
        channels=1,                 # Mono for efficiency
        sample_width=2              # 16-bit PCM
    )
)

client = AsyncFunASRClient(config=config)
```

### Performance Tuning Guidelines

| Parameter | Recommended Value | Impact |
|-----------|------------------|---------|
| `mode` | `TWO_PASS` ⭐ | Best accuracy/latency balance |
| `chunk_interval` | `10` | Standard real-time performance |
| `chunk_interval` | `5` | Lower latency, higher CPU usage |
| `chunk_interval` | `20` | Higher latency, lower CPU usage |
| `enable_vad` | `True` | Reduces unnecessary processing |
| `sample_rate` | `16000` | Optimal for most ASR models |

### Connection Pooling

```python
from funasr_client import ConnectionManager

# Use connection manager for multiple clients
manager = ConnectionManager(max_connections=10)
client1 = AsyncFunASRClient(connection_manager=manager)
client2 = AsyncFunASRClient(connection_manager=manager)
```

### Audio Processing

```python
from funasr_client import AudioProcessor

# Pre-process audio for better performance
processor = AudioProcessor(
    target_sample_rate=16000,
    enable_vad=True,
    chunk_size=1024
)

processed_audio = processor.process_file("examples/audio/asr_example.wav")
result = await client.recognize_audio(processed_audio)
```

## Testing

Run the test suite:

```bash
# Install test dependencies
pip install funasr-python[test]

# Run all tests
pytest

# Run with coverage
pytest --cov=funasr_client

# Run specific test categories
pytest -m unit
pytest -m integration
```

## Development

### Setup Development Environment

```bash
git clone https://github.com/alibaba-damo-academy/FunASR.git
cd FunASR/clients/funasr-python

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .[dev]

# Install pre-commit hooks
pre-commit install
```

### Code Quality

```bash
# Format code
ruff format src/ tests/

# Lint code
ruff check src/ tests/

# Type check
mypy src/

# Run all quality checks
pre-commit run --all-files
```

## API Reference

### Core Classes

- **`AsyncFunASRClient`**: Main asynchronous client
- **`FunASRClient`**: Synchronous client wrapper
- **`ClientConfig`**: Client configuration
- **`AudioConfig`**: Audio processing configuration
- **`RecognitionResult`**: Recognition result container

### Callback System

- **`RecognitionCallback`**: Abstract callback interface
- **`SimpleCallback`**: Basic callback implementation
- **`LoggingCallback`**: Logging-based callback
- **`MultiCallback`**: Combines multiple callbacks

### Audio Processing

- **`AudioProcessor`**: Audio processing utilities
- **`AudioRecorder`**: Microphone recording
- **`AudioFileStreamer`**: File-based audio streaming

### Utilities

- **`ConfigManager`**: Configuration management
- **`ConnectionManager`**: Connection pooling
- **`Timer`**: Performance timing utilities

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Development Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Support

- **Documentation**: [FunASR Documentation](https://github.com/alibaba-damo-academy/FunASR)
- **Issues**: [GitHub Issues](https://github.com/alibaba-damo-academy/FunASR/issues)
- **Discussions**: [GitHub Discussions](https://github.com/alibaba-damo-academy/FunASR/discussions)

## Acknowledgments

- Built on the excellent [FunASR](https://github.com/alibaba-damo-academy/FunASR) speech recognition toolkit
- Inspired by best practices from the Python asyncio ecosystem
- Thanks to all contributors and users for feedback and improvements