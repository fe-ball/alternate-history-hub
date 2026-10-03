# POST-V26 FT / Q1 ATTRITION / INDIAN OCEAN WORKING HANDOFF — 2026-10-04

**Axis:** `asai-china-war-v24-v26-post-v26`  
**Canonical historical authority:** V26 remains unchanged.  
**Canonical clock:** `1941-12-07T14:30:00-10:30 HST`.  
**Status:** **WORKING HANDOFF ONLY — NO CANON PROMOTION.**  
**Parent working handoff:** `16-POST-V26-FT-PEARL-FORCEZ-WORKING-HANDOFF-2026-10-02.md`.  
**Campaign guard:** the existing MO replay-local branch through 1942-04-30 remains preserved but is **frozen** while this FT/Q1/Indian-Ocean re-audit is propagated. Do not silently overwrite later MO outcomes before the re-audit reaches them.

---

## 0. Purpose

This handoff records the 2026-10-02 through 2026-10-04 discussion that:

1. redefined FT accuracy and miss behavior away from a Fritz-X-like 2D impact model;
2. separated FT HE / SAP / IR / GR roles and clarified the limited terminal-dip / water-contact branch;
3. moved mixed FT + Type 91 tactical study back into the prewar exercise period rather than treating Enterprise / Force Z as the discovery point;
4. re-audited Pearl/Enterprise, Force Z, Wake/Saratoga, and several 1942Q1 non-decisive anti-shipping actions;
5. created a working 1942Q1 FT production/replenishment ramp;
6. traced indirect operational effects through Makassar, Timor, Lexington/Rabaul, and Lae-Salamaua;
7. reopened the First Indian Ocean operation at the 1942-04-05 afternoon Eastern Fleet search gate;
8. closed the “night IR strike” idea as an interesting technical temptation, **not** the practical mainline;
9. set the next discussion gate to the **Japanese first-strike decision after Force A contact**.

All numerical values below remain WORKING unless an inherited authority is explicitly identified.

---

## 1. Core FT model correction

### 1.1 Do not use Fritz X as the principal analogy

The earlier Fritz-X-style comparison is rejected for FT hit modeling.

FT is not treated as a two-axis point-impact guided bomb. The intended architecture is:

- vertical / height axis: programmed pitch / glide behavior plus radio-altimeter sea-height control where applicable;
- horizontal axis: gyro/course control, target-motion solution, and on IR variants one-dimensional terminal yaw correction;
- longitudinal axis: the weapon continues along its terminal corridor rather than “arriving at one impact point and falling into the sea.”

Therefore the useful error measures are:

1. vertical containment / terminal-height success;
2. cross-track dispersion;
3. target-motion / lead-solution error;
4. target maneuver after release;
5. run-on distance / terminal corridor persistence;
6. IR yaw-correction capture and residual cross-track error.

Do not assign FT one circular CEP and then reuse guided-bomb hit-rate analogies.

### 1.2 Miss-after-passage behavior

A missed FT is not automatically harmless.

Working modes:

- **RUN-ON:** continue terminal flight after the predicted first intersection; useful in open-ocean fleet attack and can create a hazardous corridor through a formation.
- **CUT / SELF-DESTRUCT:** terminate by timer / fuel / programmed destruct after a selected terminal interval; useful where friendly shipping, coastlines or neutral traffic make long run-on undesirable.

No autonomous “choose a second target” behavior is implied.

A standard FT that misses the first ship continues on its set corridor. An IR FT does not become a modern multi-target seeker.

### 1.3 Target aspect matters strongly

Because vertical height is constrained separately, the effective target width in the horizontal hit problem depends strongly on target aspect.

Approximate projected horizontal span:

`effective horizontal width ≈ ship length × sin(aspect) + beam × cos(aspect)`

Therefore:

- bow/stern-on geometry is difficult;
- broadside / large crossing aspect materially increases the horizontal acceptance window;
- “take the side” is an accuracy doctrine as well as a damage doctrine.

This is one reason Type 91, FT, dive bombing and multi-axis pressure can strengthen one another without requiring modern guidance.

---

## 2. Warhead / terminal-profile closure

### 2.1 HE

HE / blast-fragmentation FT is not merely an inferior SAP.

Natural roles:

