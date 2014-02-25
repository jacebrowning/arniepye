#!/usr/bin/env python

"""Main entry points for ArniePye."""

from arniepye import installer
from arniepye import server


def install(*args, **kwargs):
    """Wrap main installer entry point."""
    return installer.install(*args, **kwargs)


def uninstall(*args, **kwargs):
    """Wrap main uninstaller entry point."""
    return installer.uninstall(*args, **kwargs)


def serve(*args, **kwargs):
    """Wrap main server entry point."""
    return server.run(*args, **kwargs)
