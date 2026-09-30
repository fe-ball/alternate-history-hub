# 20/21 Jun night relief — hit probability / radar / moon / mission-logic audit
## 2026-09-30

Status: **SELECTED WORKING INTERPRETATION AUDIT / NOT AUTHORITY / NO CANONICAL CLOCK ADVANCE**

Authority remains **Branch B v100**.
Canonical clock remains **1944-06-16T14:15**.
Files 72–73 remain the selected event realization unless explicitly changed below.

Purpose:
- test whether the selected hits are plausible;
- prevent SG from becoming a magic hit-rate multiplier;
- prevent new-moon darkness from becoming a permanent Japanese blindness penalty;
- make mission objectives control exposure time and therefore cumulative hit probability.

---

## 1. New-moon correction

20 Jun 1944 is effectively exact new moon (~0% illumination).

This matters strongly **before** firing:
- visual detection / classification is poor;
- optical ranging and silhouette-based acquisition are degraded;
- unlit DD / boat / transport movement is harder to read;
- radar advantage is magnified.

It matters much less **after** firing:
- muzzle flashes;
- fires;
- shell splashes;
- star shell / illumination;
- shore flash bearings;
- DD reports
create local visual / bearing information.

Therefore:
**new moon is a phase-dependent information modifier, not a permanent Japanese accuracy penalty.**

---

## 2. SG is not the gun director

U.S. surface-search advantage remains strong.

Use:
**SG -> CIC / plot -> target designation / course-speed estimate -> fire-control director/radar -> gun solution.**

Do not write:
**SG contact = automatic main-battery hit solution.**

For 6-in+ U.S. batteries, Mark-8-class microwave fire-control radar can provide precise range/bearing and radar spotting where actually installed.
For DD / 5-in batteries, appropriate director/fire-control radar channels are separate from SG.

Because the two forward TG58.7 CAs remain unnamed:
- do not assume every possible CA has identical main-battery radar/director quality;
- do assume U.S. systemic radar/CIC handoff remains superior to the Japanese system.

Thus file-72 wording “SG track becomes weapon quality” should be read as:
**SG/CIC track becomes good enough for a fire-control channel to acquire and solve**, not SG itself laying the guns.

---

## 3. Japanese pre-fire detection is not zero

Branch Japanese ships retain:
- Type-22-class surface radar where installed;
- selected improved/pre-series sets on priority hulls;
- common target numbering / report timestamps / simple plotting;
- strong night-surface training;
- Type-93 doctrine.

No SG/PPI/CIC equivalence exists.

Selected interpretation:
- U.S. SG normally reaches **clean track / tactical picture first**;
- Japanese Type 22 / lookouts / prior area estimate can produce **contact candidates / rough bearing-range information before U.S. first fire**;
- U.S. normally reaches **weapon-quality radar-directed gunnery first**.

This is an advantage in track quality / latency, not “U.S. sees, Japan sees nothing.”

---

## 4. First D1 engagement — probability audit

Scenario geometry:
- U.S. main-axis forward element = 2 CA + 4 DD;
- Japanese D1 = 2 combat DD;
- initial clean SG contact mid/high-teens nmi;
- firing solution around ~12–15 nmi;
- both sides maneuver;
- D1 mission is torpedo release / corridor creation, not gun duel.

These are **modeling bands, not historical measured hit percentages**.

### U.S. gunnery against D1
For the short first-fire interval:

Probability at least one D1 DD receives useful light/medium damage:
**~55–75% class**.

Probability of a mission-kill / sinking before D1 completes torpedo release:
**~15–30% class**.

Therefore file 72:
- one D1 DD medium damaged;
- no D1 sinking before release
is a reasonable selected center.

Do not import Washington-vs-Kirishima shell hit percentages:
that was a much larger target, shorter/favorable range and unusually stable radar-directed firing opportunity.

---

## 5. Type-93 first salvo

Assume:
- two D1 DD;
- ready torpedo batteries;
- launch after U.S. first fire / during maneuver;
- practical release geometry roughly ~10–13 nmi preferred, with longer launch possible but lower-quality;
- U.S. is already aware of Japanese torpedo risk and maneuvers.

Selected engagement probability:
- if launch quality is good / nearer the ~10–13 nmi band: **~30–50%** chance of >=1 damaging torpedo hit in the forward group;
- if release occurs nearer ~13–15 nmi after radical U.S. maneuver has begun: **~20–35%**.

Thus file-72’s one U.S. DD Type-93 hit is:
**plausible selected realization, but not a deterministic >50% expectation.**

Keep it.
Do not use that hit to imply Japanese torpedo “accuracy” exceeded U.S. radar gunnery.
A single Type-93 hit has much greater ship-level consequence than a single shell hit.

---

## 6. Long-range heavy-gun exchange

### Yamato/Musashi 20–22 nmi counter-interdiction
Targets:
- maneuvering CA/DD group;
- incomplete Japanese track;
- short pulse;
- Japanese ships maneuver after firing.

Selected direct-hit probability per short pulse:
**low, ~0–10% class**.

Therefore:
- no 46-cm direct hit center
is correct.

Its principal effect is:
- forcing maneuver;
- interrupting pursuit;
- enlarging safety distance;
not expected direct destruction.

### Lee vs Japanese heavy cover
If Lee obtained a stable Mark-8-quality battle-line solution and fired sustained salvos at a BB-sized target, the U.S. hit probability would rise materially.

But current event does not do that:
- Lee's mission is Saipan protection / stopper;
- major night battle is not the goal;
- Japanese torpedo threat forces maneuver;
- Japanese heavy cover fires in pulses and moves;
- forward friendly ships complicate fire sectors;
- the geometry is repeatedly broken.

