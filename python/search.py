# -*- coding: utf-8 -*-
import re


def search(document, pattern, key=None):
    prog = re.compile(pattern)
    if key is not None:
        return [item for item in document if prog.match(item[key])]
    else:
        return [item for item in document
                if any([prog.match(item[k]) for k in item.keys()])]


def search_category(document, pattern):
    return search(document, pattern, key='category')


def search_action(document, pattern):
    return search(document, pattern, key='action')


def search_key(document, pattern):
    return search(document, pattern, key='keys')
