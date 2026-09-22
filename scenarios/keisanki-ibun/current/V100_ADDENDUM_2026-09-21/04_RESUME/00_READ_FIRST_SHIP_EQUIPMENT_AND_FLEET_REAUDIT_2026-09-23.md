# READ FIRST — 艦艇装備・改装・個艦台帳 再監査引継ぎ
## 2026-09-23 session handoff

Status: **WORKING / NOT AUTHORITY / NO CLOCK ADVANCE**

- Current authority: **Branch B v100**
- Canonical clock remains: **1944-06-16T14:15**
- This file records the 2026-09-22/23 discussion that reached the chat-context boundary.
- Nothing here promotes post-14:15 event outcomes.
- Do not write these working values back into authority merely because they are numerically detailed.
- Next chat should read this file **before resuming fleet discussion**.

---

# 0. Why the next task changed

The previous mandatory promotion gate — TF58 whole-system ASW meta-audit — **still remains mandatory before any post-14:15 working event line is promoted to authority**.

However, the latest discussion exposed a more basic modeling deficit:

> Japanese surface ships, especially surviving capital ships / cruisers / destroyers / support hulls, are often carried forward from construction or an old refit state while the Branch technical system continued to evolve through 1942–44.

Therefore the immediate next analytical task is now:

> **reconstruct the 1944 Japanese fleet as actual individual hulls with dated refits, equipment, material / electronics / German-link inputs, readiness and location — not as historical hull names frozen at their historical same-date configuration.**

Do this first. Then return to TF58 ASW / post-14:15 event promotion.

---

# 1. Data-layer cleanup already resolved for resume

## 1.1 Current authority identity
Use separately:
- authority_version = **Branch B v100**
- canonical_clock = **1944-06-16T14:15**
- clock_state = OPEN / EVENT-SIMULATION with post-14:15 work **NOT AUTHORITY**
- frontier = fleet hull/equipment re-audit first; TF58 ASW meta-audit still mandatory before event promotion.

## 1.2 Stale metadata
The following are stale for current-state identity:
- scenario README still saying v098 / 1944-06-14T12:00;
- SCENARIO-RULES current pointer still saying v098 / 1944-06-14T12:00;
- import/IMPORT-STATUS current pointer still saying v098.

Their methodological text can remain useful where non-conflicting. They do **not** override scenarios.yaml + v100 authority entrypoint.

## 1.3 Imported source != current force authority
The full v097 source snapshot is provenance / retained-reference material.
A file being canonical inside the old snapshot does **not** automatically make its old force-state values current.

Use the chain:
**v100 > v099 > v098 > v097 > v096 > retained older non-conflicting technical canon**.

## 1.4 Old later-clock ledgers
Do not restore old July/August force states merely because they reached a later historical date.
In particular, old "1944 July Marianas availability" ledgers are not current force authority after the clock rollback/resync.

## 1.5 Mutsu conflict
Old retained documents that kept the historical 1943-06-08 Mutsu explosion are **SUPERSEDED**.

Current v098 structural settlement:
> **Mutsu: ALIVE. Do not reopen explosion history.**

The old Mutsu technical reconstruction / 1942 state remains useful where non-conflicting; the old loss result does not.

---

# 2. Current national battleship physical wallet

Derived from current structural settlements and surviving-hull ledgers, with no later current-branch loss found:

1. Yamato
2. Musashi
3. Nagato
4. Mutsu
5. Kongo
6. Haruna
7. Hiei
8. Kirishima
9. Fuso
10. Yamashiro
11. Ise
12. Hyuga

**Physical = 12** is the safe national wallet for the re-audit.

This does **not** mean:
- 12 serviceable;
- 12 crewed;
- 12 mission-ready;
- 12 in the Marianas theater;
- 12 with identical modernization.

Shinano remains a future battleship-construction line, not part of the 12 physical operational hulls.

---

# 3. Method for every ship from now on

