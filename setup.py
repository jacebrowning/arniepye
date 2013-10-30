#!/usr/bin/env python

"""
Setup script for ArniePye.
"""

import sys

import setuptools

from arniepye import __project__, CLI

# Append the Python main version number to the end of the CLI name
CLIN = CLI + str(sys.version_info[0])


setuptools.setup(
    name=__project__,
    version='0.0.2-rc.1',

    description="Wrapper for the PyPI server and PIP installer.",
    url='http://arnie/pypi/ArniePye',
    author='Jace Browning',
    author_email='Jace.Browning@dornerworks.com',

    packages=['arniepye', 'arniepye.test'],
    package_data={'arniepye': ['files/*'], 'arniepye.test': ['files/*']},

    entry_points={'console_scripts': [CLI + ' = arniepye.cli:main',
                                      CLIN + ' = arniepye.cli:main']},

    long_description=open('README.rst').read(),

    install_requires=["pypiserver==1.1.3", "pip==1.4.1",
                      "passlib", "requests", "mock"],
)
