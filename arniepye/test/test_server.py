#!/usr/bin/env python

"""Unit tests for the arniepye.server module."""

import unittest
from mock import patch, Mock

import os
import shutil
import tempfile

from arniepye import server


class TestRun(unittest.TestCase):  # pylint: disable=R0904

    """Unit tests for the run function."""  # pylint: disable=C0103,W0212

    def setUp(self):
        """Run setup for each test method."""
        self.temp = tempfile.mkdtemp()

    def tearDown(self):
        """Run teardown for each test method."""
        if os.path.exists(self.temp):
            shutil.rmtree(self.temp)

    def test_serve(self):
        """Verify the server can be started and stopped."""
        packages = os.path.join(self.temp, 'packages')
        self.assertTrue(server.run(path=packages, forever=False))

    @patch('subprocess.Popen.poll', Mock(return_value=1))
    def test_serve_exit(self):
        """Verify the server process can exit normally."""
        self.assertTrue(server.run(path=self.temp))

    @patch('subprocess.Popen.wait', Mock(side_effect=KeyboardInterrupt))
    def test_serve_interrupt(self):
        """Verify the server can be interrupted."""
        self.assertFalse(server.run(path=self.temp))


if __name__ == '__main__':  # pragma: no cover, manual test
    unittest.main()
