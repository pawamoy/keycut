"""
Module that contains the command line application.

Why does this file exist, and why not put this in __main__?

You might be tempted to import things from __main__ later,
but that will cause problems: the code will get executed twice:

- When you run `python -m keycut` python will execute
  ``__main__.py`` as a script. That means there won't be any
  ``keycut.__main__`` in ``sys.modules``.
- When you import __main__ it will get executed again (as a module) because
  there's no ``keycut.__main__`` in ``sys.modules``.

Also see http://click.pocoo.org/5/setuptools/#setuptools-integration.
"""

import argparse

from . import load, ui
from .search import search
from .utils import print_err


def main(args=None):
    """The main function, which is executed when you type ``keycut`` or ``python -m keycut``."""
    parser = get_parser()
    args = parser.parse_args(args=args)

    document = load.from_yaml(args.app)

    if document:
        if args.pattern:
            document = search(document, args.pattern)
        ui.reload(document, clear=False)
    else:
        print_err("Document not found: %s" % args.app)

    return 0


def get_parser():
    parser = argparse.ArgumentParser(prog="keycut", description="Command description.")
    parser.add_argument("app", metavar="APP", help="The app to print shortcuts of.")
    parser.add_argument("pattern", metavar="PATTERN", nargs="?", help="A regex pattern to search for.")
    return parser
