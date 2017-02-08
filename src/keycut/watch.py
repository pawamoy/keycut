# -*- coding: utf-8 -*-

import json
import time
# from subprocess import Popen
from threading import Thread

import load
import ui
from search import search


class FirefoxWatcher(Thread):
    # FIXME: do this dynamically
    f = open('/home/pawantu/.mozilla/firefox/7vjr1dfd.default/'
             'sessionstore-backups/recovery.js', 'r')
    jdata = json.loads(f.read())
    f.close()
    tab_number = jdata['windows'][0]['selected']
    for win in jdata.get('windows'):
        for tab in win.get('tabs'):
            i = tab.get('index') - 1
            if i == tab_number:
                current_url = tab.get('entries')[i].get('url')


class XdotoolWatcher(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.name = ''
        self.sleep = 0.2

    @staticmethod
    def _run_command(command):
        pass
        # return Popen(
        #     command, shell=True, stdout=PIPE
        # ).stdout.read().decode().rstrip('\n')

    def run(self):
        name_command = 'xdotool getwindowfocus getwindowname'

        while True:
            name = self._run_command(name_command)

            if name != self.name:
                document = load.from_yaml(name, command_line=name)
                if document:
                    self.name = name
                    ui.reload(document)
                else:
                    print('Not found:')
                    print(name)
            time.sleep(self.sleep)


class WindowFocusWatcher(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.name = ''
        self.cmdline = ''
        self.sleep = 0.2

    @staticmethod
    def _run_command(command):
        pass
        # return Popen(
        #     command, shell=True, stdout=PIPE
        # ).stdout.read().decode().rstrip('\n')

    def run(self):
        wid_command = 'xprop -root | grep _NET_ACTIVE_WINDOW\(WINDOW\) | ' \
                      'grep -o "0x.*"'
        pid_command = 'xprop -id %s | grep _NET_WM_PID | grep -o "[0-9]*"'
        name_command = 'cat /proc/%s/comm'
        cmdline_command = 'cat /proc/%s/cmdline'

        while True:
            wid = self._run_command(wid_command)
            pid = self._run_command(pid_command % wid)
            name = self._run_command(name_command % pid)
            cmdline = self._run_command(cmdline_command % pid)

            if name != self.name and cmdline != self.cmdline:
                document = load.from_yaml(name, cmdline)
                if document:
                    self.name = name
                    self.cmdline = cmdline
                    ui.reload(document)
                else:
                    print('Not found:')
                    print(wid, pid)
                    print(name, cmdline)
            time.sleep(self.sleep)


class FileWatcher(Thread):
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
