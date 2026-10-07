# Saipan re-audit pivot — combat-power curves and threshold-triggered regeneration
## 2026-10-07

Status: **SELECTED WORKING AUDIT METHOD / NOT AUTHORITY / NO CANONICAL CLOCK ADVANCE**

Parents:
- `97_SAIPAN_FULL_REAUDIT_MASTER_REGISTER_v001.md`
- `101_PHASE1_SAIPAN_DDAY_15JUN_REAUDIT_v001.md`
- `102_PHASE2_3_SAIPAN_16_19JUN_REAUDIT_v001.md`
- `103_PHASE4_20_21JUN_RELIEF_BOMBARDMENT_COUNTERLANDING_REAUDIT_v001.md`
- `104_PHASE5_21_25JUN_CONVERSION_AND_REINFORCEMENT_BRANCH_AUDIT_v001.md`
- `105_MARIANAS_KON_DATED_FORCE_REALIZATION_GATE_v001.md`
- `106_PHASE6_25_26JUN_BRANCH_S_DECISIVE_RELIEF_REAUDIT_v001.md`
- `107_PHASE6_25_26JUN_DECISIVE_TRANSPORT_AIRSEA_FREEZE_GATE_v001.md`
- `108_PHASE7_US_REINFORCEMENT_ARCHITECTURE_CLOSEOUT_v001.md`
- `109_PHASE7_POST25JUN_MARIANAS_AVIATION_WALLET_GATE_v001.md`
- `110_PHASE7_LOCAL_CRAFT_EVACUATION_WALLET_GATE_v001.md`
- `111_PHASE7_SAIPAN_JAPANESE_POPULATION_IDENTITY_GATE_v001.md`

Authority remains Branch B v100 / 1944-06-16T14:15.

---

# 0. Why the method changes

The chronological re-audit succeeded in recovering important qualitative deltas, but exact closure of every:
- headcount;
- craft hull;
- aircraft;
- special-ammunition round;
- transport pulse;
- wounded state;
- gun state
before proceeding creates an infinite upstream dependency chain.

Therefore the audit changes method.

> **Apply already-established qualitative and bounded quantitative corrections directly to each side's combat-power trajectory.**
>
> **Only reopen the earliest causal checkpoint when a corrected trajectory crosses a decision/phase threshold that changes campaign structure.**

This replaces:
> close every ledger first -> then replay

with:
> correct the curves -> test thresholds -> reopen only the threshold-causing dependencies.

No previously identified decisive FREEZE is erased.
A frozen branch remains a sensitivity until a threshold depends on selecting it.

---

# 1. Curves to carry

Do not reduce either side to one fake scalar strength number.

Carry six functional curves.

## Japan J(t)

### J-I — coherent infantry
- equipped rifle/MG/AT/mortar formations;
- officer/NCO skeleton;
- ability to assemble >company/battalion packets.

### J-F — fire system
- artillery/mortars;
- ammunition access;
- survey/fire data;
- OP;
- wire/radio;
- alternate positions.

### J-C — command / synchronization
- sector C2;
- route communications;
- ability to coordinate several attack axes.

### J-M — mobility / regeneration
- trucks/prime movers;
- engineer plant;
- local craft;
- repair;
- night route reopening.

### J-A — local aviation / external observation
- Tinian/Guam/Rota/water-air;
- reconnaissance;
- small attack/interception;
- no automatic carrier credit.

### J-L — logistics depth
- ammunition;
- water;
- medical;
- repair;
- receiving/evacuation capability.

## United States U(t)

### U-I — coherent assault infantry
- battalion/company cohesion;
- leaders/NCO/specialists;
- reserve freshness.

### U-F — fire-support system
- artillery/FDC/FO/comms;
- NGFS;
- CVE/air support;
- ammunition.

### U-A — armor / engineer assault system
- Sherman MR;
- engineer teams;
- mine/obstacle/route clearing;
- flame/demolition support where present.

### U-R — reserve / rotation
- fresh battalion-equivalents;
- ability to relieve depleted units;
- afloat reserve / later reinforcement.

### U-B — base conversion
- Aslito physical/tactical/operational ladder;
- road/security;
- repair;
- fuel/ammunition;
- dispersal/AA/control.

### U-L — amphibious/logistics system
- LVT/boat/shore-party;
- unloading;
- casualty evacuation;
- repair/tow;
- turnaround for Tinian/Guam.

---

# 2. Corrections already allowed to bend the curves

## Japanese curve rises / decays more slowly because of

