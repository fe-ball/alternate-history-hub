# 18 — 航空機枝・Enterprise技術吸収・1943戦力台帳 forward

> **Authority:** Relaunch R3 supporting / forward-analysis ledger  
> **Status:** mixed CLOSED technical closure + PROVISIONAL conditional 1943 force ledger  
> **Canonical clock remains:** **1942-06-26 約18:00**  
> 本稿の1943年数値は、1942-06-26時点から現行central planningをそのまま延長した場合のconditional forward baselineであり、canonical future factではない。途中で大損害、工場被害、資源不足、作戦変更が生じれば再OPENする。

## 0. 定義とガード

本稿の1943 checkpoint:
- **spring:** 1943-03-31
- **autumn:** 1943-09-30

数え方:
- **combat-capable pool / 実在機:** 訓練専用の完全旧式機・廃棄待ち機を除く、戦闘用途へ戻せる機体
- **first-line / 第一線:** 実戦航空隊・戦隊・航空戦隊へ配当済み
- **serviceable:** 第一線配当機のうち短時間で作戦出撃可能
- prototype / increase-prototype / service-trialは量産第一線へ二重計上しない

国家総生産のguard:
- 史実日本は1942年にcombat aircraft約6,335機 / total約8,861機、1943年にcombat約13,406機 / total約16,693機を生産した。
- R3は国家総生産を魔法的に倍増させるのではなく、**開発時計・機種mix・損耗・serviceabilityを変える**。
- Guadalcanal / historical Midway carrier-aircrew attritionがないため、同じ生産でも1943年の残存在庫は史実より厚い。

---

## 1. O5 / 峰 2000PS級 — production closure

### 技術状態

1941-12-07:
- 145×160mm ×18 = 47.56L
- 2000PS-class early-production / qualification branch exists
- 2150–2200PS growthは開発中
- dry 約915–940kg
- high 30min 約1750–1820PS @6–6.5km

### PROVISIONAL production ramp

| period | 峰2000PS級完成基数 |
|---|---:|
| 1942 Q1 | 18–30 |
| 1942 Q2 | 30–45 |
| 1942 Q3 | 50–70 |
| 1942 Q4 | 80–110 |
| **1942 total** | **180–255** |
| 1943 Q1 | 120–150 |
| 1943 Q2 | 175–220 |
| 1943 Q3 | 240–300 |
| 1943 Q4 | 300–390 |
| **1943 total** | **835–1,060** |

central working:
- 1942 約210基
- 1943 約945基
- 1943後半に90–115基/月級へ到達するが、200基/月級を早期に無料生成しない
- large crankcase / crank / supercharger / reduction gear / 4-blade prop / forging / skilled-machiningがramp gate
- depot / spare / developmentへ18–22%級を残し、完成発動機=完成機数とはしない

主需要:
1. A7M / 烈風equivalent
2. B7A / 流星
3. limited 峰Ki-44 specialist interceptor
4. Ki-67初期量産
5. test / depot / reserve

---

## 2. IJA次期一般戦闘機 — Ki-63 / 二式戦闘機

### project identity

**CLOSED working lineage:**
- 1940 Q2 Ki-43後継 / 次期一般戦闘機study
- Ki-44 general-fighter branchをparentとして拡大翼・燃料・防御・脚・重武装余地を統合
- 1941中に「Ki-44改」から独立projectへ別機化
- historical Ki-62/Ki-63 air-cooled-study numberingとの整合から、R3独立air-cooled project numberは **Ki-63** を採る

**service designation:**
- 1942 formal adoption centralなら **二式戦闘機**
- **「疾風」** はPROVISIONAL official nickname central。分析上のKi-84-equivalent呼称は正本world-internal名として使わない

### 二式戦闘機一型甲 / Ki-63-Ia working production configuration

- engine: 昴二二 1650PS
- 4-blade constant-speed prop 約3.0–3.1m
- wing 約20.5m²
- normal combat mass 約3.30–3.38t、center 3.34t
- max practical mass 約3.65–3.75t
- max speed **635–642km/h、center 約640**
- 5000m **4:35–4:50**
- internal fuel 650–700L
- practical internal range 1200–1350km
- drop-tank range 1750–1950km
- armor / head-back protection
- main tanks self-sealing / fire protection
- practical radio standard