- destroyers and light combatants;
- transports and auxiliaries;
- carrier hangar-side / exposed aviation systems;
- AA galleries;
- command / communications;
- ventilation and electrical systems;
- exposed topside personnel / equipment.

Main-belt impact on a heavily armored ship is poor use of an instantaneous HE round.

HE remains useful before RF proximity is mature because direct hits against light structure can produce severe system-suppression damage.

### 2.2 SAP / APHE-like

SAP / short-delay FT:

- uses a stronger nose/body and lower explosive fraction than HE;
- seeks light/unarmored side structure, upper hull, hangar side and internal support spaces;
- is not treated as a naval AP shell;
- is especially useful for internal mission-kill damage after target maneuver / AA / flight operations have already been degraded.

### 2.3 Terminal-dip / water-contact branch — LIMITED / NOT GUARANTEED

A high-grade SAP line may test:

- tighter sea-height control;
- a small terminal nose-down bias;
- stronger / optimized nose geometry;
- tolerance to very short-distance water contact before hull intersection.

This is **not** promoted into routine underwater-running performance.

Working interpretation:

- primary goal = reduce “over-the-top” miss and move impact distribution toward lower side;
- accidental water contact immediately before the hull can retain a lucky hit branch;
- no sustained underwater run;
- no guaranteed skip / dive / waterline hit;
- exact nose geometry, wing/tail water-impact behavior and reliable water-contact envelope remain OPEN.

Do not use this branch as a normal bonus in combat replay unless a later dedicated proof/qualification closes it.

### 2.4 RF / proximity

Ordinary impact HE / short-delay HE can plausibly reach demonstration and service use before RF proximity.

RF / proximity HE:

- may have bench / flying demonstration work before the war;
- remains **test-only / non-ordinary forward issue in late 1941**;
- sea-clutter, safe/arm, altitude-system interaction, target geometry and production reliability remain separate gates.

---

## 3. Development and doctrine chronology correction

The old V26:16 interpretation that Enterprise “discovers” FT-Type91 synergy and Force Z is the first deliberate separated attack is **SUPERSEDED for this WORKING thread**.

Use this progression instead:

- **1935–36:** Asai proposes the Type-91-class airborne anti-ship projectile and Navy interface work begins.
- **1936–37:** full-scale inert winged articles; gyro / separation / early ramjet work; paper attack-line and run-on/destruct studies.
- **1937–38:** powered articles; B5N / E5 high-speed drop; fixed and moving-target cross-track measurement; HE static/live demonstrations can begin after physical/fuze gates.
- **1938–39:** FT-G / FT-GR short-range line; HE/SAP comparison; moving-target work; run-on / destruct study; mixed Type91/FT tactical work begins.
- **late 1938–40:** one-dimensional IR yaw-correction branch emerges from measured lateral-miss data.
- **1939–40:** fleet-level / unit-level mixed exercises can compare FT-first, Type91-first, simultaneous/multi-axis and screen-suppression forms.
- **1940–41:** standard FT and selected IR variants mature toward service; target-class allocation and mixed attack cards exist before combat.
- **1941 spring and later exercises:** not the beginning of doctrine, but one later stage; can explicitly war-game 1942 conditions with larger IR stocks.
- **late 1941:** operational doctrine is imperfect but not improvised from zero.

Prewar doctrine can already recognize:

- FT/HE first to degrade eyes / arms / aviation / AA;
- Type91 for underwater mobility / buoyancy damage;
- SAP FT as exploitation / internal mission-kill;
- Type91-first where forcing a target turn is more useful than early suppression;
- IR allocation to attack lines where healthy maneuver makes unguided miss risk high;
- GR/HE use against a key screen ship when opening one corridor is more valuable than attacking every escort.

Do not turn this into perfectly synchronized modern missile doctrine. Command/signaling burden and target motion remain real.

---

## 4. 1941 carrier-aviation baseline retained

Do not silently revert to generic historical aircraft values in later FT replay.

### A6M2 Model 21 — V26 replay coordinate

- Sakae-powered;
- working maximum roughly **543–550 km/h class**;
- 20 mm ×2 + 7.7 mm ×2;
- improved exhaust integration / cooling / vibration / QC;
- improved radio/EMI, formation integrity and boresight / first-burst repeatability;
- **no blanket armor or self-sealing retrofit**;
- not invulnerable.