- 43d Division earlier/coherent integration;
- higher physical -> usable artillery conversion;
- optical/survey/communications package completeness;
- better alternate-position and re-registration recovery;
- better prime-mover / repair organization;
- local craft preserved from the historical 17-Jun mass loss;
- bounded coastal mobility from D-day onward;
- 20/21 relief support-first regeneration;
- no premature evacuation of healthy infantry/NCO/C2/specialists;
- distributed late Marianas aviation outside Saipan.

## Japanese curve does not receive

- free extra fixed guns;
- free Marpi M3;
- free Branch-T thick relief;
- free S2 25/26 landing;
- free carrier aviation;
- automatic extra population.

## U.S. curve falls / regenerates more slowly because of

- higher early casualties and specialist loss;
- repeated Japanese artillery/OP regeneration;
- Aslito physical possession != immediate operational base;
- repeated suppression/engineer/security demand;
- local Japanese aviation/recon survives outside Saipan;
- Japanese craft/logistics system is not inert.

## U.S. curve gains

- overwhelming daylight fire superiority remains;
- coherent artillery/CVE/NGFS recovery;
- already-afloat 1/22 option;
- additional 1st Provisional Marine Brigade slice if required;
- 77th RCT later on a real Hawaii transport clock.

---

# 3. Threshold rule

Do not re-audit a detail merely because it changes a number.

Reopen the earliest causal point only when the corrected curve crosses one of the following:

## T-US1 — immediate local reinforcement
Trigger if:
- current assault divisions cannot preserve a fresh battalion reserve / rotation;
- Aslito remains tactically insecure;
- Japanese coherent fire/attack system remains able to disrupt reconstitution.

Response:
- release **1/22 Marines** first.

## T-US2 — second local escalation
Trigger if:
- U1 fails to restore rotation/security;
- Japanese attack/fire system still has repeated operational effect.

Response:
- consume another bounded 1st Provisional Marine Brigade slice;
- direct Guam readiness loss.

## T-US3 — deep reinforcement / plan redesign
Trigger if:
- Saipan continues to consume the Guam force;
- Tinian/Guam assault preparation cannot regenerate on schedule.

Response:
- redirect / accelerate **77th RCT** on a real Hawaii shipping clock;
- FORAGER sequencing changes structurally.

## T-J1 — large local counterattack opportunity
Trigger requires simultaneous:
- U.S. local support output at an unusually weak trough;
- Japanese coherent infantry/mobile packet available;
- J-F fire system current;
- routes/C2 open;
- exploitation window long enough to matter.

Result:
- test early/local counterattack.
Do not create one merely because U-F temporarily dips.

## T-J2 — true offensive counterlanding
Requires:
- temporary sea/fire corridor;
- spare craft beyond essential receiving/logistics;
- veteran packet;
- land link-up plausibility.

If not all exist:
- NO-GO remains rational.

## T-FA — final attack
Trigger is not a date.

Use the **last** night when:
- >~1,000-class coherent force can still be assembled under one intent;
- several axes can still synchronize;
- ammunition/mortar/MG support remains;
- routes remain open long enough;
- waiting longer is expected to reduce attack power faster than it improves conditions.

## T-END — organized resistance end
Trigger when:
- formation-scale C2 is gone;
- major cells are isolated;
- repeatable night logistics/evacuation ends;
- no meaningful mobile reserve remains;
- U.S. can sustain artillery/tactical-air cycle over the remaining pocket.

---

# 4. Current expected threshold crossings

These are hypotheses to test, not authority.

## A. U.S. reinforcement threshold
**Most likely material campaign change.**

Current audit direction makes T-US1 substantially more likely than the old historical-like replay.

Likely sequence:
1. 1/22 is released to Saipan;
2. if Japanese resistance remains coherent, another Guam-force slice follows;
3. if Saipan still prevents formation rotation, 77th destination/planning changes later.

This damages FORAGER more naturally than teleporting the 77th directly to Saipan.

The main strategic change may therefore be:
> not one huge extra U.S. reinforcement, but **several escalating reinforcement decisions that progressively destroy the original Tinian/Guam timetable.**

---

# 5. Japanese final attack — timing elasticity vs strength elasticity

Current hypothesis:

> **final-attack timing has relatively low elasticity; final-attack strength/effect has much higher elasticity.**

Reasons timing may not move very far:
- U.S. compression eventually cuts routes;
- daylight artillery/air superiority steepens once high ground/observation is lost;
- a stronger organized force also becomes a larger target;
- Japanese command rationally attacks before its still-coherent force is fragmented.

Reasons attack strength rises:
- 43d formations are more coherent;
- fewer healthy infantry/NCOs are evacuated;
- support specialists remain until their combat value collapses;
- artillery/mortar system decays more gracefully;
- local aviation/Tinian support remains part of the operation;
- fresh/backfill manpower, where present, frees terrain-experienced troops.

