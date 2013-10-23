#!/usr/bin/env python

"""
Installs Python packages from a package server.
"""

import os
import sys
import argparse
import logging

from arniepye import CLI, VERSION
from arniepye import settings
from arniepye import main as _main


class _HelpFormatter(argparse.HelpFormatter):
    """Command-line help text formatter with wider help text."""
    def __init__(self, *args, **kwargs):
        super(_HelpFormatter, self).__init__(*args, max_help_position=32,
                                             **kwargs)


class _WarningFormatter(logging.Formatter, object):
    """Logging formatter that always displays a verbose logging
    format for logging level WARNING or higher."""

    def __init__(self, default_format, verbose_format, *args, **kwargs):
        super(_WarningFormatter, self).__init__(*args, **kwargs)
        self.default_format = default_format
        self.verbose_format = verbose_format

    def format(self, record):
        if record.levelno > logging.INFO:
            self._fmt = self.verbose_format  # Python 2
            self._style._fmt = self.verbose_format  # Python 3
        else:
            self._fmt = self.default_format  # Python 2
            self._style._fmt = self.default_format  # Python 3
        return super(_WarningFormatter, self).format(record)


def main(args=None):
    """Process command-line arguments and run the program.

    @param args: manually override arguments
    """
    # Debug parser
    debug = argparse.ArgumentParser(add_help=False)
    debug.add_argument('-V', '--version', action='version', version=VERSION)
    debug.add_argument('-v', '--verbose', action='count', default=0,
                        help="enable verbose logging")

    # Main parser
    parser = argparse.ArgumentParser(prog=CLI, description=__doc__,
                                     formatter_class=_HelpFormatter,
                                     parents=[debug])
    subs = parser.add_subparsers(help="", dest='command', metavar="<command>")

    # Installer subparser
    sub = subs.add_parser('install', formatter_class=_HelpFormatter,
                          parents=[debug], help="install/upgrade packages")
    sub.add_argument('name', nargs='+',
                     help="project names to install")

    # Uninstaller subparser
    sub = subs.add_parser('uninstall', formatter_class=_HelpFormatter,
                          parents=[debug], help="uninstall packages")
    sub.add_argument('name', nargs='+',
                     help="project names to install")

    # Server subparser
    sub = subs.add_parser('serve', formatter_class=_HelpFormatter,
                          parents=[debug], help="start a PyPI package server")
    sub.add_argument('--temp', action='store_true',
                     help="remove all packages and temporary files on exit")
    sub.add_argument('--test', action='store_true',
                     help="stop the server once it's started")

    # Parse arguments
    args = parser.parse_args(args=args)

    # Configure logging
    _configure_logging(args.verbose)

    # Run the program
    if args.command:
        function = globals()['_run_' + args.command]
    else:
        parser.print_help()
        parser.exit(1)
    try:
        success = function(args, os.getcwd(), parser.error)
    except KeyboardInterrupt:
        logging.debug("manually terminated")
        success = False
    if not success:
        sys.exit(1)


def _configure_logging(verbosity=0):
    """Configure logging using the provided verbosity level (0+)."""

    # Configure the logging level and format
    if verbosity >= 1:
        level = settings.VERBOSE_LOGGING_LEVEL
        if verbosity >= 3:
            default_format = verbose_format = settings.VERBOSE3_LOGGING_FORMAT
        elif verbosity >= 2:
            default_format = verbose_format = settings.VERBOSE2_LOGGING_FORMAT
        else:
            default_format = verbose_format = settings.VERBOSE_LOGGING_FORMAT
    else:
        level = settings.DEFAULT_LOGGING_LEVEL
        default_format = settings.DEFAULT_LOGGING_FORMAT
        verbose_format = settings.VERBOSE_LOGGING_FORMAT

    # Set a custom formatter
    logging.basicConfig(level=level)
    formatter = _WarningFormatter(default_format, verbose_format)
    logging.root.handlers[0].setFormatter(formatter)


def _run_install(args, cwd, error):
    """Process arguments and run the `install` subcommand.
    @param args: Namespace of CLI arguments
    @param cwd: current working directory
    @param error: function to call for CLI errors
    """
    return _main.install(args.name)


def _run_uninstall(args, cwd, error):
    """Process arguments and run the `uninstall` subcommand.
    @param args: Namespace of CLI arguments
    @param cwd: current working directory
    @param error: function to call for CLI errors
    """
    return _main.uninstall(args.name)


def _run_serve(args, cwd, error):
    """Process arguments and run the `serve` subcommand.
    @param args: Namespace of CLI arguments
    @param cwd: current working directory
    @param error: function to call for CLI errors
    """
    return _main.serve(forever=not args.test, temp=args.temp)


if __name__ == '__main__':  # pragma: no cover, manual test
    main()
