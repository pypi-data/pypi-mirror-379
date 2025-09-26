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
import json
import logging
from typing import Any

from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor, LogExporter
from opentelemetry.sdk.resources import Resource

from training_telemetry.config import ApplicationConfig, BackendType, OTLPLogsFormat
from training_telemetry.internal.backends.event_based_backend import EventBasedBackend, RecordWriter
from training_telemetry.internal.backends.logger_backend import PythonLoggerRecordWriter
from training_telemetry.verbosity import Verbosity


def make_otlp_logger(
    name: str, level: int, exporter: LogExporter, application: ApplicationConfig, version: str
) -> tuple[LoggerProvider, logging.Logger]:
    resource: Resource = Resource.create(
        {
            "job_name": application.job_name,
            "job_id": application.job_id,
            "job_restart_count": application.job_restart_count,
            "environment": application.environment,
            "rank": application.rank,
            "world_size": application.world_size,
            "training_telemetry_version": version,
        }
    )
    provider = LoggerProvider(resource=resource)
    processor = BatchLogRecordProcessor(exporter)
    provider.add_log_record_processor(processor)

    # Create a Python logger that will send logs through OpenTelemetry
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a LoggingHandler that will send logs to OpenTelemetry
    handler = LoggingHandler(level=level, logger_provider=provider)
    logger.addHandler(handler)

    # Prevent propagation to avoid duplicate logs
    logger.propagate = False

    return provider, logger


class OTLPythonLogsRecordWriter(PythonLoggerRecordWriter):
    """Backend implementation that sends OpenTelemetry logs over OTLP."""

    def __init__(
        self,
        logger: logging.Logger,
        provider: LoggerProvider,
    ) -> None:
        self._provider = provider
        self._logger = logger
        super().__init__(logger)

    def close(self) -> None:
        super().close()
        self._provider.shutdown()


class OTLJsonLogsRecordWriter(RecordWriter):
    """Backend implementation that sends OpenTelemetry logs over OTLP."""

    def __init__(
        self,
        logger: logging.Logger,
        provider: LoggerProvider,
    ) -> None:
        self._provider = provider
        self._logger = logger

    def serialize(self, record: dict[str, Any]) -> str:
        return json.dumps(record)

    def write(self, record: str) -> None:
        self._logger.info(record)

    def close(self) -> None:
        self._provider.shutdown()


class OTLPLogsBackend(EventBasedBackend):
    """Backend implementation that sends OpenTelemetry logs over OTLP."""

    def __init__(
        self,
        name: str,
        level: int,
        exporter: LogExporter,
        verbosity: Verbosity,
        application: ApplicationConfig,
        version: str,
        format: OTLPLogsFormat,
    ) -> None:
        self._verbosity = verbosity
        self._provider, self._logger = make_otlp_logger(name, level, exporter, application, version)
        self._record_writer = (
            OTLPythonLogsRecordWriter(self._logger, self._provider)
            if format == OTLPLogsFormat.KEY_VALUE
            else OTLJsonLogsRecordWriter(self._logger, self._provider)
        )
        super().__init__(self._record_writer)

    def verbosity(self) -> Verbosity:
        return self._verbosity

    def type(self) -> BackendType:
        return BackendType.OTLP_LOGS

    def close(self) -> None:
        super().close()