### B5N2

- Sakae piston line;
- later EX2/QC lots roughly **382–384 km/h class**;
- normal mission range roughly historical order;
- the Type91 400–430 km/h figure is the **weapon qualification envelope**, not ordinary B5N torpedo-attack speed.

### D3A1

- later EX2/QC roughly **391–393 km/h class**;
- ordinary dive 45–60°;
- ordinary ship-target release roughly 450–650 m;
- valid-release and direct-hit chain remains per D3AAUDIT1;
- Type 99 No.25 ordinary/SAP ~250 kg, ~60–62 kg explosive class.

### Type91 Mod2

- ~935 kg;
- ~205 kg Type97 explosive;
- ~41–43 kt / ~2,000 m;
- correct-release stable entry/run ~96–99% at ordinary B5N/G3M/G4M speeds;
- carrier/cruiser-size maneuvering-target post-release hit planning band ~10–18% unless geometry is further constrained.

These baselines were already part of the V26 Enterprise replay. Do not re-apply them as a new bonus.

---

## 5. Pearl / Enterprise — WORKING reinterpretation

### Pearl

No central FT use inside Pearl Harbor.

Retain V26 first/second waves and their ordnance logic:

- shallow-water Type91;
- 800 kg special AP;
- FT retained for a moving fleet / carrier target.

### Enterprise strike

Retain the V26:16 54-aircraft package as a strong working center:

- A6M 18
- D3A 18
- B5N Type91 9
- B5N FT 6
- B5N FT-IR 3

But change the tactical meaning:

- not an accidental discovery of mixed geometry;
- a first major combat execution of prewar mixed FT/Type91 doctrine;
- HE-first / D3A / Type91 / SAP exploitation is already a known option.

Central damage remains qualitatively the same:

- FT direct hits ~4 class across HE/SAP/IR mixture;
- 250 kg-class bomb hits ~2;
- Type91 hit ~1;
- Enterprise afloat but mission-killed;
- no automatic sinking.

Japanese irreversible aircraft losses remain **7–9, center ~8**, not further reduced by re-applying Zero advantages already present in V26.

Later I-75 Type95 hit and Enterprise repair path remain the existing WORKING branch; frontline return remains around mid-April 1942 center.

---

## 6. Force Z — WORKING reinterpretation

Keep the basic Force Z search and strike geometry from post-V26.

Working heavy anti-ship mix center:

- Type91 ~33
- FT ~18
- IR 0 center
- GR 0 center

IR is not central because daylight large targets do not require spending scarce terminal correction.

Revised tactical sequence is more FT-first than V26:16:

- HE FT can begin AA/command/ventilation/electrical suppression;
- Type91 remains principal underwater sinking / mobility weapon;
- SAP FT exploits a degraded / maneuver-constrained target.

Working terminal damage remains broadly:

- Prince of Wales: Type91 ~4, FT ~4–5, bomb ~1;
- Repulse: Type91 ~3, FT ~3–4, bomb ~1.

Strategic result remains Force Z destruction. FT does not become the primary battleship-sinking mechanism.

Japanese aviation loss working center remains low compared with the earlier Type91-only branch:

- immediate ~1–2;
- return writeoff 0–1;
- damaged ~8–13 class.

---

## 7. Wake / Saratoga — WORKING-CLOSE for this thread

### 7.1 Search

H7Y Dec 21 contact and Dec 22 reacquisition skeleton retained.

FT does **not** materially widen the strategic H7Y search fan by itself.

FT can save a few B5N from the anti-ship strike allocation, but this is a diminishing marginal search effect. Central discovery remains dominated by H7Y + E13A / floatplane layers.

### 7.2 Strike baseline

Central Japanese attack:

- A6M 12
- D3A 18
- B5N 18
  - Type91 9
  - FT 9
- total 48

Saratoga is not treated as an FT-naive target:

- CXAM-1 warning exists;
- Enterprise combat reporting provides at least basic warning that B5N can release a winged low-altitude flying weapon at standoff distance;
- mature anti-FT doctrine does not yet exist.

### 7.3 Closed central hit packet

Saratoga:

- FT/HE ×1
- FT/SAP short delay ×1
- 250 kg SAP ×2
- Type91 Mod2 ×1

State:

