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
import os
from io import TextIOWrapper
from typing import Any

from training_telemetry.config import BackendType
from training_telemetry.internal.backends.event_based_backend import EventBasedBackend, RecordWriter
from training_telemetry.verbosity import Verbosity


class FileRecordWriter(RecordWriter):
    """A record writer that writes to a file."""

    def __init__(self, filepath: str):
        self._filepath: str = filepath
        self._file: TextIOWrapper | None = self._open_file()

    def _open_file(self) -> TextIOWrapper:
        parent_dir = os.path.dirname(self._filepath)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
        return open(self._filepath, "w")

    def serialize(self, record: dict[str, Any]) -> str:
        return json.dumps(record, separators=(",", ":"))

    def write(self, record: str) -> None:
        if not self._file:
            raise RuntimeError("File backend not initialized or already closed")
        self._file.write(record + "\n")
        self._file.flush()

    def close(self) -> None:
        if self._file is not None:
            self._file.close()
            self._file = None


class FileBackend(EventBasedBackend):
    """Backend implementation that writes events and metrics to a JSONfile."""

    def __init__(self, filepath: str):
        self._record_writer = FileRecordWriter(filepath)
        super().__init__(self._record_writer)

    def type(self) -> BackendType:
        return BackendType.FILE

    def verbosity(self) -> Verbosity:
        return Verbosity.INFO