armament:
- early pilot lot: 4×12.7mm acceptable
- production convergence: **2×Ho-103 12.7mm nose + 2×Ho-5 20mm wing**
- Ho-5 production clockを飛ばさず、1942Q3–Q4に武装移行

### production / deployment

1942:
- Q2 pilot / increase lot
- Q3 50–70級
- Q4 100–140級
- **1942 total 180–240、central 約210**

1943 conditional:
- Q1 150–190
- Q2 210–270
- Q3 270–340
- Q4 330–400
- no-disruption annual 960–1,200級までgrowth可能だが、actual allocation / engine / armament / line conversion gateで再監査

role:
- Ki-43 / 九九戦を即全廃しない
- Ki-63 = long-range / field / general air-superiority main successor
- Ki-44 = point-defense / high-speed interceptor branchへspecialize

---

## 3. Ki-44 — O4 mass branch縮小、峰specialist branch

O4 Ki-44はKi-63がgeneral-fighter envelopeを大きく包むため、1942以降の新規大量増産価値が低下。

CLOSED direction:
- existing O4 Ki-44はhome / Manchuria / industrial / point-defenseへ転用
- 新規O4 mass productionは漸減
- 1942H2以後の研究価値は**峰2000PS specialist interceptor**

峰Ki-44 working:
- normal 3.0–3.1t
- wing 18.5–19.0m²
- 650–660km/h
- 5000m 3:35–3:50
- 8km 6:30–7:00
- range internal 900–1100km / drop 1400–1600
- initial 4×12.7mm、growth 2×12.7 + 2×20mm / 4×20mm
- first lot 60–100級をupper practical bandとし、Ki-63一般量産を食わない

---

## 4. IJN fighter branch — 昴零戦 → 烈風、雷電は別財布

### 昴二二零戦

1942H2–1943H1のquantity bridge / first-line standard。

working:
- 昴二二 1650PS
- 3.05–3.10t級
- max **620–625km/h**
- 5000m 約4分級
- 2×20mm + 2×13.2mm
- pilot armor / partial self-sealing / radio + DF
- 20mm ammunition漸増
- 1943H2以降もCVL / second-line carrier / dispersed baseで長く残る

昴三一:
- two-stage / high-altitude specialized
- B-17/B-24迎撃、高高度CAPへ少数配備
- 全面標準化しない

### A7M / 烈風equivalent

historical lineageを維持するため **A7M** を使用。
R3では2000PS級発動機欠如による16-shi停止を回避し、峰前提で継続。

clock:
- 1941: 16-shi successor study継続
- 1942 Q3: first flight central
- Q4: increase prototypes 6–10
- 1943 Q1: land service trial / carrier qualification preparation
- Q2: pilot production 20–30
- Q3: 40–60
- Q4: 70–90
- 1943 year-end cumulative production / trial pool **150–180級** central

working configuration:
- 峰2000PS
- normal 4.0–4.15t
- wing 26.5–27.5m²
- 645–655km/h
- 6000m 5:20–5:40
- early 2×20mm + 2×13.2mm
- later 4×20mm growth

role:
- large fleet carriers first
- CVLを無理に即転換しない
- 1943H2から limited first-line conversion

### J2M / 雷電

残す理由は**Kasei production lineを使うspecialist land interceptor**であること。

central:
- short-shaft Kasei + pressure cowl + optimized cooling outlet + ejector exhaust
- long-shaft branchは比較 / secondary
- 1942Q4 pilot production
- 1943 spring 60–90 aircraft physical pool candidate
- 1943 full-year 180–240級
- Midway / Rabaul / Port Moresby / home-defense等へpriority
- Zero / A7M carrier-fighter capacityをland point-defenseへ貼り付けないための別財布

---

## 5. IJN carrier attack / dive branch

### B5N / 九七艦攻

