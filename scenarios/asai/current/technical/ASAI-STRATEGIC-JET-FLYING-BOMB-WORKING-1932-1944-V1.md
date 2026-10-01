# ASAI WORLDLINE — STRATEGIC JET FLYING-BOMB WORKING STUDY — 1932–1944 — V1

**Status:** WORKING TECHNICAL / INSTITUTIONAL STUDY.  
**Authority:** does NOT supersede current technical canon unless a later closeout explicitly promotes individual items.  
**History effect:** NONE AUTOMATIC. Any China/1940–42 operational interpretation in this file is reversible working material.  
**Combat clock:** unchanged.  
**German-transfer ledger:** unchanged.

## 0. Purpose

This note records the technical detour on long-range unmanned jet flying bombs. The core problem is treated as **long-range unmanned navigation**, not as a mature modern guided-missile problem.

The branch is separate from Kayaba's independent ramjet line. Asai may cooperate with Kayaba and may share non-proprietary test, combustion, inlet, ignition, instrumentation and safety data, but Kayaba is not automatically an Asai subordinate and no proprietary production dependency is implied.

## 1. Parent technical anchors

Use current authority for the following parent facts:

- E4 pure-jet flight exists in the 1931–33 period and makes unmanned one-way jet flight a plausible early concept.
- E5-J is the first mature compact pure-jet family, roughly 430–470 kgf class.
- E6-M-J current product authority is roughly 850 kgf non-Ni / 900 kgf selected Ni.
- E6-M-JF current production center is roughly 950–1,000 kgf with materially lower TSFC than the comparable pure-J.
- E5/E6 Twin lines already prove high-speed reconnaissance, radio/photo integration and repeated fixed-target attack.
- German jet technology does not start the Asai/Japanese program. Under the existing ledger, BMW 003, Jumo 004, HWK 509 and related material arrive only on the already-established 1944 clock and serve mainly as design-space reduction / answer-checking.

Relevant current parents include:
- `23-GT-E5-J-JF-INSTALLED-PRODUCT-CANON-V8.md`
- `20-GT-E6S-JF-E7-E9-REBASE-CANON-V8.md`
- `ASAI-E6-TWIN-J-JF-PERFORMANCE-FUEL-FRP-REBASELINE-1939-1940-V1.md`
- `ASAI-E5-DERIVED-E6-FAST-HEAVY-BOMBER-OUTLOOK-1938-1941-V1.md`
- Library/current T53 jet/Kayaba authority.

## 2. Conceptual origin — working, not yet canon

A plausible institutional sequence is:

- **1932–34:** after E4 autonomous jet flight becomes credible, Asai can submit a technical memorandum noting that a one-way unmanned aircraft can trade recovery structure, crew, landing gear and return fuel for range and payload.
- **mid-1930s:** strategic-air advocates in Army/Navy may press for "how far if it need not return?" rather than merely a 500 km tactical weapon.
- **1937–39:** automatic-flight, short-life engine, long-range navigation and full-scale unmanned articles are explored.
- The exact role of Ishiwara Kanji, Yamamoto Isoroku or other named sponsors remains HISTORY/INSTITUTIONAL WORKING and is not promoted here as dated canon.

The important programmatic effect is that the short-range flying bomb can lose economically to reusable Twin aircraft without killing the **long-range strategic research branch**.

## 3. Main technical series — working envelopes

These are first-order design bands, not qualified service specifications.

| working series | propulsion | launch mass | warhead class | fuel class | cruise class | practical one-way range |
|---|---|---:|---:|---:|---:|---:|
| A / theater demonstrator | E5-J short-life derivative | ~1.8–2.2 t | ~0.45–0.60 t | ~0.45–0.65 t | ~560–620 km/h | ~750–1,100 km |
| B / strategic main candidate | E6-M-J short-life derivative | ~3.8–4.6 t | ~0.8–1.1 t | ~1.2–1.6 t | ~620–680 km/h | ~1,300–1,700 km |
| C / long-range strategic candidate | E6-M-JF short-life derivative | ~5.0–6.2 t | ~1.0–1.3 t | ~1.8–2.4 t | ~600–660 km/h | ~1,800–2,400 km |

Interpretation:

- **A** is physically credible but economically weak for ordinary fixed-target work because E5/E6 Twin can repeatedly deliver roughly the same order of payload, abort, retask, return and perform BDA.
- **B** becomes the natural strategic center once the target lies clearly outside reusable fast-bomber/Twin round-trip radius.
- **C** is expensive and mechanically more complex, but at very long range the JF fuel-economy gain can repay its added backend mass. It is a low-volume strategic weapon candidate, not a cheap saturation round.

Do not use these bands as combat availability.

## 4. Navigation architecture

