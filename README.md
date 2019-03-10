<!--
IMPORTANT:
  This file is generated from the template at 'scripts/templates/README.md'.
  Please update the template instead of this file.
-->

# keycut
[![pipeline status](https://github.com/pawamoy/keycut/badges/master/pipeline.svg)](https://github.com/pawamoy/keycut/commits/master)
[![coverage report](https://github.com/pawamoy/keycut/badges/master/coverage.svg)](https://github.com/pawamoy/keycut/commits/master)
[![documentation](https://img.shields.io/readthedocs/keycut.svg?style=flat)](https://keycut.readthedocs.io/en/latest/index.html)
[![pypi version](https://img.shields.io/pypi/v/keycut.svg)](https://pypi.org/project/keycut/)

A command line tool that helps you remembering ALL the numerous keyboard shortcuts of ALL your favorite programs.

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

## Usage (as a library)
TODO

## Usage (command-line)
```
usage: keycut [-h] [NAME [NAME ...]]

Command description.

positional arguments:
  NAME        A name of something.

optional arguments:
  -h, --help  show this help message and exit

```


