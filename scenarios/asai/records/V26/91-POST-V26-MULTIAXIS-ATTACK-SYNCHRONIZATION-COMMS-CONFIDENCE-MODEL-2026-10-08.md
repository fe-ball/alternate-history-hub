# POST-V26 multi-axis attack synchronization / communications-confidence model — 2026-10-08

Status: WORKING-CLOSE / ATTACK-COMMAND MODEL / NO COMBAT OUTCOME PROMOTION

## Authority guard

V26 canon remains 1941-12-07T14:30:00-10:30 HST.

Inputs:
- V26:17 / V26:29 prewar FT+Type91 mixed-attack doctrine;
- V26:63 timing-sensitive suppression model;
- V26:79-88 communications / airborne-command architecture;
- V26:89-90 pre-MO replay map.

Purpose:
model how reliably a preplanned D3A / FT / Type91 multi-axis sequence is actually synchronized under live CAP, AA, maneuver and radio friction.

This file does not assign combat losses, valid releases, hits or damage.

## 1. Synchronization is not one variable

Separate:

### Planned synchronization
What the strike intends before contact:
- axis;
- order;
- relative phase;
- trigger;
- reserve/exploitation condition.

### Achieved synchronization
What actually happens after:
- CAP delay;
- formation breakup;
- target maneuver;
- leader loss;
- radio quality;
- visual acquisition;
- AA;
- fuel/position error.

A mature doctrine can still execute poorly.
An imperfect radio picture can still produce acceptable phase order if the plan is robust.

## 2. Synchronization methods

Use four mechanisms.

### T — time-based
Prebriefed clock / elapsed-time sequence.

Strength:
- works under radio failure.

Weakness:
- becomes stale if one package is delayed or target geometry changes.

### R — radio-cued
Leader reports:
- contact;
- attack commencing;
- release;
- abort;
- delayed;
- shift axis.

Strength:
- allows live correction.

Weakness:
- depends on COM state, channel load and acknowledgement.

### V — visual-cued
Packages use visible events:
- D3A dive commencement;
- FT smoke/fire effect;
- target turn;
- AA concentration;
- torpedo-combing maneuver.

Strength:
- independent of radio after visual contact.

Weakness:
- smoke/cloud/aspect can cause ambiguity;
- visual cue arrives too late for some mother-aircraft setup decisions.

### E — event-cued
A package waits for a tactical state:
- target begins combing turn;
- screen node is suppressed;
- CAP drawn low;
- carrier commits to evasive heading.

This may be recognized by radio, visually, or both.

The best prewar mixed-attack doctrine combines T + R + V/E rather than trusting one mechanism.

## 3. Communications do not create synchronization from zero

The 1939-40 exercises already provide:
- FT-first;
- Type91-first;
- multi-axis;
- screen-suppression;
- exploitation concepts.

Radio improvement changes:
- how much a delayed package can announce its delay;
- whether another axis can hold / accelerate;
- whether a leader can cancel an obsolete phase;
- whether two separated axes can confirm common target / attack state.

Thus communications reduce execution variance.

They do NOT create the doctrinal idea at Enterprise.

## 4. Synchronization states

### SYNC0 — independent / fragmented
- packages attack on their own local opportunity;
- original multi-axis intent mostly lost;
- no useful live correction.

Possible:
- attack still dangerous;
- but suppression/exploitation ordering may invert or disappear.

### SYNC1 — phase order preserved
- FT-first / Type91-first broad order remains;
- actual spacing/axis relation is poor or inconsistent;
- one package may be early/late.

This is achievable under weak communications if the prebrief is strong.

### SYNC2 — leader-level coordinated
- major packages maintain intended order;
- one delayed axis can report / adjust;
- target-turn / suppression cue can alter follow-on timing;
- broad multi-axis relation survives.

This is the normal desired state for a prepared first-line 1941-42 strike with COM2 / A-CMD2.

### SYNC3 — locally well synchronized
- multiple package leaders have good communication/visual confirmation;
- timing/axis adaptation survives until final setup;
- suppression / maneuver / exploitation sequence is closely matched.

This is temporary and local.
It is not precision missile-era simultaneous time-on-target control.

## 5. Relation to COM and A-CMD

Typical mapping, not a deterministic table:

COM0-1:
- SYNC0-1 common;
- SYNC2 only if prebrief / visual cues happen to align.

COM2:
- SYNC1-2 normal;
- SYNC3 possible briefly.

COM3:
- SYNC2 strong;
- SYNC3 possible if A-CMD also remains high.

A-CMD1:
- package/shotai execution only;
- cross-package synchronization degrades.

A-CMD2:
- two-shotai/type-package coordination usable;
- SYNC2 plausible.

A-CMD3:
- overall strike leader can coordinate several type/package leaders;
- SYNC3 possible before dense merge / final attack.

Leader casualty can produce:
A-CMD3 -> 2 -> 1,
with corresponding synchronization decay.

## 6. Synchronization is phase-specific

Track at least four points.

### S1 — assembly / route
Can packages remain on planned relative geometry en route?

### S2 — target acquisition
Do all relevant leaders have the same target / target-group picture?

