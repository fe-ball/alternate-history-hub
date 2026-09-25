#!/usr/bin/env python3
"""Reject retired Keisanki Ibun files, including byte-identical renamed copies.

Checks committed Git objects, not the working directory. Does not rewrite history
or inspect nested archives. Policy changes require an explicit owner decision.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys

POLICY_PATH = Path(__file__).resolve().parents[1] / "retired-keisanki-sources.json"


def violations(entries, policy):
    blocked = set(policy["blocked_git_blob_sha1"])
    fragments = [x.casefold() for x in policy["blocked_path_fragments"]]
    failures = []
    for path, sha in entries:
        if sha in blocked:
            failures.append(f"{path}: retired content (including renamed copies)")
        elif any(x in path.casefold() for x in fragments):
            failures.append(f"{path}: retired package path")
    return failures


def git_entries(ref):
    raw = subprocess.check_output(
        ["git", "ls-tree", "-r", "-z", "--full-tree", ref]
    )
    entries = []
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, path = record.split(b"\t", 1)
        _, kind, sha = metadata.split()
        if kind == b"blob":
            entries.append((path.decode("utf-8"), sha.decode("ascii")))
    return entries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", default="HEAD")
    args = parser.parse_args()
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    failures = violations(git_entries(args.ref), policy)
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print("PASS: no retired Keisanki Ibun files or package paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
