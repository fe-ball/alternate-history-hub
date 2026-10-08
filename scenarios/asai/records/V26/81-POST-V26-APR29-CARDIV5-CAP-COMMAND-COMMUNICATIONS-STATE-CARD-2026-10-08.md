# POST-V26 Apr29 CarDiv5 CAP command / communications state card — 2026-10-08

Status: WORKING-CLOSE / COMBAT-MODEL INPUT / NO HIT OR LOSS PROMOTION

## Authority guard

V26 canon remains 1941-12-07T14:30:00-10:30 HST.

Inputs:
- V26:71-76 A6M-only CarDiv5 force-state cards;
- V26:79-80 communications-to-doctrine maturation;
- V26:25 Type21 / AA/FCS state;
- V26:67 TRUE_STATE vs CONTROLLER_ESTIMATE.

This file defines Apr29 defensive command state.
It does not resolve aircraft losses, valid releases, hits or carrier damage.

## 1. Command architecture

Do not model a modern fighter-direction center.

Use a distributed carrier-division system:

### Radar / lookout node
One CarDiv5 carrier has the Type21-line air-warning set central.

Inputs:
- Type21 broad bearing / approach timing;
- visual lookouts;
- search-aircraft / screen reports;
- other ship reports.

### Plot / air-group control function
The radar-fitted carrier's operations/air staff maintains:
- broad threat bearing;
- estimated approach time;
- known CAP group task/state;
- ready fighter state.

This is a function, not a claim of a U.S.-style formal Fighter Direction Officer school.

### Local carrier control
Each carrier retains:
- deck launch/recovery control;
- local ready-fighter decision;
- local CAP recovery/fuel state;
- local visual/AA information.

### CAP leadership
Airborne fighters are controlled primarily through:
- shotai/chutai leaders;
- prebriefed sector/altitude/task;
- short voice reports.

The ship does not attempt to vector every pilot individually.

## 2. Radio fit / usability

First-line CarDiv5 A6M:
- radio fit is treated as standard operational equipment;
- worldline EMI/installation standards make leader-level voice routinely useful when the set is serviceable.

Do NOT assume:
- 100% serviceability;
- clear reception in every attitude/range;
- no combat damage;
- no channel congestion.

Normal pre-contact state:
- COM2 leader-level reliable tactical voice.

Local COM3:
- possible for brief periods with low traffic / good propagation.

COM0/1:
- still possible locally from equipment fault, range, masking, damage or congestion.

## 3. Pre-contact tactical organization

Formal fighter structure remains:
- three-plane shotai;
- nine-plane chutai where available.

For defensive CAP, assignment is by:
- sector;
- altitude band;
- readiness/fuel state.

The exact geometry is not fixed here.

Use four functional states:

### HIGH
- higher CAP / outer approach;
- protects against SBD/high escort;
- costs fuel/energy if maintained too far out.

### MID
- main interception/reinforcement band;
- flexible response.

### LOW
- carrier-local low-altitude / torpedo-defense reserve.

### READY/RELIEF
- deck-ready or recently recovered/refueled;
- launched when threat picture justifies.

These are roles, not permanent clean layers.

## 4. What the controller can know

CONTROLLER_ESTIMATE may contain:

- Shotai A: HIGH, north/east sector, last report recent;
- Shotai B: MID, carrier-local, available;
- Shotai C: engaged / contact high;
- reserve shotai: deck-ready;
- one element: fuel low / returning.

It generally does NOT contain:
- individual aircraft coordinates;
- exact energy;
- exact remaining ammunition;
- exact opponent count after merge.

Leader reports refresh the picture.

Thus the picture can survive longer than a historical-unreliable-radio model, but loses fidelity during dense combat.

## 5. Pre-contact command maturity

Before first merge:

Typical planning state:
- CMD2 normal:
  shotai/chutai task allocation and relief procedure working.

CMD3:
- achievable when:
  - Type21/visual plot is coherent;
  - leaders are reporting;
  - channel load is manageable.

CMD3 means:
- useful group-level sector/task control.

It does NOT mean:
- precision GCI.

## 6. Engagement doctrine

### First contact
Controller/leader attempts to determine:
- high versus low threat;
- approximate strength;
- bearing;
- whether a second element is visible/expected.

### Commitment rule
Do not automatically send every CAP fighter to the first sighted group.

Working doctrine:
- one fighter element engages;
- another may remain uncommitted/high or carrier-local until the threat picture improves;
- deck-ready fighters are launched/held according to the perceived second threat.

