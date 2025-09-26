#
#  Copyright (c) 2025, NVIDIA CORPORATION. All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an
# express license agreement from NVIDIA CORPORATION is strictly
# prohibited.
#

import logging
import os
from dataclasses import fields
from typing import Optional, Type, TypeVar

import yaml  # type: ignore[import-untyped, unused-ignore]

from training_telemetry.config import (
    ApplicationConfig,
    BackendConfig,
    BackendType,
    FileBackendConfig,
    LoggerBackendConfig,
    NVTXBackendConfig,
    OTLPLogsBackendConfig,
    OTLPLogsFormat,
    OTLPTracesBackendConfig,
    TelemetryConfig,
    default_backends,
)

T = TypeVar("T")


def load_config_from_dict(config: dict) -> TelemetryConfig:
    """Create a TelemetryConfig from a dictionary containing some or all of the class properties."""
    if not config:
        return TelemetryConfig()

    config = config.copy()
    config["backends"] = [_backend_from_dict(backend) for backend in config["backends"]] if "backends" in config else []
    if "application" in config:
        config["application"] = _dataclass_from_dict(ApplicationConfig, config["application"])
    if "log_level" in config:
        config["log_level"] = _get_log_level(config["log_level"])
    return TelemetryConfig(**config)


def load_config_from_env(config: dict) -> TelemetryConfig:
    """
    Create a TelemetryConfig from environment variables with the same name as the class properties, but uppercase
    and with the prefix "TRAINING_TELEMETRY_".
    If an environment variable is not set, any value already in the config dictionary, if it exists, will be used.

    Args:
        config: The configuration dictionary to update, for example the config read from file, or set manually from the user.
                Note that this dictionary will be updated in place.
    """
    application: ApplicationConfig = _dataclass_from_env(
        ApplicationConfig,
        config["application"] if "application" in config else {},
        ["TRAINING_TELEMETRY_APPLICATION", "APPLICATION", ""],
    )
    backends = _load_backends_from_env(config, application.rank, application.world_size)
    log_level = _get_log_level(os.getenv("TRAINING_TELEMETRY_LOG_LEVEL", "INFO"))
    log_format = os.getenv("TRAINING_TELEMETRY_LOG_FORMAT")
    return TelemetryConfig(backends=backends, application=application, log_level=log_level, log_format=log_format)


def _load_backends_from_env(config: dict, rank: int, world_size: int) -> list[BackendConfig]:
    """
    Helper function to load_config_from_env to load the backends from environment variables.
    Only load backends that are either in the config dict, or have at least one environment variable set.
    If no backends are loaded, return the default backends.
    """
    backends: list[BackendConfig] = []
    backend_configs_by_type: dict[BackendType, dict] = {}
    for backend_config in config["backends"] if "backends" in config else []:
        backend_configs_by_type[BackendType(backend_config["backend_type"])] = backend_config

    for backend_type in BackendType:
        enabled_in_env = os.getenv(f"TRAINING_TELEMETRY_BACKENDS_{backend_type.value.upper()}_ENABLED_RANKS") in (
            "all",
            str(rank),
            str(rank - world_size),
        )
        enabled_in_config = backend_type in backend_configs_by_type
        if enabled_in_env or enabled_in_config:
            backends.append(
                _backend_from_env(backend_type, backend_configs_by_type[backend_type] if enabled_in_config else {})
            )

    return backends if backends else default_backends()


def load_config(
    config_file: Optional[str | os.PathLike] = None,
    defaults: Optional[dict] = None,
    override_from_env: bool = True,
) -> TelemetryConfig:
    """
    Create a TelemetryConfig from a file and with optional overrides from environment variables, and starting from optional default values.
    The order of precedence is: command line defaults, config file, environment variables. Environment variables will
    override the config file and config file will override command line defaults.

    Args:
        config_file: The path or path-like object to the config file.
        defaults: Optional command-line default set of values that can be passed by the application code.
        override_from_env: If true, the default, the config will be overridden by environment variables, if they are set. These
        environment variables must have the prefix "TRAINING_TELEMETRY_", followed by the name of the class property.
    """
    # If no config arguments are provided, return the default config.
    if not (config_file or defaults or override_from_env):
        return TelemetryConfig()

    if not config_file:
        yaml_config = {}
    else:
        with open(config_file, "r") as file:
            yaml_config = yaml.safe_load(file)
            if not yaml_config:
                raise RuntimeError(f"Could not parse config file {config_file}")
    if defaults:
        config = defaults.copy() | yaml_config
    else:
        config = yaml_config

    if override_from_env:
        return load_config_from_env(config)
    else:
        return load_config_from_dict(config)


