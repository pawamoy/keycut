# -*- coding: utf-8 -*-

# import os

from . import render
from .search import (
    in_action, in_category, in_keys, search, word_in_action, word_in_category,
    word_in_keys, word_search)


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


def reload(document, clear=True):
    global UI_DOCUMENT
    UI_DOCUMENT = document
    text = render.as_colored_text(document)
    # B605:start_process_with_a_shell
    # B607:start_process_with_partial_path
    # if clear:
    #     os.system('clear')
    print(text)
