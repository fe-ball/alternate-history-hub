# POST-V26 MI multistage CAP / attack state model WORKING handoff — 2026-10-08

Status: WORKING-CLOSE / MODEL-DEFINITION / NO COMBAT OUTCOME PROMOTION

## Authority guard

V26 remains canonical at 1941-12-07 14:30 HST.

This file defines the combat state-transition model that must be used before any new MI air-combat loss, valid-release, hit, or damage result is promoted.

It supersedes the use of simple homogeneous-CAP or one-pass attack assumptions.

## 1. Current robust replay input

Carry forward as robust working inputs:
- V26:43-44 force state / OOB;
- V26:45-46 search and first-contact geometry;
- V26:47-48 launch packages and launch timing.

Re-open as model outputs:
- V26:49-50 air-combat losses;
- V26:49-50 valid-release counts;
- V26:51-56 all downstream allocations, hits and damage.

Therefore the authoritative combat replay is now at:
**attack approach / defensive engagement before final CAP-AA attrition and valid-release closure.**

V26:49-50 are retained only as a numerical baseline/sample for comparison.

## 2. Core principle

Do not model either side as:

CAP aircraft count x generic fighter coefficient x generic AA coefficient.

Instead each attack is a sequence of state changes.

For every time slice / attack element, update:
1. warning quality;
2. CAP availability by type / altitude / energy / fuel;
3. CAP vectoring latency;
4. attacker cohesion;
5. escort engagement;
6. local AA/director state;
7. formation geometry;
8. target maneuver;
9. mother-aircraft release setup;
10. weapon release;
11. terminal weapon behavior;
12. only then hit / miss / damage.

## 3. Japanese CAP must be heterogeneous

### A6M2 role

Worldline A6M2 retains the V26 improvements:
- better radio reliability / formation control;
- better QC and boresight repeatability;
- improved reacceleration / section integrity relative to historical-stock assumption;
- no blanket armor/self-sealing assumption.

Natural CAP roles:
- inner and middle CAP;
- long-duration patrol;
- low/medium-altitude interception;
- repeated short-range re-engagement;
- torpedo-bomber interception;
- escort combat where maneuverability and endurance matter.

### Gaifu role

Gaifu is not modeled as "A6M with a higher kill multiplier."

Its principal system-level gains are:
- expands the reachable interception envelope in distance / altitude / time;
- allows faster reaction to a late radar/visual cue;
- permits an outer/high-energy intercept layer without spending every A6M there;
- can re-position between threat sectors faster;
- can disengage/re-enter differently from A6M;
- creates a second performance envelope the attacker must account for.

Do not assume:
- perfect altitude performance;
- perfect radar vectoring;
- invulnerability;
- that every Gaifu sortie converts to a kill.

## 4. Heterogeneous-CAP gain categories

Track separately.

### G1 — reach / time-to-intercept gain

Question:
Does the fighter reach the attack group before:
- escort separation;
- dive initiation;
- torpedo setup;
- FT setup/release?

Gaifu can create an intercept opportunity that A6M may miss when warning is late or the sector is distant.

This gain depends strongly on warning quality.

No warning -> little system gain.
Good early cue -> potentially large gain.

### G2 — mission-specialization gain

Mixed CAP allows:
- Gaifu outer/high-energy intercept;
- A6M inner/low-altitude and persistence work.

Benefit:
A6M aircraft are not consumed in every high-speed chase.

This changes the number and energy state of fighters available for later attack elements.

### G3 — re-engagement / sector-shift gain

After the first pass, ask:
- how long until the fighter can make a second useful attack?
- can it shift to another bearing?
- does it still have altitude/energy?
- is fuel/endurance becoming limiting?

This affects later waves more than the first contact.

### G4 — adversary uncertainty gain

A U.S. formation cannot assume every Japanese fighter has one performance envelope.

Possible consequences:
- escort commits early against the faster threat;
- SBD/TBD formations alter altitude/speed discipline;
- evasive behavior costs cohesion;
- pilots misjudge safe disengagement margins.

This is a cohesion/decision effect, not a free kill bonus.

### G5 — force-preservation gain

A specialized fighter may reduce the need to commit more total fighters to one sector.

Potential benefit:
- preserve fighters for later waves;
- reduce CAP exhaustion;
- maintain low-altitude torpedo defense while another element handles high threats.

Again this is conditional on command/vectoring quality.

## 5. Heterogeneous-CAP costs

Track explicitly.

### C1 — command / vectoring friction
Type21-line radar provides coarse warning and bearing, not mature GCI.

Mixed types increase the burden of:
- assigning altitude/bearing;
- keeping track of which group has which speed/endurance;
- deconflicting interceptions.

### C2 — formation incompatibility
A6M and Gaifu should not be assumed to maneuver as one perfectly homogeneous section.

Mixed patrols may:
- separate under acceleration;
- require looser rendezvous;
- suffer communication delay.

### C3 — deck / maintenance burden
Gaifu creates:
- distinct spares;
- distinct maintenance knowledge;
- qualification burden;
- deck-spotting / launch-cycle differences.

At MI scale this is manageable because Gaifu is concentrated on Zuikaku, but it is not zero.

### C4 — pilot qualification
Only qualified pilots can exploit the new envelope.

Do not apply full aircraft performance to replacement pilots automatically.

## 6. Japanese CAP state vector

At any time slice t, track:

- N_A6M_outer(t)
- N_A6M_inner(t)
- N_Gaifu_outer(t)
- N_Gaifu_inner(t)
- altitude band by element
- energy state: HIGH / MED / LOW
- fuel/endurance state
- location/sector
- current target assignment
- re-engagement delay
- radio/vector confidence
- pilot qualification quality band

Do not collapse these into one CAP number until after the encounter.

## 7. Defensive warning state

