"""Basic tests for debugn functionality."""

import os
import sys
from io import StringIO
from unittest import TestCase, mock

from debugn import debug, disable, enable, enabled


class TestDebugnBasics(TestCase):
    """Basic functionality tests."""

    def setUp(self):
        # Clear environment
        if 'DEBUG' in os.environ:
            del os.environ['DEBUG']

    def test_debug_creation(self):
        """Test creating a debug function."""
        log = debug('test')
        assert callable(log)
        assert log.namespace == 'test'

    def test_basic_logging_disabled(self):
        """Test that logging is disabled by default."""
        old_stderr = sys.stderr
        sys.stderr = StringIO()

        log = debug('test')
        log('This should not appear')

        output = sys.stderr.getvalue()
        assert output == ''

        sys.stderr = old_stderr

    def test_basic_logging_enabled(self):
        """Test basic logging when enabled."""
        old_stderr = sys.stderr
        sys.stderr = StringIO()

        with mock.patch.dict(os.environ, {'DEBUG': 'test'}):
            log = debug('test')
            log('Hello world')

            output = sys.stderr.getvalue()
            assert 'Hello world' in output
            assert 'test' in output

        sys.stderr = old_stderr

    def test_import_structure(self):
        """Test that all expected functions are importable."""
        from debugn import debug, disable, enable, enabled, select_color

        # All should be callable or classes
        assert callable(debug)
        assert callable(enable)
        assert callable(disable)
        assert callable(enabled)
        assert callable(select_color)

    def test_version_available(self):
        """Test that version is available."""
        import debugn
        assert hasattr(debugn, '__version__')
        assert debugn.__version__ == '0.1.0'

    def test_npm_compatibility_alias(self):
        """Test npm debug compatibility alias."""
        from debugn import default
        assert default is debug

    def test_extend_functionality(self):
        """Test extend method works."""
        base = debug('app')
        extended = base.extend('server')

        assert extended.namespace == 'app:server'
        assert callable(extended)

    def test_color_selection(self):
        """Test color selection is consistent."""
        from debugn import select_color

        color1 = select_color('test')
        color2 = select_color('test')

        assert color1 == color2  # Same namespace should have same color
        # Different namespaces might have different colors (not guaranteed but likely)

    def test_enabled_check(self):
        """Test enabled() function."""
        with mock.patch.dict(os.environ, {'DEBUG': 'enabled:*'}):
            assert enabled('enabled:test') is True
            assert enabled('disabled:test') is False

    def test_enable_disable_programmatic(self):
        """Test programmatic enable/disable."""
        # Initially disabled
        assert enabled('test') is False

        # Enable programmatically
        enable('test')
        assert enabled('test') is True

        # Disable programmatically
        disable()
        assert enabled('test') is False

    def test_properties_exist(self):
        """Test that debug function has expected properties."""
        log = debug('test')

        assert hasattr(log, 'namespace')
        assert hasattr(log, 'enabled')
        assert hasattr(log, 'color')
        assert hasattr(log, 'use_colors')
        assert hasattr(log, 'extend')
        assert hasattr(log, 'inspect_opts')

    def test_multiple_args(self):
        """Test logging with multiple arguments."""
        old_stderr = sys.stderr
        sys.stderr = StringIO()

        with mock.patch.dict(os.environ, {'DEBUG': 'test'}):
            log = debug('test')
            log('Number:', 42, 'Boolean:', True)

            output = sys.stderr.getvalue()
            assert 'Number: 42 Boolean: True' in output

        sys.stderr = old_stderr