R3でもopening-war standard。
非尾張engineだが:
- installation
- prop
- oil/fuel
- exhaust / cooling interface
- QC / acceptance

はindustry diffusionでhistorical baselineより良い。

1943:
- B6Nへ主力交代
- training / second-line / patrol / smaller-carrier用途へ後退

### B6N / 天山

CLOSED direction:
- Mamoru main試験と**Kasei fallbackを早期並行**
- Kasei fallback aircraftはlate-1941 flight-test可能
- Midway 1942-06には間に合わない
- 1942H2 carrier / torpedo / prop / tail / hook qualification
- 1942Q4 limited operational issue
- 1943 spring first-line transition

尾張/industry diffusionの効き方:
- Kaseiの馬力を魔法的に増やすのではない
- pressure cowl / low-backpressure exhaust / cooling-outlet
- prop / torsion measurement
- oil/fuel installation
- acceptance / teardown / QC
を前倒し

survivability:
- main tank partial self-sealing / fire protection
- crew protectionを初期重量budgetへ
- radio / EMI改善をlate blocksへ反映

### D3A / 九九艦爆

R3で最もhistorical-airframeに近い枝。
改善:
- exhaust
- cowl/oil cooling
- prop governor
- radio
- production QC

ただし固定脚・基本構造・airframe dragは変わらず、1943には正しく旧式化する。

### D4Y / 彗星

- reconnaissance-first
- historical flutter / spar gateは消さない
- 1942 recon production / operational use
- bombing versionはstructural qualification後、1942Q4 service-trial → 1943Q1量産方向
- Atsuta liquid-cooled branchのmanufacturing / maintenance difficultyは残る
- 尾張由来のsystem-measurement文化はradiator duct / oil cooling / exhaust / installationへ波及
- Enterprise / SBD比較はdive brake / bomb displacement / release / gear / maintenanceの成熟に効く
- mass radial conversionを急がず、B7Aへの世代交代を見ながら使い切る

### B7A / 流星

historical requirement / first-flight lineageを維持。
史実でもprototype first flightは1942-05。R3の差は**機体の発明ではなく、峰と成熟化能力が間に合うこと**。

clock:
- 1942-05 first flight
- 1942 Q3 dive / torpedo / structural / carrier-system test
- Q4 increase prototypes 8–12
- 1943 Q1 service trial 12–18
- Q2 pilot production 24–36
- Q3 45–60
- Q4 70–90
- 1943 year-end physical pool **170–200級** candidate

working:
- 峰2000PS
- max 590–600km/h級
- 800kg torpedo or heavy bomb / dive-bomb capability
- 2×20mm + rear 13.2mm
- practical strike range / fuel kept in historical-role class, no magical long-range jump

carrier gate:
- 4t超回収・arresting gear・elevator / deck handlingは別gate
- 1943H1 land-based service-trial first
- Shokaku / Zuikaku first carrier qualification
- Akagi / Kaga major repair時のarresting / handling improvementを利用
- 1943Q3–Q4 limited carrier operation
- existing carriers全部が自動対応とはしない

意味:
- 1943H2から「fighter + torpedo bomber + dive bomber」の三本立てを
  **fighter + multi-role strike + recon**へ移す入口
- B6N / D4Yは過渡期主力として十分価値を持つ

---

## 6. Enterprise exploitation → aircraft / air-defense feedback

### 原則

Enterpriseは日本の設計思想を米式へ置換するものではない。

価値:
- completed comparison standard
- carrier / squadron maintenance practice
- F4F-4 deep wing-fold
- SBD dive / bomb-release / fixed-wing structure
- arresting / elevator / hydraulic
- radar / fighter-direction implementation
- aircraft-status / maintenance / fuel / ammunition paperwork
- aviation-fuel isolation / firefighting / repair-locker

**CONCEPT / IMPLEMENTATION OBSERVED ≠ domestic mass-production qualified**

### 1942H2–1943 feedback

A7M:
- F4F deep-foldのload path / lock / handlingを評価
- F4Fそのものをcopyせず、Japanese spar / gun / fuel / manufacturing constraintでfold depthを選ぶ

