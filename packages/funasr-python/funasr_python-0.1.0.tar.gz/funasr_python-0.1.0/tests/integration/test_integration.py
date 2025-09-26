"""Integration tests for FunASR client components."""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from funasr_client import (
    AsyncFunASRClient,
    FunASRClient,
    SimpleCallback,
    create_async_client,
)
from funasr_client.models import ClientConfig, FinalResult, PartialResult


class TestEndToEndIntegration:
    """Test end-to-end integration scenarios."""

    @patch("funasr_client.client.StreamingProtocol")
    @patch("funasr_client.audio.AudioFileStreamer")
    def test_complete_recognition_workflow(
        self, mock_streamer_class, mock_protocol_class
    ):
        """Test complete recognition workflow from file to result."""
        # Setup mocks
        mock_protocol = AsyncMock()
        mock_protocol_class.return_value = mock_protocol

        mock_streamer = MagicMock()
        mock_streamer.get_duration.return_value = 2.5
        mock_streamer.stream_chunks.return_value = [b"chunk1", b"chunk2", b"chunk3"]
        mock_streamer_class.return_value = mock_streamer

        # Mock recognition result
        final_result = FinalResult(
            text="This is a complete integration test",
            confidence=0.92,
            timestamp=1234567890.0,
            is_final=True,
            session_id="integration_session",
        )
        mock_protocol.recognize_file.return_value = final_result

        # Create client and recognize file
        client = FunASRClient()
        client.connect()

        result = client.recognize_file("test_integration.wav")

        # Verify result
        assert isinstance(result, FinalResult)
        assert result.text == "This is a complete integration test"
        assert result.confidence == 0.92
        assert result.is_final is True

        # Verify protocol was called correctly
        mock_protocol.recognize_file.assert_called_once()

        client.disconnect()

    @patch("funasr_client.client.StreamingProtocol")
    @patch("funasr_client.audio.AudioFileStreamer")
    async def test_async_complete_recognition_workflow(
        self, mock_streamer_class, mock_protocol_class
    ):
        """Test async complete recognition workflow."""
        # Setup mocks
        mock_protocol = AsyncMock()
        mock_protocol_class.return_value = mock_protocol

        mock_streamer = MagicMock()
        mock_streamer.get_duration.return_value = 3.0
        mock_streamer_class.return_value = mock_streamer

        # Mock recognition result
        final_result = FinalResult(
            text="Async integration test successful",
            confidence=0.95,
            timestamp=1234567890.0,
            is_final=True,
            session_id="async_integration_session",
        )
        mock_protocol.recognize_file.return_value = final_result

        # Create async client and recognize file
        client = AsyncFunASRClient()
        await client.start()

        result = await client.recognize_file("async_integration.wav")

        # Verify result
        assert isinstance(result, FinalResult)
        assert result.text == "Async integration test successful"
        assert result.confidence == 0.95

        await client.close()

    @patch("funasr_client.client.StreamingProtocol")
    async def test_realtime_recognition_workflow(self, mock_protocol_class):
        """Test real-time recognition workflow."""
        mock_protocol = AsyncMock()
        mock_protocol_class.return_value = mock_protocol

        # Mock session and streaming
        from funasr_client.models import RealtimeSession

        mock_session = RealtimeSession(session_id="realtime_integration")
        mock_protocol.start_realtime.return_value = mock_session

        client = AsyncFunASRClient()
        await client.start()

        # Start real-time session
        session = await client.start_realtime()
        assert session.session_id == "realtime_integration"

        # Send some audio chunks
        audio_chunks = [b"chunk1", b"chunk2", b"chunk3"]
        for chunk in audio_chunks:
            await client.send_audio_chunk(chunk)

        # End session
        await client.end_realtime_session(session)

        # Verify protocol calls
        mock_protocol.start_realtime.assert_called_once()
        mock_protocol.end_realtime_session.assert_called_once_with(session)
        assert mock_protocol.send_audio_chunk.call_count == len(audio_chunks)

        await client.close()


