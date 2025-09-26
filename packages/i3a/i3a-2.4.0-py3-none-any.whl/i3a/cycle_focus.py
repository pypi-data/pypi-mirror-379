# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2024 DjejDjej

import argparse
import asyncio

from i3ipc.aio import Connection

FLOATING_MODES = ("auto_on", "user_on")


async def move_stack(direction: str):
    """
    Move the focused window up or down the stack in the current workspace.
    :param direction: 'up' to move up, 'down' to move down.
    """
    i3 = await Connection(auto_reconnect=True).connect()
    tree = await i3.get_tree()
    focused = tree.find_focused()

    if not focused:
        return

    ws = focused.workspace()
    if not ws:
        return

    # Collect all tiled (non-floating) windows
    tiled_windows = [
        n
        for n in ws.leaves()
        if n.floating not in FLOATING_MODES
    ]

    if len(tiled_windows) < 2:
        return

    try:
        idx = tiled_windows.index(focused)
        if direction == "up":
            target_idx = (idx - 1) % len(tiled_windows)
        elif direction == "down":
            target_idx = (idx + 1) % len(tiled_windows)
        else:
            raise ValueError("Invalid direction; use 'up' or 'down'.")

        target_window = tiled_windows[target_idx]
        await i3.command(f'[con_id="{target_window.id}"] focus')
    except ValueError:
        pass


def main():
    parser = argparse.ArgumentParser(
        description="Move the focused window up or down the stack."
    )
    parser.add_argument(
        "direction",
        choices=["up", "down"],
        help="Direction to move the window in the stack.",
    )
    args = parser.parse_args()

    asyncio.run(move_stack(args.direction))
