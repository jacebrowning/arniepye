#!/usr/bin/env python

"""
Setup script for ArniePye.
"""

import sys

import setuptools

from arniepye import __project__, CLI

CLIN = CLI + str(sys.version_info[0])


setuptools.setup(
    name=__project__,
    version='0.0.0',

    description="DornerWorks PyPI server and PIP installer.",
    url='http://arnie/pypi/ArniePye',
    author='Jace Browning',
    author_email='Jace.Browning@dornerworks.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': [CLI + ' = arniepye.cli:main',
                                      CLIN + ' = arnipye.cli:main']},

    long_description=open('README.rst').read(),
    license='TBD',  # TODO: determine DornerWorks license

    install_requires=["pypiserver==1.1.3", "pip==1.4.1",
                      "mock"],
)
