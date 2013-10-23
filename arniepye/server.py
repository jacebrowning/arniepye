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


def main():
    run()


def run(port=8080, path=settings.PACKAGES_DIR, temp=False, launch=False):
    """Create a packages directory and run the server forever.
    """

    if not os.path.isdir(path):
        logging.info("creating packages directory at '{}'...".format(path))
        os.mkdir(path)

    logging.debug("creating the pypi process...")
    process = subprocess.Popen([sys.executable, '-m', 'pypiserver',
                                '-p', str(port), path])
    try:
        logging.debug("pypi running")
        while True:
            pass
    except KeyboardInterrupt:
        logging.warning("pypi manually terminated")
    finally:
        process.terminate()
        if temp or not os.listdir(path):
            logging.info("removing packages directory..")
            shutil.rmtree(path)


if __name__ == '__main__':
    main()