Japanese warning is a chain:

picket / visual / Type21 cue
-> plotting
-> bearing estimate
-> altitude uncertainty
-> CAP order
-> fighter transit
-> visual acquisition.

Track warning quality as:
- W0 no useful early warning;
- W1 bearing cue only;
- W2 useful bearing + timing window;
- W3 useful moving threat picture but still no mature altitude/GCI precision.

For MI Japanese carriers, W1-W2 is common and W3 is possible locally; mature U.S.-style GCI is not granted.

Gaifu gains are larger when moving from W1 to W2 than when moving from W0 to W1.

## 8. U.S. strike-wave state changes

Do not model all 169 U.S. aircraft as one arrival.

Track separate arrival/attack elements:
- Enterprise elements;
- Saratoga elements;
- Hornet elements;
- late/mis-vector SBD tail;
- TBD groups;
- fighter escorts.

Within each:
- arrival time band;
- altitude;
- cohesion;
- target-cell discovery;
- escort state;
- whether earlier U.S. elements pulled CAP down or away;
- whether Japanese fighters are recovering energy.

This permits:
- one wave to worsen conditions for the next;
- or one wave to consume CAP and improve conditions for the next;
- without forcing the historical exact sequence.

## 9. Japanese multi-stage anti-carrier attack model

Japanese attack is not one simultaneous packet.

For each carrier cell, construct attack elements from:
- fighter escort;
- D3A;
- B5N Type91;
- B5N/B6N FT;
- FT family / warhead.

Each element chooses a target class based on current state.

Possible targets:
- carrier;
- AA cruiser / major director node;
- heavy cruiser screen;
- selected destroyer only if tactically valuable;
- no target / abort if geometry collapses.

## 10. FT target-allocation decision rule

Do not pre-fix "X FT to screen."

A screen/AA target is rational only if:

expected downstream gain from degrading that node
>
opportunity cost of not firing that FT at the carrier
+
risk that the defender adapts / changes geometry unfavorably.

Relevant downstream gain channels:
- lower heavy-AA fire density on a specific bearing;
- director disruption;
- reduced local communications;
- forced screen maneuver;
- corridor opening for Type91;
- reduced pull-out fire against D3A;
- altered carrier turn.

Relevant costs:
- fewer direct carrier weapons;
- screen target may evade;
- suppression may occur too late;
- carrier may gain maneuver freedom;
- CAP may compensate.

## 11. Multi-stage attack phase types

Do not require a fixed order.
Each carrier cell may choose among:

### S — suppression opening
FT/HE or FT-GR/HE against a high-value AA/screen node.

### T — torpedo forcing
Type91 threat to force combing / side-aspect change.

### D — dive pressure
D3A attack forcing turn / AA elevation / CAP displacement.

### F — FT carrier attack
standard FT / FT-IR against the carrier.

### X — exploitation
SAP / IR-SAP against an already constrained/degraded carrier.

Examples of valid sequences:
- S -> T -> F/D
- T -> F -> D
- D -> T -> F
- F -> T -> D
- parallel D + T with later X

The model must choose based on local state, not doctrine slogan alone.

## 12. Defender state vector for multi-stage attack

For each U.S. task group and each major bearing, track:

- CAP fighters available;
- CAP altitude / energy / fuel;
- AA director state;
- heavy-AA effective mounts;
- medium/light-AA local state;
- screen geometry;
- carrier course/speed;
- current evasive turn;
- smoke;
- communications / command state;
- prior damage;
- attack-bearing congestion;
- friendly-ship masking;
- target identity confidence.

Each phase updates only the affected sectors/nodes.
No blanket fleet-wide AA percentage reduction.

## 13. Interaction examples that must be possible

### Example A
FT/HE hits an AA node.
Later Type91 axis gains a cleaner approach.
But carrier turns away and makes FT-IR geometry worse.

### Example B
Type91 comes first.
Carrier combs torpedoes.
That exposes broadside/side aspect to FT or changes D3A dive geometry.

### Example C
D3A attack pulls CAP upward.
B5N/FT mothers reach release setup more easily.

### Example D
Gaifu intercepts the leading U.S. SBD group early.
A6M remains available for TBD.
Later Hornet SBD arrives when Gaifu is low-energy / re-positioning.

### Example E
Mixed CAP command friction causes a Gaifu/A6M handoff failure.
The theoretical second-type advantage is not fully realized.

## 14. Outputs to derive before hits

For the U.S. strike against Japan:
- losses / aborts by element;
- Japanese fighter losses / energy state;
- revised SBD valid dives by target cell;
- revised TBD valid runs by target cell.

For the Japanese strike against U.S.:
- losses / aborts by element;
- target allocation by weapon family;
- screen/AA effects if any;
- revised D3A valid dives;
- revised Type91 valid runs;
- revised FT valid releases;
- carrier-directed versus support-target FT split.

Only after these are derived should hit adjudication begin.

## 15. Status of V26:49-50 numbers

V26:49-50 numerical outputs:
- U.S. SBD70;
- U.S. TBD17;
- Japanese D3A34;
- Japanese Type9116;
- Japanese FT22;
and associated air-combat losses

are now:
**PROVISIONAL COMPARISON BASELINES, not closed combat results.**

The model may converge near them.
It may also move materially away from them.

## 16. Next gate

Instantiate the model in order:

1. Japanese defense versus Midway land-based packets;
2. Japanese heterogeneous CAP versus U.S. carrier-strike waves;
3. U.S. CAP/AA versus Japanese Cell 1;
4. update TF16 state;
5. U.S. CAP/AA versus Cell 2 under updated state;
6. update TF16 state again;
7. U.S. CAP/AA versus Cell 3 / Saratoga group;
8. derive revised valid-release ledgers;
9. stop before hits.
