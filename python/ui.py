# -*- coding: utf-8 -*-
import render
from search import (
    search, in_action, in_category, in_keys,
    word_search, word_in_action, word_in_category, word_in_keys)

UI_COMMANDS = {
    's': search,
    'a': in_action,
    'c': in_category,
    'k': in_keys,
    'ws': word_search,
    'wa': word_in_action,
    'wc': word_in_category,
    'wk': word_in_keys
}

UI_DOCUMENT = None


def reload(document):
    global UI_DOCUMENT
    UI_DOCUMENT = document
    text = render.as_text(document)
    print(text)
