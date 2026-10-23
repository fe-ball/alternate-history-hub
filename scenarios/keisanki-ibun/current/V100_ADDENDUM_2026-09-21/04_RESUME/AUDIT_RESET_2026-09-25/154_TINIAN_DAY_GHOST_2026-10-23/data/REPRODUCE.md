# Reproduction and integrity check — Tinian day-only ghost archive

**WORKING conditional arithmetic, NOT CANON.** Canonical clock: **1944-06-16 14:15**. This test does not establish new ship sinkings, casualties, or Japanese cargo arrivals.

## Run from a GitHub checkout

Requires Python 3.10 or later, standard library only. From repository root execute:

    python3 scenarios/keisanki-ibun/current/V100_ADDENDUM_2026-09-21/04_RESUME/AUDIT_RESET_2026-09-25/154_TINIAN_DAY_GHOST_2026-10-23/data/reproduce_all.py

The runner creates a temporary directory; it does not change tracked files. It runs all four archived models for 15 June, 16–20 June, 16–24 June, and 25 June–6 July. Legacy model scripts use an absolute output location, so the runner changes that path **in temporary source copies only**. It creates the compatibility ZIP containing the newly generated 16–24 assumptions that the later model expects, then compares all **12 generated CSVs / 2,764 data rows** to the committed tables with numerical tolerance 1e-9.

## Input and output fidelity

All six later Python and JSON sources previously missing from the first integration commit now reside alongside the data. The three JSONs document diagnostic assumptions and/or generated input summaries; **these are not verified wartime shell stocks, accurate historical aiming rates, or independently verified US target positions**. The underlying scenario controls are in the scripts.

The earliest archival copy of tinian_day15_scenarios.csv was accidentally saved with a spreadsheet parser wrapper, an extra 'index' column and numerical formatting differences. It has been repaired to standard machine-readable CSV with three data rows and the original field layout. Re-execution verifies numerical equality at 1e-9 tolerance; do not interpret the local pre-repair SHA-256 in the manifest as the repaired GitHub blob hash.

The other 11 CSV source tables were verified byte-identical to their locally regenerated originals in the isolated check. Reproduction confirms arithmetic consistency, **not battle-outcome realism or historical ship damage**. A (same 15 June physical guns as B, weaker resilience/return-to-fire) is a deliberately simplified comparison, **not a restored full prior-branch baseline**.

## Simulation boundaries

Phase 1: Tinian Japanese artillery survival, readiness, repairs and ammunition roll forward; US hulls, men and unloading are affected **within each day** but additional losses reset at the next dawn to that day's pre-existing branch schedule. No extra continuing US loss or autonomous operational reprioritization is allowed. Phase 2 US cumulative losses and phase 3 bilateral adaptive decisions have **not been run**. Saipan's existing ground artillery/counter-fire and aviation audit remain intact.

Interpret fractional rounds, guns and mission-minutes as hypothetical expectations. 'UNDETERMINED' and 'NOT ESTABLISHED' do not mean zero. Refer to [archive README](../README.md), [numeric generations](../03_NUMERIC_RESULTS_AND_SUPERSESSION.md), [manifest](../06_DATA_MANIFEST_AND_INTEGRITY.md) and [latest entry 155](../../155_NEXT_CHAT_TINIAN_DAY_GHOST_POST_ARCHIVE_AUDIT_2026-10-23_v001.md).
