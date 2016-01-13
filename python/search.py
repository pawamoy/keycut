# -*- coding: utf-8 -*-
import re


def _search(document, pattern, key=None, word=False):
    exp = r'.*\b%s\b.*' if word else r'.*%s.*'
    prog = re.compile(exp % pattern, re.IGNORECASE)
    if key is not None:
        return [item for item in document if prog.match(item[key])]
    else:
        l = []
        for item in document:
            if prog.match(item['action']):
                l.append(item)
            elif prog.match(item['category']):
                l.append(item)
            else:
                for key in item['keys']:
                    if prog.match(key):
                        l.append(item)
        return l


def search(document, pattern):
    return _search(document, pattern)


def in_category(document, pattern):
    return _search(document, pattern, key='category')


def in_action(document, pattern):
    return _search(document, pattern, key='action')


def in_keys(document, pattern):
    return _search(document, pattern, key='keys')


def word_search(document, pattern):
    return _search(document, pattern, word=True)


def word_in_category(document, pattern):
    return _search(document, pattern, key='category', word=True)


def word_in_action(document, pattern):
    return _search(document, pattern, key='action', word=True)


def word_in_keys(document, pattern):
    return _search(document, pattern, key='keys', word=True)
