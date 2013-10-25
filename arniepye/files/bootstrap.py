#!/usr/bin/env python

"""
Bootstaps package management for an existing Python 2 or 3 installation.
"""

import os
import sys
import shutil
import tempfile
import subprocess
import logging

IS_PYTHON3 = (sys.version_info[0] == 3)
IS_WINDOWS = (os.name == 'nt')
IS_CYGWIN = (sys.platform == 'cygwin')  # which is also Windows

PYTHON = sys.executable
BIN = os.path.dirname(PYTHON)
if IS_CYGWIN:
    pass
elif IS_WINDOWS:
    if os.path.basename(BIN) != 'Scripts':
        BIN = os.path.join(BIN, 'Scripts')  # not inside a virtualenv
else:
    BIN = '/usr/local/bin'

SETUPTOOLS_URL = "https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py"
EASY_INSTALL = os.path.join(BIN, 'easy_install')

PYWIN32_URL = "http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/pywin32-218.win32-py2.7.exe"
if IS_PYTHON3:
    PYWIN32_URL = PYWIN32_URL.replace('2.7', '3.3')

PIP_URL = "https://raw.github.com/pypa/pip/master/contrib/get-pip.py"
PIP = os.path.join(BIN, 'pip')

SERVER_URL = 'http://{ADDRESS}/simple/'  # set dynamically on the server
ARNIE = os.path.join(BIN, 'arnie3' if IS_PYTHON3 else 'arnie2')

GTK_URL = "http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.24/pygtk-all-in-one-2.24.0.win32-py2.7.msi"
if IS_PYTHON3:
    GTK_URL = None


def main():
    """Process command-line arguments and run the program."""

    clean = ('--clean' in sys.argv)
    run(clean=clean)


def run(clean=False):
    """Install setuptools, pip, arniepye, and non-pip components.
    On Windows, add Python to the user PATH variable.

    @param clean: remove all Python paths from the Windows PATH first
    """
    # Create a temporary directory
    temp = tempfile.mkdtemp()
    logging.debug("temporary directory: {0}".format(temp))
    os.chdir(temp)

    # Install setuptools from source
    python(download(SETUPTOOLS_URL))

    # Install pip using setuptools
    easy_install('pip')

    # Install virtualenv using pip
    pip('virtualenv')

    # Install non-pip-installable packages
    msiexec(download(GTK_URL))
    # TODO: install PySVN, couldn't find 1.7.1 for Python 2.7?

    # Install  ArniePye using pip
    pip('ArniePye', url=SERVER_URL)

    # Install "essential" packages with ArniePye
    arnie('pep8')

    # Delete the temporary directory
    os.chdir(os.path.dirname(temp))
    shutil.rmtree(temp)


def download(url, path=None):
    """Download a file from the URL to a local path."""
    if url is None:
        return
    if path is None:
        path = os.path.join(os.getcwd(), url.rsplit('/')[-1])
    logging.debug("downloading {0} to {1}...".format(url, path))

    if IS_PYTHON3:
        import urllib.request
        response = urllib.request.urlopen(url)
        data = response.read()
    else:
        import urllib2
        response = urllib2.urlopen(url)
        data = response.read()

    with open(path, 'wb') as outfile:
        outfile.write(data)

    return path


def python(path):
    """Run a script with Python."""
    args = [PYTHON, path]
    _call(args)


def easy_install(*names):
    """Install Python packages using easy_install."""
    args = [EASY_INSTALL] + list(names)
    _call(args)


def pip(*names, **kwargs):
    """Install Python packages using pip and a local server."""
    url = kwargs.get('url', None)  # Python 2 compatibility
    args = [PIP, 'install', '--upgrade'] + list(names)
    if url:
        args.extend(['--index-url', url])
    else:
        logging.warning("no local PyPI specified")
    _call(args)


def arnie(*names):
    """Install Python packages using ArniePye."""
    args = [ARNIE, 'install'] + list(names)
    _call(args)


def msiexec(path):
    """Install an MSI package."""
    if path:
        args = ['msiexec', '/i', path]
        _call(args)


def _call(args):
    logging.debug("$ {0}".format(' '.join(args)))
    subprocess.call(args)


if __name__ == '__main__':  # pragma: no cover
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    main()
