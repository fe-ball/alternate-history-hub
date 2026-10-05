"""Validate captured text, current files, live ECN references and finance totals.

Run from anywhere with Python 3. No third-party dependencies are needed.
Use --write-report to refresh VALIDATION.json after changes to the scenario.
This is a consistency check, not a proof of historical or technical feasibility.
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from decimal import Decimal
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
CURRENT = ROOT / 'current'
ERRORS = []


def require(condition, message):
    if not condition:
        ERRORS.append(message)


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def scalar(value):
    match = re.fullmatch(r'([\d.,]+)(億円|万円|円|機分|機|個|本)?', value.replace(' ', ''))
    if not match:
        return None
    number, unit = match.groups()
    multiplier = {'億円': 100000000, '万円': 10000, '円': 1}.get(unit, 1)
    return Decimal(number.replace(',', '')) * multiplier, ('円' if unit in ('億円', '万円', '円') else unit)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-report', action='store_true')
    args = parser.parse_args()
    source = load(ROOT / 'import/SOURCE-MANIFEST.json')
    current = load(ROOT / 'audit/CURRENT-MANIFEST.json')
    require(len(source['files']) == len(current['files']) == 39, 'Expected 39 source and current files')
    expected_names = {Path(e['current_path']).name for e in source['files']}
    require(expected_names == {p.name for p in CURRENT.glob('*.md')}, 'Current file inventory differs from capture')
    require(expected_names == {Path(e['path']).name for e in current['files']}, 'Current manifest inventory differs')
    total = 0
    for entry in source['files']:
        raw = (ROOT / entry['path']).read_bytes()
        total += len(raw)
        require(len(raw) == entry['bytes'], f"Source byte count: {entry['path']}")
        require(hashlib.sha256(raw).hexdigest() == entry['sha256'], f"Source SHA256: {entry['path']}")
        blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        require(blob == entry['git_blob_sha1'], f"Source Git blob: {entry['path']}")
    require(total == source['total_utf8_bytes'], 'Source total bytes')
    changed = 0
    for entry in current['files']:
        raw = (ROOT / entry['path']).read_bytes()
        require(len(raw) == entry['bytes'], f"Current byte count: {entry['path']}")
        require(hashlib.sha256(raw).hexdigest() == entry['sha256'], f"Current SHA256: {entry['path']}")
        differs = raw != (ROOT / 'import/source-2026-10-06' / Path(entry['path']).name).read_bytes()
        require(differs == entry['changed_from_capture'], f"Revision status: {entry['path']}")
        changed += differs

    master = (CURRENT / 'Master_Parameters.md').read_text(encoding='utf-8')
    definitions = {}
    for line in master.split('## 1. 経済ベースライン', 1)[1].splitlines():
        for match in re.finditer(r'`ECN:([A-Z0-9_]+)`', line):
            following = line[match.end():].replace('**', '')
            value = re.search(r'[:|]\s*([\d,.]+(?:[〜~–－-][\d,.]+)?)(万円|円|機分|機|個|本)?', following)
            if value:
                code = match.group(1)
                require(code not in definitions, f'Duplicate definition: {code}')
                definitions[code] = ''.join(x or '' for x in value.groups())
    require(bool(definitions), 'No ECN definitions parsed')
    references = []
    for p in sorted(CURRENT.glob('*.md')):
        fenced = False
        for number, line in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            if line.lstrip().startswith('```'):
                fenced = not fenced
                continue
            if fenced:
                continue
            for match in re.finditer(r'\[([^]\n]+)\]\{\{ECN:([A-Z0-9_]+)\}\}', line):
                value, code = match.groups()
                if code == 'CODE' and value == '数値':
                    continue  # The documented syntax placeholder, not a parameter.
                references.append({'file': p.name, 'line': number, 'code': code, 'value': value})
                require(code in definitions, f'{p.name}:{number}: undefined {code}')
                if code in definitions:
                    require(scalar(value) is not None and scalar(value) == scalar(definitions[code]),
                            f'{p.name}:{number}: {code}: {value} != {definitions[code]}')
    # The manually maintained section-0 index must agree with the definitions.
    for code, value in definitions.items():
        match = re.search(r'^\| `' + re.escape(code) + r'`[^|]*\| ([^|]+) \|', master.split('## 1. 経済ベースライン', 1)[0], re.M)
        require(match is not None, f'Master index missing {code}')
        if match:
            index = match.group(1).strip()
            if code.startswith(('REV_', 'CAPEX_')) and not index.endswith('円'):
                index += '万円'
            require(index == value or scalar(index) == scalar(value) and scalar(value) is not None,
                    f'Master index mismatch {code}: {index} != {value}')

    def yen(code):
        value = scalar(definitions[code])
        require(value is not None and value[1] == '円', f'Currency definition: {code}')
        return value[0]

    revenue = (CURRENT / 'Revenue_Model.md').read_text(encoding='utf-8')
    finances = {}
    for period in range(1, 7):
        start = revenue.index('## 第' + str(period) + ('期' if period != 4 else '〜5期'))
        block = revenue[start:]
        block = block.split('\n## ', 1)[0]
        items = []
        for line in block.splitlines():
            if not line.startswith('|') or any(term in line for term in ['**', '| うち ', '未配賦']):
                continue
            items += re.findall(r'\[[^]]+\]\{\{ECN:(REV_P' + str(period) + r'_[A-Z0-9_]+)\}\}', line)
        if period == 5:
            # These four original rows show raw currency amounts rather than ECN tags.
            for label, code in [('練習機（公開・初練）', 'REV_P5_AVIA_TRAINER'),
                                ('連絡機（DR連絡）', 'REV_P5_AVIA_LIAISON'),
                                ('哨戒機（四号・D哨）', 'REV_P5_AVIA_PATROL'),
                                ('自社機向け補用品・整備支援', 'REV_P5_AVIA_SPARE')]:
                row = re.search(r'^\| ' + re.escape(label) + r'\| ([\d,]+)万円', block, re.M)
                if not row:
                    row = re.search(r'^\| ' + re.escape(label) + r' \| ([\d,]+)万円', block, re.M)
                require(row is not None, f'P5 completed-aircraft row missing: {label}')
                if row:
                    require(Decimal(row.group(1).replace(',', '')) * 10000 == yen(code), f'P5 raw row differs: {label}')
                items.append(code)
        require(len(items) == len(set(items)), f'P{period}: duplicate revenue leaf')
        subtotal = sum(yen(code) for code in items)
        target = yen('REV_P' + str(period))
        residual = target - subtotal
        expected_open = {3: Decimal(400000), 4: Decimal(2200000)}.get(period, Decimal(0))
        require(residual == expected_open, f'P{period}: unexplained residual {residual} yen')
        finances[f'P{period}'] = {'leaf_tags': items, 'subtotal_yen': int(subtotal), 'macro_target_yen': int(target), 'unallocated_yen': int(residual), 'state': 'OPEN' if residual else 'ARITHMETIC_MATCH_ONLY'}

    growth = (CURRENT / 'Detailed_Growth_Simulation.md').read_text(encoding='utf-8')
    profit_block = growth.split('### 3.3', 1)[1].split('## 4.', 1)[0]
    profit = Decimal(0)
    for line in profit_block.splitlines():
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        if len(cells) == 4 and re.fullmatch(r'[\d,]+万', cells[3]) and not any(x in cells[0] for x in ['**', 'マクロ', '未照合']):
            profit += Decimal(cells[3][:-1].replace(',', '')) * 10000
    profit_delta = profit - yen('REV_P5_PROFIT')
    require(profit_delta == Decimal(1800000), f'P5 profit discrepancy changed: {profit_delta}')

    git = shutil.which('git')
    if not git and sys.platform == 'win32':
        candidate = Path('C:/Program Files/Git/cmd/git.exe')
        git = str(candidate) if candidate.is_file() else None
    link_count = 0
    for p in ROOT.rglob('*.md'):
        for link in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
            if '://' in link or link.startswith('#'):
                continue
            path = unquote(link.split('#', 1)[0].strip('<>'))
            if not path:
                continue
            target = (p.parent / path).resolve()
            exists = target.exists() or (args.write_report and target in [ROOT / 'audit/VALIDATION.json', ROOT / 'audit/ECN-REFERENCES.json'])
            # Sparse checkouts may omit unchanged common rules. Check the Git tree.
            if not exists and git and target.is_relative_to(REPO):
                result = subprocess.run([git, 'cat-file', '-e', 'HEAD:' + target.relative_to(REPO).as_posix()], cwd=REPO, capture_output=True)
                exists = result.returncode == 0
            require(exists, f'Broken link: {p.relative_to(ROOT)} -> {link}')
            link_count += 1

    state = load(CURRENT / 'ACTIVE-STATE.json')
    require(state['canonical_clock'] is None, 'Clock was promoted without a designation')
    coverage = load(ROOT / 'audit/COVERAGE.json')
    require(coverage['revision'] == current['revision'] == state['authority_version'], 'Audit/state revision mismatch')
    require(len(coverage['files']) == 39, 'Audit coverage must contain 39 entries')
    require({Path(e['path']).name for e in coverage['files']} == expected_names, 'Audit coverage inventory mismatch')
    source_hashes = {Path(e['current_path']).name: e['sha256'] for e in source['files']}
    for entry in coverage['files']:
        name = Path(entry['path']).name
        require(entry['source_sha256'] == source_hashes[name], f'Coverage source hash: {name}')
        require(entry['current_sha256'] == hashlib.sha256((ROOT / entry['path']).read_bytes()).hexdigest(), f'Coverage current hash: {name}')
        require(bool(entry['checked_dimensions']) and entry['all_external_claims_verified'] is False, f'Coverage scope missing or overstated: {name}')

    scope = load(ROOT / 'audit/FINANCE-COVERAGE.json')
    require(scope['revision'] == current['revision'], 'Finance scope revision mismatch')
    included = [e for e in scope['items'] if e['baseline_revenue_yen'] is not None]
    aircraft = [e for e in included if e['id'] != 'SPARES']
    require(sum(e['baseline_quantity'] for e in aircraft) == scope['baseline_aircraft_quantity'] == 125, 'Baseline aircraft count')
    require(sum(e['baseline_revenue_yen'] for e in aircraft) == scope['baseline_aircraft_sales_yen'] == 8150000, 'Aircraft versus support scope')
    require(sum(e['baseline_revenue_yen'] for e in included) == scope['baseline_aircraft_and_support_yen'] == yen('REV_P5_AVIA_BASE'), 'Coverage baseline versus master')
    require(scope['p5_macro_target_yen'] == yen('REV_P5') and scope['p6_macro_target_yen'] == yen('REV_P6'), 'Coverage macro versus master')
    require([sum(e['alternative_quantities'][i] for e in scope['items'] if e['alternative_quantities'] is not None) for i in range(3)] == scope['alternative_aircraft_totals'] == [95, 187, 295], 'Alternative aircraft row sums')
    require(all(e['full_plan_price_yen'] is None and e['full_plan_revenue_yen'] is None for e in scope['items']), 'Unknown full-plan amounts were promoted')
    require(all(e['incremental_revenue_yen'] is None for e in scope['unallocated_businesses']), 'Additional unpriced business amounts must remain null')
    for entry in scope['unallocated_businesses']:
        for code, amount in entry['known_tagged_revenue_yen'].items():
            require(amount == yen(code), f'Known business revenue erased or altered: {code}')
    require(set(scope['open_ids']).issubset(state['open_items']), 'Finance scope issues missing from active state')
    require(scope['original_complete_plan_share_percent'] == 40 and scope['original_share_state'] == 'WORKING_SCOPE_NOT_RECONCILED', 'Original full-plan share lost or promoted')
    for name in ['CFRP_Complete.md', 'Carbon_Material_Hierarchy.md']:
        content = (CURRENT / name).read_text(encoding='utf-8')
        require('PAN系CFRPは到達不可能' not in content and '主人公の知識投入では解決できない' not in content, f'PAN categorical ban regressed: {name}')
    decisions = (ROOT / 'audit/DECISION-REGISTER.md').read_text(encoding='utf-8')
    require(all(item in decisions for item in state['open_items']), 'Active OPEN list differs from register')
    report = {'revision': current['revision'], 'status': 'PASS' if not ERRORS else 'FAIL',
              'source_files': len(source['files']), 'source_utf8_bytes': total,
              'current_files': len(current['files']), 'corrected_files': changed,
              'ecn_definitions': len(definitions), 'checked_ecn_references': len(references),
              'relative_links': link_count, 'finance': finances,
              'p5_profit_unreconciled_yen': int(profit_delta), 'open_items': state['open_items'],
              'source_audit_coverage_files': len(coverage['files']),
              'finance_scope': {'baseline_aircraft_count': scope['baseline_aircraft_quantity'], 'aircraft_sales_yen': scope['baseline_aircraft_sales_yen'], 'aircraft_and_support_yen': scope['baseline_aircraft_and_support_yen'], 'alternative_counts': scope['alternative_aircraft_totals'], 'full_plan_revenue_yen': None, 'original_plan_share_state': scope['original_share_state'], 'unallocated_businesses': len(scope['unallocated_businesses'])},
              'limits': ['Arithmetic consistency only; OPEN residuals are not revenue or incurred costs.', 'Not a full audit of historical, technical, legal or commercial feasibility.', 'Hashes cover recovered UI text, not original upload bytes.'],
              'errors': ERRORS}
    if args.write_report:
        (ROOT / 'audit/ECN-REFERENCES.json').write_text(json.dumps({'revision': current['revision'], 'scope': 'explicit numeric references outside fenced examples; syntax placeholders excluded', 'references': references}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
        (ROOT / 'audit/VALIDATION.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return bool(ERRORS)


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
