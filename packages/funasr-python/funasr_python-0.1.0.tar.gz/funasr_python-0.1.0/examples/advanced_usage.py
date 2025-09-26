"""Advanced usage examples for FunASR client."""

import asyncio
import json
import logging
import os
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    logging.warning(
        "python-dotenv not installed. Install with: pip install python-dotenv"
    )

from funasr_client import AsyncFunASRClient, create_async_client
from funasr_client.callbacks import AsyncSimpleCallback, LoggingCallback, MultiCallback
from funasr_client.models import AudioConfig, ClientConfig, RecognitionMode


async def custom_audio_configuration():
    """Example with custom audio configuration."""
    logging.info("=== Custom Audio Configuration ===")

    # Create custom audio configuration compatible with FunASR server
    # FunASR server expects: 16kHz, mono, PCM format for optimal recognition
    audio_config = AudioConfig(
        sample_rate=16000,  # Standard ASR sample rate (matches server default)
        channels=1,  # Mono (most ASR models work best with mono)
        sample_width=2,  # 16-bit audio (standard PCM format)
    )

    # Create client configuration
    config = ClientConfig(
        server_url=os.environ.get("FUNASR_WS_URL", "ws://localhost:10095"),
        audio=audio_config,
        mode=RecognitionMode.TWO_PASS,
        enable_itn=True,
        enable_punctuation=True,
    )

    client = AsyncFunASRClient(config=config)

    try:
        await client.start()
        logging.info(
            "Custom audio format: %dHz, %d channels, %d-bit",
            config.audio.sample_rate,
            config.audio.channels,
            config.audio.sample_width * 8,
        )

        # The client will automatically convert audio to the target format
        # This configuration is optimized for FunASR server compatibility
        audio_file = "examples/audio/asr_example.wav"
        if Path(audio_file).exists():
            result = await client.recognize_file(audio_file)
            logging.info("Result: %s", result.text)

    except Exception:
        logging.exception("Error occurred")
    finally:
        await client.close()


async def hotwords_example():
    """Example using hotwords/keywords."""
    logging.info("=== Hotwords Example ===")

    # Define hotwords with boost values
    hotwords = {
        "FunASR": 20,  # High boost for "FunASR"
        "speech recognition": 15,  # Medium boost
        "artificial intelligence": 10,  # Lower boost
        "machine learning": 10,
    }

    config = ClientConfig(
        server_url=os.environ.get("FUNASR_WS_URL", "ws://localhost:10095"),
        hotwords=hotwords,
        mode=RecognitionMode.TWO_PASS,
    )

    client = AsyncFunASRClient(config=config)

    try:
        await client.start()
        logging.info("Using hotwords: %s", list(hotwords.keys()))

        audio_file = "examples/audio/asr_example.wav"
        if Path(audio_file).exists():
            result = await client.recognize_file(audio_file)
            logging.info("Result with hotword boosting: %s", result.text)

    except Exception:
        logging.exception("Error occurred")
    finally:
        await client.close()


async def multiple_callbacks_example():
    """Example using multiple callbacks."""
    logging.info("=== Multiple Callbacks Example ===")

    # Create multiple callbacks
    results_log = []

    def result_collector(result):
        results_log.append(
            {
                "text": result.text,
                "confidence": result.confidence,
                "timestamp": result.timestamp,
                "is_final": result.is_final,
            }
        )

    def progress_printer(result):
        if result.is_final:
            logging.info("✅ Final: %s", result.text)
        else:
            logging.info("🔄 Partial: %s", result.text)

    # Create individual callbacks
    from funasr_client.callbacks import SimpleCallback

    collector_callback = SimpleCallback(
        on_partial=result_collector,
        on_final=result_collector,
    )

    printer_callback = SimpleCallback(
        on_partial=progress_printer,
        on_final=progress_printer,
    )

    logging_callback = LoggingCallback()

    # Combine callbacks
    multi_callback = MultiCallback(
        [
            collector_callback,
            printer_callback,
            logging_callback,
        ]
    )

    client = create_async_client()

    try:
        await client.start()

        audio_file = "examples/audio/asr_example.wav"
        if Path(audio_file).exists():
            await client.recognize_file(audio_file, multi_callback)

            logging.info("Collected %d results:", len(results_log))
            for i, log_entry in enumerate(results_log, 1):
                logging.info(
                    "%d. %s (confidence: %.2f)",
                    i,
                    log_entry["text"],
                    log_entry["confidence"],
                )

    except Exception:
        logging.exception("Error occurred")
    finally:
        await client.close()


