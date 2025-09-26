"""Real-time microphone recognition example using FunASR client."""

import asyncio
import logging
import signal
import sys
from typing import Optional

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    logging.warning(
        "python-dotenv not installed. Install with: pip install python-dotenv"
    )

try:
    import pyaudio

    PYAUDIO_AVAILABLE = True
except ImportError:
    PYAUDIO_AVAILABLE = False
    logging.warning("PyAudio not available. Install with: pip install pyaudio")

from funasr_client import create_async_client
from funasr_client.callbacks import SimpleCallback
from funasr_client.models import FinalResult, PartialResult


class MicrophoneStreamer:
    """Real-time microphone audio streamer."""

    def __init__(self, sample_rate=16000, channels=1, chunk_size=1024):
        """Initialize microphone streamer.

        Args:
            sample_rate: Audio sample rate in Hz
            channels: Number of audio channels
            chunk_size: Audio chunk size in samples
        """
        if not PYAUDIO_AVAILABLE:
            raise ImportError("PyAudio is required for microphone streaming")

        self.sample_rate = sample_rate
        self.channels = channels
        self.chunk_size = chunk_size
        self.audio = pyaudio.PyAudio()
        self.stream: Optional[pyaudio.Stream] = None
        self.is_streaming = False

    def start_streaming(self):
        """Start microphone streaming."""
        if self.is_streaming:
            return

        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=self.channels,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size,
        )
        self.is_streaming = True
        logging.info("🎤 Microphone streaming started at %dHz", self.sample_rate)

    def stop_streaming(self):
        """Stop microphone streaming."""
        if not self.is_streaming:
            return

        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None

        self.is_streaming = False
        logging.info("🔇 Microphone streaming stopped")

    def read_chunk(self) -> bytes:
        """Read audio chunk from microphone.

        Returns:
            Audio chunk as bytes
        """
        if not self.is_streaming or not self.stream:
            return b""

        try:
            data = self.stream.read(self.chunk_size, exception_on_overflow=False)
            return data
        except Exception:
            logging.exception("Error reading microphone data")
            return b""

    def __enter__(self):
        """Context manager entry."""
        self.start_streaming()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop_streaming()
        self.audio.terminate()


async def realtime_recognition_example():
    """Real-time speech recognition from microphone."""
    logging.info("=== Real-time Recognition from Microphone ===")
    logging.info("Speak into your microphone. Press Ctrl+C to stop.")

    if not PYAUDIO_AVAILABLE:
        logging.error("❌ PyAudio not available. Cannot use microphone.")
        return

    # Track recognition results
    results = []
    current_sentence = []

    def on_partial_result(result: PartialResult):
        """Handle partial recognition results."""
        # Clear line and logging partial result
        logging.info("🔄 %s", result.text)
        current_sentence.append(result.text)

    def on_final_result(result: FinalResult):
        """Handle final recognition results."""
        logging.info("✅ %s", result.text)
        logging.info("   Confidence: %.2f", result.confidence)

        results.append(
            {
                "text": result.text,
                "confidence": result.confidence,
                "timestamp": result.timestamp,
            }
        )

        current_sentence.clear()
        logging.info("🎤 Listening...")

    def on_error(error):
        """Handle recognition errors."""
        logging.error("❌ Recognition error: %s", error)
        logging.info("🎤 Listening...")

    # Create callback
    callback = SimpleCallback(
        on_partial=on_partial_result,
        on_final=on_final_result,
        on_error=on_error,
    )

    # Create client using .env configuration
    client = create_async_client()

    # Setup signal handler for graceful shutdown
    shutdown_event = asyncio.Event()

    def signal_handler(signum, frame):
        logging.info("🛑 Shutdown signal received")
        shutdown_event.set()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        # Start client
        await client.start()
        logging.info("🚀 Client connected successfully")

        # Start real-time session
        session = await client.start_realtime(callback)
        logging.info("🎙️  Real-time session started")
        logging.info("🎤 Listening...")

        # Start microphone streaming
        with MicrophoneStreamer(
            sample_rate=16000,
            channels=1,
            chunk_size=1024,
        ) as mic:
            # Stream audio chunks to the recognition service
            while not shutdown_event.is_set() and session.is_active:
                try:
                    # Read audio chunk from microphone
                    audio_chunk = mic.read_chunk()

                    if audio_chunk:
                        # Send to recognition service
                        await client.send_audio_chunk(audio_chunk)

                    # Small delay to prevent overwhelming the service
                    await asyncio.sleep(0.01)

                except Exception:
                    logging.exception("Error in streaming loop")
                    break

        # End the recognition session
        await client.end_realtime_session(session)
        logging.info("🏁 Real-time session ended")

        # Display summary
        logging.info("=== Recognition Summary ===")
        logging.info("Total utterances: %d", len(results))

        if results:
            avg_confidence = sum(r["confidence"] for r in results) / len(results)
            logging.info("Average confidence: %.2f", avg_confidence)

            logging.info("📜 Recognition Results:")
            for i, result in enumerate(results, 1):
                logging.info(
                    "%2d. %s (confidence: %.2f)",
                    i,
                    result["text"],
                    result["confidence"],
                )
        else:
            logging.info("No speech detected")

    except Exception:
        logging.exception("❌ Error during real-time recognition")

    finally:
        # Ensure client is closed
        await client.close()
        logging.info("👋 Client disconnected")


