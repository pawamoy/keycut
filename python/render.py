# -*- coding: utf-8 -*-
import yaml

try:
    from clint.textui import colored
except ImportError:
    colored = lambda x:x


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


def _colored_match(line, positions):
    l = len(positions)
    # Concat until first pos
    s = [line[:positions[0][0]]]
    # For each (start, end), concat colored from start to end
    for index, pos in enumerate(positions):
        s.append(colored.green(line[pos[0]:pos[1]]))
        # If not last (start, end), concat until next start
        if index < l-1:
            s.append(line[pos[1]:positions[index+1][0]])
        # Else concat until end of string
        else:
            s.append(line[pos[1]:])
    s.append('\n')
    return s


def as_colored_text(document):
    str_list = []
    for item in document:
        s = []
        category = item.get('category', None)
        if category:
            s.append('Category: ')
            category_pos = item.get('category_pos', None)
            if category_pos:
                s.extend(_colored_match(category, category_pos))
            else:
                s.append('%s\n' % category)
        action = item['action']
        action_pos = item.get('action_pos', None)
        s.append('Action: ')
        if action_pos:
            s.extend(_colored_match(action, action_pos))
        else:
            s.append('%s\n' % action)
        str_list.append(''.join(s))
    return '\n'.join(str_list) if str_list else ''


def as_yaml(document):
    return yaml.dump(document)
