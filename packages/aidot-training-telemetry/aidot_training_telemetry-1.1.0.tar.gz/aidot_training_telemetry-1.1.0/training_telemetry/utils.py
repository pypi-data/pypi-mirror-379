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
import sys
import time
from datetime import datetime
from typing import Optional

_DEFAULT_LOGGER_NAME = "training_telemetry"


def get_default_logger() -> logging.Logger:
    """Get the default logger for the training telemetry library."""
    return logging.getLogger(_DEFAULT_LOGGER_NAME)


def set_default_logger(level: int = logging.INFO, fmt: Optional[str] = None) -> logging.Logger:
    """Set the default logger for the training telemetry library."""
    return get_logger(_DEFAULT_LOGGER_NAME, level=level, propagate=False, fmt=fmt)


def get_logger(
    name: str, level: int = logging.INFO, propagate: bool = False, fmt: Optional[str] = None
) -> logging.Logger:
    """Initialize a Python logger configured with timestamp and INFO level.

    Args:
        name: Name of the logger
        level: Logging level
        propagate: Whether to propagate the logger to the root logger
        fmt: Format string for the logger

    Returns:
        logging.Logger: Configured Python logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # this prevents the logger from propagating to the root logger
    logger.propagate = propagate

    # Check if this logger already has handlers configured
    if len(logger.handlers) > 0:
        return logger

    # Create file handler with timestamp in filename if the log_file is provided, otherwise create a stream handler for stdout
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)

    if fmt is None:
        fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_current_time() -> float:
    """
    Get the start time in seconds since epoch.
    """
    return time.perf_counter()


def get_elapsed_time(start_time: float) -> float:
    """
    Get the elapsed time in seconds since the start time.
    """
    return time.perf_counter() - start_time


def get_timestamp_in_local_timezone() -> datetime:
    """
    Get the current time in the local timezone.
    """
    return datetime.now().astimezone()
