======
KeyCut
======

.. start-badges


|travis|
|codacygrade|
|codacycoverage|
|version|
|wheel|
|pyup|
|gitter|


.. |travis| image:: https://travis-ci.org/Pawamoy/keycut.svg?branch=master
    :target: https://travis-ci.org/Pawamoy/keycut/
    :alt: Travis-CI Build Status

.. |codacygrade| image:: https://api.codacy.com/project/badge/Grade/d6b55dcf0ea3428d902b7d291c0805ce
    :target: https://www.codacy.com/app/Pawamoy/keycut/dashboard
    :alt: Codacy Code Quality Status

.. |codacycoverage| image:: https://api.codacy.com/project/badge/Coverage/d6b55dcf0ea3428d902b7d291c0805ce
    :target: https://www.codacy.com/app/Pawamoy/keycut/dashboard
    :alt: Codacy Code Coverage

.. |pyup| image:: https://pyup.io/repos/github/Pawamoy/keycut/shield.svg
    :target: https://pyup.io/repos/github/Pawamoy/keycut/
    :alt: Updates

.. |version| image:: https://img.shields.io/pypi/v/keycut.svg?style=flat
    :target: https://pypi.python.org/pypi/keycut/
    :alt: PyPI Package latest release

.. |wheel| image:: https://img.shields.io/pypi/wheel/keycut.svg?style=flat
    :target: https://pypi.python.org/pypi/keycut/
    :alt: PyPI Wheel

.. |gitter| image:: https://badges.gitter.im/Pawamoy/keycut.svg
    :target: https://gitter.im/Pawamoy/keycut
    :alt: Join the chat at https://gitter.im/Pawamoy/keycut



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

License
=======

Software licensed under `ISC`_ license.

.. _ISC: https://www.isc.org/downloads/software-support-policy/isc-license/

Installation
============

::

    [sudo -H] pip install keycut

You will also need to download the data by cloning the repository somewhere:

::

    git clone https://github.com/Pawamoy/keycut-data keycut_data

Usage
=====

The program needs to know where the data are. By default, it will search
in the (relative) `keycut-data/default` directory.

.. code:: bash

    export KEYCUT_DATA=/somewhere/keycut_data/default

Show all bash shortcuts:

.. code:: bash

    keycut bash

Show all bash shortcuts matching *proc* (in Category, Action, or Keys):

.. code:: bash

    keycut bash proc


Documentation
=============

http://keycut.readthedocs.io/en/latest/


Development
===========

To run all the tests: ``tox``

Todo
====

- Interactive UI with search commands
- Follow the principles in `keycut-data`_ repo (inheritance, attributes)

.. _keycut-data: https://github.com/Pawamoy/keycut-data
.. _keycut-data README: https://github.com/Pawamoy/keycut-data/blob/master/README.md