- heavy mission kill;
- afloat / self-propelled;
- initial 18–20 kt class;
- after isolation/dewatering ~20–23 kt class;
- normal carrier flight operations effectively stopped for the day;
- shaft and rudder survive.

Human loss working center:

- KIA ~95 (band 85–110)
- WIA ~175 (band 150–200)

Aircraft irreversible loss working center ~18 class.

### 7.4 U.S. counterstrike

Most of the improvised U.S. counterstrike leaves the deck before the Japanese attack arrives.

Working counterstrike:

- SBD ~18
- TBD ~8
- fighter escort very small / near-zero center because VF is required for Saratoga defense.

Central Japanese result:

- **Soryu** takes one ~500 lb-class bomb hit.
- Hiryu hull direct hit = 0 center.
- U.S. torpedo hit on Japanese carrier = 0 center.

Soryu:

- after flight-deck / upper-hangar local hit;
- machinery / shaft / fuel main / magazine survive;
- flight operations stopped ~2–3 h;
- local repair ~5–7 days class;
- Japanese aircraft irreversible total for the carrier battle ~9 class.

CarDiv2 major-operation re-entry center remains roughly Jan 16–18 class.

### 7.5 Saratoga repair rebase

Old Mar 5–15 return center is superseded.

New WORKING:

- Pearl return ~Dec 26–28;
- Puget Sound permanent repair through early/mid March;
- flight and deck-system test mid-March;
- combat work-up after physical repair;
- frontline return band **Mar 20–Apr 5**;
- center about **Mar 27**.

Reason: additional FT/HE/SAP damage to hangar-side, electrical, ventilation, aviation-support and personnel/training recovery extends the combat-ready clock more than the ship-float clock.

---

## 8. 1942Q1 FT production / replenishment — WORKING ramp

The opening-war surge is not assumed to start from zero on Dec 8.

Use:

- autumn 1941: advance ordering / materials / supplier positioning as war risk rises;
- Nov operational orders: stronger pre-commitment;
- Dec war decision: full military priority;
- visible finished-output increase: mainly Jan–Mar 1942 after production lead time.

Working service-release monthly bands:

| period | FT-family service release / month |
|---|---:|
| 1941 Q1 | ~35–50 |
| 1941 Q2 | ~50–70 |
| 1941 Q3 | ~70–90 |
| 1941 Oct–Nov | ~90–110 |
| 1941 Dec 8–31 | ~65–85 additional completion |
| 1942 Jan | ~105–125 |
| 1942 Feb | ~125–150 |
| 1942 Mar | ~140–165 |
| 1942 Apr | ~145–175 if bottlenecks do not worsen |

This is a WORKING industrial ramp, not recovered archival accounting.

Relative expansion:

- FT-G / FT-GR expand fastest;
- standard FT expands next;
- IR remains detector / optical-electric / calibration yield limited;
- RF proximity remains test-limited.

Q1 non-decisive use therefore need not treat every FT as a national-strategic one-off round.

Do not infer unlimited issue. Forward distribution, adapters, trained armorers, storage and local acceptance remain gates.

---

## 9. 1942Q1 selective non-decisive use

General doctrine after combat data accumulates:

- ordinary low-value merchant / harbor target -> bombs if adequate;
- important transport / tanker / auxiliary -> FT-G / FT-GR HE can be rational;
- destroyer / light cruiser -> GR/HE or standard FT depending geometry;
- heavy cruiser / large combatant -> standard FT HE/SAP;
- high-speed carrier -> standard FT + selective IR + Type91;
- Type91 retained where underwater kill / mobility damage is worth the torpedo-production and mother-aircraft exposure cost.

“Normal anti-ship ammunition” does **not** mean “use FT on every ship.”

### 9.1 Makassar Strait — Feb 4

Working FT use:

- standard FT ~9;
- IR 0 central;
- HE/SAP mixed.

Central FT direct hits ~2.

Working result:

- Marblehead remains a heavy-damage / theater-exit case;
- Houston receives its existing heavy-bomb damage plus one FT/SAP internal-damage event;
- De Ruyter light damage;
- Tromp no important new damage.

Houston practical repair extends from ~3 days toward **6–9 days**, enough for the central branch to **miss the Feb 15 Timor reinforcement convoy escort**, while still allowing return before the Feb 27 Java Sea action.

