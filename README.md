# keycut

[![ci](https://github.com/pawamoy/keycut/workflows/ci/badge.svg)](https://github.com/pawamoy/keycut/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://pawamoy.github.io/keycut/)
[![pypi version](https://img.shields.io/pypi/v/keycut.svg)](https://pypi.org/project/keycut/)

![logo](logo.jpg)

A command line tool that helps you remembering ALL the numerous keyboard shortcuts of ALL your favorite programs.

KeyCut (for keyboard shortcut) is a command line tool
that helps you remembering the numerous keyboard shortcuts
of your favorite programs, both graphical and command line ones,
by allowing you to print them quickly in a console and search through them.

Shortcut data are provided by the [keycut-data][1].

This repository contains the sources for a Python implementation of KeyCut.

[1]: https://github.com/pawamoy/keycut-data

## How it looks

The yellow parts are the one that matched a pattern using a regular expression.

![screenshot](http://i.imgur.com/ZaqTOUb.png)

## Requirements

keycut requires Python 3.6 or above.

<details>
<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>

```bash
# install pyenv
git clone https://github.com/pyenv/pyenv ~/.pyenv

# setup pyenv (you should also put these three lines in .bashrc or similar)
export PATH="${HOME}/.pyenv/bin:${PATH}"
export PYENV_ROOT="${HOME}/.pyenv"
eval "$(pyenv init -)"

# install Python 3.6
pyenv install 3.6.8

# make it available globally
pyenv global system 3.6.8
```
</details>

## Installation

With `pip`:
```bash
python3.6 -m pip install keycut
```

With [`pipx`](https://github.com/pipxproject/pipx):
```bash
python3.6 -m pip install --user pipx

pipx install --python python3.6 keycut
```

## Usage

The program needs to know where the data are. By default, it will search
in the (relative) `keycut-data/default` directory.

```bash
export KEYCUT_DATA=~/.keycut-data/default
```

Show all bash shortcuts:

```bash
keycut bash
```

Show all bash shortcuts matching *proc* (in Category, Action, or Keys):

```bash
keycut bash proc
```

Command-line help:

```console
$ keycut -h
usage: keycut [-h] APP [PATTERN]

Command description.

positional arguments:
  APP         The app to print shortcuts of.
  PATTERN     A regex pattern to search for.

optional arguments:
  -h, --help  show this help message and exit
```
