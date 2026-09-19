# V23 — CURRENT FRONTIER — RETRO-AUDIT / SOURCE REPAIR TO 1939–1941

## Status

**CURRENT ACTIVE FRONTIER**

The canonical history clock remains 1946-06-30T24:00 class. The current discussion intentionally returns to 1939–1941.

This is not a rollback of authority.

## Purpose

Re-audit the upstream state that feeds the China-war continuation route and later German technology-transfer branch.

A complete byte-exact V22B source mirror is now available. The immediate task is therefore not to reconstruct missing history from memory, but to determine whether the earlier partial import caused any source loss, false “ledger missing” assumptions, or downstream working estimates that should be repaired.

## Source-recovery rule

For the contents of the original V22B ZIP:

- use `scenarios/asai/import/source-v22b-full-exact/` as the exact recovery source;
- retain `scenarios/asai/import/source-v22b-full/` only as historical partial-import provenance;
- where both contain the same path/subject, the partial reconstruction must not override the exact source;
- source presence does not itself promote an older OPEN/WORKING/ARCHIVE file over V23/V22B/V21 precedence.

The archive copy and exact source tree have been verified against the uploaded ZIP:
- 1,122 / 1,122 files;
- 27,856,505 bytes expanded payload;
- ZIP SHA-256 `4bea918064d011331dfe5e0ba3ceed3994e59cc4d2187e84495e59719bc63307`;
- archive Git blob `c51075904e597ef5b37fb3917f2dd6b64e91f8e2`;
- path + blob + size fingerprint `3f8dbee80b9473f3`.

## Current-authority integrity result

A first comparison of `current/` against the exact source found:

- 49 current blobs total;
- 42 files with direct original-source counterparts;
- 38 already byte-identical;
- 4 differed only by trailing newline/whitespace and are restored to the exact source blobs in the recovery commit;
- 7 are V23/new routing files with no V22B source counterpart.

No substantive corruption has yet been found in the inherited V21/V22B/current technical-parent files.

This does **not** clear every conversational working claim made while the source package was only partially accessible.

## Working claims requiring re-audit

In particular, do not carry forward without source checking:

- claims that the 1939–41 normal-aircraft ledgers were absent;
- reconstructions of Zero/Hayabusa/Shoki/Ki-46/bomber/attack-aircraft timing or performance based mainly on historical data;
- production or fielding estimates made before the full procurement/weapon-gate ledgers were recovered;
- China-war operational availability estimates built on those incomplete aviation assumptions;
- Indochina and converted-carrier arguments that depend on aircraft inventory, training or mission capability.

These were conversation-level working analyses unless separately persisted by higher authority.

## Mandatory no-backflow rule

1945–46 outcomes may be used to identify questions worth auditing.

They may not be used as actor knowledge in 1939–41.

Do not backflow:

- later battlefield lessons;
- later production statistics;
- later diplomatic outcomes;
- later Soviet/German loss knowledge;
- postwar technology;
- final armistice incentives;
- later E-generation hardware not yet physically available.

## Technical-recovery priority

Read the exact-source layers before inventing new values, especially:

- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/`;
- `71-CURRENT-TECHNICAL-CONTROL-V9/`;
- `75-CURRENT-TECHNICAL-ADDENDA-V10/`;
- `76-CURRENT-1940-WEAPON-GATE-V10/`;
- `78-CURRENT-2026-09-08-AIRCRAFT-DEVELOPMENT-CLOSE/`;
- `79-CURRENT-2026-09-08-FIXED-WING-PROCUREMENT-CLOSE/`;
- `84-CURRENT-2026-09-11-THREAD-CONSOLIDATION-V16/`;
- relevant manifests/decision registers that define supersession and quarantine.

For historical-named aircraft, first resolve identity, engine/propeller, exhaust, cooling, materials, fire-control/bombing, production and fielding ledgers. Historical calendar/specification is only an anchor.

## Next reconstruction target

Build a clean 1941-05-31 aviation/technical state from the last closed upstream states.

Required separation:

`ordered/reserved -> factory accepted -> physically extant -> service released -> unit assigned -> serviceable -> forward -> immediately operational`.

At minimum cover:

- E5 Twin / Ki-42;
- E6 Twin / E6 Single / E6-B;
- A6M;
- Ki-43 / Ki-44;
- Ki-46;
- Ki-21 / Ki-48 / Ki-51 and other relevant Army bombing/attack layers;
- B5N / D3A / G3M / G4M and relevant Navy reconnaissance/water-aircraft layers;
- experimental A7M Gaifu / A8N Sakufu / TP reconnaissance only at their actual maturity state;
- E7 / Homare / Ha-43 as research-development states, not premature service hardware.

## Precedence during retro audit

V23 downstream result remains the current route unless a retro audit explicitly demonstrates a causal contradiction that requires amendment.

When such a contradiction is found:

1. identify the exact upstream value/event;
2. identify the downstream V23/V22B claims affected;
3. revise only the causally affected chain;
4. update scenarios.yaml authority/clock/frontier only if those axes actually change.

## Immediate next question

First repair any state genuinely damaged or mis-inferred during the partial-import period. Then recover the technical/procurement/fielding state from the exact package. Only after the 1941-05 ledger is coherent should the discussion return to continuation of the China war, French Indochina advance and converted-carrier expansion.
