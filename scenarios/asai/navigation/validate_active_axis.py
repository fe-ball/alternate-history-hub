#!/usr/bin/env python3
"""Validate ASAI routing, not historical/engineering correctness. No dependencies.

Normally run from a complete repository checkout. --tree-index accepts a verified
Git tree index {repo_relative_path: {sha, type}} for connector-only verification.
--verify-migration additionally checks all relocated source trees against origin.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import posixpath
import re
import subprocess
import sys
from pathlib import Path

PREFIX = 'scenarios/asai/'
STATES = ['capability', 'physical article', 'qualification', 'adopted',
          'factory accepted', 'service released', 'assigned', 'serviceable',
          'forward', 'combat-present']

def validate(root: Path, index: dict | None = None, migration: bool = False) -> dict:
    errors: list[str] = []
    checks = 0
    def check(ok: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not ok:
            errors.append(message)
    def text(path: str) -> str:
        return (root / path).read_text(encoding='utf-8')
    def exists(path: str) -> bool:
        if index is None:
            return (root / path).exists()
        return path in index or any(p.startswith(path.rstrip('/') + '/') for p in index)
    def digest(path: str) -> str | None:
        if index is not None:
            return index.get(path, {}).get('sha')
        p = root / path
        if p.is_file():
            b = p.read_bytes()
            return hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
        try:
            return subprocess.check_output(['git', '-C', str(root), 'rev-parse',
                                            'HEAD:' + path], text=True).strip()
        except subprocess.CalledProcessError:
            return None
    def files_under(path: str) -> set[str]:
        if index is not None:
            return {p for p, v in index.items() if p.startswith(path.rstrip('/') + '/')
                    and v.get('type') == 'blob'}
        return {p.relative_to(root).as_posix() for p in (root / path).rglob('*') if p.is_file()}
    m = json.loads(text(PREFIX + 'current/ACTIVE-STATE.json'))
    routes = json.loads(text(PREFIX + m['source_routes']))
    check(m['scenario_id'] == 'asai', 'Wrong scenario in active manifest')
    check(m['physical_states'] == STATES, 'Physical status fields missing/reordered')
    check(m['kind'] == 'NAVIGATION-ONLY-NO-CANON-PROMOTION', 'Unexpected authority promotion')
    check(m['new_history_or_status_promoted'] is False, 'Routing change promotes history')
    expected_order = ['00-SESSION-HANDOFF.md', '01-DECISION-REGISTER.tsv',
                      '02-CONTINUITY-STATE.md', '03-OPEN-ITEMS-AND-NEXT-GATES.tsv']
    check(m['default_read_order'] == ['current/active/' + p for p in expected_order],
          'Default read order or scope changed without updating validator')
    for p in m['default_read_order'] + m['lineage_sources']:
        check(exists(PREFIX + p), 'Missing reading/source target: ' + p)
    sources = m['sources']
    for key, s in sources.items():
        check(exists(PREFIX + s['path']), 'Missing source: ' + key)
        check(digest(PREFIX + s['path']) == s['blob_sha'], 'Source changed; resync manifest: ' + key)
    registered = {PREFIX + s['path'] for s in sources.values()}
    actual = files_under(PREFIX + m['source_root'])
    check(actual == registered, 'Unregistered or missing continuation file: ' + str(sorted(actual ^ registered)))
    for p in m['default_search_scope']:
        check(not p.startswith(('archive', 'import', 'scenarios/keisanki')), 'Unsafe default search scope')
    ledger = list(csv.DictReader(text(PREFIX + m['default_read_order'][1]).splitlines(), delimiter='\t'))
    gates = list(csv.DictReader(text(PREFIX + m['default_read_order'][3]).splitlines(), delimiter='\t'))
    for rows in (ledger, gates):
        active = [r for r in rows if r['navigation_role'] == 'CURRENT-NEXT']
        check(len(active) == 1, 'Current next gate is absent/ambiguous')
        if active:
            check(active[0]['sources'] == m['discussion_frontier']['next_gate_source'], 'Next gate pointer mismatch')
        for r in rows:
            check(bool(r['source_status']), 'Source status missing')
            for token in r['sources'].split(';'):
                base = token.split('#', 1)[0]
                check(base in sources or exists(PREFIX + base), 'Unknown source ID/path: ' + token)
    expected_legacy: set[str] = set()
    for route in routes['routes']:
        dest = PREFIX + route['target_prefix'].rstrip('/')
        check(exists(dest), 'Missing relocated tree: ' + dest)
        if migration or route['role'] == 'SIBLING-HISTORY-NOT-ACTIVE':
            check(digest(dest) == route['original_tree_sha'], 'Preserved tree changed: ' + dest)
        for target in files_under(dest):
            old = PREFIX + route['legacy_prefix'] + target[len(dest) + 1:]
            expected_legacy.add(old)
            check(exists(old), 'Old URL lacks redirect: ' + old)
            if (root / old).is_file():
                check('LEGACY-NAVIGATION-ONLY' in text(old), 'Old URL exposes obsolete source: ' + old)
    for f in routes['files']:
        old, dest = PREFIX + f['legacy_path'], PREFIX + f['target_path']
        expected_legacy.add(old)
        check(exists(old) and exists(dest), 'Broken entrypoint relocation: ' + old)
        check(digest(dest) == f['blob_sha'], 'Original entrypoint changed: ' + dest)
    allowed_top = {'active', 'technical', 'ACTIVE-STATE.json', 'README.md', '00-START-HERE-CURRENT.md'}
    allowed_top |= {r['legacy_prefix'].split('/')[1] for r in routes['routes']}
    allowed_top |= {f['legacy_path'].split('/')[1] for f in routes['files']}
    for p in files_under(PREFIX + 'current'):
        check(p[len(PREFIX + 'current/'):].split('/')[0] in allowed_top,
              'Unregistered current checkpoint/package: ' + p)
    prompt = text(PREFIX + 'START-PROMPT.txt')
    check(len(prompt) <= 1000, 'Start prompt exceeds 1000 characters including newline')
    central = text('scenarios.yaml').split('  asai:\n', 1)[1].split('\n  keisanki-ibun:', 1)[0]
    for value in (m['canonical_authority'], m['canonical_clock'], m['axis_id'],
                  PREFIX + 'current/ACTIVE-STATE.json'):
        check(value in central, 'Central registry out of sync: ' + value)
    if migration:
        for p, key in [('current/technical', 'preserved_technical_tree_sha'),
                       ('import', 'preserved_import_tree_sha')]:
            check(digest(PREFIX + p) == routes[key], 'Unexpected migration change: ' + p)
    # Check new navigation links, not pre-existing links inside frozen source records.
    owned = [PREFIX + p for p in m['default_read_order'] if p.endswith('.md')]
    owned += [PREFIX + p for p in ['README.md', '00-READ-FIRST-GENERIC.md', 'SCENARIO-RULES.md',
              'current/README.md', 'current/00-START-HERE-CURRENT.md', 'records/README.md',
              'archive/README.md', 'archive/non-active-history/README.md']]
    link_count = 0
    for p in owned:
        for link in re.findall(r'\]\(([^)]+)\)', text(p)):
            if link.startswith(('https:', 'http:', '#')):
                continue
            dest = posixpath.normpath(posixpath.join(posixpath.dirname(p), link.split('#')[0]))
            check(exists(dest), 'Broken navigation link: ' + p + ' -> ' + dest)
            link_count += 1
    return {'ok': not errors, 'checks': checks, 'navigation_links': link_count,
            'sources': len(sources), 'legacy_source_paths': len(expected_legacy),
            'prompt_characters_including_final_newline': len(prompt), 'errors': errors,
            'scope': 'Routing, inventory and retained Git objects only; not historical/engineering correctness.'}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument('--tree-index', type=Path)
    parser.add_argument('--verify-migration', action='store_true')
    args = parser.parse_args()
    try:
        index = json.loads(args.tree_index.read_text()) if args.tree_index else None
        report = validate(args.root, index, args.verify_migration)
    except (OSError, ValueError, KeyError, IndexError) as exc:
        print(json.dumps({'ok': False, 'error': str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report['ok'] else 1

if __name__ == '__main__':
    sys.exit(main())
