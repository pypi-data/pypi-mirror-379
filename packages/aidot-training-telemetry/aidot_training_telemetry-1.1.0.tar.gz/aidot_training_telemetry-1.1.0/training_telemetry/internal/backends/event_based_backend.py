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

import os
from abc import ABC, abstractmethod
from threading import Lock
from typing import Any, Optional

from training_telemetry.events import Event, ExceptionEvent
from training_telemetry.internal.backend import Backend
from training_telemetry.internal.backends.record_type import RecordType
from training_telemetry.spans import Span
from training_telemetry.utils import get_default_logger

_logger = get_default_logger()


class RecordWriter(ABC):
    """A record writer is used by the EventBasedBackend to serialize andwrite records to a backend."""

    @abstractmethod
    def serialize(self, record: dict[str, Any]) -> str:
        """Serialize a record, encoded as a dict, to a raw string for writing in write."""

    @abstractmethod
    def write(self, record: str) -> None:
        """Write a serialized record to the backend, e.g. a python logger, or a file."""

    @abstractmethod
    def close(self) -> None:
        """Close the writer, e.g. a file."""


class EventBasedBackend(Backend):
    """
    An abstract backend base class that records events in order to represent spans.
    Callers must supply a RecordWriter, and implement the backent type and verbosity methods.
    """

    def __init__(self, record_writer: RecordWriter):
        self._record_count: int = 0
        self.pid = os.getpid()
        self._lock: Lock = Lock()
        self._last_start_span: Optional[Span] = None
        self._record_writer = record_writer
        self._closed = False

    def _write_record(self, record: dict[str, Any]) -> None:
        """Write a serialized record to the backend, e.g. a python logger, or a file."""
        if self._closed:
            raise RuntimeError("Backend is closed")

        try:
            with self._lock:
                self._record_count += 1
                record["count"] = self._record_count
                record["pid"] = self.pid
                record_str = self._record_writer.serialize(record)
                self._record_writer.write(record_str)
        except Exception as e:
            _logger.error(f"Error writing record to backend: {e}")
            raise

    def record_span(self, span: Span, record_type: RecordType) -> None:
        """Record a span."""
        record: dict[str, Any] = {
            "type": record_type.value,
            "id": str(span.id),
            "name": span.name.value,
        }
        if record_type == RecordType.START:
            record["event"] = span.start_event.to_json()
        elif record_type == RecordType.COMPLETE:
            assert span.stop_event
            record["elapsed"] = span.duration.elapsed
            record["start_event"] = span.start_event.to_json()
            record["stop_event"] = span.stop_event.to_json()
        elif record_type == RecordType.STOP:
            assert span.stop_event
            record["elapsed"] = span.duration.elapsed
            record["event"] = span.stop_event.to_json()
        else:
            raise ValueError(f"Invalid type: {record_type}")

        self._write_record(record)

    def record_start(self, span: Span) -> None:
        if self._last_start_span is not None:
            self.record_span(self._last_start_span, RecordType.START)
        self._last_start_span = span

    def record_stop(self, span: Span) -> None:
        if span.stop_event is None:
            raise ValueError(f"Span {span.id} has no stop event")
        if self._last_start_span:
            if self._last_start_span.id == span.id:
                # record a complete span rather than two
                self.record_span(span, RecordType.COMPLETE)
                self._last_start_span = None
                return
            else:
                # record the previous span before recording the stop event
                self.record_span(self._last_start_span, RecordType.START)
                self._last_start_span = None

        # record the stop event
        self.record_span(span, RecordType.STOP)

    def record_event(self, event: Event, span: Span) -> None:
        if self._last_start_span:
            self.record_span(self._last_start_span, RecordType.START)
            self._last_start_span = None
        record = {
            "type": RecordType.EVENT.value,
            "id": str(span.id),
            "name": span.name.value,
            "event": event.to_json(),
        }
        self._write_record(record)

    def record_error(self, event: ExceptionEvent, span: Span) -> None:
        if self._last_start_span:
            self.record_span(self._last_start_span, RecordType.START)
            self._last_start_span = None

        record = {
            "type": RecordType.ERROR.value,
            "id": str(span.id),
            "name": span.name.value,
            "event": event.to_json(),
        }
        self._write_record(record)

    def close(self) -> None:
        if self._closed:
            return

        if self._last_start_span:
            _logger.warning(f"Span {self._last_start_span.id} was not closed")

        with self._lock:
            self._last_start_span = None
            self._record_writer.close()
            self._closed = True