### 9.2 Timor reinforcement convoy — Feb 16

Because Houston is absent, convoy AA is materially weaker.

Working strike:

- G4M 35
- H6K 10
- of G4M, ~6 carry FT-GR/HE;
- Type91 0 in this specific working strike;
- IR 0;
- standard ramjet FT 0.

Central GR/HE:

- Mauna Loa: direct hit -> propulsion/support/fire damage -> mission kill -> abandoned/lost later that day;
- Meigs: direct hit -> serious cargo/electrical/fire damage -> transport mission kill but returns toward Darwin;
- Tulagi / Portmar: light or minor damage central.

Japanese losses:

- immediate irreversible ~1–2;
- return writeoff 0–1;
- damaged ~5–8.

Timor strategic result remains failure of Allied reinforcement, but convoy loss and Japanese attrition differ.

### 9.3 Darwin — Feb 19

Do not double-count Mauna Loa; it is already lost in the Feb 16 branch.

Darwin remains primarily a conventional bomb/dive-bomb target.

No large FT expenditure is central.

Working:

- Peary still lost;
- Meigs, already damaged, is finished / sunk in the Darwin raid;
- Portmar damaged;
- Tulagi can take somewhat more damage than history because target distribution differs;
- overall Darwin strategic result remains broadly recognizable.

### 9.4 Lexington / Rabaul — Feb 20

This is the largest Q1 attrition-effect case.

Rabaul FT combat-present working center:

- physical local ~18–24;
- serviceable ~15–20;
- immediate G4M-loadable ~12–16;
- central available ~15.

Japanese G4M strike remains ~17 aircraft.

FT does not erase Lexington radar CAP.

Key correction:

- FT-loaded G4M still must survive outer CAP interception;
- benefit occurs after weapon release because the mother aircraft need not continue to the fleet-center / normal bomb-run overflight.

Working central result:

- G4M irreversible loss ~9 (band ~7–11), rather than near-total historical-like loss;
- 6–8 return, several damaged;
- effective FT terminal runs ~11–13;
- Lexington direct FT/SAP hits ~1 center, 0–2 band.

Lexington damage:

- hangar-side / aviation support / electrical / ventilation local damage;
- flight operations stopped ~2–4 h;
- no machinery / shaft / rudder critical hit;
- no avgas / magazine catastrophe;
- still capable of returning to combat before Mar 10.

Human loss working band:

- KIA ~25–40
- WIA ~50–80

Strategic effect:

- 24th Air Flotilla is badly hit but **not destroyed as an operational cadre**;
- the aviation-replacement component of the historical SR delay is greatly reduced;
- do not assume every other logistical cause disappears.

### 9.5 Lae–Salamaua timing and Mar 10 raid

Working SR landing center shifts toward **Mar 5 class**, with Mar 4–6 band, rather than the historical-like Mar 8 timing.

By Mar 10 (D+5 class), more major transports have completed unloading and withdrawn.

Central already-departed / not exposed in anchorage:

- Kongo Maru
- Yokohama Maru
- China Maru
- Kinryu Maru class

Central U.S. carrier raid still occurs.

U.S. strike ~100–102 aircraft class.

Lae has a small A6M layer:

- physical ~6–8
- serviceable ~5–7
- initial CAP ~2–3

The raid still penetrates.

Working Japanese result:

- Tenyo Maru sunk;
- Kokai Maru heavily damaged / grounded;
- Kiyokawa Maru moderate damage;
- one destroyer moderate damage;
- Yubari / Tsugaru and others light damage class;
- airfield/fuel/support local damage;
- A6M ~3 irreversible including air/ground losses.

Human loss working:

- KIA ~60–85
- WIA ~110–160

This is materially below the historical-like loss level because major loaded transports are no longer concentrated there.

### 9.6 Langley / Sea Witch and Java collapse

Central FT use = 0 for:

- Langley;
- Sea Witch;
- Java Sea fleet battle;
- Sunda Strait;
- Exeter / Encounter / Pope;
- Edsall;
- Pecos.

Reason varies:

- conventional G4M / D3A bombing is already adequate;
- target intelligence does not justify premium ordnance;
- night / mixed surface battle makes air-launched FT inappropriate;
- small highly maneuverable destroyer is an inefficient unguided-FT target unless it is operationally gating a higher-value attack.

