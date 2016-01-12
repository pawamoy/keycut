#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import readline

from load.yaml import load_file

# class CustomFormatter(argparse.HelpFormatter):
#     def _format_action_invocation(self, action):
#         if not action.option_strings:
#             metavar, = self._metavar_formatter(action, action.dest)(1)
#             return metavar
#         else:
#             parts = []
#             if action.nargs == 0:
#                 parts.extend(action.option_strings)
#             else:
#                 default = action.dest.upper()
#                 args_string = self._format_args(action, default)
#                 for option_string in action.option_strings:
#                     parts.append('%s' % option_string)
#                 parts[-1] += ' %s'%args_string
#             return ', '.join(parts)
#
#
# def process_command_line(argv):
#     """
#     Return a 2-tuple: (settings object, args list).
#     `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
#     """
#     if argv is None:
#         argv = sys.argv[1:]
#     # initialize the parser object:
#     parser = argparse.ArgumentParser(
#         formatter_class=CustomFormatter,
#         add_help=False,
#         usage="%(prog)s [option] [SHORTCUT]",
#         description="%(prog)s is a command-line tool used to memorize keyboard "
#                     "shortcuts. A shortcut has several data attached on it: "
#                     "the keys combination, the program affected, the action it "
#                     "does (several, for translations), and the features "
#                     " concerned (edit, resize, focus, ...). "
#                     "Positionnal SHORTCUT is composed of a combination of the "
#                     "four filter options: -pfkc STRING [STRING ...]")
#     # define options here:
#     parser.add_argument('shortcut', nargs='*')
#     group = parser.add_mutually_exclusive_group(required=True)
#     group.add_argument('-a', '--add', dest='add',
#                        help='Add a shortcut', action='store_true')
#     group.add_argument('-r', '--remove', dest='remove',
#                        help='Remove a shortcut', action='store_true')
#     group.add_argument('-e', '--edit', dest='edit',
#                        help='Edit a shortcut', action='store_true')
#     group.add_argument('-l', '--list', action='store_true',
#                        help='List all shortcuts')
#     parser.add_argument('-p', '--programs', nargs='+', action='append',
#                         help='Filter on programs', metavar='PRO')
#     parser.add_argument('-f', '--features', nargs='+', action='append',
#                         help='Filter on features', metavar='FEAT')
#     parser.add_argument('-k', '--keys', nargs='+', action='append',
#                         help='Filter on keys', metavar='KEY')
#     parser.add_argument('-c', '--actions', nargs='+', action='append',
#                         help='Filter on actions', metavar='ACT')
#     group.add_argument('-h', '--help', action='help',
#                        help='Show this help message and exit.')
#     args = parser.parse_args(argv)
#     return args


# def gen_hook(text):
#     def startup_hook():
#         readline.insert_text(text)
#     return startup_hook

# def input_data(shortcut=None):
#     keys, actions, programs, features = None, None, None, None
#     insert = ' '.join(shortcut.keys) if shortcut else ''
#     readline.set_startup_hook(gen_hook(insert))
#     try:
#         keys = input("Keys: ")
#     except EOFError:
#         print()
#     insert = ' '.join(shortcut.actions) if shortcut else ''
#     readline.set_startup_hook(gen_hook(insert))
#     try:
#         actions = input("Actions: ")
#     except EOFError:
#         print()
#     insert = shortcut.program if shortcut else ''
#     readline.set_startup_hook(gen_hook(insert))
#     try:
#         programs = input("Programs: ")
#     except EOFError:
#         print()
#     insert = ' '.join(shortcut.features) if shortcut else ''
#     readline.set_startup_hook(gen_hook(insert))
#     try:
#         features = input("Features: ")
#     except EOFError:
#         print()
#     print(keys, actions, programs, features)


# def main(argv=None):
#     # set editable line in console
#     # readline.parse_and_bind('set editing-mode vi')
#     readline.parse_and_bind('tab: complete')
#     args = process_command_line(argv)
#     global shortcut_list
#     try:
#         shortcut_list = load_shortcuts()
#         add_shortcut(programs=['geany', 'hey'])
#         save_shortcuts()
#     except ValueError:
#         return 1
#
#     use selected filters (+ positionnal) to retrieve concerned shortcuts
#     add, edit, search -> ok, remove -> ask confirmation for each one found
#
#     try:
#         input_data()
#     except KeyboardInterrupt:
#         print
#         return 2

# if __name__ == '__main__':
#     status = main()
#     sys.exit(status)


if __name__ == '__main__':
    document = load_file('/media/pawantu/Data/git/keycut-data/default/bash.yml')
    print(document)
