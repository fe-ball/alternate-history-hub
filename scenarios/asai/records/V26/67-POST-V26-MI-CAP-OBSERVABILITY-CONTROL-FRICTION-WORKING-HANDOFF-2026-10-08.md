# POST-V26 MI CAP observability / control-friction correction WORKING handoff — 2026-10-08

Status: WORKING-CLOSE / MODEL-CORRECTION / NO COMBAT OUTCOME PROMOTION

## Authority guard

V26 remains canonical at 1941-12-07 14:30 HST.

Inputs:
- V26:25 limited Type21-line air-warning / coarse CAP vectoring;
- V26:59 heterogeneous-CAP model;
- V26:61 Gaifu role cards;
- V26:65 Gaifu technical grounding.

This file corrects an overly clean reading of "Gaifu outer / A6M inner" CAP layering.

## 1. Two different states must be tracked

### Physical / true state
The analyst may track:
- actual A6M / Gaifu position;
- altitude;
- energy;
- fuel;
- target assignment;
- re-engagement delay.

### Actor-known / controller state
Japanese shipboard control knows only a degraded estimate:
- last reported fighter group position;
- coarse bearing / sector;
- approximate altitude band when available;
- assigned mission;
- last radio report;
- expected fuel state;
- whether contact is believed active.

These are not the same.

## 2. Why Japanese control is only marginally sufficient

Type21-line air warning at MI provides:
- coarse early warning;
- bearing cue;
- rough timing;
- useful plotting assistance.

It does NOT provide:
- reliable precision altitude;
- continuous individual-fighter tracking;
- modern IFF picture;
- mature U.S./RAF-style GCI;
- data-link vectoring.

A6M/Gaifu radio reliability is improved relative to historical-stock Japanese execution, but:
- voice reporting remains intermittent;
- combat breaks formation;
- fighters may be below radio line / masked / busy;
- exact fuel/energy is not visible to the controller;
- different performance envelopes increase estimation error.

## 3. Mixed-type CAP therefore has both benefit and control cost

The real benefit:
- different aircraft can be assigned different tasks before contact;
- Gaifu can be preferentially launched/vectoring for time-critical or higher intercepts;
- A6M can be retained for inner/persistent work.

But after contact:
- the controller cannot continuously keep a clean "Gaifu layer" and "A6M layer" picture;
- elements cross altitude/sector boundaries;
- returning/re-engaging fighters may be mis-estimated;
- a requested handoff may arrive late or to the wrong element.

Thus "layering" is doctrinal intent, not a modern controlled air picture.

## 4. Controller-confidence states

Use:

### C0 — lost / no useful picture
- visual/radio reports absent;
- controller cannot meaningfully vector a specific element.

### C1 — coarse sector knowledge
- knows a fighter element is in a broad sector;
- altitude/energy/fuel uncertain.

### C2 — usable group picture
- recent report gives approximate sector/altitude/task;
- enough to issue a plausible vector.

### C3 — temporarily good tactical picture
- recent radar cue + radio report + visual/plot agreement;
- still not continuous precision tracking.

C3 is local/temporary, not a fleet-wide persistent state.

## 5. State-estimation error must affect decisions

Examples:
- controller believes Gaifu element remains high/outer, but it is already low-energy after first engagement;
- A6M inner element is ordered toward TBD but is farther away than plotted;
- Gaifu reserve is launched too late because an existing element is thought still available;
- two elements are sent to the same threat while another bearing is thin.

These are normal 1942 control-friction outcomes.

## 6. Implication for G-E / G-B / G-D cards

The cards define **initial allocation intent**, not continuously maintained disposition.

G-B 5 escort / 5 CAP / 1 reserve means:
- five Gaifu are initially allocated to defensive CAP;
- it does not guarantee five Gaifu remain correctly positioned throughout the raid.

Likewise:
- G-D defense-heavy gains more theoretical defensive coverage,
- but also increases mixed-type control burden.

Therefore the marginal benefit of additional Gaifu CAP should flatten when controller confidence is low.

## 7. U.S. identification is also limited

U.S. pilots do not immediately know:
- "this is A7M Gaifu";
- exact speed/climb;
- exact number in the CAP;
- which carrier operates them.

They may report:
- Zero-like fighter;
- new/faster Japanese fighter;
- different silhouette/closing behavior.

Early tactical adaptation is therefore based on observed behavior, not exact intelligence.

## 8. Model rule

For every CAP time slice, maintain both:

TRUE_STATE:
- actual fighter type/position/energy/fuel.

CONTROLLER_ESTIMATE:
- sector;
- altitude band;
- availability confidence;
- last report age.

Orders are generated from CONTROLLER_ESTIMATE.
Combat resolution uses TRUE_STATE.

This prevents analyst omniscience from becoming Japanese command capability.

## 9. Current consequence

V26:59-66 remain valid as model structure, but any language implying clean persistent outer/middle/inner layers must be read as:
- intended allocation;
- only imperfectly maintained in combat.

No air-combat result is changed yet.

Next:
run G-E/G-B/G-D against the U.S. arrival sequence with controller-confidence / stale-track friction included.
