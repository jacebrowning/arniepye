#!/usr/bin/env python

"""
Tests for the arniepye package.
"""

import unittest

import os

from arniepye.cli import main


ENV = 'TEST_INTEGRATION'  # environment variable to enable integration tests
REASON = "'{0}' variable not set".format(ENV)


@unittest.skipUnless(os.getenv(ENV), REASON)  # pylint: disable=R0904
class TestCLI(unittest.TestCase):  # pylint: disable=R0904
    """Integration tests for the ArniePye CLI."""

    def test_main_help(self):
        """Verify the CLI help text can be requested."""
        self.assertRaises(SystemExit, main, ['--help'])

    def test_install_error(self):
        """Verify an error occurs when no package specified to install."""
        self.assertRaises(SystemExit, main, ['install'])

    def test_uninstall_error(self):
        """Verify an error occurs when no package specified to uninstall."""
        self.assertRaises(SystemExit, main, ['uninstall'])

    def test_install_uninstall(self):
        """Verify the install/uninstall CLI can be called."""
        self.assertIs(None, main(['install', 'testpackage']))
        self.assertIs(None, main(['uninstall', 'testpackage']))

    def test_serve(self):
        """Verify the server CLI can be called."""
        self.assertIs(None, main(['serve', '--test']))
