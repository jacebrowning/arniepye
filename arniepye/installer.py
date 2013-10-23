#!/usr/bin/env python

"""
Wrapper for pip to install packages.
"""

import sys
import subprocess
import logging


def main():
    pass


def run(names):

    logging.debug("creating the pip process...")
    process = subprocess.Popen([sys.executable, '-m', 'pip', 'install',
                                '--upgrade'] + names)

    try:
        logging.debug("pip running")
        while True:
            pass
    except KeyboardInterrupt:
        logging.warning("server manually terminated")
    finally:
        process.terminate()


if __name__ == '__main__':
    main()
