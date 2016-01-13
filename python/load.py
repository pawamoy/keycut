# -*- coding: utf-8 -*-
import yaml


def from_yaml(file):
    with open(file) as f:
        doc = yaml.load(f)
    if isinstance(doc, dict):
        document = [dict(category=key, **v)
                    for key, value in doc.items() for v in value]
    else:
        document = [dict(category=None, **value) for value in doc]
    return document
