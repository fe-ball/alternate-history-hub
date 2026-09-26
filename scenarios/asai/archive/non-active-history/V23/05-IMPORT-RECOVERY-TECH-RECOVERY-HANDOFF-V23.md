# V23 HANDOFF — SOURCE IMPORT REPAIR / TECHNOLOGY RECOVERY — 2026-09-20

**Status:** CURRENT NEXT-CHAT HANDOFF  
**Authority:** V23 unchanged  
**Canonical history clock:** 1946-06-30T24:00 class  
**Active work clock:** retro-audit 1939–1941  
**Next substantive target:** repair partial-import-era damage if any, recover technical state, then close 1941-05 aviation/war-continuation baseline

## 1. Exact V22B source package is now fully available

The user re-imported the original V22B handoff package into GitHub.

Verified source locations:

- original archive: `scenarios/asai/import/archives/ASAI-WORLDLINE-HANDOFF-2026-09-19-FULL-V22B-CHINA-PEACE-GERMAN-JET-BRANCH-GATE(1).zip`;
- byte-exact expanded mirror: `scenarios/asai/import/source-v22b-full-exact/`.

Verification against the conversation-uploaded ZIP:

- ZIP size: **20,996,153 bytes**;
- SHA-256: **4bea918064d011331dfe5e0ba3ceed3994e59cc4d2187e84495e59719bc63307**;
- archive Git blob: **c51075904e597ef5b37fb3917f2dd6b64e91f8e2** — matches the Git blob hash computed from the uploaded ZIP bytes;
- ZIP file entries: **1,122 files** plus 106 directory entries;
- exact GitHub mirror: **1,122 blobs**;
- expanded payload: **27,856,505 bytes** in both ZIP and GitHub mirror;
- sorted `relative-path + git-blob-SHA + size` fingerprint: **3f8dbee80b9473f3** on both sides;
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/`: **134 / 134 files** present.

Treat the exact mirror as the recovery source for what the V22B package actually contained.

## 2. Old partial mirror warning

`scenarios/asai/import/source-v22b-full/` is the earlier partial/reconstructed import.

It contains only a small subset and some files differ materially from the exact source. It is retained as provenance only.

**Do not use it for source reconstruction when an exact counterpart exists.**

Do not confuse this rule with scenario authority: exact source presence does not make every old file current CANON. Supersession and V23/V22B/V21 precedence still control.

## 3. Current-authority corruption check

A first integrity comparison was performed between `scenarios/asai/current/` and the exact V22B source.

Result before cleanup:

- current blobs: 49;
- current files with direct V22B source counterparts: 42;
- already byte-identical: 38;
- four one-byte differences: trailing newline/whitespace only;
- V23/new files without V22B counterparts: 7.

The four whitespace-only drifts are restored to their exact source blobs in the recovery commit.

No substantive text corruption has been found in the inherited V21/V22B and main technical-parent files currently promoted under `current/`.

Therefore the main risk is **not corrupted current canon**. The main risk is conversational reasoning performed while the full source was unavailable.

## 4. Conversation-level conclusions to distrust until replayed

During the partial-import period, the assistant incorrectly concluded that important normal-aircraft ledgers were missing and began rebuilding several historical aircraft from public historical baselines.

That approach is superseded.

Re-audit any working conclusion depending on:

- Zero / Hayabusa / Shoki / Ki-46 development timing or performance;
- piston exhaust adoption and its maturity;
- ordinary Army/Navy bomber/attack/recon aircraft state;
- 1940–41 production and service fielding;
- 1941-05 front-line aviation strength;
- Indochina aviation capacity;
- carrier-air-group availability and the value/timing of converted-carrier expansion.

Do not treat those conversation-level estimates as persisted decisions unless an explicit V23/V22B/current file independently closes them.

## 5. Recovered technical anchors already identified

Examples now confirmed in the exact package:

- A6M1 / 12-Shi first-flight window: **1939-03-24 to 26**;
- A6M from first flight: roughly 900 hp-class Z-900N path, **three-blade constant-speed propeller**, thrust-exhaust design-origin;
- piston exhaust has explicit EX0–EX3 state accounting; A6M2 worldline uses EX2/EX3 design integration;
- Ki-43 production configuration evaluates EX2/EX3 rather than inheriting historical early exhaust state;
- Ki-46-II uses high-priority EX3 treatment;
- E6 Twin normal-unit eligibility: **1940-04-01**;
- E6 Single normal-unit eligibility: **1940-05-01**;
- A6M China operational trial gate: **1940-07-01**; major combat anchor **1940-09-13**;
- 1940 E5/E6 transition ledger contains monthly factory-acceptance planning and year-end extant/serviceable centers;
- 1941 fixed-wing procurement closes annual factory-acceptance planning at E6 Twin **216–240, center 228**, E6 Single **180–210, center 195**, while explicitly separating factory accepted from service/unit/OOB state.

These are anchors for recovery, not permission to interpolate 1941-05 counts by simple fractions.

## 6. Next-chat work order

### A. Repair audit
1. Use exact-source manifests and supersession files.
2. Identify any persisted/current value that was actually damaged by the incomplete import.
3. Restore only genuine source/import corruption.
4. Keep later V23 decisions intact unless causal contradiction is demonstrated.

### B. Technology recovery
Recover all materially relevant 1939–41 state from the exact package before inventing values:
- piston engines and supercharging;
- propellers;
- exhaust;
- cooling;
- materials/CFRP;
- computation/test/QC;
- fire-control/bombing/photo workflow;
- E5/E6/E7;
- conventional historical-named aircraft;
- production facilities/capacity;
- maintenance/training/serviceability;
- Navy aircraft/torpedo/carrier interfaces;
- relevant ground/naval technologies where they constrain China/Indochina operations.

### C. 1941-05 ledger
Reconstruct month-by-month or gate-by-gate from 1940-12-31 through 1941-05-31.

Never collapse:
- produced;
- accepted;
- extant;
- service released;
- unit assigned;
- serviceable;
- forward;
- immediately operational.

### D. Return to strategy
Only after C, resume:
- continuation of the China war after failed peace;
- holdings and operational choices;
- French Indochina advance;
- converted-carrier expansion and air-group consequences.

## 7. User direction

The user explicitly warned that historical-named aircraft have extensive worldline changes in **appearance date, production quantity and performance**, and that early mature thrust exhaust affects many types.

The user wants the aircraft/technical state checked **one item at a time while proceeding as far as possible in one pass**, not reconstructed from historical specifications by default.

Do not ask for information already present in the exact source package. Retrieve it first.