For each hull, separate:

1. **physical**
2. **serviceable**
3. **crewed / worked-up**
4. **mission-ready**
5. **actual location / assignment**
6. **fuel / ammunition / spares**
7. **damage / repair clock**

And reconstruct equipment in this order:

### Layer A — what the Branch could technically do by that date
- weight / KG / longitudinal-strength calculation;
- power / switchboards / feeder segregation;
- cable routing / ventilation / cooling;
- radar room / antenna / plotting;
- mechanical fire-control + electronic residual correction;
- radar/optical I/O;
- stable vertical / servo;
- pumps / firemain / drainage;
- steering / emergency steering;
- local splinter protection;
- AA ammunition supply;
- machinery / shaft / fuel economy;
- maintenance / fault-isolation;
- damage-control doctrine.

### Layer B — what the individual hull actually received
Trace:
- real yard windows;
- Branch battle damage;
- installation date;
- removal date;
- equipment availability;
- production wallet;
- dock / skilled-worker cost;
- training / work-up cost.

Never convert "technically available" directly into "installed."

---

# 4. Branch-wide causal inputs that must be included in refits

## 4.1 Computation
Computation helps:
- design-space comparison;
- weight/KG bookkeeping;
- vibration / heat / tolerance analysis;
- fault/lot statistics;
- acceptance inspection;
- test feedback;
- power-load analysis;
- calibration;
- repair diagnosis.

It does not create:
- nickel;
- machine tools;
- gun mounts;
- directors;
- trained crews;
- dock time;
- production capacity.

## 4.2 Axis submarine liaison / Penang–Sabang system
Realized / retained chain:
- I-30 complete return in late Oct 1942 with German technical cargo;
- Würzburg precision tracking / servo / calibration / director-integration references;
- Metox-class metric RWR;
- optical / AA / fire-control / metrology / precision-tool samples;
- U-180/I-29 Apr 1943 becomes a second-pass answer package;
- RO-500 gives welding / machinery-mounting / vibration / maintenance comparison;
- I-8 Dec 1943 return adds tacit calibration / fault-diagnosis / test-equipment knowledge;
- Penang primary, Sabang secondary liaison/service system.

Use this as **card completion / design-space pruning / field-service improvement**, not a national scalar bonus.

Do not backdate later German hardware.
Do not create SG/PPI/CIC equivalence.

## 4.3 New Caledonia strategic minerals
Current retained materials settlement:
- NC nickel does **not** solve Japan's national nickel shortage;
- selective high-value allocation is allowed;
- 1943 research/special allocation can reach Ni-equivalent 20–40 t class.

For ships, the natural uses are:
- bearings;
- valves;
- pumps;
- generator / auxiliary machinery;
- high-temperature parts;
- springs / contacts;
- precision tooling;
- heat-treated small parts;
- radar/director/servo parts;
- selected repair spares.

Do not turn NC resources into new armor belts or wholesale machinery replacement.

---

# 5. Battleships already audited in this session — WORKING STRONG, not authority

## 5.1 Mutsu
Structural:
- physical YES by v098;
- retain Branch-assisted 1934–36 reconstruction;
- 1942-11 state has no radar;
- 41 cm main battery unchanged;
- good-condition 25.3–25.4 kt trial-equivalent;
- sustained practical 24.7–25.0 kt;
- cruise fuel use ~2–4% better than historical realization.

Working modernization line:
- 1943 summer: Type 21 + first AA / plot / power / DC update;
- 1944 Q1: second electronics / AA / power / DC update;
- 14 cm secondary battery 18 -> **16 center**;
- Type 89 remains **8 guns center** pending fleet mount/director wallet;
- Type 96 25 mm ~**70 class center** before the newly opened 40 mm allocation audit;
- Type 21 x1;
- Type 22 x2 center candidate;
- Type 13 x1 center candidate;
- mechanical/optical main FC remains primary;
- limited residual/radar-optical auxiliary computing;
- crew roughly 1,600–1,660 working class.

