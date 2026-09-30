# Marianas aviation-system depth gap audit
## 2026-09-30

Status: **SELECTED WORKING SYSTEM AUDIT / NO COMBAT RESULT CHANGE / NOT AUTHORITY**

Use relative-day notation from file 84.
Authority remains Branch B v100.
Canonical machine clock remains 1944-06-16T14:15.

Depends on:
- `86_JAPANESE_ISLAND_BASE_CAPABILITY_MARIANAS_AIRFIELD_NETWORK_REAUDIT_WORKING_v001.md`
- `41_MARIANAS_JAPANESE_AVIATION_FULL_ROLE_REAUDIT_11_18JUN_v001.md`
- `47_MARIANAS_LOCAL_AIR_WALLET_15JUN_0430_v001.md`
- `50_MARIANAS_LOCAL_AIR_WALLET_16JUN_DAWN_v001.md`
- `53_MARIANAS_FERRY_REGENERATION_NETWORK_14_18JUN_v001.md`
- V098 Marianas air-defense state on 10 Jun
- V099 aircraft / Homare pool audit.

Purpose:
identify what Marianas aviation capability was already modeled strongly and what was left implicit because earlier discussion focused disproportionately on fortification / water-air / individual high-end fighters.

No opening-battle loss or OOB number is changed here.

---

## 1. Existing Branch aviation is already a major force

Current 10-Jun Working regional state:

### Fighters MR
**143–176**
center ~160.

Indicative:
- Ki-44: 25–29
- Ki-84: 27–31
- late Zui-sei Zero: 41–49
- Kinsei Zero mod: 17–21
- Raiden: 17–21
- Shiden-Kai: 8–12
- Kyofu: 8–13

### Non-fighter ready
- D4Y: 14–19
- B6N: 11–15
- older attack / land-attack: 8–13
- water recon / observation: 12–18
- H6K/H8K: 4–7

### Total regional MR
**192–248**
center ~220.

Island distribution working:
- Saipan: 80–96 all-air ready
- Tinian: 63–77
- Guam: 38–53
- Rota/Pagan/other: 11–17

This is not a token island air arm.
It is already a substantial operational air system.

---

## 2. Existing replay already spends this force heavily

Current event line has already used Marianas aviation for:

- large fighter defense on 11–12 Jun;
- 12-Jun night attack;
- maritime ISR / invasion identification;
- local anti-shipping reaction on SAI B-D+0;
- battlefield observation;
- D4Y photo confirmation;
- dusk handling-zone attack;
- recovery defense for First Mobile Fleet survivors;
- ferry / redistribution;
- SAR / liaison;
- water-air observation;
- later bounded night harassment.

Thus the problem is not:
“we forgot Japanese airplanes existed.”

The problem is:
**the physical base system supporting all these tasks was under-specified.**

---

## 3. What was modeled well

### A. Aircraft / engine scarcity
The Branch already correctly treats:
- Ki-84;
- Shiden-Kai;
- B7A;
- C6N;
- P1Y;
- Homare engines
as finite national / theater wallets.

High-end aircraft cannot be increased because another runway exists.

### B. Fighter quality / command depth
Branch avoids part of the historical carrier-air / Solomons leader attrition chain.

Credit already exists for:
- deeper senior flight leadership;
- better unit continuity;
- better tactical understanding of F6F / U.S. fighter-direction methods.

Do not turn this into a universal pilot-quality multiplier.

### C. Air warning
Existing Branch already has:
- radar / visual / DF warning;
- plot correlation;
- Army/Navy formatted handoff;
- enough warning to disperse and launch some fighters before a sweep.

### D. Regional ferry
File 53 already allows:
- ~6–12 aircraft-class gross relocations/day under heavy pressure;
- small dusk / pre-dawn transfer cells;
- damaged-aircraft diversion;
- repair concentration.

### E. Multi-role air use
Files 40–50 already distinguish:
- interception;
- escort;
- maritime search;
- ground observation;
- photo;
- attack;
- night attack;
- liaison;
- SAR.

This should remain.

---

## 4. What was under-modeled

### A. Within-island field network
We had island totals but not:
- aircraft by field;
- field physical state;
- emergency strips;
- alternate taxi / parking;
- field-specific service depth.

### B. Ground-service echelon
No explicit field-by-field accounting of:
- mechanics;
- armorers;
- engine teams;
- radio / instrument;
- fuel / bowser / pump;
- tractor / recovery vehicle;
- firefighting;
- crater-repair;
- airfield construction teams.

Yet repeated sortie generation requires these.

