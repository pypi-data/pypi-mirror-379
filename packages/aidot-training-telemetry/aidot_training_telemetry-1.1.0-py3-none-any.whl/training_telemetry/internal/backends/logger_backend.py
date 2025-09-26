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
import re
from typing import Any

from training_telemetry.config import BackendType
from training_telemetry.internal.backends.event_based_backend import EventBasedBackend, RecordWriter
from training_telemetry.verbosity import Verbosity


class PythonLoggerRecordWriter(RecordWriter):
    """A record writer that writes to a python logger."""

    def __init__(self, logger: logging.Logger):
        self._logger = logger

    def serialize(self, record: dict[str, Any]) -> str:
        return self.format_log(record)

    def format_log(self, event_json: dict[str, Any]) -> str:
        """
        Format the dictionary into a log string. The output string will be in the format of "[key1=value1 | key2=value2 | ...]".
        Nested dictionaries are formatted recursively, and will be in the format of "key1.key2=value where key1 is the top
        level key and key2 is the nested key in the nested dictionary".

        Args:
            event_json (dict): The dictionary to format.

        Limitations:
            - dictionary keys cannot contain dots.
        Returns:
            str: The formatted log string.
        """
        items: list[str] = []
        for k, v in sorted(event_json.items(), reverse=True):
            if "." in k:
                raise ValueError(f"keys cannot contain dots: {k}")

            if isinstance(v, dict):
                items.append(self._format_log_nested(event_json=v, prefix=k))
            else:
                items.append(f"{k}={v}")

        return "[" + " | ".join(items) + "]"

    def _format_log_nested(self, event_json: dict[str, Any], prefix: str) -> str:
        """
        Helper function called by format_log to recursively format nested dictionaries.
        Args:
            event_json (dict): The nesteddictionary to format.
            prefix (str): The prefix is the key of the nested dictionary in the parent dictionary.
                          This function is in called recursively to format nested dictionaries,
                          with the prefix as the parent key.
        """
        items: list[str] = []
        for k, v in sorted(event_json.items(), reverse=True):
            if "." in k:
                raise ValueError(f"keys cannot contain dots: {k}")

            if isinstance(v, dict):
                items.append(self._format_log_nested(event_json=v, prefix=f"{prefix}.{k}"))
            else:
                items.append(f"{prefix}.{k}={v}")

        return " | ".join(items)

    @staticmethod
    def deserialize_log(text: str) -> dict[str, Any]:
        """
        Unformat a log string back into a dictionary by reversing the format_log function. Refer to that function
        for details on the format of the log string.
        """
        # First extract all the characters that are in the top level square brackets.
        pattern = r"\[(.*?)\]"
        matches = re.findall(pattern, text, re.DOTALL)
        if not matches:
            raise ValueError(f"Log string must be enclosed in square brackets: {text}")

        # Then extract the content of the last match (the main log body inserted by format_log)
        # and split on the pipe character but exclude the pipe characters that are inside double quotes.
        # Pattern explanation:
        # - r'\|(?=(?:[^"]*"[^"]*")*[^"]*$)'
        # - \|: Matches the pipe character
        # - (?=...) is a positive lookahead assertion
        # - (?:[^"]*"[^"]*")* matches pairs of quotes and their contents
        # - [^"]*$ ensures we're not inside quotes by checking that there are an even number of quotes after the pipe
        content = matches[-1]
        pattern = r'\|(?=(?:[^"]*"[^"]*")*[^"]*$)'
        items = re.split(pattern, content)
        items = [item.strip() for item in items if item.strip()]

        ret: dict[str, Any] = {}
        for item in items:
            # we know keys won't contain the = or . character, so splitting
            # on the first one is safe even if there a = character in the value
            k, v = item.split("=", 1)
            d = ret
            while "." in k:
                k1, k2 = k.split(".", 1)
                if k1 not in d:
                    d[k1] = {}
                k = k2
                d = d[k1]
            try:
                d[k] = json.loads(v)
            except ValueError:
                d[k] = v
        return ret

    def write(self, record: str) -> None:
        self._logger.info(record)

    def close(self) -> None:
        pass


class PythonLoggerBackend(EventBasedBackend):
    """
    Backend implementation that writes spans and events using a python logger.
    Note that this python logger may be backed by an Open Telemetry logger.
    Events are formatted as key=value pairs with hierarchical keys separated by dots.
    """

    def __init__(self, logger: logging.Logger, verbosity: Verbosity):
        self._logger = logger
        self._verbosity: Verbosity = verbosity
        self._record_writer = PythonLoggerRecordWriter(logger)
        super().__init__(self._record_writer)

    def type(self) -> BackendType:
        return BackendType.LOGGER

    def verbosity(self) -> Verbosity:
        return self._verbosity