Open:
- whether Type 89 rises to 12 guns;
- exact Type 22 variant;
- 40 mm allocation;
- actual 16 Jun location/readiness.

## 5.2 Hiei
Structural:
- survives historical Guadalcanal loss chain;
- most fully re-integrated Kongo-class refit / test hull;
- Branch refit work band: pure reallocation center ~240 t class;
- good-condition 30.7–30.9 kt;
- fuel efficiency ~5–7% better than historical realization.

Important Branch history:
- radar / stable-vertical test lineage;
- Branch NC campaign gives Hiei a real light/moderate damage + repair feedback cycle in 1942;
- by 8 Nov 1942 it is first-line ready again.

Working 1944 line:
- Type 21 by 1942 summer;
- 15.2 cm secondary battery **8 guns center**;
- Type 89 **12 guns center**, subject to common wallet check;
- 25 mm no longer hard-center at 84: hold **70–90 class working band** until 40 mm wallet is closed;
- Type 22 x2 / Type 13 x1 working;
- one Type 22 may plausibly be improved/Mod-4-equivalent pre-series;
- stable vertical ~5–7 arcmin class;
- permanent small electronic residual/I-O aid ~3–6 t class;
- metric RWR/ESM = selected-use candidate, not closed;
- crew ~1,600–1,670 working class.

Do not use historical Hiei sinking damage as future knowledge for the refit.
DC/steering changes must derive from Branch battle experience and general tests.

## 5.3 Kirishima
Structural:
- survives historical Guadalcanal loss chain;
- first full computation-assisted major reconstruction generation, but earlier than Hiei;
- pure reallocation center ~125 t class;
- good-condition 30.6–30.7 kt;
- cruise efficiency ~3–4% better than historical realization.

Branch history:
- no major Santo damage;
- first-line ready by 8 Nov 1942.

Working 1944 line:
- Type 21 after MI / 1942 summer;
- 15.2 cm secondary battery **8 guns center**;
- Type 89 **12 guns center**, wallet check still required;
- Type 96 25 mm **60–78, center ~72** before 40 mm allocation;
- Type 22 x2 / Type 13 x1 working;
- stable vertical 7–10 arcmin class;
- standardized small electronic auxiliary ~2.5–4.5 t;
- metric RWR center = NO / prepared interface only;
- crew ~1,570–1,640 working class.

Interpretation:
- Hiei = teacher / experimental hull;
- Kirishima = standardized production implementation.

---

# 6. "IJN 45+" delayed / unfinished equipment audit — working closure through 1944

The discussion explicitly reopened equipment historically associated with 1945 or late 1944.

Do **not** treat "historically 1945" as an automatic barrier.
Audit why it was late:
- unknown principle?
- design?
- materials?
- machining?
- spring / recoil / feed?
- receiver / power?
- servo / calibration?
- production priority?
- integration / doctrine?

## 6.1 Type 22 improved / Mod-4-equivalent
Working conclusion:
- one of the strongest early-materialization candidates;
- Branch domestic radar maturation + Würzburg calibration / servo / metrology + field service directly attack historical bottlenecks;
- 1944 Q1 prototype / sea trial;
- 1944 Q2 pre-series on highest-priority large ships is plausible;
- 1944 H2 expansion.

At 6/16:
- do **not** give every Type 22 installation the improved standard;
- allow priority hulls to have one improved/pre-series set after individual audit.

Still not SG/PPI/CIC.

## 6.2 Würzburg-derived precision tracking
Use primarily as:
- technical teacher;
- fixed-base / experimental precision tracker;
- source of servo/calibration/director-interface practice.

Do not create a parallel fleetwide German-style radar family if Japanese Type 22 development can absorb the useful cards.

