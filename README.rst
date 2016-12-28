======
KeyCut
======

.. start-badges


|travis|
|codecov|
|landscape|
|version|
|wheel|
|pyup|
|gitter|


.. |travis| image:: https://travis-ci.org/Pawamoy/keycut.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/Pawamoy/keycut/

.. |codecov| image:: https://codecov.io/github/Pawamoy/keycut/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/Pawamoy/keycut/

.. |landscape| image:: https://landscape.io/github/Pawamoy/keycut/master/landscape.svg?style=flat
    :target: https://landscape.io/github/Pawamoy/keycut/
    :alt: Code Quality Status

.. |pyup| image:: https://pyup.io/repos/github/pawamoy/keycut/shield.svg
    :target: https://pyup.io/repos/github/pawamoy/keycut/
    :alt: Updates

.. |gitter| image:: https://badges.gitter.im/Pawamoy/keycut.svg
    :alt: Join the chat at https://gitter.im/Pawamoy/keycut
    :target: https://gitter.im/Pawamoy/keycut?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. |version| image:: https://img.shields.io/pypi/v/keycut.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/keycut/

.. |wheel| image:: https://img.shields.io/pypi/wheel/keycut.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/keycut/


.. end-badges

Helper tool to show and search shortcuts for your favorite programs.

KeyCut (for keyboard shortcut) is a command line tool
that helps you remembering the numerous keyboard shortcuts
of your favorite programs, both graphical and command line ones,
by allowing you to print them quickly in a console and search through them.

Shortcut data are provided by the `keycut-data`_ repository.

This repo contains the sources for a Python implementation of KeyCut.

It looks like this
==================

The yellow parts are the one that matched a pattern using a regular expression.

.. image:: http://i.imgur.com/ZaqTOUb.png

=======
License
=======

Software licensed under `MPL 2.0`_ license.

.. _MPL 2.0 : https://www.mozilla.org/en-US/MPL/2.0/

Installation
============

::

    pip install keycut

Usage
=====

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

You can then use these functions like this:

.. code:: bash

    k vim README.rst
    kgrep vim replace
    k htop

Documentation
=============

https://github.com/Pawamoy/keycut/wiki

Development
===========

To run all the tests: ``tox``

License
=======

Copyright (c) 2015 Timothée Mazzucotelli

This Source Code is subject to the terms of the Mozilla Public
License, v. 2.0. See the LICENSE file for more details.

Todo
====

- Interactive UI with search commands
- Follow the principles in `keycut-data`_ repo (inheritance, attributes)

.. _keycut-data : https://github.com/Pawamoy/keycut-data
.. _keycut-data README : https://github.com/Pawamoy/keycut-data/blob/master/README.md