### S3 — attack commitment
Can the strike leader/type leaders preserve intended phase order under CAP/AA?

### S4 — final release
Do release windows actually overlap / sequence usefully?

A strike can be:
- SYNC2 at S1-S2;
- degrade to SYNC1 at S3;
- fragment to SYNC0 among some subelements at S4.

Do not assign one synchronization score to the entire sortie.

## 7. Enterprise doctrinal interpretation

Enterprise is NOT the discovery point of mixed-weapon synchronization.

Prewar plan can already specify, for example:
- D3A pressure / fighter engagement;
- FT/HE suppression axis;
- Type91 axis;
- FT/SAP or premium exploitation element.

What Enterprise newly tests:
- whether those package leaders can hold relative phase under F4F CAP;
- whether a delayed B5N group can report and be re-sequenced;
- whether target maneuver creates a usable event cue;
- whether AA suppression occurs early enough to help a later conventional torpedo run;
- whether the overall strike leader can keep the attack coherent after the first merge.

Thus Enterprise is a **synchronization stress test**.

## 8. Suppression timing guard

Retain V26:63:

suppression helps only if:
t_effect < t_follow-on exposure/release.

No retroactive bonus.

If FT/HE hits after Type91 mothers have already completed the dangerous final run:
- it cannot reduce their earlier CAP/AA exposure.

If Type91 induces a turn after the FT element has already committed to its corridor:
- it may not improve that FT geometry.

Sequence must be physically ordered.

## 9. Multi-axis does not mean simultaneous

For many attacks the optimal relation is:
- offset by enough time to force incompatible defensive responses,
not exact same-second arrival.

Therefore model:
- useful overlap window;
- useful sequence window;
- failed separation;
rather than demanding exact simultaneity.

Examples:
- FT/HE may need to lead;
- Type91 may exploit a few moments later;
- D3A may arrive before, during or between to force maneuver/AA attention.

Exact numeric seconds remain an event-level replay variable.

## 10. Failure modes

Must represent:

1. one package delayed by F4F;
2. leader radio call unreadable;
3. acknowledgement missing;
4. target identity mismatch between axes;
5. target turns before all packages are ready;
6. D3A attack begins too early and draws CAP/AA before low group is set;
7. FT suppression arrives too late;
8. Type91 run begins before screen suppression;
9. smoke obscures visual event cue;
10. one type leader killed / separated;
11. channel congestion;
12. package chooses local opportunity instead of waiting;
13. strike leader intentionally abandons synchronization to avoid losing the attack opportunity.

The last case is not incompetence.
Sometimes desynchronizing is rational.

## 11. Communication confidence versus tactical initiative

Do not penalize every break from plan.

A strong airborne leader may deliberately:
- advance one axis;
- delay another;
- redirect suppression-capable FT to a screen node;
- convert a planned FT-first sequence into Type91-first.

The criterion is:
does the change preserve mission intent and improve current geometry?

This is where mature A-CMD matters.

## 12. Attack synchronization and fighter escort

Escort is part of synchronization.

A6M packages can:
- clear one axis first;
- hold high/free cover;
- shift to protect a delayed low-altitude package;
- fail to shift because engaged.

Thus Japanese fighter command affects valid release not only by kills,
but by whether the D3A/B5N/FT axes stay synchronized.

This is a major reason Enterprise must be replayed after V26:79-88.

## 13. Attack synchronization and U.S. defense

U.S. CAP / AA can win by desynchronizing the strike even without destroying many aircraft.

Examples:
- force FT mother aircraft to release late / wrong axis;
- make D3A dive before Type91 is ready;
- split fighter escort from low attack group;
- force the strike leader to choose between waiting and losing opportunity.

Therefore:
**desynchronization is a defensive effect separate from aircraft destruction.**

Track:
- killed;
- damaged;
- aborted;
- delayed;
- displaced;
- target-lost;
- released but wrong phase.

## 14. Planning bands for early-war Japanese execution

Do not hard-code one success rate.

Prewar exercises / first-line crews justify:
- pre-contact SYNC2 as a plausible planning center;
- SYNC3 possible during favorable approach;
- CAP/AA commonly degrade some axes to SYNC1;
- SYNC0 remains possible after leader loss / severe breakup.

Enterprise replay should sample / adjudicate this progression rather than assume perfect or zero synchronization.

## 15. Force Z and later battles

Force Z:
- uses Enterprise AAR to refine timing/communication procedures;
- does not discover separated attack concept.

Wake/Saratoga:
- benefits from Enterprise synchronization data;
- may tighten event cues and leader handoffs.

Indian Ocean / Yorktown:
- by then the Navy has multiple combat examples, so planned synchronization should be more robust;
- enemy adaptation also improves.

Thus combat learning should change:
- execution confidence;
- preferred timing windows;
- abort/convert rules;
not the existence of mixed doctrine itself.

## 16. Current next

Enterprise replay must resolve:

1. prebriefed attack architecture;
2. A6M escort package assignment;
3. F4F disruption by axis;
4. COM / A-CMD state;
5. SYNC state at S1-S4;
6. delayed/displaced/aborted attack-aircraft counts;
7. only then D3A / Type91 / FT valid releases;
8. stop before hits.