B7A:
- SBD dive brake / bomb displacement / release / landing gear / hook / hydraulic servicingが高価値
- maximum speedより**first operational maturity**を押し上げる

B6N / D4Y:
- hook / landing-gear / hydraulic / servicing / parts tracking / checklistへ即効性

carrier air groups:
- engine-hour card
- component-change record
- discrepancy sheet
- illustrated parts list
- specialized-tool policy
を新型機部隊から制度化

serviceability effect:
- 全海軍へ即日普及ではない
- 1943のnew-type unitsで**3–7 percentage-point級**のready-rate improvementを許容
- remote / weather / spares shortageは別gate

---

## 7. Radio / EMI — 「大電力で実用」からsystem-level suppressionへ

### 1941状態の再解釈 — CLOSED

昴二一零戦等の **practical radio + DF standard** は:
- 1600PS-class aircraftの重量余裕
- larger generator / dynamotor
- larger / less compromised radio set
- antenna / wiring / DFの重量許容
- partial installation improvement

により、**pilotが常用する価値のある無線**になったことを意味する。

これは:
- ignition / generator / bonding / grounding noiseを完全解決
- 米軍級のlong-range crystal-clear fighter direction
を意味しない。

### 尾張の寄与

尾張はradio makerではない。
engine / installation側から:
- magneto / high-voltage lead layout
- shield interface
- accessory-case earth
- generator mounting
- filter connection
- bonding strap
- engine-run + radio-on noise measurement
を要求できる。

### Enterprise / F4F feedback

1942H2に完成実装から学ぶ:
- shielded ignition harness
- braided shielding
- bonding jumpers
- panel bonding
- antenna / ignition separation
- generator filtering
- bypass / choke practice
- radio chassis grounding

timeline:
- 1942 summer: captured-system comparison
- autumn: IJN provisional installation / noise-suppression standard
- winter: late Zero / J2M / B6N / D4Y new blocksへ反映
- 1943 A7M / B7A: **EMI / grounding / bondingを初期設計要求へ組み込む**

IJA:
- own air-radio experienceを持つため「Navyから全部輸入」ではない
- Army experience + Owari installation/QC + Navy captured implementationが1942H2以後にsupplier levelで合流

---

## 8. IJA other major branches — 1943 interpretation

### Ki-43 / 九九式戦闘機

- 1939採用済みmature mass fighter
- 550km/h級
- long-range / field-service / low-speed handling
- 1943でもquantity backbone
- Ki-63増勢でproduction priorityは漸減
- initial armamentを全機retroactiveにheavy-upgradeしない

### Ki-61

historical independent liquid-cooled lineageは残る。
ただしR3では:
- Ki-43 quantity backbone
- Ki-44 interceptor
- Ki-63 general successor
が既に存在。

よってKi-61は:
- adopted / combat-used
- second modern fighter line / technical hedge
- **Army next-main monopolyにはならない**
- Ha-40 liquid-cooling / maintenance gateを無料解決しない

### Ki-45

1943までに:
- bomber interception
- long-range sweep / armed reconnaissance
- ground / shipping attack
- night-fighter study
へ任務分化済み。

initial universal typeの成功 / 不成功を次世代specialized twin requirementへfeed backする。

### Ki-46

1940–41から600–610km/h級のmature operational reconnaissance。
1943にはhistorical worldも追いつくため、差はabsolute top speedより:
- early field experience
- photo / ISR doctrine
- radio / maintenance
- operational integration
に残る。

### Ki-21 / Ki-48 / Ki-49 / Ki-51

「historical name = historical performance」ではないが、R3差は新世代fighterほど大きくない。
- installation / cooling / exhaust / radio / QC
- better serviceability / support
が主差分。

### Ki-67

- 峰×2 next-generation heavy / fast bomber branch
- 1943 spring prototype / service-trial
- 1943H2 limited initial production candidate
- twin-engine峰消費が重いためA7M/B7Aとのallocation competitionを必ず計上

---

## 9. 1943-03-31 major combat-aircraft pool — CONDITIONAL PROVISIONAL

### IJN

