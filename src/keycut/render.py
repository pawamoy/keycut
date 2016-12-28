# -*- coding: utf-8 -*-

import termcolor
import yaml


MATCH_COLOR = 'yellow'
CATEGORY_COLOR = 'blue'
ACTION_COLOR = None
KEY_COLOR = 'white'


def as_text(document):
    str_list = []
    for item in document:
        category = item.get('category', None)
        if category:
            str_list.append('Category: %s\nAction: %s\nKeys: %s\n' % (
                category, item['action'].rstrip(), item['keys']))
        else:
            str_list.append('Action: %s\nKeys: %s\n' % (
                item['action'].rstrip(), item['keys']
            ))
    return '\n'.join(str_list) if str_list else ''


def _color_match(line, positions, default):
    l = len(positions)
    # Concat until first pos
    s = [_color(line[:positions[0][0]], default)]
    # For each (start, end), concat colored from start to end
    for index, pos in enumerate(positions):
        s.append(_color(line[pos[0]:pos[1]], MATCH_COLOR))
        # If not last (start, end), concat until next start
        if index < l-1:
            s.append(_color(
                    line[pos[1]:positions[index+1][0]], default))
        # Else concat until end of string
        else:
            s.append(_color(line[pos[1]:], default))
    return s


def _color(text, color):
    if color is None:
        return text
    else:
        return termcolor.colored(text, color)


def as_colored_text(document):
    str_list = []
    for item in document:
        s = []
        category = item.get('category', None)
        if category:
            s.append('Category: ')
            category_pos = item.get('category_pos', None)
            if category_pos:
                s.extend(_color_match(category, category_pos, CATEGORY_COLOR))
                s.append('\n')
            else:
                s.append('%s\n' % _color(category, CATEGORY_COLOR))
        action = item['action'].rstrip('\n')
        action_pos = item.get('action_pos', None)
        s.append('  Action: ')
        if action_pos:
            s.extend(_color_match(action, action_pos, ACTION_COLOR))
            s.append('\n')
        else:
            s.append('%s\n' % _color(action, ACTION_COLOR))
        s.append('    Keys: ')
        s_key = []
        keys = item['keys']
        for key in keys:
            key_pos = item.get('keys_pos', {}).get(key)
            if key_pos:
                s_key.append(''.join(_color_match(key, key_pos, KEY_COLOR)))
            else:
                s_key.append('%s' % _color(key, KEY_COLOR))
        s.append(', '.join(s_key))
        s.append('\n')
        str_list.append(''.join(s))
    return '\n'.join(str_list) if str_list else ''


def as_yaml(document):
    return yaml.dump(document)
