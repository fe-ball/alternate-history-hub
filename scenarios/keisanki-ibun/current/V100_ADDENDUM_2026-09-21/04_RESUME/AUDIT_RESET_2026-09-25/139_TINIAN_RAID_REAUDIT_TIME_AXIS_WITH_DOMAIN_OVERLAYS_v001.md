# Tinian raid re-audit — time axis with domain overlays
## 2026-10-08

Status: **SELECTED WORKING AUDIT METHOD / NOT AUTHORITY / NO CANONICAL CLOCK ADVANCE**

Parents:
- `91_10JUN_MARIANAS_AIR_POWER_ISR_BASE_PROTECTION_RESET_CLOSEOUT_v001.md`
- `93_NEXT_CHAT_D0_JOINT_FIRST_COUNTERSTRIKE_MARIANAS_AIR_SYSTEM_HANDOFF_v001.md`
- `134_TINIAN_FORTIFICATION_AND_ARTILLERY_SURVIVABILITY_BASELINE_v001.md`
- `135_TINIAN_FIRE_NODE_INTEGRATION_AND_US_SUPPRESSION_TAX_v001.md`
- `136_TINIAN_CANDIDATE_GUN_POSITION_PRECOMPUTED_FIRE_DATA_GATE_v001.md`
- `137_TINIAN_BULK_FORTIFICATION_MATERIAL_AND_LATENT_BATTERY_NETWORK_v001.md`
- `138_TINIAN_BATTERY_RANGE_ARC_AND_SAIPAN_REACH_BOARD_v001.md`

Purpose:
define the correct audit method for Tinian/Marianas raids before and during the Saipan campaign, especially where old replay files predate the file-91 air-power reset and omit the strengthened Tinian artillery/fortification system.

---

# 0. Method choice

Do NOT audit only by weapon category.

Do NOT replay only as prose chronology.

Use:

> **time axis as the controlling spine**
> +
> **domain overlays as state columns**

Each raid/day must update the same five domains:

1. AIR
   - physical / serviceable / crewed / MR / immediate;
   - reinforcement / ferry;
   - CAP / scramble / recovered carrier aircraft;

2. AA
   - 120/76-mm DP;
   - 25-mm / lighter AA;
   - radar / fighter-direction;
   - ammunition / crew / damage;

3. BATTERY
   - fixed coastal guns;
   - mobile field artillery;
   - current / alternate / dummy positions;
   - suppression / reactivation state;

4. BASE
   - runway;
   - taxiway;
   - apron;
   - maintenance;
   - fuel / ordnance;
   - communications / power;
   - dispersal / repair;

5. OBS/C2
   - OP;
   - water-air / D4Y photo;
   - radar;
   - wire/radio;
   - common-grid / target-board state.

This prevents causal loss across categories.

---

# 1. Why time must be primary

A raid changes the next raid's target problem.

Example:

U.S. attacks runway heavily
-> fewer aircraft launch next cycle
-> but coastal batteries / AA survive
-> next U.S. raid faces stronger AA / shore-fire environment.

Or:

U.S. attacks batteries heavily
-> Saipan support ships gain freedom
-> but Tinian aircraft / maintenance survive
-> next Japanese air reaction is stronger.

Therefore:
**target allocation cannot be audited independently of chronology.**

---

# 2. Why domain overlays are still required

If replay is purely chronological, the same hidden state errors can persist.

Examples:
- aircraft count updated, but AA wallet forgotten;
- battery damage updated, but alternate OP survives untracked;
- runway cratered, but dispersed aircraft are incorrectly destroyed;
- battery suppressed, but prepared alternate position never credited.

Thus every time step closes all five domain columns even if some are unchanged.

---

# 3. Mandatory restart point

The current pre-D+0 local-air replay files were created before the file-91 air-power reset.

File91 explicitly rejects the old aggregate Marianas aviation board and requires the 11-Jun replay to be regenerated from:
- physical 580–700;
- MR 420–520;
- immediate 250–310;
- Tinian MR 140–170.

Therefore:
> **11 Jun is the earliest clean restart point for Tinian raid adjudication.**

Do not inherit old 11–16 Jun aircraft loss totals automatically where they depend on the rejected small wallet.

---

# 4. Tinian-specific new target set

Old raid allocations centered heavily on:
- runway;
- apron;
- parked aircraft;
- servicing;
- fighter suppression.

The new Tinian target board must also include:

- known 140-mm batteries;
- known 120-mm DP/coastal batteries;
- suspected 6-inch / heavy positions where relevant;
- mobile-artillery candidate zones;
- OPs;
- plotting / communications;
- protected ammunition;
- prepared alternate / dummy positions.

This creates a finite-sortie target-allocation trade.

---

# 5. AA correction

