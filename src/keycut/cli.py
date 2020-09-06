# Why does this file exist, and why not put this in `__main__`?
#
# You might be tempted to import things from `__main__` later,
# but that will cause problems: the code will get executed twice:
#
# - When you run `python -m keycut` python will execute
#   `__main__.py` as a script. That means there won't be any
#   `keycut.__main__` in `sys.modules`.
# - When you import `__main__` it will get executed again (as a module) because
#   there's no `keycut.__main__` in `sys.modules`.

"""Module that contains the command line application."""

import argparse
from typing import List, Optional

from . import load, ui
from .search import search
from .utils import print_err


def get_parser() -> argparse.ArgumentParser:
    """
    Return the CLI argument parser.

    Returns:
        An argparse parser.
    """
    parser = argparse.ArgumentParser(prog="keycut", description="Command description.")
    parser.add_argument("app", metavar="APP", help="The app to print shortcuts of.")
    parser.add_argument("pattern", metavar="PATTERN", nargs="?", help="A regex pattern to search for.")
    return parser


def main(args: Optional[List[str]] = None) -> int:
    """
    Run the main program.

    This function is executed when you type `keycut` or `python -m keycut`.

    Arguments:
        args: Arguments passed from the command line.

    Returns:
        An exit code.
    """
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
