#!/usr/bin/env python

"""
Wrapper for pip to install packages.
"""

import sys
import subprocess
import logging


def install(names, reverse=False):
    """Install Python packages using PIP.

    @param names: project names to install
    @param reverse: uninstall rather than install
    @return: indication of success
    """
    logging.debug("creating the pip process...")
    process = _pip_uninstall(names) if reverse else _pip_install(names)
    try:
        logging.debug("pip running")
        while process.poll() is None:
            pass
    except KeyboardInterrupt:
        logging.warning("pip manually terminated")
        return False
    finally:
        process.terminate()

    return process.returncode == 0


def uninstall(names):
    """Uninstall Python packages using PIP.

    @param names: project names to uninstall
    @return: indication of success
    """
    return install(names, reverse=True)


def _pip_install(names):
    """Start and return a PIP install subprocess."""
    args = [sys.executable, '-m', 'pip', 'install', '--upgrade'] + names
    logging.debug("$ {0}".format(' '.join(args)))
    return subprocess.Popen(args)


def _pip_uninstall(names):
    """Start and return a PIP uninstall subprocess."""
    args = [sys.executable, '-m', 'pip', 'uninstall', '--yes'] + names
    logging.debug("$ {0}".format(' '.join(args)))
    return subprocess.Popen(args)


if __name__ == '__main__':  # pragma: no cover, manual test
    install(sys.argv[1:])