## 6.3 Type 96 25 mm
Policy direction:
- improve QC, alignment, sight, maintenance, ammunition placement and director assignment;
- **do not spend major R&D on a wholesale late redesign**;
- once 40 mm matures, Type 96 becomes cheaper inner-layer / volume weapon.

## 6.4 40 mm Bofors-derived Japanese weapon
This is the highest-value unfinished-equipment rescue candidate.

Reason:
- physical examples already exist from Singapore;
- historical Japanese copy reached test/limited production;
- historical problems were strongly tied to tolerance, springs, recoil/feed, ammunition seating, heat treatment, machining and QC;
- Branch computation / metrology / NC material margin directly help those bottlenecks.

Working production sensitivity — **NOT CANON**:
- 1943 Q3: pilot 0.5–1 gun/month class;
- 1943 Q4: 1–2/month;
- 1944 Q1: 2–3.5/month;
- 1944 Q2: 4–6/month;
- 1944 Q3: 6–8/month;
- 1944 Q4: 7–10/month.

This gives a rough working envelope:
- 6/16 domestic physical ~20–35;
- accepted/serviceable ~14–29;
- free fleet allocation lower after trials/base use;
- 12/31 domestic physical roughly 60–90 class.

Do not hard-canon these counts until a production wallet is actually calculated.

Mount:
- early line centered on simple/single mounts;
- do not conjure US-style powered twin/quad installations.

Fleet implication:
- battleship AA should **not** be finalized as "more and more 25 mm" until 40 mm allocation is solved.

## 6.5 Type 98 10 cm/65
Already a real high-performance weapon.
Branch effect should favor:
- production/rework reduction;
- barrel/liner life;
- mount acceptance;
- director / ammunition logistics;
- spares.

Do not replace every old-ship Type 89 with Type 98.
Likely policy:
- Type 89 for modest old-hull refits;
- Type 98 for new construction / major refits where magazine/hoist/foundation work is justified.

## 6.6 Type 89 12.7 cm
The gun barrel itself is not the critical national bottleneck for adding a handful of mounts.
The actual audit should track:
- twin mounts;
- Type 94 directors / channels;
- hoists / magazines;
- yard time;
- trained crews.

Hiei + Kirishima each reaching 12 guns requires four additional twin mounts total relative to a history where they were lost.
This now looks quite plausible but is **not closed until mount/director wallet is checked across all 12 battleships and carriers**.

## 6.7 Type 1 / Type 5 12.7 cm/50
Working policy:
- continue R&D / test;
- do not make it a 1944 fleet-standard ship AA gun.

Reason:
- Type 89 already exists;
- Type 98 exists and is superior in many AA roles;
- a third full gun/mount/ammunition/hoist family is likely a low-value branch.

This is a good example of computation causing **branch pruning**, not universal acceleration.

## 6.8 AA director / Type 94 upgrade
Strong 1944 Branch candidate:
- radar range input;
- stable vertical;
- improved servo;
- rate aiding;
- dead-time handling;
- target numbering / I/O;
- director-to-director handoff;
- power segregation;
- better fuze setter integration.

Do not invent a completely new US-style Mk37 equivalent.
Treat this as a mature upgrade package to an already capable mechanical system.

## 6.9 Time fuze / automatic setting
Important conclusion:
"no VT" is **not** a fixed forever cap at the historical Japanese time-fuze level.

Branch can improve:
- cam / gear pitch / backlash;
- setter alignment;
- fuze-lot variance;
- temperature / acceptance;
- dead-time estimate;
- deliberate time-bracketing / burst-distribution doctrine;
- multiple battery / director synchronization where useful.

Working target:
- fuze/setter error component materially tighter than historical median;
- do not convert that directly into overall AA hit probability.

Doctrine may choose:
- exact concentration when track quality is high;
- deliberate early/center/late burst bracketing when track covariance is larger.

Direct-hit/contact-fuze contribution is nonzero.
AA effect also includes formation disruption / forced maneuver / passing targets into the next layer.

