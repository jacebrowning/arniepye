#!/usr/bin/env python

"""
Wrapper for pypiserver to serve packages.
"""

import os
import sys
import shutil
import subprocess
import logging

from arniepye import settings


def run(port=8080, path=settings.PACKAGES_DIR, launch=False, forever=True, temp=False):
    """Create a packages directory and run the server forever.
    """

    if not os.path.isdir(path):
        logging.info("creating packages directory at '{}'...".format(path))
        os.mkdir(path)

    logging.debug("creating the pypi process...")
    process = subprocess.Popen([sys.executable, '-m', 'pypiserver',
                                '-p', str(port), path])
    try:
        logging.debug("pypi server started")
        while process.poll() is None and forever:
            pass
    except KeyboardInterrupt:
        logging.warning("pypi manually terminated")
        return False
    finally:
        process.terminate()
        if temp or not os.listdir(path):
            logging.info("removing packages directory...")
            shutil.rmtree(path)
        logging.debug("pypi server stopped")

    return True


if __name__ == '__main__':  # pragma: no cover
    run(forever=False, temp=True)
