# -*- coding: utf-8 -*-
import json
import yaml


def as_text(document):
    str_list = []
    if isinstance(document, dict):
        for key, value in document.items():
            for item in value:
                str_list.append('Keys: %s\nAction: %s\nCategory: %s\n' % (
                    item['keys'], item['action'].rstrip(), key
                ))
    elif isinstance(document, list):
        for item in document:
            str_list.append('Keys: %s\nAction: %s\n' % (
                item['keys'], item['action'].rstrip()
            ))
    return '\n'.join(str_list)


def as_json(document):
    return json.dumps(document)


def as_yaml(document):
    return yaml.dump(document)