def _backend_from_dict(config: dict) -> BackendConfig:
    """Create a BackendConfig from a dictionary by matching the backend type."""
    if isinstance(config["backend_type"], str):
        config["backend_type"] = BackendType(config["backend_type"])

    match config["backend_type"]:
        case BackendType.LOGGER:
            return _dataclass_from_dict(LoggerBackendConfig, config)
        case BackendType.FILE:
            return _dataclass_from_dict(FileBackendConfig, config)
        case BackendType.OTLP_TRACES:
            return _dataclass_from_dict(OTLPTracesBackendConfig, config)
        case BackendType.OTLP_LOGS:
            return _dataclass_from_dict(OTLPLogsBackendConfig, config)
        case BackendType.NVTX:
            return _dataclass_from_dict(NVTXBackendConfig, config)
        case _:
            raise ValueError(f"Unsupported backend type: {config['backend_type']}")


def _backend_from_env(backend_type: BackendType, config: dict) -> BackendConfig:
    """Create a BackendConfig from environment variables by matching the backend type."""
    match backend_type:
        case BackendType.LOGGER:
            return _dataclass_from_env(LoggerBackendConfig, config, ["TRAINING_TELEMETRY_BACKENDS_LOGGER"])
        case BackendType.FILE:
            return _dataclass_from_env(FileBackendConfig, config, ["TRAINING_TELEMETRY_BACKENDS_FILE"])
        case BackendType.OTLP_TRACES:
            return _dataclass_from_env(OTLPTracesBackendConfig, config, ["TRAINING_TELEMETRY_BACKENDS_OTLP_TRACES"])
        case BackendType.OTLP_LOGS:
            return _dataclass_from_env(OTLPLogsBackendConfig, config, ["TRAINING_TELEMETRY_BACKENDS_OTLP_LOGS"])
        case BackendType.NVTX:
            return _dataclass_from_env(NVTXBackendConfig, config, ["TRAINING_TELEMETRY_BACKENDS_NVTX"])
        case _:
            raise ValueError(f"Unsupported backend type: {backend_type}")


def _dataclass_from_env(cls: Type[T], config: dict, env_prefixes: list[str]) -> T:
    """
    Create an instance of a dataclass either from the environment variables, if set, or from the config dictionary.
    If neither environment variables nor the config dictionary have the value for a field, the default value will be used.
    This assumes that the dataclass has default values for all fields, as is the case for the config dataclasses.

    Args:
        config: The configuration dictionary to update, for example the config read from file, or set manually from the user.
                Note that this dictionary will be updated in place.
    """
    for field in fields(cls):  # type: ignore[arg-type]
        env_value = None
        for env_prefix in env_prefixes:
            env_value = os.getenv(f"{env_prefix}_{field.name.upper()}") if env_prefix else os.getenv(field.name.upper())
            if env_value:
                break

        if env_value:
            config[field.name] = env_value
        elif field.name not in config:
            config[field.name] = field.default

    return _dataclass_from_dict(cls, config)


def _dataclass_from_dict(cls: Type[T], config: dict) -> T:
    """
    Create an instance of a dataclass from a dictionary by converting the strings to either
    supported enums, log level, integers or booleans. These are the types supported by
    the config dataclasses.
    """
    for field in fields(cls):  # type: ignore[arg-type]
        if field.name not in config:
            continue

        # Special case for log level because it can be a string or an integer.
        if field.name == "log_level":
            config["log_level"] = _get_log_level(config["log_level"])
            continue

        # The rest is transformation of strings to the supported types.
        if not isinstance(config[field.name], str):
            continue

        if field.type == OTLPLogsFormat:
            config[field.name] = OTLPLogsFormat(config["format"])
        elif field.type == BackendType:
            config[field.name] = BackendType(config["backend_type"])
        elif field.type == bool:
            config[field.name] = config[field.name].upper() == "TRUE"
        elif field.type == int:
            config[field.name] = int(config[field.name])

    return cls(**config)


def _get_log_level(log_level: str | int) -> int:
    """
    Get the log level. If we receive an integer, we return it as is as we assume this is in the form logging.INFO, etc.
    If we receive a string, we assume can be converted to a level. Since python 3.11 there is a getLevelNamesMapping function
    that can be used to get the log level from the name but we need to support python 3.10 too.
    """
    if isinstance(log_level, int):
        return log_level
    if hasattr(logging, "getLevelNamesMapping"):
        level_mapping = getattr(logging, "getLevelNamesMapping")()
        return int(level_mapping[log_level.upper()])
    else:
        return int(getattr(logging, log_level.upper()))