Therefore do **not** expect a simple:
historical 6/7 Jul -> 20 Jul final attack.

More plausible:
- same broad early-July class window or a modest shift;
- **larger coherent assault mass**;
- better MG/mortar/artillery preparation;
- narrower, better synchronized axes;
- attacks directed at higher-value rear/support nodes.

---

# 6. Final-attack target quality

The previous broad historical-style final wave is probably the wrong geometry.

Branch force should prefer:
- narrow penetration along known route/seam;
- hit artillery/FDC;
- hit vehicle/reserve assembly;
- hit road junctions;
- interfere with Aslito support/recon/repair;
- exploit friendly-fire restrictions once Japanese troops enter the U.S. rear.

Local aviation / Tinian / remaining mortars should attack:
- U.S. rear response system,
not attempt dangerous close CAS into mixed infantry.

Expected change:
> **higher-grade targets become reachable even if total penetration width remains limited.**

Thus the main difference may be:
- not vastly farther territorial penetration;
- but temporary direct disruption of an actual artillery/FDC/base-support node.

Old 0.8–1.5 km penetration is reopened.

---

# 7. Could Japan counterattack materially earlier?

Possible threshold windows already identified:

### 20/21 Jun
U-F reaches a temporary support trough after naval bombardment.

But:
- local boat reserve is more valuable for receiving;
- Japanese coherent infantry mass is still bounded;
- U.S. bridgehead is robust.

Likely:
**bounded land exploitation, not operational counteroffensive.**

### 25/26 Jun
This is the more dangerous threshold.

If S2 / thick corridor succeeds:
- fresh troops backfill;
- veterans become mobile;
- U-F can be disrupted again;
- T-J1 may be crossed.

If S0:
- no major threshold crossing.

Therefore any genuinely larger earlier Japanese counterattack should be tied to **25/26 success**, not inserted as a generic result of stronger defense.

---

# 8. Could organized defense survive into late July?

On the current common branch:
**unlikely.**

To reach late July with organized formation-scale resistance, Japan would need several thresholds to break in its favor:
- successful large reinforcement;
- continued route/logistics connectivity;
- substantial artillery/ammunition survival;
- persistent observation;
- U.S. reinforcement/reconstitution delay;
- enough high-ground depth to avoid rapid compression.

The already-audited qualitative gains alone probably buy:
- a stronger late defense;
- a modest calendar extension;
- not three extra weeks of organized island-scale defense.

Late-July organized resistance becomes serious only on a high-success Branch-T/S2-like path.

Isolated cave/ridge survivors can persist much longer without implying organized defense.

---

# 9. Casualty-direction hypothesis

Current likely direction:

## United States
Higher than historical because:
- more repeated exposure;
- artillery/FDC/engineer specialists are targeted;
- longer contested-base phase;
- stronger final attack;
- more rotation friction.

But reinforcement can reduce the late marginal casualty rate by restoring coherent reserves.

## Japan
Also higher total combat deaths than a weaker historical-like organization is plausible because:
- more soldiers remain coherent and continue fighting;
- fewer healthy infantry are evacuated;
- final operation commits a larger share of usable infantry.

Composition shifts:
- **more infantry / combat-arms dead**;
- relatively fewer avoidable specialist/service losses where selective evacuation/rear preservation works;
- some wounded/aircrew/specialists survive through Tinian extraction.

Thus:
> “both sides die more; Japanese additional deaths skew more toward infantry/combat arms”
is a strong current hypothesis.

Do not yet set totals.

---

# 10. Most likely larger strategic change

The re-audit increasingly points to a structural effect larger than a few extra Saipan days:

> **The U.S. wins Saipan, but must progressively consume the reserve architecture intended to make Tinian and Guam a smooth follow-on sequence.**

Possible chain:
1. Saipan assault divisions wear down more.
2. 1/22 is used.
3. more Guam reserve is considered/used.
4. 77th timing/destination is reconsidered.
5. Tinian assault cycle slips.
6. Guam architecture loses margin and must be rebuilt.
7. Fifth Fleet support remains tied to a supposedly completed Saipan longer.

This can be a major FORAGER disruption even if Japanese organized resistance ends only modestly later than history.

---

# 11. Stop rule for future audit

From this file forward:

### Do not
- chase exact OOB/hull/person count merely to improve precision.

### Do
1. apply a verified qualitative correction to J(t) or U(t);
2. see whether any threshold changes state;
3. if no threshold changes:
   - keep the correction and move on;
4. if a threshold changes:
   - identify the **earliest causal checkpoint**;
   - reopen only the minimum dependencies needed to adjudicate that threshold;
5. after the threshold is resolved, regenerate downstream campaign state.

This becomes the controlling Saipan re-audit method unless explicitly superseded.
