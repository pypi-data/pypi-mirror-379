"""Unit tests for FunASR client configuration system."""

import json
import os
import tempfile
from unittest.mock import patch

import pytest

from funasr_client.config import ConfigManager
from funasr_client.errors import InvalidConfigurationError
from funasr_client.models import (
    ClientConfig,
    ConfigPresets,
    RecognitionMode,
)


class TestConfigManager:
    """Test configuration manager."""



    def test_load_default_config(self):
        """Test loading default configuration."""
        # Clear any environment variables that might interfere
        with patch.dict(os.environ, {}, clear=True):
            manager = ConfigManager()
            config = manager.load_config()

            assert isinstance(config, ClientConfig)
            assert config.server_url == "ws://localhost:10095"
            assert config.timeout == 30.0
            assert config.mode == RecognitionMode.TWO_PASS

    def test_load_config_from_dict(self):
        """Test loading configuration from dictionary."""
        config_dict = {
            "server_url": "ws://test.example.com:8080",
            "timeout": 60.0,
            "mode": "online",
            "audio": {
                "sample_rate": 44100,
                "channels": 2,
            },
        }

        manager = ConfigManager()
        config = manager.load_config(config_dict)

        assert config.server_url == "ws://test.example.com:8080"
        assert config.timeout == 60.0
        assert config.mode == RecognitionMode.ONLINE
        assert config.audio.sample_rate == 44100
        assert config.audio.channels == 2

    def test_load_config_from_file(self):
        """Test loading configuration from file."""
        config_data = {
            "server_url": "ws://file.example.com:9090",
            "timeout": 45.0,
            "mode": "2pass",
        }

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(config_data, f)
            temp_path = f.name

        try:
            manager = ConfigManager()
            config = manager.load_config(temp_path)

            assert config.server_url == "ws://file.example.com:9090"
            assert config.timeout == 45.0
            assert config.mode == RecognitionMode.TWO_PASS
        finally:
            os.unlink(temp_path)

    @pytest.mark.skip("YAML support not installed")
    def test_load_config_from_yaml_file(self):
        """Test loading configuration from YAML file."""
        yaml_content = """
server_url: "ws://yaml.example.com:7070"
timeout: 25.0
mode: "offline"
audio:
  sample_rate: 48000
  channels: 1
"""

        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            f.write(yaml_content)
            temp_path = f.name

        try:
            with patch("yaml.safe_load") as mock_yaml_load:
                mock_yaml_load.return_value = {
                    "server_url": "ws://yaml.example.com:7070",
                    "timeout": 25.0,
                    "mode": "offline",
                    "audio": {
                        "sample_rate": 48000,
                        "channels": 1,
                    },
                }

                manager = ConfigManager()
                config = manager.load_config(temp_path)

                assert config.server_url == "ws://yaml.example.com:7070"
                assert config.timeout == 25.0
                assert config.mode == RecognitionMode.OFFLINE
                assert config.audio.sample_rate == 48000
                assert config.audio.channels == 1
        finally:
            os.unlink(temp_path)

    def test_load_config_missing_file(self):
        """Test loading configuration from non-existent file."""
        manager = ConfigManager()

        with pytest.raises(InvalidConfigurationError):
            manager.load_config("/non/existent/file.json")

    def test_load_config_invalid_json(self):
        """Test loading configuration from invalid JSON file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("{ invalid json }")
            temp_path = f.name

        try:
            manager = ConfigManager()
            with pytest.raises(InvalidConfigurationError):
                manager.load_config(temp_path)
        finally:
            os.unlink(temp_path)











    def test_environment_variable_override(self):
        """Test environment variable configuration override."""
        with patch.dict(
            os.environ,
            {
                "FUNASR_WS_URL": "ws://env.example.com:9999",
                "FUNASR_TIMEOUT": "50.0",
                "FUNASR_MODE": "offline",
            },
        ):
            manager = ConfigManager()
            config = manager.load_config()

            assert config.server_url == "ws://env.example.com:9999"
            assert config.timeout == 50.0
            assert config.mode == RecognitionMode.OFFLINE

    def test_config_preset_loading(self):
        """Test loading configuration presets."""
        manager = ConfigManager()

        # Test low latency preset
        low_latency_config = manager.get_preset("low_latency")
        assert low_latency_config.mode == RecognitionMode.ONLINE
        assert low_latency_config.chunk_interval == 5

        # Test high accuracy preset
        high_accuracy_config = manager.get_preset("high_accuracy")
        assert high_accuracy_config.mode == RecognitionMode.TWO_PASS
        assert high_accuracy_config.enable_itn is True

        # Test balanced preset
        balanced_config = manager.get_preset("balanced")
        assert balanced_config.mode == RecognitionMode.TWO_PASS
        assert balanced_config.chunk_interval == 8

    def test_invalid_preset(self):
        """Test loading invalid preset."""
        manager = ConfigManager()

        with pytest.raises(InvalidConfigurationError):
            manager.get_preset("invalid_preset")




class TestConfigPresets:
    """Test configuration presets."""

    def test_all_presets_exist(self):
        """Test that all expected presets exist."""
        expected_presets = ["low_latency", "high_accuracy", "balanced"]

        for preset_name in expected_presets:
            preset_func = getattr(ConfigPresets, preset_name)
            config = preset_func()
            assert isinstance(config, ClientConfig)

    def test_preset_differences(self):
        """Test that presets have different configurations."""
        low_latency = ConfigPresets.low_latency()
        high_accuracy = ConfigPresets.high_accuracy()
        balanced = ConfigPresets.balanced()

        # Mode differences
        assert low_latency.mode == RecognitionMode.ONLINE
        assert high_accuracy.mode == RecognitionMode.TWO_PASS
        assert balanced.mode == RecognitionMode.TWO_PASS

        # Timeout differences
        assert low_latency.timeout < balanced.timeout < high_accuracy.timeout

        # Chunk size differences
        assert low_latency.chunk_size != high_accuracy.chunk_size
        assert balanced.chunk_size != low_latency.chunk_size

    def test_preset_validation(self):
        """Test that all presets produce valid configurations."""
        for preset_name in ["low_latency", "high_accuracy", "balanced"]:
            preset_func = getattr(ConfigPresets, preset_name)
            config = preset_func()

            # Should not raise any validation errors during creation
            assert isinstance(config, ClientConfig)


if __name__ == "__main__":
    pytest.main([__file__])