class TestCallbackIntegration:
    """Test integration with callback systems."""

    @patch("funasr_client.client.StreamingProtocol")
    def test_callback_integration(self, mock_protocol_class):
        """Test callback integration during recognition."""
        mock_protocol = AsyncMock()
        mock_protocol_class.return_value = mock_protocol

        # Setup callback to capture results
        partial_results = []
        final_results = []

        def on_partial(result: PartialResult):
            partial_results.append(result)

        def on_final(result: FinalResult):
            final_results.append(result)

        callback = SimpleCallback(
            on_partial=on_partial,
            on_final=on_final,
        )

        # Mock final result
        final_result = FinalResult(
            text="Callback integration test",
            confidence=0.88,
            timestamp=1234567890.0,
            is_final=True,
            session_id="callback_session",
        )
        mock_protocol.recognize_file.return_value = final_result

        # Recognize with callback
        client = FunASRClient()
        result = client.recognize_file("callback_test.wav", callback)

        # Verify result and callback
        assert isinstance(result, FinalResult)
        assert len(final_results) == 1
        assert final_results[0].text == "Callback integration test"

    @patch("funasr_client.client.StreamingProtocol")
    async def test_async_callback_integration(self, mock_protocol_class):
        """Test async callback integration."""
        mock_protocol = AsyncMock()
        mock_protocol_class.return_value = mock_protocol

        # Setup async callback to capture results
        partial_results = []
        final_results = []

        async def on_partial_async(result: PartialResult):
            partial_results.append(result)

        async def on_final_async(result: FinalResult):
            final_results.append(result)

        from funasr_client.callbacks import AsyncSimpleCallback

        callback = AsyncSimpleCallback(
            on_partial=on_partial_async,
            on_final=on_final_async,
        )

        # Mock final result
        final_result = FinalResult(
            text="Async callback integration",
            confidence=0.93,
            timestamp=1234567890.0,
            is_final=True,
            session_id="async_callback_session",
        )
        mock_protocol.recognize_file.return_value = final_result

        # Recognize with async callback
        client = AsyncFunASRClient()
        await client.start()

        result = await client.recognize_file("async_callback_test.wav", callback)

        # Verify result and callback
        assert isinstance(result, FinalResult)
        assert len(final_results) == 1
        assert final_results[0].text == "Async callback integration"

        await client.close()


class TestConfigurationIntegration:
    """Test integration with different configurations."""

    def test_preset_configuration_integration(self):
        """Test integration with configuration presets."""
        # Test low latency preset
        client = create_async_client(preset="low_latency")
        assert client.config.timeout == 10.0  # Low latency timeout
        assert client.config.chunk_interval == 5

        # Test high accuracy preset
        client = create_async_client(preset="high_accuracy")
        assert client.config.timeout == 60.0  # High accuracy timeout
        assert client.config.enable_itn is True

        # Test balanced preset
        client = create_async_client(preset="balanced")
        assert client.config.timeout == 30.0  # Balanced timeout
        assert client.config.chunk_interval == 8

    def test_custom_configuration_integration(self):
        """Test integration with custom configuration."""
        config = ClientConfig(
            server_url="ws://integration.test.com:8080",
            timeout=45.0,
            mode="online",
            enable_vad=True,
            hotwords={"test": 10, "integration": 15},
        )

        client = create_async_client(config=config)

        assert client.config.server_url == "ws://integration.test.com:8080"
        assert client.config.timeout == 45.0
        assert client.config.enable_vad is True
        assert client.config.hotwords == {"test": 10, "integration": 15}


class TestErrorHandlingIntegration:
    """Test error handling across components."""

    @patch("funasr_client.client.StreamingProtocol")
    def test_connection_error_propagation(self, mock_protocol_class):
        """Test error propagation from protocol to client."""
        from funasr_client.errors import ConnectionError

        mock_protocol = AsyncMock()
        mock_protocol.connect.side_effect = ConnectionError(
            "Integration connection failed"
        )
        mock_protocol_class.return_value = mock_protocol

        client = FunASRClient()

        with pytest.raises(ConnectionError, match="Integration connection failed"):
            client.connect()

    @patch("funasr_client.client.StreamingProtocol")
    async def test_async_error_propagation(self, mock_protocol_class):
        """Test async error propagation."""
        from funasr_client.errors import ProtocolError

        mock_protocol = AsyncMock()
        mock_protocol.recognize_file.side_effect = ProtocolError(
            "Protocol integration error"
        )
        mock_protocol_class.return_value = mock_protocol

        client = AsyncFunASRClient()
        await client.start()

        with pytest.raises(ProtocolError, match="Protocol integration error"):
            await client.recognize_file("error_test.wav")

        await client.close()

    @patch("funasr_client.client.StreamingProtocol")
    def test_recovery_integration(self, mock_protocol_class):
        """Test error recovery integration."""
        from funasr_client.errors import NetworkError

        mock_protocol = AsyncMock()

        # First call fails, second succeeds
        mock_protocol.connect.side_effect = [
            NetworkError("Network temporarily unavailable"),
            None,  # Success
        ]
        mock_protocol_class.return_value = mock_protocol

        config = ClientConfig(auto_reconnect=True, max_retries=2)
        client = FunASRClient(config=config)

        # Should eventually succeed
        client.connect()
        assert client.is_connected

        # Should have been called twice (initial + retry)
        assert mock_protocol.connect.call_count == 2