This is a procedural hedge learned from years of operations, not future knowledge.

### Target allocation
Leader-level calls may assign:
- fighters/escorts;
- dive bombers;
- low torpedo aircraft;
- stragglers.

They do not guarantee obedience once individual dogfights develop.

## 7. Shotai combat behavior

Within the existing three-plane structure, improved communications support:

- wider combat spacing;
- leader-ordered attack sequence;
- split/reform;
- one aircraft/element maintaining lookout/top cover;
- regroup after a pass;
- call to break off / return / shift target.

The shotai may still break down if:
- leader is lost;
- radio fails;
- multiple targets cross;
- pilot becomes fixated;
- visual separation becomes too large.

No two-plane doctrine is assumed.

## 8. Chutai / multi-shotai behavior

If multiple shotai are available:

Working procedure can support:
- one shotai engaged;
- one covering another altitude/sector;
- one reserve/relief.

The exact 1/1/1 allocation is not mandatory.

Chutai leader or senior CAP leader can:
- call reinforcement;
- hold an element back;
- shift a shotai;
- order reform/return.

This is where worldline communications produce their largest defensive gain.

## 9. Pursuit / discipline

Years of war do not erase Japanese aggressive fighter culture.

Use a discipline state:

### D3 — group discipline intact
- multiple shotai remain on assigned roles;
- controller/leader reports usable.

### D2 — shotai discipline intact
- each shotai still acts coherently;
- higher-level sector plan partly lost.

### D1 — local/visual control
- leader/wingmen act tactically;
- broader defense picture lost.

### D0 — free chase / fragmented
- individual aircraft pursue targets;
- major coverage holes emerge.

Apr29 pre-contact:
- D3 or D2.

After first merge:
- transition downward is possible.

Better radio/procedure reduces the chance/speed of D3->D0 collapse.
It does not prevent it.

## 10. Type21 contribution

Type21 mainly changes:
- when the READY/RELIEF element is launched;
- which broad bearing HIGH/MID CAP shifts toward;
- whether a second element is held for an unresolved threat.

It cannot directly solve:
- enemy altitude;
- exact formation split;
- individual fighter vector.

A visual/leader contact report can add altitude/type information after radar cue.

## 11. AA interaction

Improved fighter communication also reduces some fighter/AA interference by procedure:

Possible prebriefed controls:
- carrier-local minimum altitude / approach lanes;
- break-off / clear-sector calls;
- known AA engagement zones.

But:
- no automated deconfliction;
- close combat can still enter friendly AA arcs;
- ships will fire when survival demands it.

Do not award a clean combined fighter-AA multiplier.

## 12. A14 / A16 / A18 implications

The communication/doctrine gain changes the **marginal value** of defensive fighter count.

A smaller but coordinated CAP may:
- preserve altitude separation better;
- launch reserves more rationally;
- avoid some duplicate chase.

Therefore the difference between:
- 14 defensive-capable fighters,
- 16,
- 18

is not linear.

More fighters still matter.
But coordination can prevent some of the extra aircraft from being wasted on the same target.

This is why all three cards remain sensitivity cases.

## 13. Key failure modes for Apr29 replay

Must sample or represent:

1. late/ambiguous Type21 contact;
2. altitude unknown;
3. contact report misclassifies strength;
4. leader radio failure;
5. channel congestion;
6. one shotai overcommits to F4F;
7. multiple shotai descend after TBD;
8. high SBD group remains weakly covered;
9. reserve launches too late;
10. leader loss causes D3/D2 -> D1 collapse;
11. cross-carrier status lag;
12. returning Japanese strike creates deck/recovery conflict.

These are more important than applying a generic radio bonus.

## 14. Current Apr29 central control reading

Without adjudicating combat:

- CarDiv5 does have a meaningful fighter-control process;
- it is substantially better than historical "mostly visual once airborne";
- it is still far below mature U.S. radar fighter direction;
- the main benefit is preserving group-level tasking and relief long enough to matter;
- the main limitation is loss of altitude/track fidelity and discipline under merge.

## 15. Next gate

Run A14 / A16 / A18 through Apr29 in both directions.

For the Lexington counterstrike:
resolve sequentially:
1. Type21 / visual warning quality;
2. CAP launch state;
3. first fighter contact;
4. COM/CMD/D discipline transitions;
5. F4F engagement;
6. SBD/TBD cohesion and losses;
7. AA interaction;
8. valid-release bands.

Stop before direct hits.
