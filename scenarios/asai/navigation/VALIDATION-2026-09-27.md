# ASAI navigation repair — 2026-09-27

Scope: navigation and source placement only; no canon promotion or combat-clock advance.
Verified source commit: `7bfc1ba85795e2b0a715e19aab9360098602330d`.

## Change

Current history is V24 China-war continuation → V25 → V26 → post-V26 working, not V21/V22B/V23 China peace and not keisanki-ibun.

The active manifest separates canonical clock, campaign working close, replay-local/forecast dates and discussion frontier. The next gate is tied to V26:11 `at3_next_gate`, not the older Wake or AT-3-reaudit next gates.

V24/V25/V26/essence original trees are retained under records. V21/V22B/V23 are retained under archive/non-active-history. Old entrypoints and router documents are retained as source objects. Legacy URLs return navigation-only notices; 69 original document paths plus seven directory README notices are covered. Original source statuses are untouched.

## Validation

- 379 structural/routing checks passed in a connector-tree-index-backed local test.
- 27 new navigation links resolved.
- All 12 V26 source files are registered with their original blob SHAs.
- 69 legacy source/entrypoint paths have a preserved original and a navigation notice.
- Start prompt: 1000 Unicode characters including URL, internal newlines and final newline.
- Negative controls detected stale next gate, unregistered checkpoint and missing legacy notice.
- Locally computed active tree matches the created GitHub object `004a375b323c06639261ade19b0b20293a2ce86d`.
- Locally computed current tree matches the created GitHub object `92c6baa732d7fb8135298ac84bb21da03b51cfe7`.
- Relocated historical trees, current/technical and import reuse their original Git object IDs. Source content is not rewritten.

Run `python scenarios/asai/navigation/validate_active_axis.py` in a repository checkout. Use `--verify-migration` when verifying this migration snapshot. Subsequent legitimate source updates require manifest/view synchronization, not changing archived history to pass a test.

## Limits

This validates navigation, file inventory and retained Git objects. It does not certify historical or engineering calculations. Links/code-span references inside frozen historical records are not rewritten; use SOURCE-ROUTES.json and their original scenario-root context. GitHub cannot remove copies already held in Library, earlier chats or external caches; those must be matched to the active scenario and source identity before use. No CI success or external Library cleanup is claimed.