| type | combat-capable pool | first-line | first-line serviceable |
|---|---:|---:|---:|
| 昴零戦 family | 900–1,050 | 560–650 | 82–87% |
| A6M2-N / N1K water-fighter pool | 90–120 | 55–75 | 68–76% |
| J2M | 55–80 | 30–45 | 72–80% |
| A7M | 18–28 | 0; trial 12–18 | — |
| B5N | 380–450 | 120–160 | 76–82% |
| B6N | 160–220 | 80–115 | 70–78% |
| D3A | 420–500 | 180–230 | 75–82% |
| D4Y | 100–150 | 45–75 | 68–76% |
| B7A | 12–18 | 0; trial 8–12 | — |
| G4M | 480–560 | 280–330 | 70–77% |
| G3M | 220–280 | 60–90 | 65–72% |
| E13A | 350–430 | 210–260 | 75–82% |
| F1M | 280–350 | 160–200 | 73–80% |
| H6K / H8K | 85–110 | 50–65 | 68–76% |

central sum of listed major types:
- combat-capable pool **約3,950**
- first-line **約2,060**
- immediately serviceable **約1,610**

### IJA

| type | combat-capable pool | first-line | first-line serviceable |
|---|---:|---:|---:|
| Ki-43 / 九九戦 | 1,150–1,350 | 720–840 | 80–85% |
| Ki-44 | 190–250 | 125–165 | 76–82% |
| Ki-63 / 二式戦 | 330–410 | 210–260 | 77–83% |
| Ki-61 | 70–110 | 35–60 | 65–73% |
| Ki-45 | 210–270 | 135–175 | 72–79% |
| Ki-46 | 280–340 | 180–220 | 79–85% |
| Ki-48 | 600–720 | 360–430 | 74–81% |
| Ki-21 | 430–520 | 270–330 | 75–81% |
| Ki-49 | 260–340 | 165–220 | 70–77% |
| Ki-67 | 16–28 | 0; trial 8–16 | — |
| Ki-51 | 550–700 | 330–420 | 76–82% |

central sum of listed major types:
- combat-capable pool **約4,560**
- first-line **約2,830**
- immediately serviceable **約2,240**

### combined major-type checkpoint

- combat-capable pool **約8,500**
- first-line **約4,900**
- serviceable **約3,850**

trainer / transport / minor patrol / obsolete training airframes are excluded.

---

## 10. 1943-09-30 major combat-aircraft pool — CONDITIONAL PROVISIONAL

このcheckpointはFive-Go、Arakan、Aleutians、South Pacificで大規模予想外損耗がない場合のみ有効。

### IJN

| type | combat-capable pool | first-line | first-line serviceable |
|---|---:|---:|---:|
| 昴零戦 family | 1,200–1,450 | 760–900 | 82–87% |
| water-fighter pool | 120–160 | 70–95 | 70–78% |
| J2M | 150–210 | 95–135 | 78–84% |
| A7M | 70–110 | 30–50 | 74–82% |
| B5N | 300–380 | 50–85 | 72–80% |
| B6N | 380–520 | 230–320 | 76–83% |
| D3A | 330–420 | 70–110 | 72–80% |
| D4Y | 300–430 | 180–260 | 76–83% |
| B7A | 70–110 | 30–50 | 70–80% |
| G4M | 580–720 | 340–430 | 72–79% |
| G3M | 180–240 | 40–65 | 64–72% |
| E13A | 450–580 | 270–350 | 77–83% |
| F1M | 330–430 | 180–230 | 75–82% |
| H6K / H8K | 105–145 | 60–85 | 70–78% |

central sum:
- combat-capable pool **約5,240**
- first-line **約2,790**
- serviceable **約2,220**

### IJA

