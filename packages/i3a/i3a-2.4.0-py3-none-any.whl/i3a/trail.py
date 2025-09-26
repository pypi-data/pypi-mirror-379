# SPDX-License-Identifier: GPL-3.0-or-later

# Copyright (C) 2025 Michał Góral.

import argparse
import os
import sys
import tempfile
from contextlib import suppress
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

from i3ipc import Connection

from i3a import __version__ as version

TRAYMARK = "__i3a_trail.{trailid}.{winid}"
TRAYMARK_RE = r"^__i3a_trail\.{trailid}\.{winid}$"


@dataclass
class Trail:
    _id: int
    _winid: int = 0
    _end: int = 0

    @property
    def id(self):
        return self._id

    @property
    def winid(self):
        return self._winid

    @winid.setter
    def winid(self, val: int):
        assert val >= 0
        self._end = max(self._end, val + 1)
        self._winid = val

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, val: int):
        assert val == 0 or val > self._winid
        self._end = val
        self._winid = min(self._winid, val)

    @property
    def deleted(self):
        return self._end == 0

    def __iter__(self):
        i = self.winid + 1
        yield from range(i, self.end)
        yield from range(0, i)

    def __reversed__(self):
        i = self.winid - 1
        yield from range(i, -1, -1)
        yield from range(self.end - 1, i, -1)


# trail format:
#   <current_trail>
#   <trail-0-winid><space><trail-0-end>
#   <trail-1-winid><space><trail-1-end>
#   ...
@dataclass
class Db:
    _tid: int = 0
    _trails: list[Trail] = field(default_factory=list)

    def __post_init__(self):
        if self._tid > len(self._trails):
            self._tid = 0

    def trail(self, idx: int | None = None) -> Trail | None:
        if idx is None:
            idx = self._tid
        if len(self._trails) <= idx:
            return None
        return self._trails[idx]

    def add_trail(self, *args, **kwargs) -> Trail:
        trail_id = len(self._trails)
        self._trails.append(Trail(trail_id, *args, **kwargs))
        return self._trails[-1]

    def delete_trail(self, idx: int | None = None):
        trail = self.trail(idx)
        if trail:
            trail.winid = 0
            trail.end = 0

    def seek(self, idx: int) -> Trail:
        assert idx >= 0

        for _ in range(idx - len(self._trails) + 1):
            self.add_trail(0, 0)

        self._tid = idx
        return self._trails[self._tid]

    def __iter__(self) -> Iterator[Trail]:
        i = self._tid + 1
        yield from self._trails[i:]
        yield from self._trails[:i]

    def __reversed__(self) -> Iterator[Trail]:
        i = self._tid
        yield from reversed(self._trails[:i])
        yield from reversed(self._trails[i:])

    def save(self, path: Path | None = None):
        lines = [str(self._tid)]
        for i, trail in enumerate(self._trails):
            if trail.end == 0 and i > self._tid:
                continue
            lines.append(f"{trail.winid} {trail.end}")

        text = "\n".join(lines) + "\n"
        path = path or Db.dbpath()
        path.write_text(text)

    @staticmethod
    def dbpath() -> Path:
        tmpdir = tempfile.gettempdir()
        uid = os.getuid()
        sock = get_sockname()
        return Path(tmpdir) / f"i3a-trail-{uid}-{sock}"

    @classmethod
    def from_file(cls, path: Path | None = None) -> "Db":
        path = path or Db.dbpath()
        lines = path.read_text().splitlines()
        db = Db()
        for line in lines[1:]:
            winid, _, end = line.strip().partition(" ")
            db.add_trail(int(winid), int(end))
        db.seek(int(lines[0].strip()))
        return db


def get_sockname():
    path = os.environ.get("I3SOCK", os.environ.get("SWAYSOCK", ""))
    return os.path.splitext(os.path.basename(path))[0]


def seek_next_trail(db: Db, iter_fn) -> Trail | None:
    dbit = iter_fn(db)
    for trail in dbit:
        if not trail.deleted:
            return db.seek(trail.id)
    return None


def find_mark_with_prefix(marks: list[str], prefix: str) -> str | None:
    for m in marks:
        if m.startswith(prefix):
            return m
    return None


def get_winid_of_trail_from_marks(marks: list[str], trailid: int) -> int | None:
    prefix = TRAYMARK.format(trailid=trailid, winid="")
    mark = find_mark_with_prefix(marks, prefix)
    if mark:
        with suppress(ValueError):
            return int(mark.split(".")[-1])
    return None


