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

import termcolor
import yaml

from keycut._internal.types import Document

MATCH_COLOR = "yellow"
"""Color used to highlight matching text."""
CATEGORY_COLOR = "blue"
"""Default color for category names."""
ACTION_COLOR = None
"""Default color for action names; `None` leaves them uncolored."""
KEY_COLOR = "white"
"""Default color for shortcut keys."""


def as_text(document: Document) -> str:
    """Render shortcut entries as plain text.

    Args:
        document: Shortcut entries to render.

    Returns:
        Formatted text, or an empty string for an empty document.
    """
    str_list = []
    for item in document:
        category = item.get("category", None)
        if category:
            str_list.append(f"Category: {category}\nAction: {item['action'].rstrip()}\nKeys: {item['keys']}\n")
        else:
            str_list.append(f"Action: {item['action'].rstrip()}\nKeys: {item['keys']}\n")
    return "\n".join(str_list) if str_list else ""


def _color_match(line: str, positions: list[tuple[int, int]], default: str | None) -> list[str]:
    length = len(positions)
    # Concat until first pos
    s = [_color(line[: positions[0][0]], default)]
    # For each (start, end), concat colored from start to end
    for index, pos in enumerate(positions):
        s.append(_color(line[pos[0] : pos[1]], MATCH_COLOR))
        # If not last (start, end), concat until next start
        if index < length - 1:
            s.append(_color(line[pos[1] : positions[index + 1][0]], default))
        # Else concat until end of string
        else:
            s.append(_color(line[pos[1] :], default))
    return s


def _color(text: str, color: str | None) -> str:
    if color is None:
        return text
    return termcolor.colored(text, color)


def as_colored_text(document: Document) -> str:
    """Render shortcut entries with terminal colors for fields and matches.

    Args:
        document: Shortcut entries to render. Position fields, when present,
            mark the text to highlight.

    Returns:
        Formatted text, or an empty string for an empty document.
    """
    str_list = []
    for item in document:
        s = []
        category = item.get("category", None)
        if category:
            s.append("Category: ")
            category_pos = item.get("category_pos", None)
            if category_pos:
                s.extend(_color_match(category, category_pos, CATEGORY_COLOR))
                s.append("\n")
            else:
                s.append(f"{_color(category, CATEGORY_COLOR)}\n")
        action = item["action"].rstrip("\n")
        action_pos = item.get("action_pos", None)
        s.append("  Action: ")
        if action_pos:
            s.extend(_color_match(action, action_pos, ACTION_COLOR))
            s.append("\n")
        else:
            s.append(f"{_color(action, ACTION_COLOR)}\n")
        s.append("    Keys: ")
        s_key = []
        keys = item["keys"]
        for key in keys:
            key_pos = item.get("keys_pos", {}).get(key)
            if key_pos:
                s_key.append("".join(_color_match(key, key_pos, KEY_COLOR)))
            else:
                s_key.append(f"{_color(key, KEY_COLOR)}")
        s.append(", ".join(s_key))
        s.append("\n")
        str_list.append("".join(s))
    return "\n".join(str_list) if str_list else ""


def as_yaml(document: Document) -> str:
    """Serialize shortcut entries as YAML.

    Args:
        document: Shortcut entries to serialize.

    Returns:
        YAML text.
    """
    return yaml.dump(document)
