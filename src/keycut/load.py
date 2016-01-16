# -*- coding: utf-8 -*-
import os
import yaml

DIRECTORY = '/media/pawantu/Data/git/keycut/keycut-data/default/'


def isfile(file):
    return os.path.isfile(file)


def check(name, path=DIRECTORY):
    file = os.path.join(path, name) + '.yml'
    return file, isfile(file)


def from_yaml(app):
    file, exist = check(app)
    if not exist:
        return None
    with open(file) as f:
        doc = yaml.load(f)
    if isinstance(doc, dict):
        document = [dict(category=key, **v)
                    for key, value in doc.items() for v in value]
    else:
        document = [dict(category='', **value) for value in doc]
    return document
