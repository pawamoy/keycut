#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Little program to record keyboard shortcuts because there are so many."""
import os
import sys
import argparse
import json
import readline


shortcut_list = []
file_path = os.path.join(os.environ.get('cgData'), 'shortcuts.json')


class Shortcut:
    def __init__(self, keys=None, actions=None, program='', features=None):
        if not features: features = []
        if not actions: actions = []
        if not keys: keys = []
        self.keys = keys
        self.actions = actions
        self.program = program
        self.features = features

    def add_keys(self, keys=None):
        if not keys: keys = []
        self.keys.extend(keys)

    def add_actions(self, actions=None):
        if not actions: actions = []
        self.actions.extend(actions)

    def set_program(self, program=''):
        self.program = program

    def add_features(self, features=None):
        if not features: features = []
        self.features.extend(features)

    def remove_keys(self, keys=None):
        for key in keys:
            self.keys.remove(key)

    def remove_actions(self, actions=None):
        for action in actions:
            self.actions.remove(action)

    def remove_features(self, features=None):
        for feature in features:
            self.features.remove(feature)

    @staticmethod
    def serializer(obj):
        if isinstance(obj, Shortcut):
            return {"__class__": "Shortcut",
                    "keys": obj.keys,
                    "actions": obj.actions,
                    "program": obj.program,
                    "features": obj.features}
        raise TypeError(repr(obj) + " is not serializable.")

    @staticmethod
    def deserializer(obj_dict):
        if "__class__" in obj_dict:
            if obj_dict["__class__"] == "Shortcut":
                obj = Shortcut(
                    obj_dict["keys"],
                    obj_dict["actions"],
                    obj_dict["program"],
                    obj_dict["features"])
                return obj
        return obj_dict


class ShortcutList:
    def __init__(self):
        self.data = []

    def find(self, shortcut):
        :


    def add(self, shortcuts):
        for shortcut in shortcuts:
            s = self.pop(shortcut)
            if s:
                s.update(shortcut)
                self.data.append(s)
            else:
                self.data.append(shortcut)

    def remove(self, keys=None, actions=None, programs=None, features=None):
        pass


def save_shortcuts(filename=file_path):
    """
    Serialize all the shortcuts and write them to filename param.
    """
    filename = os.path.abspath(filename)
    if os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump(shortcut_list, f, indent=4, default=Shortcut.serializer)


def load_shortcuts(filename=file_path):
    """
    Read all shortcuts fom filename param and return their deserialization.
    """
    filename = os.path.abspath(filename)
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f, object_hook=Shortcut.deserializer)
    else:
        with open(filename, 'w') as f:
            pass


class CustomFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar
        else:
            parts = []
            # if the Optional doesn't take a value, format is:
            #    -s, --long
            if action.nargs == 0:
                parts.extend(action.option_strings)

            # if the Optional takes a value, format is:
            #    -s ARGS, --long ARGS
            # change to
            #    -s, --long ARGS
            else:
                default = action.dest.upper()
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    #parts.append('%s %s' % (option_string, args_string))
                    parts.append('%s' % option_string)
                parts[-1] += ' %s'%args_string
            return ', '.join(parts)


def process_command_line(argv):
    """
    Return a 2-tuple: (settings object, args list).
    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    if argv is None:
        argv = sys.argv[1:]
    # initialize the parser object:
    parser = argparse.ArgumentParser(
        formatter_class=CustomFormatter,
        add_help=False,
        usage="%(prog)s [option] [SHORTCUT]",
        description="%(prog)s is a command-line tool used to memorize keyboard "
                    "shortcuts. A shortcut has several data attached on it: "
                    "the keys combination, the program affected, the action it "
                    "does (several, for translations), and the features "
                    " concerned (edit, resize, focus, ...). "
                    "Positionnal SHORTCUT is composed of a combination of the "
                    "four filter options: -pfkc STRING [STRING ...]")
    # define options here:
    parser.add_argument('shortcut', nargs='*')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--add', dest='add',
                       help='Add a shortcut', action='store_true')
    group.add_argument('-r', '--remove', dest='remove',
                       help='Remove a shortcut', action='store_true')
    group.add_argument('-e', '--edit', dest='edit',
                       help='Edit a shortcut', action='store_true')
    group.add_argument('-l', '--list', action='store_true',
                       help='List all shortcuts')
    parser.add_argument('-p', '--programs', nargs='+', action='append',
                        help='Filter on programs', metavar='PRO')
    parser.add_argument('-f', '--features', nargs='+', action='append',
                        help='Filter on features', metavar='FEAT')
    parser.add_argument('-k', '--keys', nargs='+', action='append',
                        help='Filter on keys', metavar='KEY')
    parser.add_argument('-c', '--actions', nargs='+', action='append',
                        help='Filter on actions', metavar='ACT')
    group.add_argument('-h', '--help', action='help',
                       help='Show this help message and exit.')
    args = parser.parse_args(argv)
    return args


def gen_hook(text):
    def startup_hook():
        readline.insert_text(text)
    return startup_hook

# algo: fournir keys, features, actions ou program en cli
# avec une liste de valeur genre p=prog,f=feat,...
# si une/plusieurs valeurs genre -p prog -f feat ET une chaine (avant)
# chercher chaine partout sauf valeurs fournies
# si une seule valeur genre p=prog, chercher que prog dans programs
# si une seule valeur genre string, chercher string partout
# si aucune valeur, proposer les champs (user input)


def input_data(shortcut=None):
    keys, actions, programs, features = None, None, None, None
    insert = ' '.join(shortcut.keys) if shortcut else ''
    readline.set_startup_hook(gen_hook(insert))
    try:
        keys = raw_input("Keys: ")
    except EOFError:
        print
    insert = ' '.join(shortcut.actions) if shortcut else ''
    readline.set_startup_hook(gen_hook(insert))
    try:
        actions = raw_input("Actions: ")
    except EOFError:
        print
    insert = shortcut.program if shortcut else ''
    readline.set_startup_hook(gen_hook(insert))
    try:
        programs = raw_input("Programs: ")
    except EOFError:
        print
    insert = ' '.join(shortcut.features) if shortcut else ''
    readline.set_startup_hook(gen_hook(insert))
    try:
        features = raw_input("Features: ")
    except EOFError:
        print
    print keys, actions, programs, features


def main(argv=None):
    # set editable line in console
    # readline.parse_and_bind('set editing-mode vi')
    readline.parse_and_bind('tab: complete')
    args = process_command_line(argv)
    global shortcut_list
    try:
        shortcut_list = load_shortcuts()
        add_shortcut(programs=['geany', 'hey'])
        save_shortcuts()
    except ValueError:
        return 1

    # use selected filters (+ positionnal) to retrieve concerned shortcuts
    # add, edit, search -> ok, remove -> ask confirmation for each one found

    # try:
    #     input_data()
    # except KeyboardInterrupt:
    #     print
    #     return 2

if __name__ == '__main__':
    status = main()
    sys.exit(status)
