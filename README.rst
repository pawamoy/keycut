KeyCut
======

KeyCut (for keyboard shortcut) is a command line tool
that helps you remembering ALL the numerous keyboard shortcuts
of ALL your favorite programs, both graphical and command line ones.

You can use it to print and search keyboard shortcuts, through data
available in the `keycut-data`_ repository.

This repo contains the sources for the Python implementation of KeyCut.

It looks like this
------------------

The yellow parts are the one that matched a pattern using a regular expression.

.. image:: http://i.imgur.com/ZaqTOUb.png

Installation
------------

There is no package on PyPi yet, you will have to download
or clone the repo and install its dependencies.

Usage
-----

.. code:: bash

    python main.py bash

Show all bash shortcuts.

.. code:: bash

    python main.py bash proc

Show all bash shortcuts matching *proc* (in Category, Action, or Keys)

.. code:: bash

    python main.py --watch`

Will watch *$HOME/.keycut* file. Output a command in this file and KeyCut
will show the corresponding shortcuts (if available).

.. code:: bash

    python main.py --watch=thisFile

Same as before but change file path to absolute path of *thisFile*.

When you call it with --watch option, it will print on stdout two shell functions
that you can copy/paste in other shells:

.. code:: bash

    k() { echo "$@" > $HOME/.keycut; eval '"$@"'; }
    # Ask KeyCut to show corresponding shortcuts, then execute the command.

.. code:: bash

    kgrep() { echo "$@" > $HOME/.keycut; }
    # Just ask KeyCut to show corresponding shortcuts.

*$HOME/.keycut* will of course be replaced by the file you provided to --watch option.

Todo
----

- Interactive UI with search commands
- Follow the principles in `keycut-data`_ repo (inheritance, attributes)

.. _keycut-data : https://github.com/Pawamoy/keycut-data
