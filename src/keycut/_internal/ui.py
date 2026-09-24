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

from keycut._internal import render
from keycut._internal.search import (
    in_action,
    in_category,
    in_keys,
    search,
    word_in_action,
    word_in_category,
    word_in_keys,
    word_search,
)
from keycut._internal.types import Document

UI_COMMANDS = {
    "s": search,
    "a": in_action,
    "c": in_category,
    "k": in_keys,
    "ws": word_search,
    "wa": word_in_action,
    "wc": word_in_category,
    "wk": word_in_keys,
}
"""Command names mapped to their shortcut search functions."""


def reload(document: Document) -> None:
    """Print shortcut entries with terminal colors.

    Args:
        document: Shortcut entries to print.
    """
    text = render.as_colored_text(document)
    print(text)  # noqa: T201
