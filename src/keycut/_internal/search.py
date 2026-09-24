# SPDX-License-Identifier: ISC
#
# ISC License
#
# Copyright (c) 2015, Timothée Mazzucotelli and contributors
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import re

from keycut._internal.types import Document


def _search(document: Document, pattern: str, *, key: str | None = None, word: bool = False) -> Document:
    exp = r"(\b%s\b)" if word else r"(%s)"
    prog = re.compile(exp % pattern, re.IGNORECASE)
    if key is not None:
        return [item for item in document if prog.search(item[key])]
    items = []
    for item in document:
        added = False
        mo = prog.search(item["action"])
        if mo:
            item["action_pos"] = []
            for index, _ in enumerate(mo.groups()):
                item["action_pos"].append(mo.span(index))
            if not added:
                items.append(item)
                added = True
        mo = prog.search(item["category"])
        if mo:
            item["category_pos"] = []
            for index, _ in enumerate(mo.groups()):
                item["category_pos"].append(mo.span(index))
            if not added:
                items.append(item)
                added = True
        item["keys_pos"] = {}
        for item_key in item["keys"]:
            mo = prog.search(str(item_key.encode("utf-8")))
            if mo:
                item["keys_pos"][item_key] = []
                for index, _ in enumerate(mo.groups()):
                    item["keys_pos"][item_key].append(mo.span(index))
                if not added:
                    items.append(item)
                    added = True
    return items or document


def search(document: Document, pattern: str) -> Document:
    """Search shortcut actions, categories, and keys with a case-insensitive regex.

    Matching entries gain position fields for highlighting. If nothing matches,
    return the original document.

    Args:
        document: Shortcut entries to search.
        pattern: Regular expression to match.

    Returns:
        Matching shortcut entries, or the original document if none match.
    """
    return _search(document, pattern)


def in_category(document: Document, pattern: str) -> Document:
    """Return shortcuts whose category matches a case-insensitive regex.

    Args:
        document: Shortcut entries to search.
        pattern: Regular expression to match.

    Returns:
        Matching shortcut entries.
    """
    return _search(document, pattern, key="category")


def in_action(document: Document, pattern: str) -> Document:
    """Return shortcuts whose action matches a case-insensitive regex.

    Args:
        document: Shortcut entries to search.
        pattern: Regular expression to match.

    Returns:
        Matching shortcut entries.
    """
    return _search(document, pattern, key="action")


def in_keys(document: Document, pattern: str) -> Document:
    """Return shortcuts whose keys field matches a case-insensitive regex.

    Args:
        document: Shortcut entries to search.
        pattern: Regular expression to match.

    Returns:
        Matching shortcut entries.
    """
    return _search(document, pattern, key="keys")


def word_search(document: Document, pattern: str) -> Document:
    """Search all shortcut fields for whole-word matches.

    Matching entries gain position fields for highlighting. If nothing matches,
    return the original document.

    Args:
        document: Shortcut entries to search.
        pattern: Case-insensitive regular expression to match as a whole word.

    Returns:
        Matching shortcut entries, or the original document if none match.
    """
    return _search(document, pattern, word=True)


def word_in_category(document: Document, pattern: str) -> Document:
    """Return shortcuts with a whole-word match in their category.

    Args:
        document: Shortcut entries to search.
        pattern: Case-insensitive regular expression to match as a whole word.

    Returns:
        Matching shortcut entries.
    """
    return _search(document, pattern, key="category", word=True)


def word_in_action(document: Document, pattern: str) -> Document:
    """Return shortcuts with a whole-word match in their action.

    Args:
        document: Shortcut entries to search.
        pattern: Case-insensitive regular expression to match as a whole word.

    Returns:
        Matching shortcut entries.
    """
    return _search(document, pattern, key="action", word=True)


def word_in_keys(document: Document, pattern: str) -> Document:
    """Return shortcuts with a whole-word match in their keys field.

    Args:
        document: Shortcut entries to search.
        pattern: Case-insensitive regular expression to match as a whole word.

    Returns:
        Matching shortcut entries.
    """
    return _search(document, pattern, key="keys", word=True)
