# -*- coding: utf-8 -*-
import json
import yaml


def as_text(document):
    str_list = []
    for item in document:
        category = item.get('category', None)
        if category is not None:
            str_list.append('Category: %s\nAction: %s\nKeys: %s\n' % (
                category, item['keys'], item['action'].rstrip()))
        else:
            str_list.append('Action: %s\nKeys: %s\n' % (
                item['keys'], item['action'].rstrip()
            ))
    return '\n'.join(str_list)


def as_json(document):
    return json.dumps(document)


def as_yaml(document):
    return yaml.dump(document)
