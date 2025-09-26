"""
Core implementation of debugn - Node.js-style debug logging for Python.
Implements the same API and behavior as npm's debug module.
"""

import os
import re
import sys
import time
from datetime import datetime, timezone
from typing import Any, Dict, Protocol, Set

# ANSI colors matching npm debug's color selection
COLORS = [
    6,   # cyan
    2,   # green
    3,   # yellow
    1,   # red
    5,   # magenta
    4,   # blue
    # bright variants
    96,  # bright cyan
    92,  # bright green
    93,  # bright yellow
    91,  # bright red
    95,  # bright magenta
    94,  # bright blue
]

# Bold variants for light backgrounds (matching npm debug)
COLORS_BOLD = [
    106,  # bright cyan bg
    102,  # bright green bg
    103,  # bright yellow bg
    101,  # bright red bg
    105,  # bright magenta bg
    104,  # bright blue bg
]


class Debugger(Protocol):
    """Type definition for debug function with all its attributes."""

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        """Log a debug message."""
        ...

    @property
    def namespace(self) -> str:
        """The namespace this debugger logs to."""
        ...

    @property
    def enabled(self) -> bool:
        """Whether this debugger is currently enabled."""
        ...

    @property
    def color(self) -> int:
        """ANSI color code for this debugger."""
        ...

    @property
    def use_colors(self) -> bool:
        """Whether colors are enabled."""
        ...

    def extend(self, suffix: str) -> 'Debugger':
        """Create a new debugger with extended namespace."""
        ...


class Debug:
    """
    Singleton to manage debug configuration.
    Matches behavior of npm's debug module.
    """

    def __init__(self) -> None:
        self.enabled: Set[str] = set()
        self.disabled: Set[str] = set()
        self.last_times: Dict[str, float] = {}
        self.use_colors = self._detect_color_support()
        self.hide_date = os.environ.get('DEBUG_HIDE_DATE', '').lower() in ('true', '1')
        self.show_diff = (
            os.environ.get('DEBUG_SHOW_HIDDEN', '').lower() not in ('false', '0')
        )
        self._parse_env()

    def _detect_color_support(self) -> bool:
        """Detect if colors should be used (matching npm debug logic)."""
        # Check DEBUG_COLORS env var first
        debug_colors = os.environ.get('DEBUG_COLORS')
        if debug_colors is not None:
            return debug_colors.lower() not in ('false', '0', 'no')

        # Check if stderr is a TTY
        if not hasattr(sys.stderr, 'isatty'):
            return False

        if not sys.stderr.isatty():
            return False

        # Check TERM environment variable
        term = os.environ.get('TERM', '').lower()
        if term == 'dumb':
            return False

        # Check for common CI environments that support color
        if any(os.environ.get(var) for var in ['CI', 'GITHUB_ACTIONS', 'GITLAB_CI']):
            return True

        # Windows color support
        if sys.platform == 'win32':
            # Windows 10+ supports ANSI colors
            try:
                import platform
                version = platform.version()
                major = int(version.split('.')[0]) if version else 0
                return major >= 10
            except Exception:
                return False

        return True

    def _parse_env(self) -> None:
        """Parse DEBUG environment variable (npm debug compatible)."""
        debug_env = os.environ.get('DEBUG', '')
        if not debug_env:
            return

        # Support both comma and space as separators (like npm debug)
        patterns = re.split(r'[,\s]+', debug_env)

        for pattern in patterns:
            pattern = pattern.strip()
            if not pattern:
                continue

            if pattern.startswith('-'):
                self.disabled.add(pattern[1:])
            else:
                self.enabled.add(pattern)

    def is_enabled(self, namespace: str) -> bool:
        """Check if namespace is enabled (npm debug compatible)."""
        # Check disabled patterns first (they have priority)
        for pattern in self.disabled:
            if self._matches(pattern, namespace):
                return False

        # Check enabled patterns
        for pattern in self.enabled:
            if self._matches(pattern, namespace):
                return True

        return False

    def _matches(self, pattern: str, namespace: str) -> bool:
        """
        Check if namespace matches pattern.
        Supports wildcards exactly like npm debug.
        """
        if pattern == '*':
            return True

        # Convert pattern to regex
        # Escape special regex chars except *
        pattern = re.escape(pattern).replace(r'\*', '.*')

        # In npm debug, patterns can match partial namespaces
        # e.g., 'app' matches 'app', 'app:server', 'apple', etc.
        return bool(re.match(f'^{pattern}', namespace))

    def get_color(self, namespace: str) -> int:
        """Get consistent color for namespace (matches npm debug)."""
        # Use hash to get consistent color per namespace
        hash_val = sum(ord(c) for c in namespace)
        colors = COLORS if self.use_colors else []
        return colors[hash_val % len(colors)] if colors else 0