def jump_to_next_trailmark(db: Db, iter_fn) -> bool:
    curr = db.trail()
    if curr is None:
        return False

    i3 = Connection()
    tree = i3.get_tree()

    # set winid from mark of currently focused window to use it as a starting point
    if focused := tree.find_focused():
        focused_winid = get_winid_of_trail_from_marks(focused.marks, curr.id)
        if focused_winid is not None:
            curr.winid = focused_winid

    trail_iterator = iter_fn(curr)

    for winid in trail_iterator:
        mk_re = TRAYMARK_RE.format(trailid=curr.id, winid=winid)
        for container in tree.find_marked(mk_re):
            if container.focused:
                continue
            repl = container.command("focus")
            if repl[0].success:
                curr.winid = winid
                return True
    return False


def cmd_new_trail(args, db: Db):
    trail = db.add_trail(0, 0)
    db.seek(trail.id)
    db.save(args.db)


def cmd_delete_trail(args, db: Db):
    curr = db.trail()
    if curr:
        i3 = Connection()
        tree = i3.get_tree()
        mk = TRAYMARK.format(trailid=curr.id, winid="")
        mk_re = TRAYMARK_RE.format(trailid=curr.id, winid=".*")
        for container in tree.find_marked(mk_re):
            for mark in container.marks:
                if mark.startswith(mk):
                    container.command(f"mark --add --toggle {mark}")

    db.delete_trail()
    next_trail = seek_next_trail(db, reversed)
    if not next_trail:
        db.seek(0)

    db.save(args.db)


def cmd_next_trail(args, db: Db):
    seek_next_trail(db, iter)
    db.save(args.db)


def cmd_prev_trail(args, db: Db):
    seek_next_trail(db, reversed)
    db.save(args.db)


def cmd_mark(args, db: Db):
    trail = db.trail()
    if trail is None:
        trail = db.add_trail()

    i3 = Connection()
    focused = i3.get_tree().find_focused()
    if not focused:
        sys.exit(1)

    prefix = TRAYMARK.format(trailid=trail.id, winid="")
    if to_remove := find_mark_with_prefix(focused.marks, prefix):
        focused.command(f"mark --add --toggle {to_remove}")
    else:
        newmark = TRAYMARK.format(trailid=trail.id, winid=trail.end)
        repl = focused.command(f"mark --add {newmark}")
        if not repl[0].success:
            sys.exit(1)
        trail.winid = trail.end
        db.save(args.db)


def cmd_next(args, db: Db):
    if not jump_to_next_trailmark(db, iter):
        sys.exit(1)
    db.save(args.db)


def cmd_previous(args, db: Db):
    if not jump_to_next_trailmark(db, reversed):
        sys.exit(1)
    db.save(args.db)


def prepare_args():
    parser = argparse.ArgumentParser(
        description="i3a-trail - quick jump between window trailmarks"
    )

    sp = parser.add_subparsers(required=True)

    new_trail_sp = sp.add_parser("new-trail", help="create new trail and use it")
    new_trail_sp.set_defaults(func=cmd_new_trail)

    delete_trail_sp = sp.add_parser(
        "delete-trail", help="delete current trail and switch to the previous one"
    )
    delete_trail_sp.set_defaults(func=cmd_delete_trail)

    next_trail_sp = sp.add_parser("next-trail", help="use next trail")
    next_trail_sp.set_defaults(func=cmd_next_trail)

    prev_trail_sp = sp.add_parser("previous-trail", help="use previous trail")
    prev_trail_sp.set_defaults(func=cmd_prev_trail)

    mark_sp = sp.add_parser(
        "mark", help="toggle a trail mark on currently focused window"
    )
    mark_sp.set_defaults(func=cmd_mark)

    next_sp = sp.add_parser("next", help="jump to the next window in current trail")
    next_sp.set_defaults(func=cmd_next)

    previous_sp = sp.add_parser(
        "previous", help="jump to the previous window in current trail"
    )
    previous_sp.set_defaults(func=cmd_previous)

    parser.add_argument("--db", help="path to trail marks database")
    parser.add_argument("--version", action="version", version=f"%(prog)s {version}")

    return parser.parse_args()


def main():
    args = prepare_args()
    try:
        db = Db.from_file(args.db)
    except (IndexError, FileNotFoundError):
        db = Db()

    args.func(args, db)