| type | combat-capable pool | first-line | first-line serviceable |
|---|---:|---:|---:|
| Ki-43 / 九九戦 | 1,300–1,550 | 760–900 | 80–85% |
| Ki-44 | 240–320 | 155–210 | 78–84% |
| Ki-63 / 二式戦 | 700–900 | 450–580 | 80–86% |
| Ki-61 | 180–280 | 110–175 | 68–76% |
| Ki-45 | 300–390 | 190–250 | 75–82% |
| Ki-46 | 360–450 | 230–290 | 81–86% |
| Ki-48 | 700–850 | 420–520 | 76–82% |
| Ki-21 | 380–470 | 230–290 | 75–81% |
| Ki-49 | 380–500 | 240–320 | 73–80% |
| Ki-67 | 60–100 | 20–40 | 68–76% |
| Ki-51 | 650–800 | 390–480 | 78–83% |

central sum:
- combat-capable pool **約5,930**
- first-line **約3,620**
- serviceable **約2,910**

### combined major-type checkpoint

- combat-capable pool **約11,200**
- first-line **約6,400**
- serviceable **約5,100**

---

## 11. 1943 spring allocation ceilings — no double counting

以下は「追加生成」ではなく、§9 first-line/serviceable poolから切り出すallocation band。

### Five-Go / China launch pool

1943-03下旬 central planning:
- serviceable Army aircraft **620–740**
- fighters **380–450**
- bomber / attack **170–210**
- reconnaissance **50–65**

composition:
- Ki-43 remains numerical backbone
- Ki-63はChinaへ優先して2–3戦隊級へ拡大可能
- Ki-44 point-defense / interceptor
- Ki-46 operational reconnaissanceがoperation pacingへ高い価値

Five-Goへこれ以上積む場合:
- Burma / Manchuria / home defense / training readinessを直接食う

### Burma / Chittagong conditional branch

Arakan central branchがChittagongまで進んだ場合:
- serviceable IJA aircraft **220–280級**
- fighters **120–150**
- twin / attack / bomber **70–100**
- Ki-46 **20–30**
- IJN Bengal seaplane system **20–30 physical、15–22 serviceable級**

Ki-63を全64th-Sentai級で一挙転換せず、九九戦long-range backboneを維持しながらsmall / medium detachmentから拡大。

### IJN carrier-air pool

1943 spring:
- repaired Akagi / Kagaを含むfleet-carrier coreとJunyo/Hiyo/Ryujo/Zuiho等のsecondary carrier poolを持つ
- carrier aircraft **600–700 assigned級**を組み得る
- この数字はSouth Pacific / Indian Ocean / Central Pacificへ同時二重計上しない
- carrier sortie / raidはfleet oiler / DD / crew rest / deck qualificationもgate

### South / Central Pacific fixed-base pressure

South Pacific + Port Moresby + Midway / Central Pacific fixed bases:
- IJN serviceable combat aircraft **600–750級**を長期固定し得る
- ただし全数が同一軸にattack radiusを持つ意味ではない
- radar / radio / seaplane ISR / layered base networkにより、個々のbase aircraft数以上のdenial effectを得る

### Aleutians

1943春のbattle decision前:
- water fighter physical **18–26**
- serviceable **12–18**
- E13A等 recon physical **8–11**
- serviceable **5–8**
- Attu land-strip qualificationが進んでも、large land-air regimentを無料生成しない

---

## 12. 「史実と同様」の意味

### 名前は同じだが中身が明確に違う

- Zero: O4 / 昴、armor / fuel protection / 13.2mm / radio / EMI → historical 1943 A6Mとは別物に近い
- Ki-43: 1939からmature mass fighter、R3運用経験が数年先行
- Ki-44: O4 620km/h級 + specialized role
- Ki-45: task specialization clockが前倒し
- Ki-46: absolute performanceよりearly maturity / ISR doctrineが差
- B6N / D4Y: same lineageだがqualification / maintenance maturityが前倒し

### 本当にhistorical airframeへ比較的近い

- D3A
- E13A
- F1M
- H8K initial Kasei branch
- many Ki-21 / Ki-48 / Ki-51 airframe fundamentals

ただしこれらにも:
- exhaust / cooling
- radio / EMI
- QC
- serviceability / maintenance paperwork
のindustry-wide improvementは乗る。

### R3で戦争に間に合うこと自体が差

- A7M
- B7A
- Ki-63
- limited Ki-67

---

## 13. 1943 carrier force assumption used by this ledger

