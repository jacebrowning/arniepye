Introduction
============

ArniePye is a wrapper for ``pypiserver`` and ``pip`` to provide an
installer and server for local and public Python packages.


Getting Started
===============

Requirements
------------

* Python 2 or 3
* ``setuptools`` and/or ``pip``


Installation
------------

ArniePye can be installed with itself after bootstrapping::

    arnie install ArniePye

Or directly from the source code::

    python setup.py install


Command-line Interface
======================

After installation, ArniePye is available on the command-line as ``arnie``::

    $ arnie --version
    $ arnie --help

To use ArniePye with your non-default Python installation, use::

    $ arnie2  # Python 2
    $ arnie3  # Python 3


To install/uninstall a package::

    $ arnie install PackageName
    $ arnie uninstall PackageName

To start the PyPI server::

    $ arnie serve