async def async_callback_example():
    """Example using optimized async callbacks.

    This example demonstrates the proper way to use async callbacks without
    blocking the message processing pipeline. Key improvements:

    1. Removed blocking delays (asyncio.sleep) from callbacks
    2. Used background tasks for heavy operations
    3. Non-blocking callback execution ensures real-time performance

    Previous version had delays causing message loss and poor performance.
    """
    logging.info("=== Async Callback Example ===")

    # Async callback that does some processing
    async def async_result_processor(result):
        # Process result efficiently without blocking delays
        # Real-world example: logging, database operations, API calls
        processed_text = result.text.upper()  # Simple processing
        logging.info("Processed: %s", processed_text)

        # For heavy async operations, consider using background tasks:
        # asyncio.create_task(save_to_database(result))
        # asyncio.create_task(send_to_api(result))

        return processed_text

    async def async_error_handler(error):
        logging.error("Async error handler: %s", error)
        # Handle errors efficiently without delays

    # Create optimized async callback
    # Now uses non-blocking execution - callbacks don't block message processing
    async_callback = AsyncSimpleCallback(
        on_partial=async_result_processor,
        on_final=async_result_processor,
        on_error=async_error_handler,
    )

    client = create_async_client()

    try:
        await client.start()

        audio_file = "examples/audio/asr_example.wav"
        if Path(audio_file).exists():
            result = await client.recognize_file(audio_file, async_callback)
            logging.info("Final result: %s", result.text)

    except Exception:
        logging.exception("Error occurred")
    finally:
        await client.close()


async def streaming_with_vad_example():
    """Example using Voice Activity Detection (VAD)."""
    logging.info("=== Streaming with VAD Example ===")

    # Configure client with VAD enabled
    config = ClientConfig(
        server_url=os.environ.get("FUNASR_WS_URL", "ws://localhost:10095"),
        mode=RecognitionMode.ONLINE,  # Online mode for streaming
        enable_vad=True,  # Enable VAD
        chunk_interval=5,  # Process every 5ms for more responsive VAD
    )

    client = AsyncFunASRClient(config=config)

    # Callback to handle VAD events and results
    def on_vad_result(result):
        # Process recognition results with VAD context
        if result.text:
            confidence_info = (
                f" (confidence: {result.confidence:.2f})"
                if result.confidence > 0
                else ""
            )
            logging.info("Speech detected: %s%s", result.text, confidence_info)

    from funasr_client.callbacks import SimpleCallback

    callback = SimpleCallback(
        on_partial=on_vad_result,
        on_final=on_vad_result,
    )

    try:
        await client.start()
        logging.info("VAD-enabled client started")

        # For this example, use file recognition with VAD enabled
        # Real-time microphone streaming would require different setup
        audio_file = "examples/audio/asr_example.wav"
        if Path(audio_file).exists():
            logging.info("Processing audio file with VAD enabled...")
            result = await client.recognize_file(audio_file, callback)
            logging.info("VAD recognition complete: %s", result.text)
        else:
            logging.warning("Audio file not found: %s", audio_file)
            logging.info("In a real application, you would use:")
            logging.info("session = await client.start_realtime(callback)")
            logging.info("# Then stream microphone audio to the session")

    except Exception:
        logging.exception("Error occurred")
    finally:
        await client.close()


async def configuration_presets_example():
    """Example showing different configuration presets."""
    logging.info("=== Configuration Presets Example ===")

    presets = ["low_latency", "high_accuracy", "balanced"]

    for preset_name in presets:
        logging.info("--- Testing %s preset ---", preset_name)

        client = create_async_client(preset=preset_name)

        try:
            await client.start()

            config = client.config
            logging.info("Mode: %s", config.mode)
            logging.info("Timeout: %ss", config.timeout)
            logging.info("Chunk interval: %s", config.chunk_interval)
            logging.info("Enable ITN: %s", config.enable_itn)
            logging.info("Enable VAD: %s", config.enable_vad)

            # You would process audio here
            # result = await client.recognize_file("test.wav")

        except Exception:
            logging.exception("Error with %s", preset_name)
        finally:
            await client.close()


async def connection_statistics_example():
    """Example showing connection statistics and monitoring."""
    logging.info("=== Connection Statistics Example ===")

    client = create_async_client()

    try:
        await client.start()

        # Get initial stats
        stats = await client.get_connection_stats()
        logging.info("Initial connection stats:")
        logging.info("%s", json.dumps(stats, indent=2))

        # Simulate some activity with actual recognition tasks
        audio_file = "examples/audio/asr_example.wav"
        if Path(audio_file).exists():
            for i in range(3):
                logging.info("Running recognition task %d/3...", i + 1)
                result = await client.recognize_file(audio_file)
                logging.info("Task %d result length: %d chars", i + 1, len(result.text))
                await asyncio.sleep(0.1)
        else:
            logging.warning("Audio file not found, skipping activity simulation")

        # Get updated stats
        updated_stats = await client.get_connection_stats()
        logging.info("Updated connection stats:")
        logging.info("%s", json.dumps(updated_stats, indent=2))

        # Monitor connection health
        if "errors" in str(updated_stats) and updated_stats.get("error_count", 0) > 0:
            logging.warning("⚠️  Connection has errors")
        else:
            logging.info("✅ Connection is healthy")

    except Exception:
        logging.exception("Error occurred")
    finally:
        await client.close()