Akagi / Kaga repair closure is maintained in [15](15-ENTERPRISE-RECONSTRUCTION-AND-CARRIER-BUILDUP-1942.md):

- Kaga: 1942Q4 first-line return central
- Akagi: 1942Q4 / year-end first-line return central
- both operational by 1943Q1 absent new yard shock

Thus 1943 spring carrier calculations do not assume only four operational fleet carriers.

---

## 14. OPEN / re-open gates

The following remain conditional:
- exact A7M / B7A carrier arresting compatibility by individual hull
- N1K / 強風 → 紫電 branch priority relative to J2M / A7M
- Ki-67 actual serial ramp vs A7M/B7A/O5 engine competition
- exact 1943 aircraft allocation after Five-Go / Arakan / Aleutians combat losses
- exact carrier air-group complements after individual carrier refits
- O5 2150–2200PS growth production date
- C6N / later reconnaissance replacement clock

---

## 15. next analytical frontier

Aircraft branch audit is sufficiently closed to feed back into strategy.

Next:
1. Five-Go Phase I force / air allocation and transition gate at Guangyuan / Wanzhou line
2. predicted one-month regroup → Phase II Chengdu / Chongqing timetable and stop conditions
3. FS frozen-base strategy / Milne-Samarai / Solomons base maturity using actual aircraft allocation
4. Aleutians remains closed through winter buildup; re-open at 1943 March maritime interdiction / Komandorski decision
5. Arakan / Chittagong air allocation uses §11 conditional band, not free extra aircraft

Canonical 1942-06-26 operational gates (Enterprise onward tow, Saratoga/Wasp, Midway maturation) remain unresolved and are not overwritten by this forward ledger.


## 16. Five-Go Phase-II X-day前航空戦 — advance reservation

> **Status:** PROVISIONAL interaction reservation, not a fixed future result.  
> **Window:** first-phase consolidation from 1943-07-25級 to Phase-II X-day.  
> **X-day working center:** **1943-09-01級**, allowable window **1943-08-28〜09-05** pending logistics / Allied movement / other-theater shocks.

### 16.1 Why reserve the interaction rather than the outcome

By the Guangyuan / Daxian / Wanzhou first-phase line:
- Japan has pushed Hanzhong / Guangyuan / Wanzhou-area fields into normal fighter / reconnaissance range of Chengdu / Chongqing.
- China can no longer solve air pressure only by withdrawing aircraft farther inland without abandoning the political / industrial / logistics core.
- Chinese air units still have strong incentive to conserve aircraft.
- Fourteenth Air Force has less political / operational freedom to refuse combat because defense of Sichuan bases and support of the Chinese war effort are core missions.
- Allied reinforcement remains constrained by Hump tonnage and by competing India / Burma requirements.

Therefore the expected pattern is **episodic counter-air / interception / base attack**, not continuous maximal sortie rates and not a pre-fixed decisive air battle.

### 16.2 Japanese reserved force envelope

From §11 Five-Go pool, reserve for the pre-X air campaign:
- total serviceable IJA aircraft in China main theater: **520–620**
- fighters: **320–390**
- bomber / attack: **145–180**
- reconnaissance: **45–60**

This is a theater envelope, not a promise that all aircraft sit at Guangyuan.

Forward / near-forward distribution central:
- Hanzhong / Guangyuan northern axis: 35–40%
- Daxian / central-support axis: 15–20%
- Wanzhou / eastern axis: 25–30%
- rear reserve / repair / rotation: 15–20%

fighter mix direction:
- Ki-43 / 九九戦 remains numerical backbone
- Ki-63 / 二式戦 grows through the window; **80–120 serviceable in the China main theater early**, potentially **110–150級 by X-day** if no diversion
- Ki-44 remains smaller interceptor / point-defense / fast-sweep element
- no free additional aircraft beyond §9 / §11 national pool

### 16.3 Allied historical anchor and R3 reservation

Historical Fourteenth Air Force inventory was about:
- July 1943: 182 aircraft / 123 fighters
- August: 180 / 117
- September: 193 / 127

