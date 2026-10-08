# POST-V26 MI FT pre-load / target-allocation model WORKING handoff — 2026-10-08

Status: WORKING / MODEL-INSTANTIATION / NO COMBAT OUTCOME PROMOTION

## Authority guard

V26 remains canonical at 1941-12-07 14:30 HST.

Inputs:
- V26:29 FT family doctrine;
- V26:31 carrier FT family / warhead stocks;
- V26:47 anti-carrier strike physical scale;
- V26:59 multi-stage state model.

This file separates:
1. pre-launch FT family / warhead loading;
2. in-flight target allocation;
3. downstream state-change value.

No FT hit is fixed here.

## 1. The key distinction

An aircraft cannot observe the U.S. screen and then change:
- standard FT -> FT-GR;
- HE -> SAP;
- standard -> IR.

Those are pre-launch physical choices.

Therefore model two decisions:

### Pre-launch load decision
What family / warhead leaves the Japanese carrier?

### Contact target decision
Given that loaded round and the observed geometry, what target class is attacked?

This prevents hindsight optimization.

## 2. Physical FT inventory constraints

MI embarked total:
- standard FT = 94;
- FT-IR = 18;
- FT-GR = 4;
- total = 116.

Warheads:
- HE-family = 54;
- SAP-family = 62.

Carrier allocations:
- Akagi 24;
- Kaga 24;
- Soryu 18;
- Hiryu 18;
- Zuikaku 24;
- Ryujo 8.

Ryujo uniquely carries a small FT-GR/HE component in the central stock plan.

The first anti-carrier strike uses only a subset of this magazine.
No magical at-sea reload from staging reserve.

## 3. First-strike FT launch quantity remains a planning variable

V26:47 used 25 FT-equipped aircraft.

Retain:
- **25 FT launch slots as a planning center**,
but do not yet treat the exact family/warhead mix as closed.

Reasonable first-strike range:
- 22-28 FT-equipped mothers,
depending on Type91 balance and deck/arming cycle.

For current model comparison, keep 25 as the reference card.

## 4. Pre-launch load roles

Define four roles.

### H — HE suppression
Purpose:
- AA director;
- AA cruiser / heavy cruiser node;
- carrier exposed AA / island / ventilation / flight-support;
- command / communications.

Family:
- standard FT/HE;
- selective FT-GR/HE for short-range screen role.

### S — SAP carrier exploitation
Purpose:
- upper-side / hangar-side penetration;
- internal aviation / electrical / ventilation damage.

Family:
- standard FT/SAP.

### I — IR/SAP premium carrier
Purpose:
- moving fast carrier;
- difficult lateral/cross-track geometry.

Family:
- FT-IR/SAP central.

### R — IR/HE or special HE
Purpose:
- moving carrier topside / AA-support suppression where terminal yaw correction matters.

Small allocation only.

## 5. Candidate pre-launch load cards for 25 FT

These are planning cards, not combat outcomes.

### FT-D — direct-carrier heavy
- H suppression-capable: 5;
- S standard SAP: 13;
- I/R IR family: 7.

Use when:
- U.S. screen seems weak;
- carrier location is good;
- direct weapon concentration is preferred.

### FT-B — balanced
- H suppression-capable: 8;
- S standard SAP: 10;
- I/R IR family: 7.

Use when:
- U.S. radar/AA screen is expected strong;
- one or more screen nodes may be worth degrading;
- but carrier concentration remains primary.

### FT-S — suppression-heavy
- H suppression-capable: 11;
- S standard SAP: 7;
- I/R IR family: 7.

Use only when:
- a very strong local AA/director node is expected;
- multiple later Type91/D3A elements can exploit the corridor;
- attack sequencing is reliable enough that suppression arrives early.

Cost:
- substantial direct-carrier opportunity cost if suppression fails or arrives late.

## 6. Current doctrine center before visual contact

The U.S. carrier forces are known to possess:
- useful radar fighter direction;
- strong heavy AA for 1942;
- multiple cruiser/destroyer screens.

Japanese prewar/combat learning also supports FT-first suppression as one valid card.

Therefore the **FT-B balanced card** is the current planning center for first-strike loadout.

Important:
this does NOT mean 8 rounds will actually be fired at escorts.

It means about 8 loaded rounds are suitable for suppression tasks if the observed geometry justifies it.

## 7. Cell-level pre-load distribution — planning center

Use the 25-reference card.

### Cell 1 — Akagi/Kaga
9 FT slots:
- suppression-capable HE: 3;
- standard SAP: 4;
- IR family: 2.

### Cell 2 — Soryu/Hiryu
7 FT slots:
- suppression-capable HE: 2;
- standard SAP: 3;
- IR family: 2.

### Cell 3 — Zuikaku/Ryujo
9 FT slots:
- suppression-capable HE: 3;
- standard SAP: 3;
- IR family: 3.

Within Cell 3 suppression-capable HE:
- 0-2 may be FT-GR/HE from Ryujo;
- remainder standard FT/HE.

