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

import logging
import time
from pathlib import Path
from threading import Thread
from typing import Any

from keycut._internal import load, ui
from keycut._internal.search import search

_logger = logging.getLogger("keycut")


class XdotoolWatcher(Thread):
    """Watch the focused window name for application shortcuts."""

    def __init__(self) -> None:
        Thread.__init__(self)
        self.name = ""
        """Last window name with a loaded shortcut document."""
        self.sleep = 0.2
        """Seconds between checks of the focused window."""

    @staticmethod
    def _run_command(command: str) -> Any:
        pass
        # return Popen(
        #     command, shell=True, stdout=PIPE
        # ).stdout.read().decode().rstrip('\n')

    def run(self) -> None:
        """Poll the focused window and display shortcuts when its name changes."""
        name_command = "xdotool getwindowfocus getwindowname"

        while True:
            name = self._run_command(name_command)

            if name != self.name:
                document = load.from_yaml(name, command_line=name)
                if document:
                    self.name = name
                    ui.reload(document)
                else:
                    _logger.error(f"Not found: {name}")
            time.sleep(self.sleep)


class WindowFocusWatcher(Thread):
    """Watch the focused process for application shortcuts."""

    def __init__(self) -> None:
        Thread.__init__(self)
        self.name = ""
        """Last process name with a loaded shortcut document."""
        self.cmdline = ""
        """Last process command line with a loaded shortcut document."""
        self.sleep = 0.2
        """Seconds between checks of the focused process."""

    @staticmethod
    def _run_command(command: str) -> Any:
        pass
        # return Popen(
        #     command, shell=True, stdout=PIPE
        # ).stdout.read().decode().rstrip('\n')

    def run(self) -> None:
        """Poll the focused process and display shortcuts when it changes."""
        wid_command = "xprop -root | grep -F '_NET_ACTIVE_WINDOW(WINDOW)' | grep -o '0x.*'"
        pid_command = 'xprop -id %s | grep _NET_WM_PID | grep -o "[0-9]*"'
        name_command = "cat /proc/%s/comm"
        cmdline_command = "cat /proc/%s/cmdline"

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
                    _logger.error("Not found: {wid} {pid} {name} {cmdline}")
            time.sleep(self.sleep)


class FileWatcher(Thread):
    """Watch a command file and display shortcuts for new commands.

    Creating the watcher clears the command file.
    """

    def __init__(self, file: str) -> None:
        Thread.__init__(self)
        self.file = file
        """Path to the command file."""
        self.current = ""
        """Last command used to load a shortcut document."""
        self.write("")
        self.sleep = 0.2
        """Seconds between reads of the command file."""

    def run(self) -> None:
        """Poll the command file and display shortcuts for new commands."""
        while True:
            line = self.read()
            if line:
                words = line.split(" ")
                command = words[0]
                if len(words) > 1:
                    pattern = words[1]
                    current = f"{command} {pattern}"
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

    def read(self) -> str:
        """Return the first line of the command file without trailing whitespace."""
        with Path(self.file).open() as f:
            return f.readline().rstrip()

    def write(self, command: str) -> None:
        """Write a command and newline to the command file.

        Args:
            command: Command to store, replacing the file's contents.
        """
        with Path(self.file).open("w") as f:
            f.write(f"{command}\n")
