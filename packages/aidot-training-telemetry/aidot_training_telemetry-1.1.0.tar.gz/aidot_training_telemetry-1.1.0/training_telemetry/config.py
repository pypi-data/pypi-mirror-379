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
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


@dataclass
class ApplicationConfig:
    """Configuration for the application creating the telemetry data."""

    # The job name can be used to group jobs with the same training characteristics.
    job_name: str = "unknown"
    # The job id and the job_restart_count should uniquely identify a job run.
    job_id: str = "unknown"
    # The global rank of the process.
    rank: int = 0
    # The total number of ranks in the job run.
    world_size: int = 1
    # If the same job is restarted without changing the job id, this needs to be incremented.
    job_restart_count: int = 0
    # The name of the environment the job is running in, for example the cluster name, if known
    environment: str = "unknown"


class BackendType(str, Enum):
    """Supported backend types for telemetry data."""

    LOGGER = "logger"
    FILE = "file"
    NVTX = "nvtx"
    OTLP_TRACES = "otlp_traces"
    OTLP_LOGS = "otlp_logs"


@dataclass
class BackendConfig:
    """Configuration for a specific backend."""

    # The backend type, we currently support logger, file, and Open Telemetry (OTEL).
    backend_type: BackendType


@dataclass
class LoggerBackendConfig(BackendConfig):
    """Configuration for the logger backend, which logs JSON events using a python logger."""

    backend_type: BackendType = BackendType.LOGGER

    # The name of the logger to use.
    name: str = "training_telemetry"
    # If this is true, then the log context will be propagated to the root logger,
    # which could result in duplicate logs, so normally this should be false.
    # However, unit tests need this to be true to capture the log messages for testing
    propagate_log_context: bool = False
    # The format of the log message.
    log_format: Optional[str] = None
    # The log level to use for the logger.
    log_level: int = logging.INFO
    # If rank_aware is true, then the rank number will be added to the logger name.
    # For example, if the logger name is "training_telemetry" and the rank is 0,
    # then the logger name will be "training_telemetry_rank0".
    rank_aware: bool = True
    # If this is true, then only error events will be logged.
    errors_only: bool = False


@dataclass
class FileBackendConfig(BackendConfig):
    """Configuration for the file backend, which logs JSON events to a file."""

    backend_type: BackendType = BackendType.FILE
    # The output file path without the extension, should contain the directory
    # and the base name of the file.
    # The extension will be added automatically as .json, the only
    # format currently supported by the file backend. Later, we may
    # add .csv or other formats.
    output_file_path: str = "/tmp/training_telemetry"
    # If this is true, then the file path will contain the rank number
    # before the .json extension. For example, if the output file path
    # is "/tmp/training_telemetry" and the rank is 0, then the file will be "/tmp/training_telemetry_rank0.json".
    # The backend will likely be created before the torch distributed process group is initialized,
    # so we need to use the RANK environment variable to determine the rank number.
    rank_aware: bool = True
    # If this is true, then the file path will contain the date and time
    # after the rank number. For example, if the output file path
    # is "/tmp/training_telemetry" and the date and time is 2021-01-01 12:00:00, then the file
    # will be "/tmp/training_telemetry_rank0_20210101_120000.json".
    date_aware: bool = True


@dataclass
class OTLPTracesBackendConfig(BackendConfig):
    """
    Configuration for the Open Telemetry traces backend,
    which converts spans and events to OTEL traces.
    """

    backend_type: BackendType = BackendType.OTLP_TRACES
    # The exporter to use, OTLP can be send over grpc or http, and console will print to the console.
    exporter: str = "grpc"  # or "http", "console"
    # The endpoint when using either grpc or http as an OTLP exporter, the grpc port is normally 4317 and the http port is 4318.
    endpoint: str = "http://localhost:4317"  # or "http://localhost:4318"


class OTLPLogsFormat(str, Enum):
    """The format of the logs to send over OTLP."""

    # This format is identical to the python logger backend, which logs event
    # properties as key = value pairs separated by a pipe character.
    KEY_VALUE = "key_value"
    # This format is identical to the file backend, which logs events as JSON.
    JSON = "json"


@dataclass
class OTLPLogsBackendConfig(BackendConfig):
    """
    Configuration for the Open Telemetry logs backend. This backend
    encodes events as either key=value pairs (similarly to the logger backend)
    or JSON (similarly to the file backend), and sends these strings as logs over
    OTLP to an OTLP logs endpoint.
    """

    backend_type: BackendType = BackendType.OTLP_LOGS
    # The name of the logger to use.
    name: str = "otlp_logs"
    # The log level to use for the logger.
    log_level: int = logging.INFO
    # If rank_aware is true, then the rank number will be added to the logger name.
    # For example, if the logger name is "training_telemetry" and the rank is 0,
    # then the logger name will be "training_telemetry_rank0".
    rank_aware: bool = True
    # The exporter to use, OTLP can be send over grpc or http, and console will print to the console.
    exporter: str = "grpc"  # or "http", "console"
    # The endpoint when using either grpc or http as an OTLP exporter, the grpc port is normally 4317 and the http port is 4318.
    endpoint: str = "http://localhost:4317"  # or "http://localhost:4318"
    # The format of the logs to send over OTLP.
    format: OTLPLogsFormat = OTLPLogsFormat.KEY_VALUE


@dataclass
class NVTXBackendConfig(BackendConfig):
    """Configuration for the NVTX backend, which logs JSON events to a file."""

    backend_type: BackendType = BackendType.NVTX


def default_backends() -> list[BackendConfig]:
    """Return the default backends, used if the user doesn't provide any backends."""
    return [
        LoggerBackendConfig(),
        FileBackendConfig(),
        NVTXBackendConfig(),
    ]


@dataclass
class TelemetryConfig:
    """Configuration for the telemetry system."""

    # The backends configuration is used to determine which backends are enabled, and their configuration.
    backends: List[BackendConfig] = field(default_factory=default_backends)

    # The application configuration contains information that might be used by backends to set application properties.
    application: ApplicationConfig = field(default_factory=ApplicationConfig)

    # The log level and format used by the library to log any initialization or error messages.
    # Set to CRITICAL to disable logging completely as the highest level used is ERROR.
    log_level: int = logging.INFO
    log_format: Optional[str] = None
