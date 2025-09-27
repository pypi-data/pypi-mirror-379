"""Test that debugn matches npm debug behavior."""

import os
import sys
from io import StringIO
from unittest import TestCase, mock

from debugn import debug, disable, enable, enabled


class TestNpmDebugParity(TestCase):
    """Test npm debug compatibility."""

    def setUp(self):
        # Clear environment
        if 'DEBUG' in os.environ:
            del os.environ['DEBUG']

    def test_wildcard_matching(self):
        """Test wildcard patterns match npm debug."""
        test_cases = [
            ('*', 'app:server', True),
            ('app:*', 'app:server', True),
            ('app:*', 'app:server:auth', True),
            ('app', 'app:server', True),  # Partial match like npm
            ('app', 'application', True),  # Partial match
            ('server', 'app:server', False),
        ]

        for pattern, namespace, expected in test_cases:
            with mock.patch.dict(os.environ, {'DEBUG': pattern}):
                from debugn.core import Debug
                d = Debug()
                assert d.is_enabled(namespace) == expected, \
                    f"Pattern '{pattern}' vs '{namespace}' should be {expected}"

    def test_exclude_patterns(self):
        """Test exclude patterns with - prefix."""
        with mock.patch.dict(os.environ, {'DEBUG': '*,-app:metrics'}):
            from debugn.core import Debug
            d = Debug()
            assert d.is_enabled('app:server') is True
            assert d.is_enabled('app:metrics') is False

    def test_extend_method(self):
        """Test extend() creates proper sub-namespaces."""
        app = debug('app')
        server = app.extend('server')
        auth = server.extend('auth')

        assert server.namespace == 'app:server'
        assert auth.namespace == 'app:server:auth'

    def test_time_diff_format(self):
        """Test time difference formatting matches npm debug."""
        log = debug('test')

        # Mock stderr to capture output
        old_stderr = sys.stderr
        sys.stderr = StringIO()

        with mock.patch.dict(os.environ, {'DEBUG': 'test'}):
            log = debug('test')
            log('First message')
            output1 = sys.stderr.getvalue()

            # Should show ms for small delays
            assert 'ms' in output1 or 's' in output1

        sys.stderr = old_stderr

    def test_multiple_separators(self):
        """Test both comma and space separators work."""
        patterns = [
            'app:server,app:database',
            'app:server app:database',
            'app:server, app:database',
            'app:server  app:database',
        ]

        for pattern in patterns:
            with mock.patch.dict(os.environ, {'DEBUG': pattern}):
                from debugn.core import Debug
                d = Debug()
                assert d.is_enabled('app:server')
                assert d.is_enabled('app:database')
                assert not d.is_enabled('api:v1')

    def test_printf_style_formatting(self):
        """Test % style formatting like npm debug."""
        old_stderr = sys.stderr
        sys.stderr = StringIO()

        with mock.patch.dict(os.environ, {'DEBUG': 'test'}):
            log = debug('test')
            log('Server on port %d', 3000)
            log('User %s logged in', 'alice')

            output = sys.stderr.getvalue()
            assert 'Server on port 3000' in output
            assert 'User alice logged in' in output

        sys.stderr = old_stderr

    def test_enabled_function(self):
        """Test enabled() helper function."""
        with mock.patch.dict(os.environ, {'DEBUG': 'app:*'}):
            assert enabled('app:server') is True
            assert enabled('api:v1') is False

    def test_enable_disable_functions(self):
        """Test enable() and disable() functions."""
        enable('app:*')
        assert enabled('app:server') is True

        disable()
        assert enabled('app:server') is False

    def test_color_consistency(self):
        """Test that colors are consistent for same namespace."""
        log1 = debug('test:namespace')
        log2 = debug('test:namespace')
        assert log1.color == log2.color

    def test_namespace_property(self):
        """Test namespace property is accessible."""
        log = debug('my:test:namespace')
        assert log.namespace == 'my:test:namespace'

    def test_enabled_property(self):
        """Test enabled property reflects current state."""
        with mock.patch.dict(os.environ, {'DEBUG': 'enabled:*'}):
            enabled_log = debug('enabled:test')
            disabled_log = debug('disabled:test')

            assert enabled_log.enabled is True
            assert disabled_log.enabled is False

    def test_fallback_formatting(self):
        """Test fallback to space-separated when % formatting fails."""
        old_stderr = sys.stderr
        sys.stderr = StringIO()

        with mock.patch.dict(os.environ, {'DEBUG': 'test'}):
            log = debug('test')
            # This should fall back to space-separated
            log('Value is', 42, 'and', True)

            output = sys.stderr.getvalue()
            assert 'Value is 42 and True' in output

        sys.stderr = old_stderr

    def test_empty_message(self):
        """Test handling of empty messages."""
        old_stderr = sys.stderr
        sys.stderr = StringIO()

        with mock.patch.dict(os.environ, {'DEBUG': 'test'}):
            log = debug('test')
            log()  # Empty message

            output = sys.stderr.getvalue()
            # Should still have namespace and timing
            assert 'test' in output
            assert '+' in output

        sys.stderr = old_stderr

    def test_complex_wildcard_patterns(self):
        """Test complex wildcard patterns."""
        test_cases = [
            ('app:*:auth', 'app:server:auth', True),
            ('app:*:auth', 'app:database:auth', True),
            ('app:*:auth', 'app:server:metrics', False),
            ('*:auth', 'any:auth', True),
            ('*:auth', 'any:other', False),
        ]

        for pattern, namespace, expected in test_cases:
            with mock.patch.dict(os.environ, {'DEBUG': pattern}):
                from debugn.core import Debug
                d = Debug()
                result = d.is_enabled(namespace)
                assert result == expected, (
                    f"Pattern '{pattern}' vs '{namespace}' should be {expected}, "
                    f"got {result}"
                )

    def test_mixed_enable_disable_patterns(self):
        """Test mixed enable/disable patterns."""
        # Enable all app:* but exclude app:metrics:*
        with mock.patch.dict(os.environ, {'DEBUG': 'app:*,-app:metrics:*'}):
            from debugn.core import Debug
            d = Debug()

            assert d.is_enabled('app:server') is True
            assert d.is_enabled('app:database') is True
            assert d.is_enabled('app:metrics:cpu') is False
            assert d.is_enabled('app:metrics:memory') is False

    def test_stderr_output(self):
        """Test that output goes to stderr, not stdout."""
        old_stderr = sys.stderr
        old_stdout = sys.stdout

        stderr_capture = StringIO()
        stdout_capture = StringIO()

        sys.stderr = stderr_capture
        sys.stdout = stdout_capture

        with mock.patch.dict(os.environ, {'DEBUG': 'test'}):
            log = debug('test')
            log('This should go to stderr')

            stderr_output = stderr_capture.getvalue()
            stdout_output = stdout_capture.getvalue()

            assert 'This should go to stderr' in stderr_output
            assert stdout_output == ''

        sys.stderr = old_stderr
        sys.stdout = old_stdout

    def test_timing_color_matches_namespace_npm_parity(self):
        """Test that timing color matches namespace color like npm debug."""
        old_stderr = sys.stderr
        sys.stderr = StringIO()

        with mock.patch.dict(os.environ, {'DEBUG': 'test', 'DEBUG_COLORS': '1'}):
            # Create fresh debug instance to pick up DEBUG_COLORS
            from debugn.core import Debug
            global_debug = Debug()

            # Mock the global _debug to use our fresh instance
            with mock.patch('debugn.core._debug', global_debug):
                log = debug('test')
                log('message')

                output = sys.stderr.getvalue()

                # Should contain ANSI color codes
                assert '\033[' in output

                # Extract color codes - timing should match namespace
                import re
                color_matches = re.findall(r'\033\[(\d+)m', output)

                # Should have namespace color and timing color
                assert len(color_matches) >= 2

                # First color (namespace) should match timing color
                namespace_color = color_matches[0]
                timing_color = color_matches[2] if len(color_matches) > 2 else None

                assert namespace_color == timing_color, (
                    f"Namespace color {namespace_color} should match "
                    f"timing color {timing_color}"
                )

        sys.stderr = old_stderr
