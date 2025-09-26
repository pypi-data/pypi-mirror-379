# SPDX-License-Identifier: GPL-3.0-or-later

# Copyright (C) 2023 Michał Góral.

import argparse
import sys
from i3ipc import Connection


# fmt:off
# It's important for n/s and e/w pair to have the first command be grow/shrink.
# This allows growing and shrinking "middle" windows. Otherwise such windows
# could be only gronw or shrunk.
GROW_MAP= {
    "north": ("grow up", "shrink down"),
    "n": ("grow up", "shrink down"),
    "up": ("grow up", "shrink down"),
    "u": ("grow up", "shrink down"),

    "south": ("shrink up", "grow down"),
    "s": ("shrink up", "grow down"),
    "down": ("shrink up", "grow down"),
    "d": ("shrink up", "grow down"),

    "east": ("grow right", "shrink left"),
    "e": ("grow right", "shrink left"),
    "right": ("grow right", "shrink left"),
    "r": ("grow right", "shrink left"),

    "west": ("shrink right", "grow left"),
    "w": ("shrink right", "grow left"),
    "left": ("shrink right", "grow left"),
    "l": ("shrink right", "grow left"),
}
# fmt: on


def prepare_args():
    parser = argparse.ArgumentParser(
        description="i3a-resize-compass - resize current window in a given direction"
    )

    parser.add_argument(
        "direction",
        choices=(
            "north",
            "south",
            "east",
            "west",
            "n",
            "s",
            "e",
            "w",
            "up",
            "down",
            "right",
            "left",
            "u",
            "d",
            "r",
            "l",
        ),
        help="direction in which window should be resized",
    )
    parser.add_argument(
        "distance",
        nargs="?",
        default="1ppt",
        help="distance in px or ppt. Default: 1ppt",
    )

    return parser.parse_args()


def main():
    args = prepare_args()
    i3 = Connection()

    # whole idea of i3a-resize-compass is to try one command first and when it
    # fails (because edge window has focus), try the other one.
    #
    # One edge case is a window in the middle for which resize-compass will
    # always resize the same side (upper border). This is better than the
    # alternative that this window could only grow (because both up and down
    # commands would grow it). See a comment near GROW_MAP.
    cmd_1, cmd_2 = GROW_MAP[args.direction]
    repl = i3.command(f"resize {cmd_1} {args.distance}")
    if not repl[0].success:
        repl = i3.command(f"resize {cmd_2} {args.distance}")

    sys.exit(int(not repl[0].success))
