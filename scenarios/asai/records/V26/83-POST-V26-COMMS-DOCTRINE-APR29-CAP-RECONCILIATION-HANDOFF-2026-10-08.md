# POST-V26 communications-doctrine / Apr29 CAP reconciliation handoff — 2026-10-08

Status: WORKING-CLOSE / RECONCILIATION / NO COMBAT OUTCOME PROMOTION

## Authority guard

V26 canon remains 1941-12-07T14:30:00-10:30 HST.

This file reconciles the two parallel V26:79-82 record pairs created during the communications-doctrine re-audit.

Use this file as the current navigation authority for:
- 1932-42 communication-to-doctrine diffusion;
- Apr29 CarDiv5 A6M-only CAP command architecture;
- escort/defense sensitivity cards.

No Apr29 combat result is fixed here.

## 1. Reconciled historical logic

The correct causal chain is:

GT quiet-radio comparison
-> EMI source isolation
-> shielding/bonding/filtering/connector acceptance
-> more usable airborne voice
-> procedures that assume voice can work
-> China-war combat feedback
-> training standardization
-> leader-level fighter tasking
-> base/carrier group-level CAP control
-> Type21 plugs into an already-existing control loop.

Reject both extremes:
- "better radio instantly creates modern doctrine";
- "better radio changes nothing doctrinally through spring 1942."

## 2. Timeline — current center

### 1932Q4-1934
Technical phase:
- quiet GT-aircraft radio comparison;
- EMI source isolation;
- radio-noise acceptance;
- shielding/bonding/filtering.

Main layer: hardware usability.

### 1935-1936
Procedure begins:
- radio checks / acknowledgement;
- lost-comms fallback;
- route / rendezvous / simple report practice;
- naval/recon/bomber priority-aircraft spread.

Main layer: hardware -> procedure.

### 1937
Continuous China combat makes procedure operationally valuable:
- join-up;
- contact;
- bearing / altitude-band;
- recall;
- rejoin;
- diversion / recovery;
- fuel / trouble reporting.

The bottleneck becomes procedure/organization as well as hardware.

### 1938
Tactical employment evolves inside existing organization:
- looser spacing;
- detach/rejoin;
- altitude separation;
- escort reassignment;
- attack / cover / reserve role assignment;
- fewer redundant pursuits when leader control survives.

Three-plane shotai remains.

### 1939
Training and control mature:
- leader-centered radio discipline;
- short standard reports;
- patrol sector / altitude intent;
- ready/reserve concepts;
- warning-to-launch and relief procedures;
- after-action correlation of warning/launch/contact failures.

Army and Navy still develop separately.

### 1940
A6M combat in China enters an already-radio-assisted culture:
- multi-shotai assembly and rejoin;
- cover/reserve assignment;
- split/reform;
- sequential attack ordering;
- long-range escort fuel/status reporting.

No finger-four / universal two-plane reform.

### late 1940-1941
Carrier concentration and fleet exercises interact with the communication culture:
- common mission frequencies/callsigns;
- carrier-division/tactical-cell CAP sector and altitude intent;
- CAP leader / senior buntaicho task allocation;
- deck-ready / relief accounting;
- ship/base plot -> CAP leader broad vector.

### Dec1941-Apr1942
Combat against U.S./British forces accelerates procedure:
- raid bearing / altitude-band reports;
- high versus low threat calls;
- reserve/high-cover retention;
- chase-limit / rejoin discipline;
- fuel/relief reporting;
- after-action changes in attack geometry.

Type21 adds sensor input but does not create the doctrine.

## 3. Spring-1942 fighter organization

Retain:
- three-plane shotai;
- nine-plane chutai class;
- aggressive pilot autonomy once engaged.

Add as normal first-line procedure:
- leader-level tactical voice;
- split/reform calls;
- attack/support/lookout roles;
- cover/reserve assignment;
- group-level sector/altitude/relief control;
- broad retask by carrier/base controller.

Do not add:
- individual radar vectoring;
- precise altitude radar;
- continuous own-fighter tracking;
- IFF;
- modern CIC;
- mature U.S./RAF-style GCI.

## 4. State model

### Communication quality
- COM0: no useful voice.
- COM1: intermittent/simple calls.
- COM2: reliable leader-level tactical voice.
- COM3: locally good tactical voice for a limited period.

First-line A6M planning center when serviceable:
- COM2.

### Command maturity
- CMD0: visual/individual.
- CMD1: shotai-leader control.
- CMD2: multiple-shotai/chutai task allocation.
- CMD3: useful carrier/base group-level sector/task picture and broad retask.