# Global debug instance
_debug = Debug()
_debug._last_env = os.environ.get('DEBUG', '')  # type: ignore[attr-defined]


def select_color(namespace: str) -> int:
    """Select color for namespace (Python naming convention)."""
    return _debug.get_color(namespace)


def debug(namespace: str) -> Debugger:
    """
    Create a debug function for the given namespace.
    API matches npm's debug module.

    Usage:
        log = debug('app:server')
        log('Server starting on port %s', 3000)

        # Extend to create sub-namespaces
        log_auth = log.extend('auth')  # Creates 'app:server:auth'
        log_auth('User authenticated')

    Args:
        namespace: The namespace for this debugger (e.g., 'app:server')

    Returns:
        A Debugger function with extend() method and namespace/enabled/color properties
    """

    def log(*args: Any, **kwargs: Any) -> None:
        """Log function matching npm debug behavior."""
        # Re-read environment to handle dynamic changes (like in tests)
        global _debug
        current_debug_env = os.environ.get('DEBUG', '')
        if current_debug_env != getattr(_debug, '_last_env', None):
            _debug = Debug()
            _debug._last_env = current_debug_env  # type: ignore[attr-defined]

        if not _debug.is_enabled(namespace):
            return

        # Calculate time delta (matching npm debug's +Xms format)
        now = time.time()
        last_time = _debug.last_times.get(namespace, now)
        _debug.last_times[namespace] = now
        delta = now - last_time

        # Format time diff like npm debug
        if delta < 1:
            diff = f'{int(delta * 1000)}ms'
        elif delta < 60:
            diff = f'{delta:.1f}s'
        elif delta < 3600:
            diff = f'{delta/60:.1f}m'
        else:
            diff = f'{delta/3600:.1f}h'

        # Format message (support both % formatting and simple args)
        if args:
            msg = args[0]
            if len(args) > 1:
                # Try % formatting first (like npm debug)
                try:
                    msg = msg % args[1:]
                except (TypeError, ValueError):
                    # Fall back to space-separated (also npm debug behavior)
                    msg = ' '.join(str(arg) for arg in args)
            else:
                msg = str(msg)
        else:
            msg = ''

        # Build output matching npm debug format
        color = _debug.get_color(namespace)
        use_colors = _debug.use_colors

        if use_colors and sys.stderr.isatty():
            # Colored output: namespace message +diff
            output = f"\033[{color}m{namespace}\033[0m {msg} \033[90m+{diff}\033[0m"
        else:
            # Non-TTY format: timestamp namespace message +diff
            if not _debug.hide_date:
                timestamp = datetime.now(timezone.utc).strftime(
                    '%a, %d %b %Y %H:%M:%S GMT'
                )
                output = f"{timestamp} {namespace} {msg} +{diff}"
            else:
                output = f"{namespace} {msg} +{diff}"

        # Output to stderr (like npm debug)
        print(output, file=sys.stderr, flush=True)

    # Add extend method to create sub-namespaces
    def extend(suffix: str) -> Debugger:
        """Create a new debug function with extended namespace."""
        # Use same delimiter detection as npm debug
        delimiter = ':' if ':' in namespace else ':'
        return debug(f"{namespace}{delimiter}{suffix}")

    # Set enabled property by checking current environment
    global _debug
    current_debug_env = os.environ.get('DEBUG', '')
    if current_debug_env != getattr(_debug, '_last_env', None):
        _debug = Debug()
        _debug._last_env = current_debug_env  # type: ignore[attr-defined]

    # Store properties on the function (Python naming conventions)
    log.namespace = namespace  # type: ignore[attr-defined]
    log.enabled = _debug.is_enabled(namespace)  # type: ignore[attr-defined]
    log.use_colors = _debug.use_colors  # type: ignore[attr-defined]
    log.color = _debug.get_color(namespace)  # type: ignore[attr-defined]
    log.extend = extend  # type: ignore[attr-defined]

    # Additional properties for compatibility
    log.inspect_opts = {}  # type: ignore[attr-defined]

    return log  # type: ignore[return-value]


# Functions for programmatic control (Python naming conventions)
def enable(namespaces: str) -> None:
    """Enable debug namespaces programmatically."""
    os.environ['DEBUG'] = namespaces
    global _debug
    _debug = Debug()


def disable() -> None:
    """Disable all debug output."""
    if 'DEBUG' in os.environ:
        del os.environ['DEBUG']
    global _debug
    _debug = Debug()


def enabled(namespace: str) -> bool:
    """Check if a namespace is enabled."""
    # Re-read environment to handle dynamic changes (like in tests)
    global _debug
    current_debug_env = os.environ.get('DEBUG', '')
    if current_debug_env != getattr(_debug, '_last_env', None):
        _debug = Debug()
        _debug._last_env = current_debug_env  # type: ignore[attr-defined]
    return _debug.is_enabled(namespace)


# For backwards compatibility
reload_debug = enable
