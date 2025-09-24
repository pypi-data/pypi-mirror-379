"""Convenience exports for syntaxmod's timing and looping helpers."""

from importlib import metadata as _metadata

from .general import (
    Stopwatch,
    Timer,
    loop,
    printstr,
    wait,
    wait_until,
)

__all__ = (
    "loop",
    "wait",
    "printstr",
    "wait_until",
    "Stopwatch",
    "Timer",
)

try:
    __version__ = _metadata.version("syntaxmod")
except _metadata.PackageNotFoundError:  # pragma: no cover - fallback for editable installs
    __version__ = "0.1.0"

__author__ = "Advik Mathur"
__email__ = "pranit.advik@gmail.com"

# avoid leaking helper into the public namespace
del _metadata
