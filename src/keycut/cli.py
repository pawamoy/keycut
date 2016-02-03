#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mkeycut` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``keycut.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``keycut.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import sys
import load
import os
import time
import ui
from search import search
from watch import FileWatcher, WindowFocusWatcher, XdotoolWatcher
from utils import print_err


def main(argv=sys.argv):
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Does stuff.
    """

    if len(sys.argv) == 1:
        print('usage: main.py PROG [PATTERN] | --watch[=FILE]')
        sys.exit(1)

    if sys.argv[1].startswith('--watch'):
        watcher = watch = None
        args = sys.argv[1].split('=')
        if len(args) > 1:
            watch = args[1]
        else:
            if len(sys.argv) > 2:
                watch = sys.argv[2]
            else:
                watcher = WindowFocusWatcher()

        if watcher is None and watch is not None:
            watch = os.path.abspath(watch)
            watcher = FileWatcher(watch)
            print('Watching file %s' % watch)
            print('You can use the following functions in your shell')
            print()
            print('k() { echo "$@" > %s; eval '"$@"'; }' % watch)
            print('kgrep() { echo "$@" > %s; }' % watch)
            print()
            print('and use it like: k vim somefile; kgrep htop pid')
            print('------------------------------------------------')

        watcher.daemon = True
        watcher.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)

    else:
        app = sys.argv[1]
        document = load.from_yaml(app)

        if document:
            if len(sys.argv) == 3:
                pattern = sys.argv[2]
                document = search(document, pattern)
            ui.reload(document, clear=False)
        else:
            print_err('Document not found: %s' % app)
    return 0
