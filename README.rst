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

To bootstrap ArniePye, obtain and run ``boostrap.py`` from a server::

    wget http://<SERVER>/packages/bootstrap/bootstrap.py
    python bootstrap.py

If Python is not installed, run ``bootstrap.bat`` instead::

    wget http://<SERVER>/packages/bootstrap/bootstrap.bat
    bootstrap.bat

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


Uploading Packages
==================

Create a .pypirc in your home directory::

   [distutils]
   index-servers =
    arnie
    local

   [arnie]
   repository: http://arnie
   username: dw
   password: dw

   [local]
   repository: http://127.0.0.1:8080
   username: dw
   password: dw

After incrementing the version number of your project, run::

   python setup.py sdist upload -r arnie