class TestAudioProcessingIntegration:
    """Test integration with audio processing components."""

    @patch("funasr_client.client.StreamingProtocol")
    @patch("funasr_client.audio.AudioProcessor")
    def test_audio_processing_pipeline(self, mock_processor_class, mock_protocol_class):
        """Test audio processing pipeline integration."""
        mock_protocol = AsyncMock()
        mock_protocol_class.return_value = mock_protocol

        mock_processor = MagicMock()
        mock_processor.load_audio_file.return_value = (
            # Mock numpy array (audio data) and sample rate
            MagicMock(shape=(16000,)),  # 1 second of audio
            16000,
        )
        mock_processor_class.return_value = mock_processor

        # Mock final result
        final_result = FinalResult(
            text="Audio processing integration",
            confidence=0.91,
            timestamp=1234567890.0,
            is_final=True,
            session_id="audio_session",
        )
        mock_protocol.recognize_file.return_value = final_result

        client = FunASRClient()
        result = client.recognize_file("audio_integration.wav")

        # Verify audio processor was used
        mock_processor.load_audio_file.assert_called()

        # Verify result
        assert result.text == "Audio processing integration"

    @patch("funasr_client.audio.AudioFileStreamer")
    def test_streaming_integration(self, mock_streamer_class):
        """Test streaming integration."""
        mock_streamer = MagicMock()

        # Mock streaming chunks
        test_chunks = [b"audio_chunk_1", b"audio_chunk_2", b"audio_chunk_3"]
        mock_streamer.stream_chunks.return_value = test_chunks
        mock_streamer.get_duration.return_value = 1.5
        mock_streamer_class.return_value = mock_streamer

        # Test that streamer is properly initialized and used
        from funasr_client.audio import AudioFileStreamer

        streamer = AudioFileStreamer("streaming_test.wav", chunk_size=1024)

        chunks = list(streamer.stream_chunks())
        duration = streamer.get_duration()

        assert len(chunks) == 3
        assert duration == 1.5


class TestConcurrencyIntegration:
    """Test concurrent operations integration."""

    @patch("funasr_client.client.StreamingProtocol")
    async def test_concurrent_recognition(self, mock_protocol_class):
        """Test concurrent recognition requests."""
        mock_protocol = AsyncMock()
        mock_protocol_class.return_value = mock_protocol

        # Mock different results for different files
        def mock_recognize_file(file_path, callback=None):
            if "file1" in str(file_path):
                return FinalResult(
                    text="Result from file 1",
                    confidence=0.90,
                    timestamp=1234567890.0,
                    is_final=True,
                    session_id="concurrent_session_1",
                )
            else:
                return FinalResult(
                    text="Result from file 2",
                    confidence=0.85,
                    timestamp=1234567891.0,
                    is_final=True,
                    session_id="concurrent_session_2",
                )

        mock_protocol.recognize_file.side_effect = mock_recognize_file

        client = AsyncFunASRClient()
        await client.start()

        # Run concurrent recognition tasks
        tasks = [
            client.recognize_file("concurrent_file1.wav"),
            client.recognize_file("concurrent_file2.wav"),
        ]

        results = await asyncio.gather(*tasks)

        # Verify both results
        assert len(results) == 2
        assert results[0].text == "Result from file 1"
        assert results[1].text == "Result from file 2"

        await client.close()

    @patch("funasr_client.client.StreamingProtocol")
    async def test_concurrent_realtime_sessions(self, mock_protocol_class):
        """Test concurrent real-time sessions."""
        mock_protocol = AsyncMock()
        mock_protocol_class.return_value = mock_protocol

        # Mock session creation
        from funasr_client.models import RealtimeSession

        def mock_start_realtime(callback=None):
            session_id = f"concurrent_realtime_{len(mock_protocol.start_realtime.call_args_list)}"
            return RealtimeSession(session_id=session_id)

        mock_protocol.start_realtime.side_effect = mock_start_realtime

        client = AsyncFunASRClient()
        await client.start()

        # Start multiple concurrent real-time sessions
        session1 = await client.start_realtime()
        session2 = await client.start_realtime()

        assert session1.session_id != session2.session_id
        assert mock_protocol.start_realtime.call_count == 2

        # End both sessions
        await client.end_realtime_session(session1)
        await client.end_realtime_session(session2)

        await client.close()


if __name__ == "__main__":
    pytest.main([__file__])
