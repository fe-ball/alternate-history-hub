# Saipan artillery survey / fire-data depth and combat re-registration ledger

Date: 2026-09-26
Status: SELECTED WORKING TECHNICAL LEDGER / NO CAMPAIGN AUTHORITY PROMOTION
Canonical authority remains Branch B v100 / 1944-06-16T14:15.
Approved ground frontier remains 1944-06-16 dawn.

## Air-observation interface

For Japanese aerial ground observation / artillery spotting / photo-confirmation in the Marianas, read `40_MARIANAS_JAPANESE_GROUND_AIR_OBSERVATION_LEDGER_v001.md`. Aerial observation updates target registration and observation freshness but does not replace lost site survey / ballistic data.

## 0. Purpose

Refine the ground replay's artillery/fire-control assumption.

Do NOT assume that Branch computing means every gun on Saipan owns a perfect site-specific fire table for every conceivable position.

Separate:
1. standard weapon ballistic tables;
2. site survey;
3. battery / individual-gun correction data;
4. target registration;
5. current battlefield target data.

The Branch advantage is the ability to prepare and update more of these layers, more consistently, before invasion and during battle. It is not omniscient precomputation.

## 1. Data-depth tiers

### Tier A — heavy fixed / semi-fixed coastal and fortress batteries

Expected preparation depth: HIGH.

Likely prepared before invasion for priority batteries:
- precise battery datum / surveyed coordinates;
- battery altitude and principal azimuth references;
- standard ballistic tables;
- sector limits and dead ground;
- selected site-specific height / geometry corrections;
- range/bearing to major sea approaches and fixed terrestrial reference points;
- charge / propellant-temperature correction procedures;
- barrel-wear / muzzle-velocity correction record where measurements or firing history permit;
- selected alternate observation stations;
- precomputed fire missions on likely beaches, road exits, anchorage/approach zones where mission fits.

For a high-priority battery it is reasonable that the calculation/technical staff has prepared:
- a table for the actual emplacement;
- correction cards based on the battery's accepted initial gun condition / calibration;
- revised corrections after meaningful wear, charge-lot change or observed discrepancy.

Do NOT assume every heavy battery possesses perfect live meteorology, intact OPs, or current target coordinates after bombardment.

### Tier B — priority medium artillery batteries with prepared primary / alternate positions

Expected preparation depth: MEDIUM-HIGH on selected sectors, uneven island-wide.

Likely:
- standard service firing tables;
- surveyed primary position;
- selected pre-surveyed alternate positions;
- battery orientation / datum stakes;
- map-grid-to-deflection/elevation aids;
- registered priority target boxes: beach exits, road junctions, likely artillery positions, tank assembly areas, seams, airfield approaches;
- battery zero / calibration corrections;
- selected position-specific correction sheets for important primary/alternate emplacements.

Less likely to exist comprehensively:
- unique full ballistic solution sets for every possible emergency emplacement;
- individual-gun full correction tables for all medium batteries;
- exhaustive precomputed data for every small ravine/field.

Branch computing makes it plausible to precompute a **family of position cards** for selected alternatives, but the survey / distribution / crew training burden still limits coverage.

### Tier C — ordinary field artillery, infantry guns and mortars

Expected preparation depth: STANDARD TABLE + LOCAL FIRE PLAN.

Likely:
- standard firing tables / range scales;
- local grid and aiming references;
- range cards;
- a limited registered-target list;
- primary and a few alternate firing points in important sectors;
- observed-fire correction records.

Priority mortar cells can have very good local fire cards and registered points without possessing a bespoke full ballistic table for every shell hole.

### Tier D — AT guns, MGs and local direct-fire cells

Expected preparation:
- range cards;
- range stakes / terrain reference points;
- preselected kill zones;
- armor approach lanes;
- flank-fire arcs;
- alternate firing pits/routes.

Do not call these "full firing tables" in the same sense as indirect heavy artillery.

## 2. What computation changes

Branch calculation capacity can plausibly produce:
- standardized worksheets / nomograms;
- conversion between common grid and gun data;
- precomputed primary/alternate-position cards;
- sensitivity tables for site altitude, charge lot, propellant temperature, barrel wear and muzzle-velocity deviation;
- quicker recalculation after a gun is moved within an already surveyed local network;
- faster consistency checks between Army/Navy grids and target numbers;
- better recordkeeping of correction history.

It does NOT create:
- the original survey observation;
- a new OP after the old one is destroyed;
- current wind/temperature aloft without observation;
- intact wire/radio;
- current enemy coordinates;
- exact gun muzzle velocity without firing/measurement/calibration evidence.

The calculation advantage acts after measurements and before orders.

## 3. Per-gun versus battery-level corrections

### Heavy guns
Individual-gun correction is plausible where:
- gun identity is stable;
- barrel wear / firing history is tracked;
- enough test/registration rounds exist;
- technical staff and records survive.

Use:
- individual gun zero / MV/wear correction where traced or selected for high-priority fixed batteries;
- otherwise battery-average correction with wider dispersion.

### Medium batteries
Default:
- battery-level zero / charge-lot / site correction;
- individual gun boresight/alignment correction where available;
- full individual-gun ballistic correction only for priority or technically mature batteries.

### Mortars / infantry guns
Default:
- piece/battery alignment and observed correction;
- no assumption of elaborate individualized ballistic bookkeeping beyond what the weapon/crew can exploit.

## 4. Combat-time fire-data state

