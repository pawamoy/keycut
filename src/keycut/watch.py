# -*- coding: utf-8 -*-
import time
import load
import ui
from threading import Thread
from search import search


class Watcher(Thread):
    def __init__(self, file):
        Thread.__init__(self)
        self.file = file
        self.current = ''
        self.write('')
        self.sleep = 0.2

    def run(self):
        while True:
            line = self.read()
            if line:
                words = line.split(' ')
                command = words[0]
                if len(words) > 1:
                    pattern = words[1]
                    current = '%s %s' % (command, pattern)
                else:
                    current = command
                    pattern = False
                if current != self.current:
                    document = load.from_yaml(command)
                    if document:
                        if pattern:
                            document = search(document, pattern)
                        self.current = current
                        ui.reload(document)
            time.sleep(self.sleep)

    def read(self):
        with open(self.file) as f:
            return f.readline().rstrip()

    def write(self, command):
        with open(self.file, 'w') as f:
            f.write('%s\n' % command)