Tinian AA must not be inferred only from aircraft-defense files.

Important coupling:
- 120-mm DP guns may be both:
  - AA assets;
  - cross-channel / anti-ship artillery assets.

Damage or suppression therefore has multi-domain consequences.

If U.S. raids attack the 120-mm system:
- AA density falls;
- shore-fire capacity may also fall.

If the U.S. ignores it:
- later strike losses / ship exposure may rise.

Track AA battery state explicitly.

---

# 6. Aviation reinforcement correction

File91 makes Tinian a near-peer aviation node:
- physical 190–230;
- MR 140–170;
- immediate 85–105.

Also:
- Bonins reinforcement 10–16 physical / 6–11 immediate MR is a real but not exclusive increment;
- carrier-origin survivors may land on Tinian and remain in the island wallet.

Therefore every post-raid state must ask:
- what arrived from another island;
- what arrived from carriers;
- what was repaired;
- what was dispersed;
- what was destroyed;
- what is actually launchable next cycle.

No old one-way attrition curve is allowed.

---

# 7. Raid-by-raid audit order

Recommended sequence:

## 11 Jun
First major TF58 sweep / suppression.

Close:
- Tinian fighter commitment;
- AA;
- battery target allocation;
- ground-aircraft destruction vs damage/dispersal;
- runway/support damage.

## 12 Jun
Repeat pressure / night aftermath.

Close:
- repair conversion;
- reinforcement/ferry;
- AA/battery survival;
- target-board learning by both sides.

## 13 Jun
Fast-BB / naval bombardment interaction.

Close:
- battery survival;
- battery BDA;
- anti-ship firing opportunities;
- repair / alternate OP.

## 14 Jun
Oldendorf close bombardment / invasion approach.

Close:
- Tinian coastal batteries vs ships;
- U.S. target allocation between Saipan and Tinian;
- pre-D-day battery state.

## 15 Jun
Saipan D-Day.

This is the key joint state:
- Tinian anti-ship fire;
- Tinian air;
- Tinian AA;
- Saipan landing support;
- U.S. suppression split.

## 16–17 Jun
Carrier battle / recovery-node raids.

Rebuild:
- Tinian as recovery node;
- stronger fighter wallet;
- AA;
- protected batteries;
- target competition.

## 18–20 Jun
Transition to:
- Saipan-based 155-mm counterbattery;
- recurring battery reactivation;
- Aslito interdiction.

After 20 Jun:
daily full replay becomes unnecessary unless a threshold crosses.

---

# 8. What should be recalculated numerically

Recalculate:
- Japanese aircraft irreversible/damaged by raid;
- U.S. strike aircraft losses to CAP + AA;
- Tinian runway/service interruption;
- battery suppression/destruction;
- Tinian available aircraft next cycle;
- U.S. sortie allocation split.

Do NOT automatically recalculate:
- every Saipan ground casualty total;
- every front-line yardage;
- entire carrier battle
unless the revised Tinian state crosses a known threshold.

---

# 9. Thresholds that justify downstream replay

Reopen later campaign only if Tinian correction causes one of:

1. materially more Japanese aircraft available for D+0 / D+1;
2. materially more U.S. carrier-air attrition;
3. one or more Tinian heavy batteries survive into a combat window previously treated as neutralized;
4. U.S. Saipan close-support allocation falls enough to alter a ground-phase threshold;
5. Aslito operationalization shifts by >~12–24 h;
6. 20/21 or 25/26 relief terminal geometry changes materially.

Otherwise:
carry the correction qualitatively and do not restart the whole campaign.

---

# 10. Practical board format

For each event use one row:

| Time | U.S. package | Target allocation | JP air | JP AA | JP batteries | Base damage | OBS/C2 | US loss | JP loss | Next-state delta |

Then carry forward only the resulting state.

This is the anti-context-overflow format:
- one row per event;
- explicit state transition;
- no need to reload full prose history.

---

# 11. Immediate concern

Existing files such as:
- `44_MARIANAS_LOCAL_AIR_REPLAY_11JUN_TO_16DAWN_WORKING_v001.md`
- `15_RECON16_1715_1930_TINIAN_DUSK_STRIKE_WORKING_v001.md`
- `28_RECON17_1450_1730_US_MARIANAS_SUPPRESSION_WORKING_v001.md`

contain useful geometry / logic,
but their force levels or loss conversions may be stale because they predate:
- file91 air-wallet reset;
- later Tinian fortification / battery corrections.

Use them as:
**event geometry / tactical reference**

not as:
**unchanged force-state authority.**

---

# 12. Close

Selected audit method:

> **chronology decides causality; domain columns prevent omissions.**

This is the correct way to re-audit Tinian without either:
- losing causal state in a category-by-category review;
- or drowning in another long prose replay.
