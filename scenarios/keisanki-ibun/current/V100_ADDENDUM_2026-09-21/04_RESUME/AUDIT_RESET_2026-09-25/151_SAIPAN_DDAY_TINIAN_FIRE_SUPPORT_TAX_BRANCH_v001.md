# Saipan D-Day — Tinian fire-support tax branch
## 2026-10-08

Status: **SELECTED WORKING D-DAY BRANCH / SUPPORT-ALLOCATION CORRECTION / NOT AUTHORITY**

Parents:
- `101_PHASE1_SAIPAN_DDAY_15JUN_REAUDIT_v001.md`
- `138_TINIAN_BATTERY_RANGE_ARC_AND_SAIPAN_REACH_BOARD_v001.md`
- `150_TINIAN_14JUN_OLDENDORF_CLOSE_BOMBARDMENT_AND_COUNTERBATTERY_v001.md`

Purpose:
activate the previously frozen Tinian fixed-gun contribution to Saipan D-Day without silently adding a casualty multiplier.

File101 explicitly froze fixed naval/coast/DP-gun effects pending later audit and required a branch if that audit closed a material battery contribution.

That condition is now met.

---

# 0. What changed relative to file101

File101 remains controlling for:
- Saipan ground defense geometry;
- D3 fortress mechanisms;
- Japanese land-artillery quality;
- first-24h U.S. ground casualty working band;
- no bridgehead-destruction result.

This branch adds only the previously under-modeled **external Tinian fire node**.

No extra Saipan-installed heavy guns are created.

The new question is:
> **How much U.S. support capacity is consumed by keeping Tinian batteries suppressed during the Saipan landing?**

---

# 1. Historical hard floor

Historical 14–15 Jun already proves that Tinian was not a passive neighbor.

Before D-Day:
- U.S. fire-support units were specifically assigned to Tinian;
- Pennsylvania operated off northeastern Tinian to neutralize guns threatening Saipan;
- Terry's unit was assigned both northern-Tinian gun suppression and Ushi airfield neutralization.

During the 14-Jun UDT/support operation:
- Tinian batteries straddled Cleveland;
- hit California;
- hit Braine.

Therefore:
**Tinian suppression was already a real U.S. Saipan-support mission historically.**

Branch does not invent this tax.
It increases its persistence.

---

# 2. Branch Tinian D-Day firing system

15-Jun dawn from file150:

## Ushi 140-mm
- immediately useful: **~1–2**
- additional physical gun may return during the day.

## Faibus 140-mm
- immediately useful: **~1–2**

## Asiga 140-mm
- four physical guns largely intact;
- exact Saipan-bearing arc remains a sensitivity.

## 120-mm DP
- **~5–7 immediately useful across all roles**
- must divide between:
  - AA;
  - surface/channel fire;
  - possible land fire.

## mobile 75-mm
- selected northern C2/C3 positions can reach southern-Saipan/channel boxes.

Thus the Japanese do not possess one continuously firing mass battery.

They possess:
**several short-duration firing cells that can reappear.**

---

# 3. Japanese D-Day employment doctrine

Do NOT maximize round count.

Selected priority:

1. U.S. ships supporting Agingan / southern Saipan;
2. UDT / boat / landing-support concentrations where geometry permits;
3. fire-support destroyers/cruisers forced into known channel boxes;
4. southern Saipan logistics/road boxes only where fixed-gun arc is actually valid;
5. preserve guns if no high-value target exists.

Firing pattern:
- short salvos;
- precomputed target data;
- rapid silence after U.S. counterbattery;
- alternate OP / communications re-entry.

This maximizes:
**support disruption per exposed firing minute.**

---

# 4. U.S. counterbattery system

U.S. response is strong.

Assets include:
- old battleships;
- cruisers;
- destroyers;
- observation aircraft;
- carrier/CVE air;
- later shore artillery once established.

On D-Day morning:
U.S. does not lack shell weight.

The constraint is:
**concurrency and attention.**

A ship firing on Tinian is not simultaneously delivering its planned Saipan target mission at full effectiveness.

A spotter searching for a reopened Tinian battery is not observing another target.

A carrier/CVE section suppressing Ushi/AA is not simultaneously supporting a Saipan beach box.

---

# 5. Selected 08:00–12:00 Tinian firing windows

Use three bounded activity windows rather than continuous shelling.

## Window T1 — approach / H-hour
Duration:
**~8–15 min effective firing opportunity**

Targets:
- southern fire-support ships;
- landing/support-water geometry;
- channel traffic.

Likely outcome:
- quick U.S. counterbattery;
- Japanese guns silence / shift observation.

## Window T2 — post-H-hour congestion
Duration:
**~10–20 min cumulative**, fragmented.

Targets:
- ships holding predictable support stations;
- transport/support movement;
- southern Saipan handling areas only if firing arc confirmed.

## Window T3 — late morning reappearance
Duration:
**~5–15 min cumulative**

Enabled by:
- repaired wire;
- alternate OP;
- U.S. attention shifting inland.

