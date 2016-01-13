# -*- coding: utf-8 -*-
import yaml


def as_text(document):
    str_list = []
    for item in document:
        category = item.get('category', None)
        if category is not None:
            str_list.append('Category: %s\nAction: %s\nKeys: %s\n' % (
                category, item['action'].rstrip(), item['keys']))
        else:
            str_list.append('Action: %s\nKeys: %s\n' % (
                item['action'].rstrip(), item['keys']
            ))
    return '\n'.join(str_list)


def as_yaml(document):
    return yaml.dump(document)