R3 does not automatically multiply this force. It may receive emergency reinforcement, but:
- every extra aircraft still requires fuel / ammunition / spares over the Hump
- India / Assam / Chittagong pressure can compete for the same fighters, transports, engineers and fuel
- Chinese Air Force units can preserve strength more aggressively than US units

Working pre-X Allied combat envelope in Sichuan / China central:
- Fourteenth AF total combat aircraft available to the China theater: **175–220**
- US fighters: **110–145 physical**, typically **75–105 serviceable** depending supply / maintenance / dispersal
- Chinese combat-capable fighters: **60–100 physical**, with a smaller fraction willingly exposed to repeated sweeps
- emergency US reinforcement beyond this range is a **trigger**, not baseline

### 16.4 Operational pattern

Japanese objectives:
1. protect Ki-46 reconnaissance / photo cycle
2. force Allied fighters to reveal / disperse
3. damage runway / fuel / repair nodes enough to reduce sortie generation
4. cover first-phase road / bridge / dump reconstruction
5. suppress daylight movement / artillery concentration before Phase II
6. avoid wasting bomber strength on symbolic city bombing when counter-air / logistics targets are more valuable

Chinese Air Force:
- conservation first
- rise for high-value bomber interception / capital-defense / favorable-warning contacts
- disperse to satellite strips / camouflage / decoys
- avoid routine pursuit of every Japanese sweep

Fourteenth Air Force:
- cannot fully adopt conservation
- selective P-40 / P-38 interception and sweeps
- periodic fighter-bomber / B-25 attacks on Hanzhong / Guangyuan / Wanzhou forward aviation system
- B-24 use remains selective because heavy-bomber fuel / replacement burden is high

### 16.5 Tempo and attrition reservation

Weather / repair / dispersal prevent continuous maximum effort.

Normal-intensity central over roughly five weeks:
- **12–18 major contact / strike days**
- additional small reconnaissance / interception / harassment sorties between them

If no major reinforcement or diversion occurs, planning attrition band before X-day:
- Japanese combat / operational write-offs: **45–70**
- US Fourteenth AF write-offs: **35–55**
- Chinese air-force write-offs: **30–50**
- Allied total: **65–105**

This is an accounting reserve, not pre-written battle results.

Expected qualitative result if the band materializes:
- Chinese aviation shifts further toward preservation
- Fourteenth AF remains coherent and dangerous
- Japan does **not** gain permanent air supremacy
- Japan gains **intermittent / sectoral daylight operational superiority** sufficient for Phase-II ground movement on chosen days

### 16.6 X-day air-condition gate

Phase II does not require destruction of Allied aviation.

Air gate is satisfied if:
- Japanese China-theater serviceable aircraft remain **>=500級**
- fighters remain **>=320級**
- forward Hanzhong / Guangyuan / Daxian / Wanzhou air system is repairable / supplied
- Ki-46 reconnaissance can still obtain regular operational imagery
- Allied fighters cannot impose continuous daylight denial over both Chengdu and Chongqing axes
- Chinese large daytime ground movements remain materially constrained

Air gate fails / X-day slips if:
- Japanese forward-field fuel / road / runway serviceability breaks down
- Fourteenth AF receives a major additional fighter force and sustains it
- another theater forces removal of roughly **80–120 Japanese fighters** or equivalent aviation-support capacity
- a major Allied base-attack cycle destroys enough fuel / maintenance infrastructure to reduce sortie generation for >1 week

### 16.7 Re-open triggers before X-day

Recalculate this reservation if any of the following occurs:
1. major US carrier / South Pacific move changes Japanese strategic priority
2. Chittagong / India requires substantially more IJA aviation than §11 band
3. US diverts a full additional fighter group or equivalent into China
4. Hump throughput materially exceeds / falls below expected 1943 trajectory
5. Chinese Air Force chooses an unexpectedly aggressive decisive battle
6. Japanese Phase-I ground logistics force a Phase-II delay beyond mid-September

Absent those triggers, carry this reservation forward to the Phase-II decision meeting rather than re-simulating every routine sortie.
