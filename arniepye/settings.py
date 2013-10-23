#!/usr/bin/env python

"""
Settings for ArniePye.
"""

import os
import logging

# Server settings
SERVERS = [
'DW-89',  # TODO: update with valid server names
]
PACKAGES_DIR = os.path.expanduser("~/packages")


# Logging settings
DEFAULT_LOGGING_FORMAT = "%(message)s"
VERBOSE_LOGGING_FORMAT = "%(levelname)s: %(message)s"
VERBOSE2_LOGGING_FORMAT = "%(asctime)s: %(levelname)s: %(message)s"
VERBOSE3_LOGGING_FORMAT = "%(asctime)s: %(levelname)s: %(module)s:%(lineno)d: %(message)s"
DEFAULT_LOGGING_LEVEL = logging.INFO
VERBOSE_LOGGING_LEVEL = logging.DEBUG
