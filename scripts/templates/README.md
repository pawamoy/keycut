<!--
IMPORTANT:
  This file is generated from the template at 'scripts/templates/README.md'.
  Please update the template instead of this file.
-->

# keycut
![logo](logo.jpg)

[![pipeline status](https://gitlab.com/pawamoy/keycut/badges/master/pipeline.svg)](https://gitlab.com/pawamoy/keycut/pipelines)
[![coverage report](https://gitlab.com/pawamoy/keycut/badges/master/coverage.svg)](https://gitlab.com/pawamoy/keycut/commits/master)
[![documentation](https://img.shields.io/readthedocs/keycut.svg?style=flat)](https://keycut.readthedocs.io/en/latest/index.html)
[![pypi version](https://img.shields.io/pypi/v/keycut.svg)](https://pypi.org/project/keycut/)

A command line tool that helps you remembering ALL the numerous keyboard shortcuts of ALL your favorite programs.

KeyCut (for keyboard shortcut) is a command line tool
that helps you remembering the numerous keyboard shortcuts
of your favorite programs, both graphical and command line ones,
by allowing you to print them quickly in a console and search through them.

Shortcut data are provided by the [keycut-data][1].

This repository contains the sources for a Python implementation of KeyCut.

[keycut-data]: https://github.com/pawamoy/keycut-data

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

With [`pipx`](https://github.com/cs01/pipx):
```bash
# install pipx with the recommended method
curl https://raw.githubusercontent.com/cs01/pipx/master/get-pipx.py | python3

pipx install --python python3.6 keycut
```

You will also need to download the data by cloning the repository somewhere:

```
git clone https://github.com/pawamoy/keycut-data ~/.keycut-data
```

## Usage
The program needs to know where the data are. By default, it will search
in the (relative) `keycut-data/default` directory.

```
export KEYCUT_DATA=~/.keycut-data/default
```

Show all bash shortcuts:

```
keycut bash
```

Show all bash shortcuts matching *proc* (in Category, Action, or Keys):

```
keycut bash proc
```

Command-line help:

```
{{ command_line_help }}
```

{% if commands %}Commands:
{% for command in commands %}
- [`{{ command.name }}`](#{{ command.name }}){% endfor %}

{% for command in commands %}
### `{{ command.name }}`
```
{{ command.help }}
```

{% include "command_" + command.name.replace("-", "_") + "_extra.md" ignore missing %}
{% endfor %}{% endif %}