## 6.10 Radio proximity fuze
1944 fleet combat credit = **ZERO**.

Branch computation helps:
- circuit exploration;
- shock-failure correlation;
- tube / battery lot control;
- potting;
- sensitivity;
- false-trigger testing;
- QC.

It does not magically create:
- miniature shock-resistant tubes;
- compact batteries;
- mass precision-electronics capacity.

Working clock:
- 1944 H1: research / low-acceleration experiments;
- H2: shock-tolerant subcomponents / instrumented large-projectile trials candidate;
- 1945: prototype/pre-series debate becomes plausible.

U.S. VT advantage remains a major relative advantage.

## 6.11 Metric vs centimetric RWR
Metric RWR:
- already Branch-selected operational from 1943.

Centimetric RWR:
- current Feb44 authority says the cm-wave hole remains;
- 6/16 = NO;
- H2 prototype only if actual German hardware/data/personnel gate is achieved;
- by 12/31 selected B/C use is possible only after that physical gate.

Never use metric RWR as SG immunity.

## 6.12 Snorkel
- not standard by Feb44 current authority;
- no 6/16 combat credit;
- German/Penang comparison can accelerate valve/mast/pressure/exhaust/vibration work;
- H2 prototype retrofit to a tiny number of boats is a conditional candidate;
- broader standardization is a later gate.

## 6.13 Type 5 30 mm aircraft cannon
Equipment-only working direction:
- 6/16 prototype/C;
- H2 pre-series hardware plausible;
- Q4 physical pre-series may exist.

Do not assign combat aircraft without the separate aircraft processing-history audit.

## 6.14 Type 5 15 cm AA / guided weapons
- 1944 combat credit = ZERO;
- computation can shorten design / proof work;
- physical forging / mount / test / control-system clocks remain hard;
- late-1944 prototype-progress is acceptable, not operational deployment.

---

# 7. How to treat "VT cap" in future AA adjudication

Do not use:
> VT absent -> Japanese heavy AA fixed at historical effectiveness forever.

Also do not use:
> computation -> Japanese VT in 1943/44.

Evaluate the chain:

1. warning / detection
2. track quality
3. target assignment
4. stable reference
5. predictor / director
6. gun train/elevation response
7. ammunition flow
8. fuze-time computation
9. fuze setting
10. gun / projectile dispersion
11. target maneuver during time of flight
12. burst geometry
13. fragment lethal volume
14. direct/contact hit probability
15. disruption / forced maneuver
16. handoff to 40 mm / 25 mm / fighters

Branch can materially improve 1–10 and 12/15/16.
It cannot fully eliminate 11 with a time fuze.
Radio proximity fuzing attacks that remaining post-launch geometry problem directly.

Therefore:
- U.S. VT remains a real and important advantage;
- Japanese time-fuze heavy AA can still improve substantially above historical median;
- a mature 40 mm middle layer can compensate for part of the system gap without erasing the VT difference.

---

# 8. Next fleet-audit scope — not battleships only

The next chat should rebuild the fleet by hull class / individual hull where necessary.

## 8.1 Battleships
Continue after Mutsu / Hiei / Kirishima:
- Ise / Hyuga — highest priority because non-aviation conversion creates a completely different 1942–44 refit path;
- Nagato;
- Fuso / Yamashiro;
- Kongo / Haruna;
- Yamato / Musashi confirmation under the new equipment wallet.

For each, determine:
- 40 mm vs 25 mm;
- Type 89 vs Type 98;
- Type 22 normal vs improved;
- Type 13;
- director channels;
- power / DC / crew;
- yard / work-up clock.

## 8.2 Heavy cruisers
National physical survivor direction is much larger than history.
Audit:
- Takao / Atago / Maya / Chokai individually;
- Myoko class;
- Tone class;
- Mogami class with **no automatic aviation-cruiser conversion**;
- Furutaka / Aoba survivors;
- Ibuki heavy-cruiser completion line.

