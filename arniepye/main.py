#!/usr/bin/env python

"""
Main entry points for ArniePye.
"""

from arniepye import server


def serve(*args, **kwargs):
    return server.run(*args, **kwargs)
