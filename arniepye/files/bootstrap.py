#!/usr/bin/env python

"""
Bootstaps package management for an existing Python 2 or 3 installation.
"""

import os
import sys
import tempfile
import subprocess

PY3 = (sys.version_info[0] == 3)

PYTHON = sys.executable
SCRIPTS = os.path.join(os.path.dirname(sys.executable), 'Scripts')
if SCRIPTS.count('Scripts') > 1:  # inside a virtualenv
    SCRIPTS = os.path.dirname(SCRIPTS)

SETUPTOOLS_URL = r"https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py"
EASY_INSTALL = os.path.join(SCRIPTS, 'easy_install')

PIP_URL = r"https://raw.github.com/pypa/pip/master/contrib/get-pip.py"
PIP = os.path.join(SCRIPTS, 'pip')

GTK_URL = r"http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.24/pygtk-all-in-one-2.24.0.win32-py2.7.msi"


def main():
    """Install pip, virtualenv, and other essential packages."""

    # Create a temporary directory
    temp = tempfile.gettempdir()
    os.chdir(temp)

    # Install setuptools from source
    script = 'ez_setup.py'
    download(SETUPTOOLS_URL, script)
    subprocess.call([PYTHON, script])
    os.remove(script)

    # Install pip from source
    pip = 'install_pip.py'
    download(PIP_URL, pip)
    subprocess.call([PYTHON, pip])
    os.remove(pip)

    # Install virtualenv and other essential packages
    install('virtualenv')

    # Install other essential packages
    install('pep8')  # TODO: add pylint when Windows Python 3 is supported

    # Install the GTK+ buidle
    gtk = 'install_gtk.exe'
    download(GTK_URL, gtk)
    subprocess.call([gtk])
    os.remove(gtk)

    # Delete the temporary directory



def download(url, path=None):
    """Download a file from the URL to a local path."""

    if path is None:
        path = url.rsplit('/')[-1]

    if PY3:
        import urllib.request
        response = urllib.request.urlopen(url)
        data = response.read()
    else:
        import urllib2
        response = urllib2.urlopen(url)
        data = response.read()

    with open(path, 'wb') as outfile:
        outfile.write(data)


def install(*names):
    """Install a Python packages using pip."""
    subprocess.call([PIP, 'install', '--upgrade'] + list(names))


if __name__ == '__main__':  # pragma: no cover
    main()