async def continuous_recognition_with_silence_detection():
    """Continuous recognition with automatic silence detection."""
    logging.info("=== Continuous Recognition with Silence Detection ===")

    if not PYAUDIO_AVAILABLE:
        logging.error("❌ PyAudio not available. Cannot use microphone.")
        return

    import numpy as np

    # Configuration
    silence_threshold = 0.01  # Amplitude threshold for silence
    silence_duration = 2.0  # Seconds of silence before ending utterance

    results = []
    silence_start = None
    last_audio_time = asyncio.get_event_loop().time()

    def detect_silence(audio_chunk: bytes) -> bool:
        """Detect if audio chunk contains silence."""
        # Convert bytes to numpy array
        audio_data = np.frombuffer(audio_chunk, dtype=np.int16)

        # Normalize to [-1, 1] range
        normalized_audio = audio_data.astype(np.float32) / 32768.0

        # Calculate RMS (Root Mean Square) energy
        rms = np.sqrt(np.mean(normalized_audio**2))

        return rms < silence_threshold

    def on_partial_result(result: PartialResult):
        nonlocal silence_start, last_audio_time
        if result.text.strip():
            logging.info("🔄 %s", result.text)
            silence_start = None  # Reset silence detection
            last_audio_time = asyncio.get_event_loop().time()

    def on_final_result(result: FinalResult):
        if result.text.strip():
            logging.info("✅ %s", result.text)
            logging.info("   Confidence: %.2f", result.confidence)
            results.append(result.text)
            logging.info("🎤 Listening for next utterance...")

    callback = SimpleCallback(
        on_partial=on_partial_result,
        on_final=on_final_result,
    )

    # Create client using .env configuration
    client = create_async_client()

    try:
        await client.start()
        session = await client.start_realtime(callback)

        logging.info("🎙️  Starting continuous recognition with silence detection")
        logging.info("🎤 Speak naturally. Pauses will automatically end utterances.")
        logging.info("Press Ctrl+C to stop.")

        with MicrophoneStreamer() as mic:
            while session.is_active:
                try:
                    audio_chunk = mic.read_chunk()

                    if audio_chunk:
                        # Check for silence
                        is_silent = detect_silence(audio_chunk)

                        if is_silent:
                            if silence_start is None:
                                silence_start = asyncio.get_event_loop().time()
                            elif (
                                asyncio.get_event_loop().time() - silence_start
                            ) > silence_duration:
                                # Long silence detected, end current utterance
                                logging.info(
                                    "🔇 Silence detected, processing utterance..."
                                )

                                # Send end-of-speech signal
                                await client.send_audio_chunk(
                                    b""
                                )  # Empty chunk signals end
                                silence_start = None

                                await asyncio.sleep(0.5)  # Brief pause
                                logging.info("🎤 Ready for next utterance...")
                        else:
                            silence_start = None  # Reset silence counter

                        # Send audio chunk
                        await client.send_audio_chunk(audio_chunk)

                    await asyncio.sleep(0.01)

                except KeyboardInterrupt:
                    break
                except Exception:
                    logging.exception("Error occurred")
                    break

        await client.end_realtime_session(session)

        logging.info("=== Continuous Recognition Complete ===")
        logging.info("Captured %d utterances:", len(results))
        for i, text in enumerate(results, 1):
            logging.info("%2d. %s", i, text)

    except Exception:
        logging.exception("Error occurred")

    finally:
        await client.close()