Each indirect-fire cell carries five independent states:

1. **BALLISTIC TABLE** — present / damaged / lost.
2. **SITE SURVEY** — CURRENT / PARTIAL / NEW-ROUGH / LOST.
3. **GUN CORRECTION** — CURRENT / DEGRADED / UNKNOWN.
4. **TARGET REGISTRATION** — CURRENT / STALE / LOST.
5. **OBSERVATION PATH** — DIRECT / ALTERNATE / REPORT-ONLY / BLIND.

An intact gun can therefore be physically serviceable but tactically low-value if survey/observation/target data are lost.

## 5. Re-survey / re-registration clocks

These are WORKING planning bands, not measured historical Saipan times.

### Move to a pre-surveyed alternate, references intact
- mortar / light indirect cell: **10–30 min** for useful local fire;
- field/medium battery: **20–60 min** for a useful first solution;
- heavier battery: **30–90 min** depending on lay/orientation and communications.

### Move to a known local position inside an existing survey net, not pre-tabulated
- mortar/light: **20–60 min**;
- field/medium: **45–120 min**;
- heavy mobile/semi-fixed: **1–3 h**.

### Emergency unsurveyed position
- rough map fire may be possible earlier;
- robust surveyed solution:
  - light/mortar: **0.5–2 h**;
  - field/medium: **1–4 h**;
  - heavy/semi-fixed: **3–8 h or more**.

The practical limiter is often survey/reference/communications, not arithmetic.

### Registration on a new current target box
If OP/report path exists:
- one high-value mortar/field target box: **10–30 min** after target identification to useful corrected fire;
- medium/heavy target: **20–60+ min**, ammunition/visibility/counterbattery permitting.

If registration fire would expose the battery, use transfer from a known point / map data with wider dispersion instead of assuming live registration.

## 6. Expiry and correction triggers

Recompute / downgrade data when:
- battery moves;
- OP is lost;
- landmarks are destroyed;
- front line moves into the old impact box;
- charge lot changes;
- barrel wear accumulates materially;
- powder temperature changes strongly;
- rain/soil/route damage changes access or platform conditions;
- counterbattery forces a new firing orientation;
- Army/Navy unit boundary changes create new no-fire zones.

Cratering changes access and landmarks more often than it invalidates the island's underlying geodetic grid.

## 7. Combat rework board — 16 to 18 Jun

### 16 Jun daylight
Main data problem:
- beach-target registrations age rapidly as U.S. units move inland.

Japanese priority:
- retire low-value waterline target cards;
- preserve reverse-slope batteries;
- shift target numbers to Afetna seam, Susupe exits, U.S. 105-mm assembly, tank routes and Aslito approaches.

### Night 16/17
Use surviving survey/control teams to:
- reconnect primary/alternate OPs;
- reorient displaced medium batteries onto pre-surveyed alternates where possible;
- create 1–3 priority new target boxes per surviving fire cell;
- issue updated no-fire boxes around Japanese infiltrators.

### 17 Jun daylight
As U.S. lines deepen:
- transfer fire from original beach grids to road/ravine/airfield-approach reference network;
- identify which batteries still have valid site survey and which are operating on rough map fire;
- use short firing/displacement cycles where counterbattery exposure is high.

### Night 17/18
Highest technical priority:
- re-survey Aslito west/north approach positions;
- rebuild tank/infantry range cards;
- register U.S. artillery and armor assembly boxes;
- prepare eastern/southeastern fallback fires that can interdict the runway even after U.S. physical entry;
- update friendly-risk/no-fire zones.

This night does NOT produce a complete new island fire plan.
It produces a limited number of high-value, current solutions.

### 18 Jun daylight
As U.S. enters portions of the airfield margin:
- old "defend the airfield perimeter" firing data becomes partly obsolete;
- batteries with surviving survey/OP shift to:
  - runway/taxiway interdiction;
  - west/north approach lanes;
  - U.S. artillery resupply;
  - armor movement;
  - road exits east/southeast of the field.

Physical U.S. occupation therefore does not immediately equal safe use of Aslito.

## 8. Data-preparation confidence by weapon/position

Use this default unless a named battery audit overrides it:

| Weapon / position | Pre-invasion site-specific data | Alternate-position data | Individual-gun correction |
|---|---|---|---|
| heavy fixed coastal/fortress | HIGH | MEDIUM where alternate exists | MEDIUM-HIGH |
| priority medium fixed/semi-fixed | MEDIUM-HIGH | MEDIUM | LOW-MEDIUM |
| ordinary field artillery | MEDIUM at primary | LOW-MEDIUM | LOW |
| mortars | LOW as "full table", HIGH as local range/target cards | MEDIUM | LOW |
| AT/MG/direct fire | range-card system, not full indirect table | MEDIUM at planned ambush points | not normally relevant |

This specifically rejects both extremes:
- "Japan only has generic manual tables";
- "every gun has a bespoke precomputed solution for every possible emplacement."

## 9. Ground replay consequence

The fortification advantage should be credited chiefly as:
- faster return to useful fire after displacement;
- more batteries having a second usable surveyed position;
- fewer gross coordinate/translation errors;
- better target-age discipline;
- stronger interdiction after physical terrain loss.

It should NOT be credited as:
- universally higher accuracy;
- unlimited registered fires;
- permanent knowledge of U.S. positions;
- instant recovery of destroyed observers/comms.

This fire-data ledger is the technical layer underneath the 16-dawn -> 18-evening ground replay.