async def concurrent_sessions_example():
    """Example with multiple concurrent recognition sessions."""
    logging.info("=== Concurrent Sessions Example ===")

    # Create multiple clients for concurrent processing
    clients = []
    for _ in range(3):
        client = create_async_client()
        clients.append(client)

    try:
        # Start all clients
        await asyncio.gather(*[client.start() for client in clients])
        logging.info("Started %d concurrent clients", len(clients))

        # Define tasks for each client
        tasks = []
        for i, client in enumerate(clients):

            async def recognize_task(client_idx, client_instance):
                try:
                    logging.info("Client %d: Starting recognition", client_idx)

                    # Use real audio file for recognition
                    audio_file = "examples/audio/asr_example.wav"
                    if Path(audio_file).exists():
                        result = await client_instance.recognize_file(audio_file)
                        logging.info(
                            "Client %d: Recognition complete - '%s'",
                            client_idx,
                            result.text[:50] + "...",
                        )
                        return f"Client {client_idx}: {result.text}"
                    else:
                        # Fallback to simulation if no audio file
                        await asyncio.sleep(1 + client_idx * 0.5)  # Different durations
                        logging.info(
                            "Client %d: Simulation complete (no audio file)", client_idx
                        )
                        return f"Simulated result from client {client_idx}"

                except Exception:
                    logging.exception("Client %d error", client_idx)
                    return f"Error in client {client_idx}"

            task = recognize_task(i, client)
            tasks.append(task)

        # Run all recognition tasks concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)

        logging.info("Concurrent results:")
        for i, result in enumerate(results):
            logging.info("Client %d: %s", i, result)

    except Exception:
        logging.exception("Error in concurrent sessions")

    finally:
        # Close all clients
        await asyncio.gather(*[client.close() for client in clients])
        logging.info("All clients closed")


async def error_recovery_example():
    """Example showing error recovery and reconnection."""
    logging.info("=== Error Recovery Example ===")

    # Configure client with auto-reconnect
    config = ClientConfig(
        server_url=os.environ.get("FUNASR_WS_URL", "ws://localhost:10095"),
        auto_reconnect=True,
        max_retries=3,
        retry_delay=2.0,  # Fixed: retry_delay instead of retry_interval
    )

    client = AsyncFunASRClient(config=config)

    try:
        await client.start()
        logging.info("Client started with auto-reconnect enabled")

        # Test error recovery with actual recognition tasks
        audio_file = "examples/audio/asr_example.wav"

        for attempt in range(5):
            try:
                logging.info(
                    "Attempt %d: Testing connection with recognition", attempt + 1
                )

                if Path(audio_file).exists():
                    result = await client.recognize_file(audio_file)
                    logging.info(
                        "✅ Success - Result length: %d chars", len(result.text)
                    )
                else:
                    # Simulate a simple connection test
                    stats = await client.get_connection_stats()
                    logging.info("✅ Success - Connection stats retrieved")

                # Get connection status
                stats = await client.get_connection_stats()
                if stats.get("client", {}).get("is_started"):
                    logging.info("Connection stable")

            except Exception as e:
                logging.error("❌ Error on attempt %d: %s", attempt + 1, e)

                # Client should auto-reconnect
                logging.info("Waiting for auto-reconnect...")
                await asyncio.sleep(3)

            await asyncio.sleep(1)

    except Exception:
        logging.exception("Error occurred")
    finally:
        await client.close()


async def main():
    """Run all advanced examples."""
    logging.basicConfig(level=logging.INFO)

    logging.info("FunASR Client Advanced Examples")
    logging.info("===============================")

    examples = [
        custom_audio_configuration,
        hotwords_example,
        multiple_callbacks_example,
        async_callback_example,
        streaming_with_vad_example,
        configuration_presets_example,
        connection_statistics_example,
        concurrent_sessions_example,
        error_recovery_example,
    ]

    for example in examples:
        try:
            await example()
        except Exception:
            logging.exception("Example %s failed", example.__name__)

        # Small delay between examples
        await asyncio.sleep(0.5)

    logging.info("=== Advanced Examples Complete ===")


if __name__ == "__main__":
    asyncio.run(main())
