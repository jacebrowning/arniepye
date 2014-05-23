#!/usr/bin/env python

"""Setup script for ArniePye."""

import sys

import setuptools

from arniepye import __project__, __version__, CLI

# Append the Python main version number to the end of the CLI name
CLIN = CLI + str(sys.version_info[0])

import os
if os.path.exists('README.rst'):
    README = open('README.rst').read()
else:
    README = ""  # a placeholder, readme is generated on release
CHANGES = open('CHANGES.md').read()


setuptools.setup(
    name=__project__,
    version=__version__,

    description="Wrapper for the PyPI server and PIP installer.",
    url='http://arnie/pypi/ArniePye',
    author='Jace Browning',
    author_email='Jace.Browning@dornerworks.com',

    packages=['arniepye', 'arniepye.test'],
    package_data={'arniepye': ['files/*'], 'arniepye.test': ['files/*']},

    entry_points={'console_scripts': [CLI + ' = arniepye.cli:main',
                                      CLIN + ' = arniepye.cli:main']},

    long_description=(README + '\n' + CHANGES),
    license='LGPL',

    install_requires=["pypiserver==1.1.3", "passlib", "requests", "mock"],
)
