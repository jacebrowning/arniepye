ArniePye
========

[![Build Status](http://img.shields.io/travis/dornerworks/arniepye/master.svg)](https://travis-ci.org/dornerworks/arniepye)
[![Coverage Status](http://img.shields.io/coveralls/dornerworks/arniepye/master.svg)](https://coveralls.io/r/dornerworks/arniepye)
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/dornerworks/arniepye.svg)](https://scrutinizer-ci.com/g/dornerworks/arniepye/?branch=master)

ArniePye is a wrapper for `pypiserver` and `pip` to provide an installer
and server for local and public Python packages. It also provides
boostrapping scripts to:

-   add itself to an existing Python installaion
-   install Python on a Windows computer from nothing



Getting Started
===============

Requirements
------------

* Windows

    or

* an existing Python 2 or 3 installation


Installation
------------

To bootstrap ArniePye, obtain and run `boostrap.py` from the server:

1. download: [http://\<SERVER\>/packages/bootstrap/bootstrap.py](http://arnie/packages/bootstrap/bootstrap.py)
2. `$ python bootstrap.py`

If Python is not installed, obtain and run `bootstrap.bat` instead:

1. download: [http://\<SERVER\>/packages/bootstrap/bootstrap.bat](http://arnie/packages/bootstrap/bootstrap.bat)
2. right click on `bootstrap.bat`  > **Run as administrator** 

ArniePye can be updated with itself after bootstrapping:

    $ arnie install ArniePye

Or directly from the source code:

    $ git clone https://github.com/dornerworks/arniepye.git
    $ cd arniepye
    $ python setup.py install



Usage
=====

Installing Packages
-------------------

After installation, ArniePye is available on the command-line as
`arnie`:

    $ arnie --version
    $ arnie --help

To use ArniePye with your non-default Python installation, use:

    $ arnie2  # Python 2
    $ arnie3  # Python 3

To install/uninstall a package:

    $ arnie install testpackage


Uninstalling Packages
---------------------

To uninstall a package:

    $ arnie uninstall testpackage


Uploading Packages
------------------

Create a .pypirc in your home directory:

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

After incrementing the version number of your project, run:

    $ python setup.py sdist upload -r arnie


Serving Packages
----------------

To start a temporary local server (<http://127.0.0.1:8080>), run:

    $ arnie serve --temp

The main server (<http://arnie>) is run from an Ubuntu virtual machine:

    $ sudo arnie serve --port 80



For Contributors
================

Requirements
------------

* GNU Make:
    * Windows: http://cygwin.com/install.html
    * Mac: https://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make (likely already installed)
* virtualenv: https://pypi.python.org/pypi/virtualenv#installation
* Pandoc: http://johnmacfarlane.net/pandoc/installing.html
* Graphviz: http://www.graphviz.org/Download.php


Installation
------------

Create a virtualenv:

    $ make env

Run the tests:

    $ make test
    $ make tests  # includes integration tests

Build the documentation:

    $ make doc

Run static analysis:

    $ make pep8
    $ make pep257
    $ make pylint
    $ make check  # includes all checks

Prepare a release:

    $ make dist  # dry run
    $ make upload
