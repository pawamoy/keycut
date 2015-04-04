#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Little program to record keyboard shortcuts because there are so many.
"""

import os
import sys
import argparse
import json
import readline
import sqlite3

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Shortcut(Base):
    __tablename__ = 'shortcut'
    id = Column(Integer, primary_key=True)
    sequences = relationship('Sequence', backref='shortcuts')
    apps = relationship('App', backref='shortcuts')
    tags = relationship('Tag', backref='shortcuts')
    actions = relationship('Action', backref='shortcuts')


class Sequence(Base):
    __tablename__ = 'sequence'
    id = Column(Integer, primary_key=True)
    active = Column(Boolean(), default=True)
    hotkey = Column(Boolean(), default=False)
    binding = Column(Boolean(), default=False)
    sacred = Column(Boolean(), default=False)
    default = Column(Boolean(), default=False)
    keys = Column(String(40), nullable=False)


class App(Base):
    __tablename__ = 'app'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    version = Column(String(20))


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))


class Language(Base):
    __tablename__ = 'language'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))


class Action(Base):
    __tablename__ = 'action'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    lang = Column(Integer, ForeignKey('language.id'))


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

conn = sqlite3.connect('keycut.db')
c = conn.cursor()

# @staticmethod
# def serializer(obj):
#     if isinstance(obj, Shortcut):
#         return {"__class__": "Shortcut",
#                 "keys": obj.keys,
#                 "actions": obj.actions,
#                 "program": obj.program,
#                 "features": obj.features}
#     raise TypeError(repr(obj) + " is not serializable.")
#
# @staticmethod
# def deserializer(obj_dict):
#     if "__class__" in obj_dict:
#         if obj_dict["__class__"] == "Shortcut":
#             obj = Shortcut(
#                 obj_dict["keys"],
#                 obj_dict["actions"],
#                 obj_dict["program"],
#                 obj_dict["features"])
#             return obj
#     return obj_dict


# def save_shortcuts(filename=file_path):
#     """
#     Serialize all the shortcuts and write them to filename param.
#     """
#     filename = os.path.abspath(filename)
#     if os.path.exists(filename):
#         with open(filename, 'w') as f:
#             json.dump(shortcut_list, f, indent=4, default=Shortcut.serializer)


# def load_shortcuts(filename=file_path):
#     """
#     Read all shortcuts fom filename param and return their deserialization.
#     """
#     filename = os.path.abspath(filename)
#     if os.path.exists(filename):
#         with open(filename, 'r') as f:
#             return json.load(f, object_hook=Shortcut.deserializer)
#     else:
#         with open(filename, 'w') as f:
#             pass


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

# algo: fournir keys, features, actions ou program en cli
# avec une liste de valeur genre p=prog,f=feat,...
# si une/plusieurs valeurs genre -p prog -f feat ET une chaine (avant)
# chercher chaine partout sauf valeurs fournies
# si une seule valeur genre p=prog, chercher que prog dans programs
# si une seule valeur genre string, chercher string partout
# si aucune valeur, proposer les champs (user input)


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
