# -*- coding: utf-8 -*-
import yaml
import json


def from_yaml(file):
    with open(file) as f:
        document = yaml.load(f)
    # if isinstance(document, dict):
    #     document = [value.update({'category': key})
    #                 for key, value in document.items()]
    # else:
    #     document = [value.update({'category': ''}) for value in document]
    return document


def from_json(file):
    with open(file) as f:
        document = json.load(f)
    return document