Spring-1942 first-line carrier aviation:
- CMD2 normal;
- CMD3 possible before/early in contact with good warning/reporting;
- dense combat degrades toward CMD1/2.

### Discipline
- D3: group roles preserved.
- D2: shotai cohesion preserved, broader plan partly lost.
- D1: local visual/leader control only.
- D0: fragmented/free chase.

Radio/procedure slows D3->D0 collapse but does not prevent it.

## 5. Actor knowledge

Retain TRUE_STATE vs CONTROLLER_ESTIMATE.

Controller can plausibly know:
- shotai identity;
- broad sector;
- approximate altitude/task;
- engaged/available;
- last report;
- expected fuel state.

Controller does not know:
- exact individual positions;
- exact energy/ammunition;
- continuous target geometry.

Leader reports can refresh stale estimates.

## 6. Apr29 CarDiv5 command architecture

Use:

Type21 / lookouts / screen reports
-> ship/cell plot
-> CAP leader / senior fighter leader
-> shotai leaders.

One carrier's Type21 set provides:
- coarse bearing;
- rough timing/range class.

Visual/leader reports add:
- altitude class;
- threat type/strength estimate.

Each carrier retains local:
- deck readiness;
- launch/recovery;
- fuel/relief state.

No single omniscient Kido Butai fighter director exists.

## 7. Apr29 A6M pool

Retain:
- A6M serviceable 30-34;
- center 32;
- ready ~29-32 class;
- Gaifu combat-present 0 central.

Pilot cadre is not an acute central limiter.

## 8. Escort-card reconciliation

V26:75-76 used:
- A14 / A16 / A18.

These are superseded as tactical cards because the working fighter combat element remains the three-plane shotai.

Use instead:

### A12 — defense-heavy
- escort 12 = 4 shotai;
- D3A27 + B5N27;
- total strike66;
- ~20 serviceable A6M remain at pool32.

### A15 — balanced reference
- escort15 = 5 shotai;
- total strike69;
- ~17 serviceable A6M remain at pool32.

Possible five-shotai intent:
- one high/free cover;
- two primarily D3A-axis support;
- two primarily B5N/FT-Type91-axis support;
with radio reassignment.

### A18 — offense-heavy
- escort18 = 6 shotai;
- total strike72;
- ~14 serviceable A6M remain at pool32.

A15 is the current reference planning card.
A12/A18 remain sensitivity cases.

## 9. Defensive CAP under A15

~17 serviceable fighters remaining does NOT mean 17 airborne.

Plausible warning-state planning band:
- 6-9 airborne;
- 3-6 deck/ready reinforcement;
- remainder in relief/refuel/maintenance/recent recovery.

Exact state depends on warning timing and must be replayed.

Functional roles:
- HIGH;
- MID;
- LOW;
- READY/RELIEF.

These are task states, not permanent clean layers.

## 10. How communication changes combat

Do not use a generic radio multiplier.

Effects enter through:
- earlier useful CAP commitment;
- preserving one element high while another descends;
- group-level target allocation;
- reduced duplicate pursuit;
- faster reserve/relief dispatch;
- better reform/re-engagement;
- fewer silent low-fuel disappearances from the controller picture;
- more coherent escort handoff between D3A/B5N axes.

Within close dogfight:
- benefit falls sharply;
- pilot skill, visual geometry and initiative dominate.

## 11. Historical sanity

Historical IJN doctrine itself was not frozen:
- China-war experience contributed to carrier concentration by late 1940;
- contemporary U.S. reports observed Japanese fighter tactics changing rapidly between carrier battles.

Historical Midway Japanese CAP also suffered heavily from unreliable radios and weak shipboard fighter direction.

Therefore this worldline's decade-long EMI/radio improvement is expected to alter procedure and execution materially without producing modern GCI.

## 12. Supersession map

Use V26:83 over conflicting details in:
- V26:75-76 escort-card numbers;
- restrictive V26:77-78 doctrine-static language;
- duplicate V26:79-82 record pairs.

Retain their technical/source detail where nonconflicting.

## 13. Current next

Run Apr29 A12 / A15 / A18 through both directions of the carrier action.

Japanese strike:
1. Lexington radar/CAP detection;
2. F4F interception;
3. escort COM/CMD/D behavior;
4. U.S. AA;
5. D3A / Type91 / FT valid-release bands.

Lexington counterstrike:
1. Type21/visual warning;
2. CAP launch/readiness;
3. COM/CMD/D transitions;
4. F4F escort interaction;
5. SBD/TBD cohesion/loss;
6. Japanese AA;
7. valid-release bands.

Stop before direct-hit adjudication.