### C. Fuel / ordnance distribution
Regional fuel / torpedo / bomb limits exist in places,
but not as a field network:
- main dump;
- split dump;
- emergency fuel;
- ordnance handling;
- transfer after a field is hit.

### D. Repair conversion
Current replays use broad:
- irreversible;
- repair queue;
- short unavailable.

They do not ask:
**where does the damaged aircraft physically go?**

A richer strip network changes:
- crash / ditch;
- field repair;
- cannibalization;
- next-day return.

### E. Sortie-generation capacity
No field-by-field ceiling exists for:
- simultaneous launch;
- rearm / refuel;
- returning damaged aircraft;
- congestion after carrier-origin arrivals.

### F. Carrier-shuttle absorption
Post-14:15 events use Marianas to recover First Mobile Fleet aircraft.

This requires:
- landing surfaces;
- parking;
- fuel;
- maintenance;
- crew sorting;
- communications.

The current replay mostly assumes this system works, but has not physically modeled why.

### G. U.S. target-allocation burden
More real strips / support nodes mean:
- more sweep / strike targets;
- lower concentration per target;
- repeated reconnaissance requirement.

Current U.S. suppression results do not yet distribute effort across actual fields.

---

## 5. Key structural correction

The correct model is:

**AIRFRAMES**
x
**CREWS**
x
**USABLE RUNWAY / WATER BASE**
x
**GROUND SERVICE**
x
**FUEL / ORDNANCE**
x
**WARNING / C2**
x
**REPAIR / FERRY**
=
**MISSION-READY SORTIE OUTPUT**

Not:
**aircraft count = air power**.

This matters because the Branch improvement is strongest in the middle layers:
- usable alternatives;
- repair;
- dispersion;
- service continuity;
- warning;
- ferry.

---

## 6. Why more runways can change losses without changing OOB

A richer base network primarily changes **attrition conversion**.

Example:

### Single-field logic
aircraft damaged + main runway closed
-> forced ditch / crash / abandonment
-> irreversible loss.

### Network logic
aircraft damaged + main runway closed
-> divert to Marpi / Tinian / Guam / emergency strip
-> aircraft unavailable today
-> repair / ferry later
-> not irreversible.

Therefore later replay should expect possible migration from:
- irreversible loss
toward
- damaged / repair queue / displaced.

This is especially important for:
- ordinary fighters;
- recon aircraft;
- damaged carrier-origin aircraft;
- experienced crews.

---

## 7. What “more aircraft forward” actually means

Additional base capacity does not authorize new production.

Use three categories:

### HARD-CAPPED / top-end
Examples:
- Ki-84 allocated units;
- Shiden-Kai initial cells;
- specialized night / recon cadres.

Extra strips:
- improve survival / readiness;
- do not raise physical theater count without a dated reinforcement source.

### ALLOCATION-LIMITED / upper-middle
Examples can include:
- mature Ki-44 / Raiden / late Zero cells;
- attack / recon aircraft whose national physical pool exceeds current local allocation.

Extra base depth may justify:
- modestly larger forward allocation;
only if:
- dated aircraft exist;
- crew exists;
- ferry route exists;
- maintenance / spares exist.

### SUPPORT / older / ordinary
Older fighters / attack / liaison / water-air may have more allocation elasticity.

But:
- usefulness can be lower;
- crew / maintenance / fuel still bind.

Thus the first re-audit question is:
**which categories were limited by runway/support capacity rather than national aircraft supply?**

Do not add an arbitrary aircraft percentage.

---

## 8. Saipan / Tinian / Guam roles after base re-audit

### Saipan
Likely roles:
- forward fighter / attack / recon;
- immediate battlefield support;
- main invasion observation;
- water-air / naval liaison;
- emergency recovery through Marpi if usable.

Weakness:
- closest to bombardment / ground capture.

### Tinian
Likely becomes the **most important resilient local air-operating node** once Saipan fields are heavily suppressed.

Strength:
- multiple strips;
- short distance;
- repair / redistribution;
- shuttle;
- night / dusk launch.

### Guam
Likely becomes:
- deeper repair / reserve;
- longer-range search / attack staging;
- diversion recovery;
- replacement acceptance.

Less efficient for immediate Saipan tactical work but more survivable.

### Rota / Pagan
- diversion;
- warning;
- weather;
- small ferry / emergency recovery.

This creates a real **depth ladder**:
Saipan -> Tinian -> Guam -> secondary nodes.

---

## 9. U.S. suppression must be re-modeled as a network attack

