#!/usr/bin/env python

"""
Wrapper for pip to install packages.
"""

import os
import sys
import shutil
import subprocess
import logging

import requests

from arniepye import settings

FILES = os.path.join(os.path.dirname(__file__), 'files')

URL = None  # first available PyPI server set at runtime


def install(names, reverse=False):
    """Install Python packages using PIP.

    @param names: project names to install
    @param reverse: uninstall rather than install
    @return: indication of success
    """
    # Create the installer files
    _setup()

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
        if process.returncode is None:
            process.terminate()

    return process.returncode == 0


def _setup():
    """Set up the .pypirc file."""
    dst = os.path.expanduser(os.path.join('~', '.pypirc'))
    if not os.path.exists(dst):
        logging.info("creating '{0}'...".format(dst))
        src = os.path.join(FILES, 'pypirc')
        shutil.copy(src, dst)


def uninstall(names):
    """Uninstall Python packages using PIP.

    @param names: project names to uninstall
    @return: indication of success
    """
    return install(names, reverse=True)


def _pip_install(names):
    """Start and return a PIP install subprocess."""

    if URL is None:
        _set_url()

    args = [sys.executable, '-m', 'pip', 'install',
            '--index-url', URL, '--upgrade'] + names
    return _call(args)


def _set_url():
    """Set the default PyPI server based on HTTP response."""
    global URL  # pylint: disable=W0603
    for URL in settings.SERVER_URLS + settings.FALLBACK_URLS:
        try:
            logging.debug("testing {0}...".format(URL))
            request = requests.get(URL)
            if request.status_code == 200:  # pragma: no cover, integration test
                logging.info("found server: {0}".format(URL))
                break
        except requests.exceptions.RequestException:
            logging.warning("cannot find server: {0}".format(URL))
    if URL in settings.FALLBACK_URLS:  # pragma: no cover, unit test only
        logging.warning("no local PyPI servers found")


def _pip_uninstall(names):
    """Start and return a PIP uninstall subprocess."""
    args = [sys.executable, '-m', 'pip', 'uninstall', '--yes'] + names
    return _call(args)


def _call(args):
    # Add 'sudo' for a non-Windows, non-root user
    if os.name != 'nt' and os.geteuid() != 0:  # pragma: no cover, OS-specific
        args.insert(0, 'sudo')
    # Run the command
    logging.debug("$ {0}".format(' '.join(args)))
    return subprocess.Popen(args)


if __name__ == '__main__':  # pragma: no cover, manual test
    install(sys.argv[1:])
