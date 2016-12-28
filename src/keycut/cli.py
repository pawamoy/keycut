# -*- coding: utf-8 -*-

"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later,
  but that will cause problems: the code will get executed twice:

  - When you run `python -mkeycut` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``keycut.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``keycut.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""

import argparse
import sys
import load
import ui
from search import search
from utils import print_err


parser = argparse.ArgumentParser(description='Command description.')
parser.add_argument('names', metavar='NAME', nargs=argparse.ZERO_OR_MORE,
                    help="A name of something.")


def main(argv=None):
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Does stuff.
    """

    if argv is None:
        print('usage: main.py PROG [PATTERN] | --watch[=FILE]')
        sys.exit(1)

    app = argv[0]
    document = load.from_yaml(app)

    if document:
        if len(argv) >= 2:
            pattern = ' '.join(argv[1:])
            document = search(document, pattern)
        ui.reload(document, clear=False)
    else:
        print_err('Document not found: %s' % app)

    return 0