Guards:
- Maya historical Rabaul-damage AA conversion does not auto-occur;
- Mogami historical aviation conversion does not auto-occur;
- refit state must follow actual Branch damage / dock windows.

## 8.3 Light cruisers
Audit:
- old 5500 t classes;
- Kitakami / Oi;
- Agano / Noshiro / Yahagi;
- Oyodo;
- Isuzu.

Guards:
- Kitakami only is the 40-tube demonstrator line;
- Oi remains normal CL unless separately changed;
- Isuzu historical AA/escort conversion must be causally revalidated;
- old 5500 t ships are not to be treated as new 35-kt cruisers.

## 8.4 Destroyers
Rebuild:
- Fubuki / Akatsuki;
- Hatsuharu / Shiratsuyu;
- Asashio;
- Kagero;
- Yugumo;
- Akizuki;
- Shimakaze;
- Matsu / escorts.

Need:
- actual survivors;
- construction completions;
- radar;
- AA;
- Type 93 reload state;
- second-salvo machinery / doctrine;
- sonar / ASW equipment;
- current fuel / escort allocation.

Do not reuse old rounded DD totals without rebuilding commission/loss logic.

## 8.5 Carriers / seaplane tenders
Hull equipment must also be audited, even though air-process audit is separate:
- Shokaku / Zuikaku / Hiryu / Soryu / Taiho;
- Junyo / Hiyo / Ryuho / Ryujo / Zuiho / Shoho;
- Chitose / Chiyoda remain seaplane tenders/mobile water-air bases;
- Unryu / Amagi hull completion != combat-ready carrier;
- deck / radar / power / AA / DC refits still need dated hull treatment.

## 8.6 Repair / oilers / tenders / logistics
Do not leave support hulls as background.
Audit:
- Akashi / repair capability;
- large AO / tanker survivors and actual 16 Jun locations;
- ammunition / supply / seaplane support;
- damage-repair nodes;
- fuel transfer equipment;
- escort / ASW demand.

The post-14:15 surface/ASW problem depends heavily on these hulls.

## 8.7 Submarines / escorts
Submarine technical state intersects the mandatory TF58 ASW meta-audit.
Keep separate:
- conventional patrol boats;
- SenTaka;
- I-400 family;
- liaison/cargo boats;
- escort / kaibokan / ASW screen.

Do not flatten all Japanese submarines into one effectiveness multiplier.

---

# 9. Mandatory source packet for the next chat

Read current authority first:
1. 'scenarios.yaml'
2. 'current/00_CURRENT_AUTHORITY/00_READ_FIRST_CURRENT_V100_2026-09-21.md'
3. 'current/V100_ADDENDUM_2026-09-21/00_HANDOFF/00_READ_FIRST_V100_FULL_HANDOFF.md'
4. 'current/V100_ADDENDUM_2026-09-21/01_AUTHORITY/V100_SUPERSESSION_AND_STATUS_MAP.md'
5. this file
6. 'current/V100_ADDENDUM_2026-09-21/04_RESUME/NEXT_FRONTIER_1944-06-16_1415.md'

Then current structural / technical overlays:
7. 'current/V098_ADDENDUM_2026-09-19/03_SESSION_UPDATES/01_PERSONNEL_FLEET_SURVIVAL_AND_NONCONVERSION_SETTLEMENT.md'
8. 'current/V096_ADDENDUM_2026-09-17/03_SESSION_UPDATES/04_TECH_INTEGRATION_AIR_RADAR_ELECTRONICS_SUBMARINE_1944-02-25.md'
9. v099 anti-magic / aircraft processing guard where carrier aircraft quantities enter.