Exact GR use remains pre-launch-option dependent.

## 8. Contact-time target allocation

At target acquisition, each suppression-capable element evaluates:

1. Is there a high-value AA/director node on the actual carrier approach corridor?
2. Can the node be identified with enough confidence?
3. Will the suppression element arrive early enough to affect later elements?
4. Are later Type91/D3A/FT elements actually using that corridor?
5. Would attacking the node force a maneuver that helps or hurts the later attack?
6. Is the carrier itself exposed enough that direct attack dominates?

If these tests fail:
- the suppression-capable FT may attack the carrier directly.

Thus:
**suppression-capable does not equal suppression-fired.**

## 9. Screen target hierarchy

Do not target every escort.

Preferred candidate classes:
1. dedicated / obvious AA cruiser or major director node;
2. heavy cruiser whose location dominates the intended ingress corridor;
3. command / communications node if visually identifiable;
4. destroyer only when it physically blocks / anchors a corridor and the loaded FT family is appropriate.

Small DDs remain low-value unguided-standard-FT targets in most cases.

## 10. Recognition uncertainty

Japanese attackers do not know exact U.S. ship names automatically.

They may recognize:
- carrier;
- cruiser;
- light/AA-cruiser-like silhouette;
- destroyer;
- relative screen position.

Therefore the model uses target class / tactical role, not omniscient "attack Atlanta because it is Atlanta."

A visually distinctive high-AA cruiser may be selected because:
- dense gun flashes;
- central screen position;
- observed director fire;
not because its identity is known from a database.

## 11. Suppression success has multiple levels

Do not make suppression binary.

For a screen/AA target, possible states are:

### SUP-0
No useful effect.
- miss / distant near miss;
- no meaningful later-state change.

### SUP-1
Local disruption.
- crews take cover;
- one mount/director temporarily interrupted;
- smoke / maneuver;
- short-lived local fire-density reduction.

### SUP-2
Node degradation.
- director / communications / several mounts degraded;
- meaningful bearing-specific AA reduction;
- local formation response.

### SUP-3
Node mission kill.
- major AA/command function lost for the relevant attack window.

SUP-3 should be uncommon.
Do not assume one FT hit automatically produces it.

## 12. Downstream effect channels

If suppression succeeds, update separately:

- AA-heavy fire on bearing;
- medium/light AA on bearing;
- director handoff quality;
- screen spacing;
- carrier evasive freedom;
- CAP vector/attention;
- smoke/visibility;
- friendly-fire/masking constraints.

A SUP-2 event might:
- help Type91 substantially;
- help D3A slightly;
- have little effect on a standard FT already released from standoff.

No universal percentage bonus.

## 13. Timing value

Suppression is valuable only if it precedes the weapon that benefits.

Track:
- t_suppression_release;
- t_suppression_effect;
- t_D3A_dive;
- t_Type91_final_run;
- t_FT_carrier_release.

If the screen hit occurs after Type91 release:
- it cannot retroactively improve that Type91 mother's survival.

This temporal ordering is mandatory.

## 14. Interaction with carrier maneuver

Suppression may cause:
- carrier turns toward/away from the damaged screen sector;
- screen compression;
- screen expansion;
- cruiser falling out of station;
- carrier gaining maneuver space.

Therefore a successful screen attack can:
- improve one later axis;
- worsen another.

Track per bearing.

## 15. Interaction with U.S. CAP

A suppression element itself may:
- draw F4F attention;
- reveal a low-altitude axis;
- cause CAP to descend;
- or be ignored if the main threat is recognized elsewhere.

Thus its value can exist even without a direct screen hit.

This is a **CAP-displacement effect** and must be modeled separately from AA damage.

## 16. Cell-specific doctrine tendencies

### Cell 1
Large attack weight.
Likely to justify one early suppression element if:
- a strong AA node lies on the preferred ingress.

### Cell 2
Smaller attack mass.
More sensitive to wasting direct-carrier weapons.
Suppression should be more selective.

### Cell 3
Saratoga-like separate group.
Ryujo contributes short-range GR/HE option.
Because target group is separate, its local screen geometry can be evaluated independently from TF16.

## 17. What is still OPEN

Before combat resolution:
- FT-D / FT-B / FT-S actual chosen load card;
- exact GR count;
- actual suppression target count;
- actual suppression target classes;
- suppression success level;
- resulting CAP displacement;
- resulting AA/director state;
- carrier maneuver response;
- later valid-release changes.

## 18. Current planning center

For model instantiation only:
- use FT-B as the reference load card;
- compare FT-D and FT-S as sensitivity cases.

Do not promote FT-B to a fixed historical fact until the attack sequence is instantiated against the observed U.S. geometry.

## 19. Next

Combine:
- Gaifu G-B / G-E / G-D cards;
- FT-D / FT-B / FT-S cards;

with actual U.S. and Japanese attack arrival order.

The purpose is to see whether the same tactical state favors:
- more Gaifu retained in CAP;
- more suppression-capable FT loaded;
or whether those choices trade against each other.
