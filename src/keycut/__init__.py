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

"""keycut package.

A command line tool that helps you remembering ALL the numerous keyboard shortcuts of ALL your favorite programs.
"""

from __future__ import annotations

from keycut._internal.cli import get_parser, main
from keycut._internal.load import DIRECTORY, check, from_yaml, grep, isfile
from keycut._internal.render import (
    ACTION_COLOR,
    CATEGORY_COLOR,
    KEY_COLOR,
    MATCH_COLOR,
    as_colored_text,
    as_text,
    as_yaml,
)
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
from keycut._internal.ui import UI_COMMANDS, UI_DOCUMENT, reload
from keycut._internal.utils import print_err
from keycut._internal.watch import (
    FileWatcher,
    FirefoxWatcher,
    WindowFocusWatcher,
    XdotoolWatcher,
)

__all__: list[str] = [
    "ACTION_COLOR",
    "CATEGORY_COLOR",
    "DIRECTORY",
    "KEY_COLOR",
    "MATCH_COLOR",
    "UI_COMMANDS",
    "UI_DOCUMENT",
    "FileWatcher",
    "FirefoxWatcher",
    "WindowFocusWatcher",
    "XdotoolWatcher",
    "as_colored_text",
    "as_text",
    "as_yaml",
    "check",
    "from_yaml",
    "get_parser",
    "grep",
    "in_action",
    "in_category",
    "in_keys",
    "isfile",
    "main",
    "print_err",
    "reload",
    "search",
    "word_in_action",
    "word_in_category",
    "word_in_keys",
    "word_search",
]
