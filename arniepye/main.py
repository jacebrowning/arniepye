#!/usr/bin/env python

"""
Main entry points for ArniePye.
"""

from arniepye import installer
from arniepye import server


def install(*args, **kwargs):
    """Wraps main installer entry point."""
    return installer.install(*args, **kwargs)


def uninstall(*args, **kwargs):
    """Wraps main uninstaller entry point."""
    return installer.uninstall(*args, **kwargs)


def serve(*args, **kwargs):
    """Wraps main server entry point."""
    return server.run(*args, **kwargs)