Do not add FT just because it is available.

---

## 10. Approximate cumulative numeric effect through Mar 10 — WORKING

Comparison basis: pre-FT post-V26 working branch versus this FT re-audit branch.

### Japanese shipping preserved

At Lae on Mar 10, historical-like major transport loss reference:

- Kongo Maru ~8,624 GRT
- Yokohama Maru ~6,143 GRT
- Tenyo Maru ~6,843 GRT

Old exposed total ~21,610 GRT.

New central:

- Kongo Maru and Yokohama Maru already departed;
- Tenyo Maru remains lost.

Therefore about **14,767 GRT** of Japanese transport hull survives the Mar 10 strike in this branch.

Do not interpret this as extra shipbuilding output; it is avoided loss.

### Allied shipping timing

Timor convoy:

- Mauna Loa ~5,436 GRT
- Meigs ~7,358 GRT

Combined ~12,794 GRT is removed from useful transport service on Feb 16 rather than being lost/finished in the Feb 19 Darwin sequence.

Cumulative sunk GRT by Mar 10 is therefore not automatically +12,794 because the same ships were already historical/old-branch later losses; the main difference is **earlier mission kill / transport-capacity removal**.

### Human-loss direction

Working additive Allied deltas already explicit in this thread:

- Saratoga: +~50 KIA center / +~90 WIA center versus old branch;
- Lexington: +~25–40 KIA / +~50–80 WIA new;
- Mauna Loa Feb 16: +~23–43 KIA / +~42–82 WIA versus historical-like near-miss case.

Do not yet close a final Q1 casualty ledger because Houston additional FT casualties and Enterprise old-vs-new casualty comparison were not fully re-audited.

Working Japanese avoided loss:

- Mar 10 Lae: roughly 45–70 fewer KIA and 90–140 fewer WIA versus the historical-like concentrated-shipping case;
- Feb 20: several G4M crews / aircrew cadres survive compared with near-total loss;
- use crew-seat / unit-readiness language before converting every aircraft saved into deaths avoided.

---

## 11. Indian Ocean operation — force concept retained

Existing V26:12 concept remains:

- a strong, limited-duration western strike;
- not permanent Indian Ocean sea control;
- **3–4 fleet carriers can be sufficient**;
- CarDiv5 is deliberately preserved for MO / eastern operations;
- Ryujo / Bengal Bay force and western bases add pressure after fleet carriers withdraw.

Central carrier force for the reopened tactical audit:

- Akagi
- Soryu
- Hiryu

Kaga remains outside this central branch; Shokaku / Zuikaku are retained for MO.

Central escort/search structure should retain:

- Tone / Chikuma;
- Abukuma;
- BatDiv3 / Kongo-class surface support as assigned;
- destroyer screen.

Exact escort count is still a local OOB confirmation item before damage adjudication.

### Colombo / Cornwall / Dorsetshire

Three-carrier reduction does not automatically erase the Cornwall/Dorsetshire result.

The historical-style 53-D3A cruiser strike is naturally available from Akagi/Soryu/Hiryu.

Central:

- Cornwall sunk;
- Dorsetshire sunk;
- do not spend FT merely to improve an already efficient D3A kill.

Colombo port-strike weight is lower without CarDiv5. FT is not central against fixed/harbor targets where conventional bombs are adequate.

---

## 12. Apr 5 afternoon Eastern Fleet search gate

### 12.1 Search resources

Do not invent a large spare E13A pool.

Morning search reference:

- E7K ×3
- E8N ×2

Tone E7K finds Cornwall/Dorsetshire around 10:00 class.

Tone / Chikuma each launch one E13A for tracking around 10:05 class.

By early afternoon:

- the two E13A are committed / returning from cruiser shadow;
- morning E7K/E8N may be reusable after recovery/service;
- Akagi/Soryu/Hiryu B5N returning from Colombo are the main flexible search reserve;
- D3A are returning later from the cruiser strike.

### 12.2 Second-search rationale

Do not grant a second search merely because the model knows Force A is nearby.

Worldline actor reasons that support a second search:

- Enterprise / Saratoga / Lexington combat history has repeatedly shown the cost of an unlocated enemy carrier;
- two isolated cruisers do not prove the Eastern Fleet main body is absent;
- Japanese command knows British carrier forces exist;
- improved radio/reporting makes search continuation more usable but does not widen visual search cones magically.

