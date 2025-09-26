"""Configuration management system for FunASR client."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, Optional, Union

from .errors import InvalidConfigurationError
from .models import ClientConfig, ConfigPresets


class ConfigManager:
    """Manages configuration loading and validation."""

    def load_config(
        self,
        config: Optional[Union[ClientConfig, Dict[str, Any], str, Path]] = None,
        **overrides: Any,
    ) -> ClientConfig:
        """Load configuration from various sources.

        Args:
            config: Configuration source - can be:
                - ClientConfig instance
                - Dictionary with config values
                - String path to config file
                - Path object to config file
                - None to use defaults
            **overrides: Configuration overrides

        Returns:
            Loaded and validated ClientConfig

        Raises:
            InvalidConfigurationError: If configuration is invalid
        """
        if isinstance(config, ClientConfig):
            base_config = config
        elif isinstance(config, dict):
            base_config = self._from_dict(config)
        elif isinstance(config, (str, Path)):
            base_config = self._from_file(Path(config))
        elif config is None:
            base_config = self._from_env()
        else:
            raise InvalidConfigurationError(
                "config",
                config,
                f"Unsupported config type: {type(config)}",
            )

        # Handle preset parameter
        if "preset" in overrides:
            preset_name = overrides.pop("preset")
            base_config = self.get_preset(preset_name)

        # Apply overrides
        if overrides:
            base_config = self._apply_overrides(base_config, overrides)

        # Validate configuration
        self._validate_config(base_config)

        return base_config

    def get_preset(self, preset_name: str, **overrides: Any) -> ClientConfig:
        """Get a preset configuration.

        Args:
            preset_name: Name of the preset ('low_latency', 'high_accuracy', 'balanced')
            **overrides: Configuration overrides

        Returns:
            Preset configuration with overrides applied

        Raises:
            InvalidConfigurationError: If preset name is invalid
        """
        preset_methods = {
            "low_latency": ConfigPresets.low_latency,
            "high_accuracy": ConfigPresets.high_accuracy,
            "balanced": ConfigPresets.balanced,
        }

        if preset_name not in preset_methods:
            raise InvalidConfigurationError(
                "preset_name",
                preset_name,
                f"Unknown preset: {preset_name}. Available: {list(preset_methods.keys())}",
            )

        config = preset_methods[preset_name]()

        if overrides:
            config = self._apply_overrides(config, overrides)

        self._validate_config(config)
        return config

    def _from_env(self) -> ClientConfig:
        """Load configuration from environment variables.

        Returns:
            Configuration loaded from environment
        """
        config = ClientConfig()

        # Server settings
        if server_url := os.getenv("FUNASR_WS_URL"):
            config.server_url = server_url

        if timeout := os.getenv("FUNASR_TIMEOUT"):
            try:
                config.timeout = float(timeout)
            except ValueError as e:
                raise InvalidConfigurationError(
                    "FUNASR_TIMEOUT",
                    timeout,
                    f"Invalid timeout value: {e}",
                ) from e

        if max_retries := os.getenv("FUNASR_MAX_RETRIES"):
            try:
                config.max_retries = int(max_retries)
            except ValueError as e:
                raise InvalidConfigurationError(
                    "FUNASR_MAX_RETRIES",
                    max_retries,
                    f"Invalid max_retries value: {e}",
                ) from e

        # Recognition settings
        if mode := os.getenv("FUNASR_MODE"):
            from .models import RecognitionMode

            mode_str = mode.strip().lower()
            selected: Optional[RecognitionMode] = None
            # Accept either enum value (e.g., "offline") or enum name (e.g., "OFFLINE")
            for m in RecognitionMode:
                if mode_str == m.value.lower() or mode_str == m.name.lower():
                    selected = m
                    break
            if selected is None:
                allowed = ", ".join(sorted(m.value for m in RecognitionMode))
                raise InvalidConfigurationError(
                    "FUNASR_MODE",
                    mode,
                    f"Invalid mode. Must be one of: {allowed}",
                )
            config.mode = selected

        # Audio settings
        if sample_rate := os.getenv("FUNASR_SAMPLE_RATE"):
            try:
                config.audio.sample_rate = int(sample_rate)
            except ValueError as e:
                raise InvalidConfigurationError(
                    "FUNASR_SAMPLE_RATE",
                    sample_rate,
                    f"Invalid sample rate value: {e}",
                ) from e

        # Feature flags
        if enable_itn := os.getenv("FUNASR_ENABLE_ITN"):
            config.enable_itn = enable_itn.lower() in ("true", "1", "yes", "on")

        if enable_vad := os.getenv("FUNASR_ENABLE_VAD"):
            config.enable_vad = enable_vad.lower() in ("true", "1", "yes", "on")

        if auto_reconnect := os.getenv("FUNASR_AUTO_RECONNECT"):
            config.auto_reconnect = auto_reconnect.lower() in ("true", "1", "yes", "on")

        if debug := os.getenv("FUNASR_DEBUG"):
            config.debug = debug.lower() in ("true", "1", "yes", "on")

        if log_level := os.getenv("FUNASR_LOG_LEVEL"):
            config.log_level = log_level.upper()

        return config

    def _from_dict(self, config_dict: Dict[str, Any]) -> ClientConfig:
        """Load configuration from dictionary.

        Args:
            config_dict: Configuration dictionary

        Returns:
            Configuration loaded from dictionary
        """
        try:
            # Handle nested audio config
            if "audio" in config_dict and isinstance(config_dict["audio"], dict):
                from .models import AudioConfig

                audio_dict = config_dict.pop("audio")
                config = ClientConfig(**config_dict)
                config.audio = AudioConfig(**audio_dict)
                return config
            else:
                return ClientConfig(**config_dict)
        except TypeError as e:
            raise InvalidConfigurationError(
                "config_dict",
                config_dict,
                f"Invalid configuration format: {e}",
            ) from e

    def _from_file(self, config_path: Path) -> ClientConfig:
        """Load configuration from file.

        Args:
            config_path: Path to configuration file

        Returns:
            Configuration loaded from file

        Raises:
            InvalidConfigurationError: If file cannot be loaded or is invalid
        """
        if not config_path.exists():
            raise InvalidConfigurationError(
                "config_path",
                str(config_path),
                "Configuration file does not exist",
            )

        suffix = config_path.suffix.lower()
        if suffix == ".json":
            import json

            try:
                with config_path.open("r", encoding="utf-8") as f:
                    config_dict = json.load(f)
            except json.JSONDecodeError as e:
                raise InvalidConfigurationError(
                    "config_path",
                    str(config_path),
                    f"Invalid JSON configuration: {e}",
                ) from e
            except OSError as e:
                raise InvalidConfigurationError(
                    "config_path",
                    str(config_path),
                    f"Cannot read configuration file: {e}",
                ) from e
            return self._from_dict(config_dict)

        if suffix in (".yaml", ".yml"):
            try:
                import yaml  # type: ignore
            except ImportError as e:
                raise InvalidConfigurationError(
                    "config_path",
                    str(config_path),
                    "PyYAML is required to load YAML configuration files",
                ) from e
            try:
                with config_path.open("r", encoding="utf-8") as f:
                    config_dict = yaml.safe_load(f)
            except yaml.YAMLError as e:  # type: ignore[attr-defined]
                raise InvalidConfigurationError(
                    "config_path",
                    str(config_path),
                    f"Invalid YAML configuration: {e}",
                ) from e
            except OSError as e:
                raise InvalidConfigurationError(
                    "config_path",
                    str(config_path),
                    f"Cannot read configuration file: {e}",
                ) from e
            return self._from_dict(config_dict)

        raise InvalidConfigurationError(
            "config_path",
            str(config_path),
            f"Unsupported configuration file format: {config_path.suffix}",
        )

    def _apply_overrides(
        self,
        base_config: ClientConfig,
        overrides: Dict[str, Any],
    ) -> ClientConfig:
        """Apply configuration overrides.

        Args:
            base_config: Base configuration
            overrides: Override values

        Returns:
            Configuration with overrides applied
        """
        # Create a copy to avoid modifying the original
        config_dict = base_config.__dict__.copy()

        # Handle audio config overrides
        if "audio" in overrides:
            audio_overrides = overrides.pop("audio")
            if isinstance(audio_overrides, dict):
                audio_dict = config_dict["audio"].__dict__.copy()
                audio_dict.update(audio_overrides)
                from .models import AudioConfig

                config_dict["audio"] = AudioConfig(**audio_dict)

        # Apply other overrides
        config_dict.update(overrides)

        return ClientConfig(**config_dict)

    def _validate_config(self, config: ClientConfig) -> None:
        """Validate configuration values.

        Args:
            config: Configuration to validate

        Raises:
            InvalidConfigurationError: If configuration is invalid
        """
        # Validate server URL
        if not config.server_url:
            raise InvalidConfigurationError(
                "server_url",
                config.server_url,
                "Server URL cannot be empty",
            )

        if not (
            config.server_url.startswith("ws://")
            or config.server_url.startswith("wss://")
        ):
            raise InvalidConfigurationError(
                "server_url",
                config.server_url,
                "Server URL must start with 'ws://' or 'wss://'",
            )

        # Validate timeout values
        if config.timeout <= 0:
            raise InvalidConfigurationError(
                "timeout",
                config.timeout,
                "Timeout must be positive",
            )

        if config.retry_delay < 0:
            raise InvalidConfigurationError(
                "retry_delay",
                config.retry_delay,
                "Retry delay cannot be negative",
            )

        # Validate retry settings
        if config.max_retries < 0:
            raise InvalidConfigurationError(
                "max_retries",
                config.max_retries,
                "Max retries cannot be negative",
            )

        # Validate audio settings
        supported_rates = [8000, 16000, 22050, 44100, 48000]
        if config.audio.sample_rate not in supported_rates:
            raise InvalidConfigurationError(
                "audio.sample_rate",
                config.audio.sample_rate,
                f"Sample rate must be one of: {supported_rates}",
            )

        if config.audio.channels not in (1, 2):
            raise InvalidConfigurationError(
                "audio.channels",
                config.audio.channels,
                "Channels must be 1 (mono) or 2 (stereo)",
            )

        if config.audio.sample_width not in (1, 2, 3, 4):
            raise InvalidConfigurationError(
                "audio.sample_width",
                config.audio.sample_width,
                "Sample width must be 1, 2, 3, or 4 bytes",
            )

        # Validate chunk settings
        if len(config.chunk_size) != 3:
            raise InvalidConfigurationError(
                "chunk_size",
                config.chunk_size,
                "Chunk size must be a list of 3 integers [left, chunk, right]",
            )

        if any(size < 0 for size in config.chunk_size):
            raise InvalidConfigurationError(
                "chunk_size",
                config.chunk_size,
                "Chunk sizes cannot be negative",
            )

        if config.chunk_interval <= 0:
            raise InvalidConfigurationError(
                "chunk_interval",
                config.chunk_interval,
                "Chunk interval must be positive",
            )

        # Validate buffer settings
        if config.buffer_size <= 0:
            raise InvalidConfigurationError(
                "buffer_size",
                config.buffer_size,
                "Buffer size must be positive",
            )

        if config.connection_pool_size <= 0:
            raise InvalidConfigurationError(
                "connection_pool_size",
                config.connection_pool_size,
                "Connection pool size must be positive",
            )

        # Validate log level
        valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if config.log_level not in valid_log_levels:
            raise InvalidConfigurationError(
                "log_level",
                config.log_level,
                f"Log level must be one of: {valid_log_levels}",
            )

# Global configuration manager instance
config_manager = ConfigManager()
