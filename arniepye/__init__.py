#!/usr/bin/env python

"""
Package for ArniePye.
"""

from pkg_resources import get_distribution, DistributionNotFound

__project__ = 'ArniePye'
__version__ = None  # required for initial installation

CLI = 'arnie'

try:
    __version__ = get_distribution(__project__).version  # pylint: disable=E1103
except DistributionNotFound:  # pragma: no cover, manual test
    VERSION = __project__ + '-' + '(local)'
else:
    VERSION = __project__ + '-' + __version__
