# -*- coding: utf-8 -*-

import re


def _search(document, pattern, key=None, word=False):
    exp = r'(\b%s\b)' if word else r'(%s)'
    prog = re.compile(exp % pattern, re.IGNORECASE)
    if key is not None:
        return [item for item in document if prog.search(item[key])]
    else:
        l = []
        for item in document:
            added = False
            mo = prog.search(item['action'])
            if mo:
                item['action_pos'] = []
                for index, group in enumerate(mo.groups()):
                    item['action_pos'].append(mo.span(index))
                if not added:
                    l.append(item)
                    added = True
            mo = prog.search(item['category'])
            if mo:
                item['category_pos'] = []
                for index, group in enumerate(mo.groups()):
                    item['category_pos'].append(mo.span(index))
                if not added:
                    l.append(item)
                    added = True
            item['keys_pos'] = {}
            for key in item['keys']:
                mo = prog.search(str(key))
                if mo:
                    item['keys_pos'][key] = []
                    for index, group in enumerate(mo.groups()):
                        item['keys_pos'][key].append(mo.span(index))
                    if not added:
                        l.append(item)
                        added = True
        return l if l else document


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
