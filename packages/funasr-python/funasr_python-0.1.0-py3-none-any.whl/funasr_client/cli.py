"""Command line interface for FunASR client."""

from __future__ import annotations

import argparse
import asyncio
import contextlib
import json
from pathlib import Path
import sys
from typing import Any, Dict, List, Optional

from . import (
    AsyncFunASRClient,
    RecognitionMode,
    __version__,
    create_async_client,
    setup_logging,
)
from .callbacks import SimpleCallback
from .errors import FunASRError
from .models import FinalResult, PartialResult


def create_parser() -> argparse.ArgumentParser:
    """Create command line argument parser.

    Returns:
        Configured argument parser
    """
    parser = argparse.ArgumentParser(
        prog="funasr-client",
        description="FunASR WebSocket client for speech recognition",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Recognize a single audio file
  funasr-client recognize audio.wav

  # Recognize with specific server
  funasr-client recognize audio.wav --server ws://localhost:10095

  # Use high accuracy mode
  funasr-client recognize audio.wav --preset high_accuracy

  # Recognize multiple files with JSON output
  funasr-client recognize *.wav --output results.json

  # Real-time recognition from microphone
  funasr-client realtime --duration 30

  # Test server connectivity
  funasr-client test-connection --server ws://localhost:10095
        """,
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"funasr-python {__version__}",
    )

    parser.add_argument(
        "--server",
        default="ws://localhost:10095",
        help="FunASR server WebSocket URL (default: ws://localhost:10095)",
    )

    parser.add_argument(
        "--preset",
        choices=["low_latency", "high_accuracy", "balanced"],
        help="Configuration preset to use",
    )

    parser.add_argument(
        "--mode",
        type=str,
        choices=[mode.value for mode in RecognitionMode],
        help="Recognition mode (overrides preset)",
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="Connection timeout in seconds (default: 30)",
    )

    parser.add_argument(
        "--sample-rate",
        type=int,
        choices=[8000, 16000, 44100, 48000],
        help="Audio sample rate in Hz",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        default=0,
        help="Increase verbosity (-v for INFO, -vv for DEBUG)",
    )

    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Suppress all output except results",
    )

    parser.add_argument(
        "--output",
        "-o",
        help="Output file for results (JSON format)",
    )

    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Recognize command
    recognize_parser = subparsers.add_parser(
        "recognize",
        help="Recognize audio files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    recognize_parser.add_argument(
        "files",
        nargs="+",
        help="Audio files to recognize",
    )
    recognize_parser.add_argument(
        "--streaming",
        action="store_true",
        help="Show partial results during recognition",
    )

    # Real-time command
    realtime_parser = subparsers.add_parser(
        "realtime",
        help="Real-time recognition from microphone",
    )
    realtime_parser.add_argument(
        "--duration",
        type=float,
        help="Recording duration in seconds (default: unlimited)",
    )
    realtime_parser.add_argument(
        "--save-audio",
        help="Save recorded audio to file",
    )

    # Test connection command
    subparsers.add_parser(
        "test-connection",
        help="Test connection to FunASR server",
    )

    # Info command
    subparsers.add_parser(
        "info",
        help="Show client and system information",
    )

    return parser


async def recognize_files(
    files: List[str],
    client: AsyncFunASRClient,
    streaming: bool = False,
    quiet: bool = False,
) -> List[Dict[str, Any]]:
    """Recognize multiple audio files.

    Args:
        files: List of file paths
        client: FunASR client instance
        streaming: Whether to show partial results
        quiet: Whether to suppress progress output

    Returns:
        List of recognition results
    """
    results = []

    for i, file_path in enumerate(files):
        if not quiet:
            print(f"Processing {file_path} ({i + 1}/{len(files)})...")

        try:
            file_path_obj = Path(file_path)
            if not file_path_obj.exists():
                print(f"Error: File not found: {file_path}", file=sys.stderr)
                continue

            # Create a container to hold partial results for this file
            current_file_results = {"partial": []}

            def create_partial_callback(container):
                def on_partial(result: PartialResult) -> None:
                    if streaming and not quiet:
                        print(f"  Partial: {result.text}", flush=True)
                    container["partial"].append(
                        {
                            "text": result.text,
                            "confidence": result.confidence,
                            "timestamp": result.timestamp,
                            "is_final": False,
                        }
                    )

                return on_partial

            def on_final(result: FinalResult) -> None:
                if not quiet:
                    print(f"  Final: {result.text}")

            callback = SimpleCallback(
                on_partial=create_partial_callback(current_file_results)
                if streaming
                else None,
                on_final=on_final,
            )

            final_result = await client.recognize_file(file_path, callback)

            result_data = {
                "file": str(file_path_obj.absolute()),
                "filename": file_path_obj.name,
                "text": final_result.text,
                "confidence": final_result.confidence,
                "timestamp": final_result.timestamp,
                "is_final": True,
                "session_id": final_result.session_id,
            }

            if streaming and current_file_results["partial"]:
                result_data["partial_results"] = current_file_results["partial"]

            results.append(result_data)

        except Exception as e:
            error_result = {
                "file": file_path,
                "error": str(e),
                "error_type": type(e).__name__,
            }
            results.append(error_result)
            if not quiet:
                print(f"Error processing {file_path}: {e}", file=sys.stderr)

    return results


async def realtime_recognition(
    client: AsyncFunASRClient,
    duration: Optional[float] = None,
    save_audio: Optional[str] = None,
    quiet: bool = False,
) -> Dict[str, Any]:
    """Perform real-time recognition from microphone.

    Args:
        client: FunASR client instance
        duration: Recording duration in seconds (None for unlimited)
        save_audio: Path to save recorded audio
        quiet: Whether to suppress output

    Returns:
        Recognition results
    """
    if not quiet:
        print("Starting real-time recognition...")
        print("Press Ctrl+C to stop recording")

    results = []
    audio_data = b""

    def on_partial(result: PartialResult) -> None:
        if not quiet:
            print(f"Partial: {result.text}", flush=True)
        results.append(
            {
                "text": result.text,
                "confidence": result.confidence,
                "timestamp": result.timestamp,
                "is_final": False,
            }
        )

    def on_final(result: FinalResult) -> None:
        if not quiet:
            print(f"Final: {result.text}")
        results.append(
            {
                "text": result.text,
                "confidence": result.confidence,
                "timestamp": result.timestamp,
                "is_final": True,
            }
        )

    callback = SimpleCallback(
        on_partial=on_partial,
        on_final=on_final,
    )

    try:
        session = await client.start_realtime(callback)

        if duration:
            await asyncio.sleep(duration)
            await client.end_realtime_session(session)
        else:
            # Wait for Ctrl+C
            try:
                while session.is_active:
                    await asyncio.sleep(0.1)
            except KeyboardInterrupt:
                await client.end_realtime_session(session)

    except KeyboardInterrupt:
        if not quiet:
            print("\nRecording stopped by user")

    # Save audio if requested
    if save_audio and audio_data:
        try:
            with open(save_audio, "wb") as f:
                f.write(audio_data)
            if not quiet:
                print(f"Audio saved to {save_audio}")
        except Exception as e:
            print(f"Error saving audio: {e}", file=sys.stderr)

    return {
        "total_results": len(results),
        "results": results,
    }


async def test_connection(server_url: str, timeout: float = 10.0) -> Dict[str, Any]:
    """Test connection to FunASR server.

    Args:
        server_url: Server WebSocket URL
        timeout: Connection timeout

    Returns:
        Connection test results
    """
    print(f"Testing connection to {server_url}...")

    try:
        # Allow .env override if present
        try:
            from dotenv import load_dotenv

            load_dotenv()
        except Exception:
            pass

        client = AsyncFunASRClient(server_url=server_url, timeout=timeout)
        await client.start()

        # Perform a real handshake by acquiring a connection
        conn = await client.connection_manager.acquire_connection()
        # Capture connection stats
        conn_stats = conn.protocol.get_connection_stats()
        await client.connection_manager.release_connection(conn)

        await client.close()

        return {
            "success": True,
            "server_url": server_url,
            "connection_time": conn_stats.get("connection_time", 0),
            "message": "Connection successful",
        }

    except Exception as e:
        return {
            "success": False,
            "server_url": server_url,
            "error": str(e),
            "error_type": type(e).__name__,
        }


def show_info() -> None:
    """Show client and system information."""
    from . import get_client_info
    from .utils import get_system_info

    client_info = get_client_info()
    system_info = get_system_info()

    print("FunASR Client Information:")
    print(f"  Name: {client_info['name']}")
    print(f"  Version: {client_info['version']}")
    print(f"  Author: {client_info['author']}")
    print(f"  Supported Python: {client_info['supported_python']}")
    print(
        f"  Supported Audio Formats: {', '.join(client_info['supported_audio_formats'])}"
    )
    print(
        f"  Supported Recognition Modes: {', '.join(client_info['supported_recognition_modes'])}"
    )

    print("\nSystem Information:")
    print(f"  Python Version: {system_info['python_version'].split()[0]}")
    print(f"  Platform: {system_info['platform']}")
    print(f"  Architecture: {' '.join(system_info['architecture'])}")

    if "memory" in system_info:
        memory = system_info["memory"]
        total_gb = memory["total"] / (1024**3)
        available_gb = memory["available"] / (1024**3)
        print(f"  Memory: {available_gb:.1f}GB available / {total_gb:.1f}GB total")


async def main() -> None:
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()

    # Setup logging
    if args.quiet:
        log_level = "ERROR"
    elif args.verbose >= 2:
        log_level = "DEBUG"
    elif args.verbose >= 1:
        log_level = "INFO"
    else:
        log_level = "WARNING"

    setup_logging(level=log_level)

    # Handle commands
    if not args.command:
        parser.print_help()
        return

    try:
        if args.command == "info":
            show_info()
            return

        elif args.command == "test-connection":
            result = await test_connection(args.server, args.timeout)
            if args.output:
                with open(args.output, "w") as f:
                    json.dump(result, f, indent=2)
            else:
                if result["success"]:
                    print("✓ Connection successful")
                    print(f"  Connection time: {result['connection_time']:.3f}s")
                else:
                    print("✗ Connection failed")
                    print(f"  Error: {result['error']}")
                    sys.exit(1)
            return

        # Create client configuration
        config_kwargs = {}
        if args.timeout:
            config_kwargs["timeout"] = args.timeout
        if args.sample_rate:
            config_kwargs["audio"] = {"sample_rate": args.sample_rate}
        if args.mode:
            config_kwargs["mode"] = args.mode

        # Create client
        if args.preset:
            client = create_async_client(
                args.server, preset=args.preset, **config_kwargs
            )
        else:
            client = create_async_client(args.server, **config_kwargs)

        try:
            await client.start()

            if args.command == "recognize":
                results = await recognize_files(
                    args.files,
                    client,
                    streaming=args.streaming,
                    quiet=args.quiet,
                )

                # Output results
                if args.output:
                    output_data = {
                        "command": "recognize",
                        "files": args.files,
                        "results": results,
                        "summary": {
                            "total_files": len(args.files),
                            "successful": len([r for r in results if "error" not in r]),
                            "failed": len([r for r in results if "error" in r]),
                        },
                    }
                    with open(args.output, "w") as f:
                        json.dump(output_data, f, indent=2)
                    if not args.quiet:
                        print(f"Results saved to {args.output}")

            elif args.command == "realtime":
                result = await realtime_recognition(
                    client,
                    duration=args.duration,
                    save_audio=args.save_audio,
                    quiet=args.quiet,
                )

                if args.output:
                    with open(args.output, "w") as f:
                        json.dump(result, f, indent=2)
                    if not args.quiet:
                        print(f"Results saved to {args.output}")

        finally:
            await client.close()

    except KeyboardInterrupt:
        if not args.quiet:
            print("\nOperation cancelled by user")
    except FunASRError as e:
        print(f"FunASR Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        if args.verbose >= 2:
            import traceback

            traceback.print_exc()
        sys.exit(1)


def sync_main() -> None:
    """Synchronous main entry point for setuptools console_scripts."""
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())


if __name__ == "__main__":
    sync_main()
