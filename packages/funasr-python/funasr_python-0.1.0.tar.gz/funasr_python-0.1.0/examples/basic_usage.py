"""Basic usage example for FunASR client."""

import asyncio
import logging
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    logging.warning(
        "python-dotenv not installed. Install with: pip install python-dotenv"
    )

from funasr_client import AsyncFunASRClient, create_async_client
from funasr_client.callbacks import SimpleCallback
from funasr_client.models import FinalResult, PartialResult


async def basic_file_recognition():
    """Basic file recognition example."""
    logging.info("=== Basic File Recognition ===")

    # Create client with default configuration (uses .env if available)
    client = create_async_client()

    try:
        # Start the client
        await client.start()
        logging.info("Client connected successfully")

        # Recognize an audio file
        audio_file = "examples/audio/asr_example.wav"

        if Path(audio_file).exists():
            result = await client.recognize_file(audio_file)
            logging.info("Recognition result: %s", result.text)
            logging.info("Confidence: %.2f", result.confidence)
        else:
            logging.warning("Audio file not found: %s", audio_file)

    except Exception:
        logging.exception("Error during recognition")

    finally:
        # Always close the client
        await client.close()


async def recognition_with_callbacks():
    """Recognition with real-time callbacks."""
    logging.info("=== Recognition with Callbacks ===")

    # Create callback to handle partial and final results
    def on_partial_result(result: PartialResult):
        logging.info("Partial: %s", result.text)

    def on_final_result(result: FinalResult):
        logging.info("Final: %s", result.text)
        logging.info("Confidence: %.2f", result.confidence)

    def on_error(error):
        logging.error("Recognition error: %s", error)

    # Create callback instance
    callback = SimpleCallback(
        on_partial=on_partial_result,
        on_final=on_final_result,
        on_error=on_error,
    )

    # Create client
    client = create_async_client()

    try:
        await client.start()

        audio_file = "examples/audio/asr_example.wav"

        if Path(audio_file).exists():
            # Recognize with callbacks
            result = await client.recognize_file(audio_file, callback)
            logging.info("Final result received: %s", result.text)
        else:
            logging.warning("Audio file not found: %s", audio_file)

    except Exception:
        logging.exception("Error occurred")

    finally:
        await client.close()


async def custom_configuration():
    """Using custom client configuration."""
    logging.info("=== Custom Configuration ===")

    # Example of overriding .env settings when needed
    client = create_async_client(
        server_url="ws://your-funasr-server:10095",  # Override FUNASR_WS_URL
        timeout=60.0,  # Override FUNASR_TIMEOUT
        preset="high_accuracy",  # Override FUNASR_PRESET
    )

    try:
        await client.start()
        logging.info("Connected with custom configuration")

        # Display current configuration
        config = client.config
        logging.info("Server URL: %s", config.server_url)
        logging.info("Timeout: %ss", config.timeout)
        logging.info("Recognition mode: %s", config.mode)
        logging.info("Sample rate: %sHz", config.audio.sample_rate)

        # Your recognition code here...

    except Exception:
        logging.exception("Error occurred")

    finally:
        await client.close()


async def realtime_recognition():
    """Real-time recognition from microphone."""
    logging.info("=== Real-time Recognition ===")

    # Create callback for real-time results
    def on_partial(result: PartialResult):
        logging.info("🎤 Partial: %s", result.text)

    def on_final(result: FinalResult):
        logging.info("✅ Final: %s", result.text)

    callback = SimpleCallback(
        on_partial=on_partial,
        on_final=on_final,
    )

    # Create client using .env configuration
    client = create_async_client()

    try:
        await client.start()
        logging.info("Starting real-time recognition...")
        logging.info("Speak into your microphone. Press Ctrl+C to stop.")

        # Start real-time session
        session = await client.start_realtime(callback)

        # In a real application, you would stream audio from microphone
        # For this example, we'll just wait for user interrupt
        try:
            while session.is_active:
                await asyncio.sleep(0.1)
                # Here you would capture and send audio chunks:
                # audio_chunk = capture_microphone_audio()
                # await client.send_audio_chunk(audio_chunk)

        except KeyboardInterrupt:
            logging.info("Stopping recognition...")

        # End the session
        await client.end_realtime_session(session)
        logging.info("Real-time session ended")

    except Exception:
        logging.exception("Error occurred")

    finally:
        await client.close()


async def batch_recognition():
    """Batch recognition of multiple files."""
    logging.info("=== Batch Recognition ===")

    # List of audio files to process
    audio_files = [
        "examples/audio/asr_example.wav",
        "examples/audio/61-70970-0001.wav",
        "examples/audio/61-70970-0016.wav",
        # Add more files as needed
    ]

    client = create_async_client()

    try:
        await client.start()

        results = []

        for i, audio_file in enumerate(audio_files, 1):
            logging.info("Processing file %d/%d: %s", i, len(audio_files), audio_file)

            if Path(audio_file).exists():
                try:
                    result = await client.recognize_file(audio_file)
                    results.append(
                        {
                            "file": audio_file,
                            "text": result.text,
                            "confidence": result.confidence,
                        }
                    )
                    logging.info("✅ Success: %s...", result.text[:50])

                except Exception as e:
                    logging.error("❌ Failed: %s", e)
                    results.append(
                        {
                            "file": audio_file,
                            "error": str(e),
                        }
                    )
            else:
                logging.warning("⚠️  File not found: %s", audio_file)

        # Display summary
        logging.info("=== Batch Results ===")
        successful = len([r for r in results if "text" in r])
        logging.info("Total files: %d", len(audio_files))
        logging.info("Successful: %d", successful)
        logging.info("Failed: %d", len(audio_files) - successful)

        # Display results
        for result in results:
            if "text" in result:
                logging.info("📄 %s: %s...", result["file"], result["text"][:100])
            else:
                logging.error("❌ %s: %s", result["file"], result["error"])

    except Exception:
        logging.exception("Error occurred")

    finally:
        await client.close()


async def error_handling_example():
    """Demonstrate error handling."""
    logging.info("=== Error Handling Example ===")

    client = AsyncFunASRClient(
        server_url="ws://non-existent-server:10095",  # Intentionally wrong URL
        timeout=5.0,
    )

    try:
        logging.info("Attempting to connect to non-existent server...")
        await client.start()

    except Exception as e:
        logging.info("Expected error: %s: %s", type(e).__name__, e)

    # Now try with correct server but non-existent file
    client = create_async_client()

    try:
        await client.start()
        logging.info("Connected successfully")

        # Try to recognize non-existent file
        await client.recognize_file("non_existent_file.wav")

    except FileNotFoundError as e:
        logging.error("File error: %s", e)
    except Exception as e:
        logging.error("Other error: %s: %s", type(e).__name__, e)

    finally:
        await client.close()


async def main():
    """Run all examples."""
    logging.basicConfig(level=logging.INFO)

    logging.info("FunASR Client Examples")
    logging.info("=====================")

    # Run examples
    await basic_file_recognition()
    await recognition_with_callbacks()
    await custom_configuration()
    # await realtime_recognition()
    await batch_recognition()
    await error_handling_example()

    logging.info("=== Examples Complete ===")
    logging.info("Audio files used from examples/audio/ directory")
    logging.info(
        "Replace server URL 'ws://your-funasr-server:10095' with your actual server URL if needed"
    )


if __name__ == "__main__":
    asyncio.run(main())