Then retained fleet / technical canon:
10. 'V094_ADDENDUM_2026-09-15/03_SESSION_UPDATES/02_FLEET_LEDGER.md'
11. 'V051_ADDENDUM_2026-09-05/03_SESSION_UPDATES/BRANCH_B_SURFACE_HULL_DIFFERENCE_WATCHLIST_v001.md'
12. 'V052_ADDENDUM_2026-09-05/03_SESSION_UPDATES/BRANCH_B_YAMATO_MUTSU_1942-11_REAUDIT_v001.md'
13. 'V052_ADDENDUM_2026-09-05/03_SESSION_UPDATES/BRANCH_B_HEAVY_GUN_PROJECTILE_MATERIALIZATION_1934_1942_v001.md'
14. 'CURRENT_1943-11-05_UPDATES/BRANCH_B_AXIS_SUBMARINE_LIAISON_CASCADE_MERGE_1942-10_TO_1945_v001.md'
15. 'AXIS_SUBMARINE_TECH_TRANSFER_REAUDIT_1942-1944_v001.md'
16. 'MATERIALS_NICKEL_TURBO_JET_1944SPRING_v001.md'
17. 'TECH_INDEX_v009.json'

Also locate by filename in the retained legacy canonical snapshot:
18. '10_計算援用水上艦設計.md'
19. '11_水上艦_最上型・変則艦・生残旧艦.md'
20. '30_艦載計算機・光学・電探・I-O連鎖.md'
21. '31_魚雷・水雷戦_魚雷本体・射撃指揮・再装填・運用.md'
22. '41_艦艇対潜_探信・爆雷・護衛運用.md'
23. '62_艦艇戦力評価_任務係数・艦隊運用・戦史再監査v3.md'

Some retained paths are mojibake/nested in the complete source snapshot. Search by exact basename; do not infer authority from directory depth.

When exact historical yard dates / historical hardware specifications are needed, re-verify them externally from strong sources (CombinedFleet TROMs, NavWeaps, NHHC/USNTMJ, etc.) before turning them into a Branch dated refit. Do not treat transient chat citations as canon without rechecking.

---

# 10. Next-chat recommended sequence

1. Re-read the packet above and confirm authority / clock / frontier separately.
2. Close the **common equipment wallet** first:
   - Type 89 twin mounts + Type 94 directors;
   - Type 98 10 cm complete mounts/directors;
   - 40 mm production / accepted / allocated;
   - Type 96 residual role;
   - Type 21 / Type 22 normal / Type 22 improved / Type 13 set production;
   - stable vertical / electronic auxiliary / RWR quantities;
   - shipboard generator / switchboard / power-upgrade practical limits.
3. Continue individual battleship audit:
   - **Ise / Hyuga first**;
   - then Nagato;
   - Fuso / Yamashiro;
   - Kongo / Haruna;
   - Yamato / Musashi reconciliation.
4. Audit CA -> CL -> DD -> carrier/seaplane-tender hull equipment.
5. Audit support hulls / oilers / repair / supply.
6. Build the 1944-06-16 national **physical / serviceable / crewed / MR / location** ledger.
7. Only after the fleet ledger is coherent, return to:
   - TF58 whole-system ASW meta-audit;
   - post-14:15 event-line promotion;
   - 17/18 Jun surface-action gate.

---

# 11. Guards

- No future knowledge.
- Historical same-date equipment is a reference, not an automatic Branch state.
- Historical post-damage conversions do not auto-occur if the causal damage did not occur.
- Conversely, absence of a historical emergency conversion does **not** freeze a survivor in 1941 configuration.
- Construction completion != work-up != serviceable != mission-ready.
- Physical equipment existence != national quantity != installed equipment != trained use.
- Do not multiply computation + German tech + NC materials as independent scalar bonuses if they feed the same intermediate process.
- Do not award every rescued 1945 technology simultaneously; prune low-value parallel branches.
- U.S. SG/CIC/VT/5in38 systemic advantage remains real.
- Mature Japanese time-fuze / director / 40 mm layers can improve substantially without erasing the U.S. VT advantage.
- Post-14:15 working event results remain **NOT AUTHORITY** until explicit promotion.
