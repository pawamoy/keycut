# -*- coding: utf-8 -*-

import os
import yaml

DIRECTORY = os.environ.get('KEYCUT_DATA', 'keycut-data/default')


def grep(cmdline):
    cmdline = cmdline.lower()
    for file in os.listdir(DIRECTORY):
        app = os.path.splitext(file.lower())[0]
        if app in cmdline:
            return os.path.join(DIRECTORY, file)
    return None


def isfile(file):
    return os.path.isfile(file)


def check(name, path=DIRECTORY):
    file = os.path.join(path, name) + '.yml'
    return file, isfile(file)


def from_yaml(app, command_line=None):
    file, exist = check(app)
    if not exist and command_line is not None:
        file = grep(command_line)
        if not file:
            return None
    with open(file) as f:
        doc = yaml.safe_load(f)
    if isinstance(doc, dict):
        document = [dict(category=key, **v)
                    for key, value in doc.items() for v in value]
    else:
        document = [dict(category='', **value) for value in doc]
    return document