Total actual Japanese useful firing time is therefore:
**~25–50 min cumulative across multiple cells**, not one uninterrupted battery barrage.

---

# 6. U.S. support-capacity tax

This is not equal to the Japanese firing time.

For each firing episode the U.S. pays:
- detection / localization;
- spotter attention;
- ship maneuver;
- counterbattery;
- BDA / watch for reopening.

Selected 08:00–12:00 aggregate Tinian tax:

## heavy / cruiser fire-support attention
Equivalent to:
**~25–45 ship-minutes of BB/CA main-battery attention**
spread across several ships.

## destroyer / secondary-battery attention
Equivalent to:
**~60–100 DD/secondary-battery ship-minutes**
including channel patrol / suppression / harassment.

## air suppression
**~6–12 tactical aircraft-sortie equivalents**
diverted/retasked toward:
- Ushi;
- AA;
- observed battery/OP;
rather than Saipan close support or other island targets.

These are **opportunity-cost measures**, not literal single-ship continuous absences.

---

# 7. Local Saipan-support effect

Because U.S. support is redundant,
this does NOT create a theater-wide fire-support blackout.

Selected local effects:

### southern beach / Agingan-support sectors
During individual Tinian firing/counterbattery episodes:
- planned naval fires may be delayed / shortened;
- one support ship may maneuver off ideal station;
- spotter/air attention may shift.

Local support degradation:
**~5–15 min episode class**

Across the morning:
- several episodes;
- not all simultaneous;
- ground artillery increasingly replaces part of the lost naval concurrency after landing.

### central/northern beaches
Effect:
**small / indirect**

Do not distribute the Tinian tax uniformly across the Saipan beachhead.

---

# 8. Ship-damage branch

Historical calibration demonstrates direct-hit capability.

Selected Branch D-Day class:

- one fire-support large hull:
  **light/local damage or damaging near miss**
- one DD / smaller support ship:
  **direct-hit / local mission-disruption class**
- additional straddles / maneuver.

Do NOT center:
- BB mission kill;
- cruiser sinking;
- multiple heavy-hull losses.

Important:
ship identity is left OPEN until the U.S. support-station/OOB ledger is synchronized.

---

# 9. Ground-casualty treatment

Do NOT yet add a new casualty multiplier to file101.

Reason:
the first-order Tinian effect is:
- support interruption;
- counterbattery diversion;
- ship maneuver;
- target-allocation dilution.

Some of this may already be implicitly absorbed in the existing 52/59 D-Day ground bands.

Therefore current ruling:

## Ground geometry
**retain file101 working bands for now**

## First-24h U.S. ground casualty band
**retain 3,800–4,700 class for now**

## Reopen flag
Set:
**TINIAN-SUPPORT-TAX = ACTIVE**

A numerical change is justified only if combined replay shows that:
- southern NGFS/CAS reduction overlaps a critical Japanese land-fire window;
- the reduction is not already represented by the D3 fortress candidate;
- resulting change exceeds ordinary variance.

---

# 10. Why the effect can matter later even if D-Day front does not move

The tax has cumulative consequences:

1. more BB/CA/DD ammunition spent on Tinian;
2. more destroyer fatigue / exposure;
3. more carrier/CVE sorties assigned to suppression;
4. Tinian batteries remain a recurring concern;
5. U.S. cannot freely shift every support asset to inland Saipan once the beachhead forms.

Thus:
**D-Day may stay inside the old ground band while the operational support wallet is measurably worse.**

This is exactly the kind of effect that can become more important on:
- 16–19 Jun;
- Aslito conversion;
- 20/21 relief;
than in immediate beach distance.

---

# 11. Interaction with Tinian local air

Do not double-count.

Tinian local aviation:
- has its own attack / observation / CAP wallet;
- consumes U.S. CAP / AA / fighter attention.

Tinian fixed fire:
- consumes naval gunfire / suppression / spotter attention.

The combined effect is:
**multi-domain support dilution.**

Do not translate both independently into full casualty bonuses.

---

# 12. File101 freeze status

File101's fixed-heavy-gun FREEZE is now partially released for:

**TINIAN EXTERNAL FIRE ONLY.**

Still frozen:
- extra untraced Saipan fixed guns;
- any invented Tinian gun count;
- any automatic landing-craft loss multiplier;
- any direct ground-casualty increment not traced through lost support.

---

# 13. Main finding

D-Day Tinian should be represented as:

> **a repeatedly reappearing external fire node that forces U.S. ships and aircraft to keep paying suppression costs during the Saipan landing.**

The U.S. still:
- lands successfully;
- obtains tactical air superiority;
- possesses overwhelming aggregate fire support.

But it does not enjoy full historical/nominal support concurrency against Saipan because:
**Tinian remains alive next door.**

---

# 14. Next gate

Now re-evaluate 15-Jun local aviation under the post-file91 wallet and this support-tax state.

Key question:
does the combination of:
- Tinian fixed fire;
- surviving Tinian aviation;
- Tinian AA;
- Saipan ground artillery
create a support-concurrency threshold that moves the file101 morning/afternoon ground result?

Do not answer from one domain alone.