Current U.S. air superiority remains.

A richer Japanese base system does not make U.S. suppression fail.

It changes the task:

U.S. must choose between:
- sweep fighters;
- runway cratering;
- apron / revetment attacks;
- fuel / workshop / power attacks;
- radar / C2;
- Marianas ferry-route interception;
- Saipan CAS;
- carrier defense / search.

Thus U.S. tactical air superiority may remain YES while:
**Japanese air-system neutralization takes longer / more sorties.**

That distinction is already present qualitatively in the 11-Jun replay and should now be made physical.

---

## 10. Existing 11–15 Jun losses are therefore REOPEN CANDIDATES, not automatically wrong

Current selected / working chain:

11 Jun:
- Japanese all-air irreversible 41–56;
- repair queue 28–42;
- 12 Jun dawn ready 145–179.

12 Jun:
- Japanese irreversible 33–47;
- night additional 3–5;
- 13 Jun dawn total ready 109–136.

SAI B-D+0 04:30:
- total MR 92–118.

These results already credit generic:
- warning;
- dispersal;
- repair.

Therefore site-specific bases may produce:
- similar total effective suppression;
- but different irreversible / damaged / displaced split;
- different island distribution;
- different surviving crew count;
- different later ferry / recovery margin.

Do not assume all Japanese losses fall.

The U.S. may simply redirect more attacks to:
- Marpi;
- Tinian secondary strips;
- Guam support nodes.

---

## 11. Most likely first-order effects if Marpi = M1/M2 and Tinian/Guam depth is explicit

Before detailed replay, likely direction only:

### HIGH confidence
- fewer aircraft trapped solely because Aslito is closed;
- more damaged aircraft have a diversion field;
- more U.S. sorties must be spent on runway / field suppression;
- Tinian / Guam receive more repair / parking congestion;
- Japanese airpower decays less smoothly and more node-by-node.

### MEDIUM confidence
- some current irreversible aircraft losses shift into repairable / delayed;
- experienced pilot loss decreases slightly through better diversion / SAR;
- more ordinary / upper-middle aircraft can be retained forward.

### OPEN
- net fighter MR on SAI B-D+0;
- whether total 11–15 Jun Japanese irreversible losses materially decline;
- whether U.S. losses increase;
- whether one extra local strike becomes rational.

No combat result changes until replay.

---

## 12. Campaign coupling

This base re-audit affects more than the opening fighter battle.

It reaches:

### Ground
- observation / artillery cooperation survives longer;
- air evacuation / liaison;
- Aslito denial / repair fight.

### Fleet
- carrier survivors have more recovery options;
- Marianas shuttle is less brittle;
- damaged aircraft / crews can be absorbed.

### Counterlanding
- more surviving local aviation can cover / observe:
  - incoming reinforcement;
  - boat corridors;
  - offensive counterlanding.

### U.S. FORAGER project
- more CVE / TF58 sortie demand;
- more repeated field suppression;
- later Tinian / Guam invasion still faces functioning Japanese base infrastructure.

Thus Marianas aviation is a core part of the same project-fracture question as the thick ground reinforcement.

---

## 13. Required next close

Before changing the 11–15 Jun air battle:

1. **field board**
   - Saipan: Aslito / Charan Kanoa / Marpi / Flores;
   - Tinian: each meaningful strip;
   - Guam: Orote / Agana / partial third / water-air;
   - Rota / Pagan emergency nodes.

2. **support board**
   - fuel;
   - ordnance;
   - repair;
   - ground crews;
   - power;
   - radar / comms;
   - runway repair.

3. **aircraft allocation**
   - place the existing 10-Jun 192–248 MR onto actual nodes;
   - no new aircraft yet.

4. **U.S. target plan**
   - allocate 11–12 Jun strikes across actual nodes.

5. **loss conversion**
   - air combat;
   - ground destruction;
   - damaged;
   - forced landing;
   - evacuation;
   - repair return.

Only then:
- reconsider whether upper-middle / ordinary aircraft can be added from dated regional / national pools.

---

## 14. Selected close

The old conceptual emphasis:
**fortress + water-air + a few elite fighters**

is no longer adequate.

The Branch Marianas in June 1944 should be modeled as:
**a substantial 200-aircraft-class regional land-air / water-air network with multiple operating and emergency surfaces, deepening repair / dispersal / warning infrastructure, and active interaction with the mobile fleet.**

This does not guarantee air superiority.

It does mean U.S. suppression is attacking a **system**, not simply killing aircraft parked at Aslito.

No existing combat result changes in this file.
