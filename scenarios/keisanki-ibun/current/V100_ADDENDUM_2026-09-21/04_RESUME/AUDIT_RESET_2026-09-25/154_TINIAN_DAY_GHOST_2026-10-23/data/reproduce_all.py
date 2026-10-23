"""Audit runner: regenerate all 12 CSV datasets without modifying archived inputs.

Stage-1 day-only ghost WORKING sensitivity. Not a historical damage adjudication.
"""
from __future__ import annotations
import csv
import math
import subprocess
import sys
import tempfile
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent
SCRIPTS = [
    'tinian_day_event_model.py',
    'tinian_16_20_ghost_increment_model.py',
    'tinian_16_24_dualclock_model.py',
    'tinian_25jul06_replay.py',
]
CSVS = [
    'tinian_day15_events.csv', 'tinian_day15_scenarios.csv',
    'tinian_16_20_daily.csv', 'tinian_16_20_gunroll.csv',
    'tinian_16_24_evidence_events.csv', 'tinian_16_24_ghost_days.csv',
    'tinian_16_24_ghost_deltas.csv', 'tinian_16_24_ghost_guns.csv',
    'tinian_25jul06_AB_deltas.csv', 'tinian_25jul06_day_ghost.csv',
    'tinian_25jul06_gunroll.csv', 'tinian_25jul06_summary.csv',
]

def same_value(a: str, b: str) -> bool:
    if a == b:
        return True
    try:
        return math.isclose(float(a), float(b), rel_tol=1e-9, abs_tol=1e-9)
    except ValueError:
        return False

def assert_equivalent(expected: Path, actual: Path) -> int:
    with expected.open(encoding='utf-8-sig', newline='') as f:
        reference = list(csv.reader(f))
    with actual.open(encoding='utf-8-sig', newline='') as f:
        produced = list(csv.reader(f))
    assert len(reference) == len(produced), (expected.name, len(reference), len(produced))
    for rownum, (a, b) in enumerate(zip(reference, produced), 1):
        assert len(a) == len(b), (expected.name, rownum, len(a), len(b))
        for col, (x, y) in enumerate(zip(a, b), 1):
            assert same_value(x, y), (expected.name, rownum, col, x, y)
    return len(reference) - 1

def main() -> None:
    with tempfile.TemporaryDirectory(prefix='tinian_ghost_repro_') as d:
        target = Path(d)
        for script in SCRIPTS:
            content = (ROOT / script).read_text(encoding='utf-8')
            needle = "Path('/mnt/data')"
            assert needle in content, (script, 'legacy output path changed; inspect manually')
            (target / script).write_text(
                content.replace(needle, f'Path({str(target)!r})'), encoding='utf-8'
            )
        for script in SCRIPTS:
            if script == 'tinian_25jul06_replay.py':
                with ZipFile(target / 'tinian_16_24_ghost_repro.zip',
                             'w', compression=ZIP_DEFLATED) as z:
                    z.write(target / 'tinian_16_24_ghost_assumptions.json',
                            arcname='tinian_16_24_ghost_assumptions.json')
            subprocess.run(
                [sys.executable, str(target / script)],
                cwd=target, capture_output=True, text=True, check=True, timeout=60
            )
        print('AUDIT: stage-1 day-only ghost; NOT historical casualty adjudication')
        total = 0
        for name in CSVS:
            count = assert_equivalent(ROOT / name, target / name)
            total += count
            print(f'OK {name}: {count} data rows')
        print(f'PASS: {len(CSVS)} CSVs / {total} data rows; tolerance 1e-9')

if __name__ == '__main__':
    main()