Therefore 0 U.S. BB hits through file 73 is plausible **because exposure time is short**, not because U.S. radar fire control is inaccurate.

Guard:
if a later replay creates >10–15 min of relatively stable BB-on-BB radar-controlled firing at moderate range, **0/0 heavy hits must be reopened.**

---

## 7. CA gunfire exchange

After muzzle flashes / reports / illumination, the Japanese disadvantage narrows.

For a short maneuvering CA exchange in roughly moderate night ranges:

U.S. probability of causing at least one useful hit / heavy near-hit effect:
**~25–45% class**.

Japanese probability:
**~15–30% class**.

This is not a 2:1 universal hit-rate scalar.
It reflects:
- U.S. radar/CIC/director superiority;
- Japanese improved handoff / night training;
- both sides maneuvering;
- short firing intervals.

File 73 currently gives:
- one U.S. CA light-moderate Japanese effect;
- one Japanese CA light-moderate U.S. effect.

Interpret the asymmetry explicitly:
- U.S. effect may center on a real 8-in hit or heavy near-hit;
- Japanese effect should center more conservatively on **heavy near-hit / splinter / local topside damage**, with a direct 20.3-cm hit as a plausible sensitivity.

Thus the current ship-state band can remain, but **do not read the symmetric damage labels as equal gunnery accuracy.**

---

## 8. Inner receiving fight

At ~7–10 nmi-class / illuminated near-shore geometry:
- new moon matters less;
- U.S. radar + illumination + known receiving approaches improves gunnery;
- Japanese shore observation/coast guns make pursuit geometry dangerous;
- cargo DDs are maneuvering and station time is finite.

Selected probability that at least one of the three cargo DDs receives significant damage during the receiving fight:
**~40–60% class**.

Selected probability that one becomes mission-kill class:
**~20–35% class**.

Thus file 73's one cargo-DD 18–22-kt mission kill is:
**aggressive but still inside a reasonable center/sensitivity band**.

Main uncertainty:
the exact inner U.S. NGFS cruiser/DD radar/fire-control roster remains less closed than TG58.7.
Do not increase this loss further without closing that inner OOB.

---

## 9. Nisshin hit probability

Nisshin is:
- much larger than a DD;
- ~26–28 kt;
- radar-detectable;
- a high-value target once correlated.

But:
- U.S. firing windows are intermittent;
- Japanese fast/heavy cover interferes;
- U.S. forward ships maneuver around torpedo / heavy-gun threat;
- Nisshin adjusts station / does not remain a static pier target.

Selected event-level sensitivity during approach + transfer:
- meaningful direct shell hit: **~20–35% class**;
- damaging near-hit / splinter / handling disruption without direct major hit: **~35–55% class**.

Therefore file 73's:
- no direct major-caliber hit;
- one damaging near-miss / light handling damage
is plausible, but is **favorable to Japan rather than inevitable**.

Do not harden it into a universal expected result.

---

## 10. Illumination is a shared environment

Japanese star shell / flare / coast illumination helps:
- target reacquisition;
- handoff;
- torpedo / gun target confirmation.

But once an area is illuminated:
- U.S. optical backup improves too;
- Japanese firing / observer positions become more obvious;
- U.S. counterbattery / visual identification becomes easier.

Thus illumination is not a one-sided Japanese accuracy bonus.

Use it as:
**track-recovery / identification tradeoff**.

---

## 11. Mission-objective audit

### U.S. objective
Primary:
**protect Saipan / prevent useful reinforcement.**

Not primary:
**destroy the entire Japanese battle fleet at night.**

Correct consequences:
- 2CA+6DD forward intercept is rational;
- Lee retains a screened 7-BB stopper rather than emptying all DDs into a chase;
- after Nisshin is detected, the forward group retasks toward the large transport;
- Lee positions to keep Japanese heavy cover from freely holding the corridor;
- the U.S. need not close to suicidal torpedo range merely to sink damaged DDs.

1944 U.S. night doctrine explicitly treats radar as primary and also recognizes that the mission can justify withholding an otherwise attractive damage opportunity.

### Japanese objective
Primary:
**deliver people / compact stores / heavy sustainment.**

Not primary:
**win a decisive fleet night battle first.**

Correct consequences:
- D1 launches torpedoes then breaks contact;
- cargo DDs do not chase U.S. ships;
- Kongo/CA and H1/H2 fire short counter-interdiction pulses rather than pursue;
- Nisshin cuts transfer when holding the station would require accepting a general battle.

Therefore the low number of heavy-gun hits is principally an **exposure-time / mission-choice result**.

---

## 12. Selected judgment

Current 72–73 damage realization is broadly plausible.

No mandatory replay is required.

Interpretation corrections:
1. **SG advantage = first detection / clean track / CIC handoff advantage, not a direct hit-rate multiplier.**
2. **New moon = very strong pre-fire optical-denial condition; its effect decays after firing / illumination.**
3. **Japan may have pre-fire Type-22 contact candidates; U.S. still normally wins the race to weapon-quality radar gunnery.**
4. **One Type-93 DD kill is plausible but is a selected realization, not the statistical default.**
5. **Japanese 20.3-cm effect on the U.S. CA should be read as near-hit/local damage center with direct hit sensitivity.**
6. **0/0 BB hits are plausible only because both missions prevent a sustained battle-line duel.**
7. **Nisshin's no-direct-hit outcome is favorable but credible; reopen if exact geometry gives U.S. CAs a sustained radar firing window.**

Granularity stop:
do not create shell-by-shell hit tables.
Use phase / exposure / target-size / fire-control quality / mission-duration gates.
