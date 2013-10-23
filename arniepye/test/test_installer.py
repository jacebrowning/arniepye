#!/usr/bin/env python

"""
Unit tests for the arniepye.installer module.
"""

import unittest
from mock import patch, Mock

import subprocess

from arniepye import installer


class MockPopen(Mock):

    def __init__(self, *args, **kwargs):
        super(MockPopen, self).__init__(*args, **kwargs)
        self.poll = Mock(return_value=0)
        self.terminate = Mock()
        self.returncode = 0


class TestInstall(unittest.TestCase):  # pylint: disable=R0904
    """Unit tests for the install function."""  # pylint: disable=C0103,W0212

    @patch('subprocess.Popen', MockPopen)
    def test_install(self):
        """Verify install can be called."""
        self.assertTrue(installer.install(['testpackage']))

    def test_install_cancel(self):
        """Verify installation can be cancelled."""
        def side_effect(*args):
            """First call: None, second call, raise KeyboardIntterupt."""
            def second_call(*args):
                raise KeyboardInterrupt()
            subprocess.Popen.poll.side_effect = second_call
            return None
        with patch('subprocess.Popen.poll', Mock(side_effect=side_effect)):
            self.assertFalse(installer.install(['testpackage']))

    @patch('subprocess.Popen', MockPopen)
    def test_uninstall(self):
        """Verify uninstall can be called."""
        self.assertTrue(installer.uninstall(['testpackage']))


if __name__ == '__main__':  # pragma: no cover, manual test
    unittest.main()