The mainline is layered. It does not require one all-capable onboard guidance computer.

### 4.1 Onboard base layer

Retain throughout:
- attitude gyro / course gyro;
- magnetic compass reference;
- barometric altitude;
- air-log / timer / distance integration;
- simple electromechanical sequencer and servos.

The vehicle can therefore continue toward a preset destination if external aid is lost, with degraded accuracy.

### 4.2 Early external correction

Early development can use a dedicated high-speed Twin as a **navigation/command escort aircraft**:

- flying well behind the weapon group;
- receiving a transponder or beacon response;
- estimating cross-track / range error;
- transmitting small course corrections;
- turning away before the defended terminal area.

Early capacity should be small (a few weapons per command aircraft), not a modern mass datalink claim.

### 4.3 Ground radio navigation

Plausible progressive methods:
1. directional-beam route following;
2. transponder range from a ground station;
3. two or more stations producing range/time-difference route correction;
4. hyperbolic route following where the weapon need only drive a measured error toward a preset value.

The vehicle does not need to calculate latitude/longitude numerically. An analog comparator can output "left/right of programmed route" or "before/after terminal gate."

### 4.4 Terminal offset beacon

A forward Twin may drop a temporary beacon bomb away from the actual aimpoint.

Working logic:
- weapon approaches the terminal area by preset/radio-assisted navigation;
- acquires beacon;
- corrects cross-track or bearing;
- recognizes a predetermined passage geometry;
- resets distance/time;
- flies a programmed offset from the beacon to the attack area.

The beacon is deliberately **not** the impact point. Different rounds can use different offset tables.

A beacon package may also be a delayed-action bomb/self-destruct package, so the radio equipment is not conveniently recovered after the attack window.

### 4.5 Doppler

Do not make self-contained ground-looking Doppler radar a 1930s/early-1940s mainline.

Allowed earlier concepts:
- range-rate estimated from repeated transponder range;
- cross-beam passage timing;
- experimental RF Doppler frequency-shift measurement as a research topic.

Full airborne Doppler navigation radar remains a later technology unless separately re-audited.

## 5. Accuracy interpretation

Do not treat the series as precision point-target weapons.

Working good-condition dispersion logic:
- preset-only long-range flight: area weapon, multi-km to tens-of-km class error depending range/weather;
- periodic external correction: materially smaller area error;
- external correction plus terminal offset beacon: low-single-digit-km-class attack-area concentration is a reasonable research objective.

Exact CEP is OPEN and requires a dedicated error-budget model.

Natural targets are:
- large airfield areas;
- port/warehouse/fuel complexes;
- major rail/logistics nodes;
- broad industrial districts;
- large headquarters/communications areas.

## 6. China / Chongqing operational interpretation — REVERSIBLE WORKING ONLY

A limited number of full-scale or near-full-scale rounds may plausibly be used over Chongqing or other Chinese targets as **real-environment trials**.

This is not promoted to a strategic-bombing effect.

Chinese-side interpretations can plausibly differ by echelon:

- field/AA personnel: Japanese jet/special aircraft failures, damaged aircraft diving in, or strange bombs;
- technical investigators: after intact wreckage, suspicion of an unmanned automatic-flight body;
- a small strategic-intelligence minority: possible long-range unmanned attack experiment, with scale and intent unclear.

Odd delayed-action beacon bombs can be understood primarily as another Japanese nuisance/time-fuze-bomb problem. Reports that some emit radio signals before destruction may generate several competing explanations before the navigation relationship is understood.

Any such use remains too sparse to add a meaningful new strategic-damage multiplier to the already-modeled China bombing campaign.

## 7. German technology guard

Do not alter the existing exchange ledger.

The already-scheduled 1944 German inflow may provide:
- compressor / combustor / turbine comparison;
- control and starting comparison;
- short-life versus long-life production lessons;
- material/manufacturing design-space reduction.

Do **not** silently add:
- V-1 airframes/pulsejets/autopilots;
- X/Y-Gerät;
- Kehl-Strassburg;
- German missile-guidance packages

to the transfer list.

## 8. Status semantics

At the 1941–42 history point, keep distinct:

- capability: plausible / partly demonstrated;
- physical articles: plausible;
- long-range trials: plausible;
- qualification: partial/open;
- adopted: not automatically;
- factory accepted: only where separately recorded;
- service released: not automatically;
- combat-present: only if a later history gate explicitly inserts a trial;
- strategic effect: NONE by default.

## 9. Open gates

1. exact dated Asai proposal / sponsor chronology;
2. detailed A/B/C aerodynamic and cruise-thrust closure;
3. external-navigation error budget and jamming tolerance;
4. beacon architecture and lifecycle;
5. actual procurement/service decision;
6. any history insertion.

**No current campaign replay is changed by this note.**
