import sys
from i3ipc import Connection

FLOATING_MODES = ('auto_on', 'user_on')

def tiled_nodes(tree, ws):
    return [l for l in ws.leaves() if l.floating not in FLOATING_MODES]

def main():
    i3 = Connection()
    tree = i3.get_tree()

    current = tree.find_focused()
    if not current:
        sys.exit(1)

    tiled = tiled_nodes(tree, current.workspace())
    if len(tiled) < 2:
        sys.exit(1)

    master = tiled[0]
    stack = tiled[1:]

    if current is master:
        i3.command('focus right')
        i3.command('swap container with con_id {}'.format(current.id))
    else:
        i3.command('swap container with con_id {}'.format(master.id))