async def voice_commands_example():
    """Voice commands recognition example."""
    logging.info("=== Voice Commands Example ===")

    if not PYAUDIO_AVAILABLE:
        logging.error("❌ PyAudio not available. Cannot use microphone.")
        return

    # Define voice commands
    commands = {
        "start recording": lambda: logging.info("🔴 Started recording"),
        "stop recording": lambda: logging.info("⏹️  Stopped recording"),
        "play music": lambda: logging.info("🎵 Playing music"),
        "pause music": lambda: logging.info("⏸️  Music paused"),
        "increase volume": lambda: logging.info("🔊 Volume increased"),
        "decrease volume": lambda: logging.info("🔉 Volume decreased"),
        "what time is it": lambda: logging.info(
            "🕒 Current time: %s", asyncio.get_event_loop().time()
        ),
        "exit application": lambda: logging.info("👋 Exiting..."),
    }

    recognized_commands = []

    def process_command(text: str) -> bool:
        """Process recognized text as a command."""
        text_lower = text.lower().strip()

        for command, action in commands.items():
            if command in text_lower:
                logging.info("🎯 Command recognized: '%s'", command)
                action()
                recognized_commands.append(command)
                return True

        return False

    def on_final_result(result: FinalResult):
        logging.info("💬 Heard: %s", result.text)

        if not process_command(result.text):
            logging.info("❓ No matching command found")

        logging.info("Available commands: %s", ", ".join(commands.keys()))
        logging.info("🎤 Listening for commands...")

    callback = SimpleCallback(on_final=on_final_result)

    # Create client using .env configuration
    client = create_async_client(
        # Only specify parameters that aren't in .env or need special values
        hotwords=dict.fromkeys(commands.keys(), 15),  # Voice command hotwords
    )

    try:
        await client.start()
        session = await client.start_realtime(callback)

        logging.info("🎤 Voice Commands Demo")
        logging.info("Say any of these commands:")
        for command in commands:
            logging.info("  • '%s'", command)
        logging.info("Press Ctrl+C to stop.")

        with MicrophoneStreamer() as mic:
            while session.is_active:
                try:
                    audio_chunk = mic.read_chunk()
                    if audio_chunk:
                        await client.send_audio_chunk(audio_chunk)
                    await asyncio.sleep(0.01)

                except KeyboardInterrupt:
                    break

        await client.end_realtime_session(session)

        logging.info("=== Voice Commands Session Complete ===")
        logging.info("Commands executed: %d", len(recognized_commands))
        for command in recognized_commands:
            logging.info("  ✅ %s", command)

    except Exception:
        logging.exception("Error occurred")

    finally:
        await client.close()


async def main():
    """Run real-time examples."""
    logging.basicConfig(level=logging.INFO)

    logging.info("FunASR Real-time Recognition Examples")
    logging.info("=====================================")

    if not PYAUDIO_AVAILABLE:
        logging.warning("⚠️  PyAudio not installed. Install with:")
        logging.info("   pip install pyaudio")
        logging.info("On macOS: brew install portaudio")
        logging.info("On Ubuntu: sudo apt-get install portaudio19-dev")
        return

    examples = [
        realtime_recognition_example,
        continuous_recognition_with_silence_detection,
        voice_commands_example,
    ]

    for example in examples:
        try:
            await example()
        except KeyboardInterrupt:
            logging.info("⏹️  %s interrupted by user", example.__name__)
        except Exception:
            logging.exception("❌ %s failed", example.__name__)

        logging.info("=" * 50)
        input("Press Enter to continue to next example...")

    logging.info("👋 All real-time examples complete!")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("\n👋 Goodbye!")
        sys.exit(0)
