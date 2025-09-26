"""
debugn - Node.js-style namespace debug logging for Python.

A minimal, environment-controlled logging library that's a direct port
of npm's debug module to Python.
"""

from .core import (
    Debugger,
    debug,
    disable,
    enable,
    enabled,
    reload_debug,
    select_color,
)

__version__ = "0.1.0"
__all__ = [
    "debug",
    "enable",
    "disable",
    "enabled",
    "select_color",
    "reload_debug",
    "Debugger",
]

# For npm debug compatibility
default = debug