### 12.3 Working second-search package

Central planning package after ~14:00:

- B5N search: ~4 (2–6 reasonable band);
- recovered E7K: ~1–2;
- E8N near/mid-range fill: ~1–2;
- returning E13A can later relieve a contact rather than being assumed available for the first outbound line.

Search emphasis: southwest to south-southwest of the Japanese force.

B5N search is a real opportunity cost because the same aircraft are the Type91/FT anti-carrier reserve. FT reduces, but does not erase, that opportunity cost.

### 12.4 Working contact gate

Central discovery branch for continuation:

- second search launches ~14:05–14:15;
- B5N is the most plausible first contact aircraft;
- Force A contact around **15:30–15:40 class**;
- central placeholder: **15:32**;
- initial report identifies a battleship and multiple carriers / cruisers / destroyers at useful operational scale;
- correcting position/course/speed follows within minutes;
- British Albacore can still obtain its own contact later; this is near-mutual discovery, not one-sided omniscience.

Overall “find Force A by 16:00” working probability with this second-search behavior: **roughly 55–70%**, central ~60–65%.

This is a discussion probability band, not a canon stochastic table.

---

## 13. Night IR attack idea — CLOSED AS DESIRE, NOT PLAN

A technically minded faction / individual officers can naturally observe:

> the night contact could be an unusually attractive opportunity to exploit IR terminal yaw correction.

Record this as a **USER-DIRECT / plausible actor desire**, not as the selected operation.

Reasons it is interesting:

- IR correction is most valuable against a moving target when visual geometry is degraded;
- FT vertical control is separate from yaw correction;
- a night strike could in theory reduce some optical-aiming dependence.

Reasons it is **not** the practical mainline to pursue:

- 1942 IR inventory remains scarce and calibration-limited;
- the IR branch is one-dimensional terminal correction, not a mature night target-identification / all-aspect seeker;
- target discrimination among multiple ships at night is difficult;
- friendly / enemy formation geometry is harder to control;
- mother-aircraft navigation, assembly, separation, signaling and recovery burdens rise sharply;
- night carrier landing and recovery risk can dominate the supposed terminal-guidance advantage;
- no existing branch has established a mature routine night carrier FT doctrine;
- daylight / late-afternoon first strike or maintained contact into dawn is operationally more rational than choosing night merely to demonstrate IR.

**WORKING CLOSE: “night IR” remains an interesting technical temptation and possibly a voiced proposal, but is not the central operational choice and should not be intentionally sought as the preferred attack window.**

Do not convert “some officers want to try it” into a night strike order.

---

## 14. NEXT SESSION GATE

Resume from:

**1942-04-05 ~15:32 Indian Ocean — Japanese B5N search has obtained a Force A contact.**

The next discussion begins with the **Japanese first-strike decision**.

Required sequence:

1. actor knowledge and confidence in the Force A contact;
2. Japanese carrier/aircraft state after Colombo + Cornwall/Dorsetshire cycles;
3. available A6M / D3A / B5N by carrier;
4. Type91 / FT / FT-IR / HE / SAP stocks actually combat-present;
5. distance, sunset, weather and return/recovery clock;
6. British Force A state, radar, CAP, Albacore search, ship AA and maneuver;
7. choose first-strike timing / size / ordnance / axes;
8. resolve CAP interception and valid releases;
9. only then assign hits / damage.

The night-IR desire is already closed as a non-mainline proposal. **Do not start the next chat by reopening whether Japan should deliberately wait for night.**

Do not resume the frozen MO / May 1 carrier-contact replay until the Indian Ocean / FT re-audit is carried through or explicitly abandoned.

---

## 15. Stop line

This handoff does **not** automatically change:

- V26 canonical history;
- V26 canonical 1941-12-07 14:30 HST clock;
- the authoritative status of V26:00–04;
- later MO replay-local outcomes beyond the explicit fact that they now require propagation review;
- final Indian Ocean Force A battle outcome;
- final FT production accounting;
- formal FT service designation;
- RF proximity service release;
- terminal-dip / water-contact guaranteed performance.

It preserves the latest working discussion so the next session starts at the Japanese first-strike gate rather than re-deriving FT doctrine or 1942Q1 attrition.
