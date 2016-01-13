# -*- coding: utf-8 -*-
import time
import load
import os
import ui
from threading import Thread

DIRECTORY = '/media/pawantu/Data/git/keycut/keycut-data/default/'


def isfile(file):
    return os.path.isfile(file)


def check(name, path=DIRECTORY):
    file = os.path.join(path, name) + '.yml'
    return file, isfile(file)


class Watcher(Thread):
    def __init__(self, file):
        Thread.__init__(self)
        self.file = file
        self.command = ''

        if not isfile(file):
            with open(file, 'w') as f:
                f.write('')

    def run(self):
        while True:
            line = self.read()
            if line:
                command = line.split(' ', 1)[0]
                if command != self.command:
                    file, exist = check(command)
                    if exist:
                        self.command = command
                        ui.reload(load.from_yaml(file))
            time.sleep(0.5)

    def read(self):
        with open(self.file) as f:
            return f.readline().rstrip()

    def write(self, command):
        with open(self.file, 'w') as f:
            f.write('%s\n' % command)
