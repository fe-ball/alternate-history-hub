# 15 — Enterprise再建・ミッドウェー後工廠負荷・空母建造計画 1942

> **Status:** Relaunch R3 supporting ledger
> **Canonical historical clock remains:** 1942-06-26 約18:00
> **Epistemic guard:** 本ファイルの1942-06-27以後は、6/26時点で合理的に採用されるforward plan / engineering expectationを固定する。記載された将来日付を、clock到達前から「既に成功した実績」としてactor knowledgeへ逆流させない。
> **Scope:** Enterpriseの持帰り・本土再建、ミッドウェー前後で増減する修理・改装負荷、1942以後の空母建造方針。主人公／尾張発動機は艦艇再建の技術主体ではない。

## 1. 基本原則 — CLOSED

- Enterpriseの救難・再建は海軍側の造船・造機・電気・救難専門家が担当する。
- 主人公は尾張発動機の経営・設計・試験・量産で拘束され、艦船用蒸気タービン、減速歯車、長軸、船殻構造の第一専門家でも軍人でもない。具体的な技術移転経路なしにEnterprise設計会議へ介入させない。
- 1942年日本の大型区画接合は、現代的な「完全モジュール船」ではなく、当時すでに進みつつあるblock construction / prefabricated replacement section / 大規模切戻し修理の延長で扱う。
- 主要縦強度材の継手を一横断面へ集中させず、外板・縦通材・甲板・内底等の接合位置を前後へずらす。主要荷重部は当時の日本海軍が許容する鋲接・接合を主体、二次構造では溶接を活用する。
- 「技術的に修理可能」と「戦時にその修理を選ぶ」は分離する。

## 2. Enterprise持帰り線 — CLOSED central forward plan

6/26 18:00のCLOSED input:
- Kwajalein lagoon内でsheltered salvage
- list 7–9°
- progressive flooding arrested / low pump burden
- main propulsion / steering / ship main power dead
- portable / isolated salvage power stable
- hull girderにimminent global failure兆候なし
- 5kt-class onward towはPROVISIONAL

中央計画:
- **6/29前後:** sheltered monitoring / tow-point proof / pump redundancy確認。通常4.5kt前後、良好海況5kt級をnext-stage tow planning speedとして認証する見込み。
- **7/1前後:** Kwajalein出港を中央。
  - primary tow: **Genyo Maru**
  - reserve / logistics: **Kokuyo Maru**
  - **Shinkoku Maruは6/17被雷後heavy-ocean-tow unsafeのため主曳航へ戻さない**
  - **Akashi同行**
  - Urakami MaruはKwajalein側へ戻す
- **7/11–7/12級:** Truk到着を中央。航海中は4–5kt級、海況・ASW対応で一時減速。重大事象がない限り日単位simulationは行わない。
- Trukはfleet yardではない。目的は本土回航用の補強・再調査・pump/power/tow/steeringの改善であり、主機・全配電・空母機能を完成させない。
- **7/22–7/24級:** Truk発を中央。
- **8/10–8/12級:** Kure到着を中央。
- controlled groundingはfailure contingencyであり、正常工程に組み込まない。

上記日付は現在clockから見たcentral forward scheduleであり、実際のinterdiction / weather / tow failureが発生すれば再OPENする。

## 3. 呉入渠で期待する損傷像 — CLOSED central estimate / execution not yet historical fact

Enterpriseが6/4以後の多数の水中爆発を受けながら、Kwajaleinまで生存し、さらにTruk・本土まで曳航可能であることを条件付き証拠とする。

中央見積もり:
- hull main longitudinal strength: **repairable**
- 外板・frame・floor・bulkheadには大規模局所損傷がある
- keel / principal longitudinal structureの長距離連続破断は置かない
- 4 shaft lineのうち**少なくとも3系統で単純なshaft straighteningだけでは終わらないalignment error**
- そのうち**2系統程度でbearing foundation / shaft-support / strut側の変位を伴う**
- rudder / stern structureの正確な交換範囲は入渠実測までOPEN

重要:
- 「四軸原状復旧は物理的に不可能」とはしない。
- 問題は、船体修正 → foundation / strut修正 → shaft測定・矯正 → 再alignmentを4系統について反復する工程が、戦時修理として長く、予測しにくいこと。

## 4. Enterprise再建方式 — CLOSED central forward plan

### 4.1 原状復旧方針
**Yorktown級の米式propulsion plantを戦闘用に完全原状復旧する案は中央では採らない。**

理由:
- 多数のunderwater shock / flooding後の長軸4系統を完全復元する工程がcritical path化する
- 米式boiler / turbine / reduction gear / electrical systemの予備品・保守体系を長期に抱える
- 日本側既成機関を使う方が完成後の整備・補給予測性が高い

### 4.2 鹵獲機関と再利用を分離
米Babcock & Wilcox boiler、turbine、reduction gear、switchboard等は**技術鹵獲物**として扱う。

- 9 boilerは原則取り外し対象
- 少なくとも1基は可能な限りcomplete specimenとして保存
- 別個体は分解研究、材料・tube/header・superheater・burner・feedwater等を調査
- turbine / reduction gearも「Enterpriseへ再使用する価値」と「技術調査価値」を別判定
- 技術成果の取得はEnterpriseの再就役成功に依存しない

### 4.3 日本式plant
中央採用:
- **6 boiler**
- **104,000shp-class**
- **4 shaft**
- 陽炎／夕雲系の52,000shp plant二組相当を設計・製造基盤として利用
- boiler / turbine / reduction machineryの量産系を転用するが、Enterprise用shaft / bearing / stern tube / strut / propeller / foundationは専用設計する

これは「駆逐艦の機関室をそのまま二つ貼る」意味ではない。既成の造機系列を空母用配置へ再設計して用いる。

### 4.4 長軸
- 旧米shaft 4本を全数矯正し原状復帰する案は採らない
- 修理済み船体を基準として**新造shaft lineを据える**
- 長軸そのものを日本側が技術的に忌避するとはしない
- 教訓は「被雷・船体変形後の長軸全数矯正はrepair scheduleを不安定化させる」

### 4.5 replacement blocks
中央方式:
- damaged engine foundation / shaft alley / shaft-support regionを健全部まで切り戻す
- 必要な後部構造を複数の大型prefabricated replacement sectionsとして別作業場で並行製作
- dock内で本体へ接合
- rudder post / extreme sternが健全なら保存し、損傷が大きければreplacement scopeを後方へ延長
- exact cut stationは入渠surveyまでOPEN

## 5. Enterprise再建工程 — CLOSED central planning band

**改装工事は「最短奇跡」でも「慎重すぎる長期化」でもなく、中庸工程を中央とする。**

| 時期 | 中央工程 |
|---|---|
| 1942-08-10〜12級 | Kure arrival |
| 08-15〜09-05級 | 大入渠 / complete survey / 米機関・shaft・boiler判定 |
| 09月上旬 | 日本式104,000shp再建造へ正式移行 |
| 09〜11月 | 米boiler / main machinery / old shaft撤去、損傷構造切戻し。新block / machinery側を並行製作 |
| 11月〜1943-01月 | underwater hull恒久修理、new foundation / shaft-support replacement sections接合 |
| 1943-01〜03月 | boiler / turbine / reduction gear、steam/feed/condenser、essential electrical / steering接続 |
| 03月末〜04月 | 再入渠、最終shaft alignment / propeller / rudder / bottom inspection |
| 05月 | main sea trials |
| 06〜07月 | elevator / arresting gear / aviation fuel / flight operations trials |
| **08月級** | **limited operational readiness central** |

planning band:
- 上振れ: 1943-06〜07級 limited readiness
- 中央: **1943-08級**
- 難航: 1943-10〜12級

1943年春の戦闘空母復帰は中央には置かない。

## 6. 完成性能 — CLOSED central target

- installed power: **104,000shp-class**
- maximum speed target: **30kt-class**
- expected trial band: **29.5–30.8kt**
- 28kt級を無理なく戦時運用できればfleet-carrier valueは成立
- 31kt以上は上振れ
- 32–33ktのYorktown原速力を工期延長して追わない

日本側は「元どおりのEnterprise」を完成条件とせず、**日本式plantで維持可能な30kt級fleet carrier**を完成条件とする。

## 7. 呉船渠占有 — CLOSED planning rule

Enterpriseを1942-08から1943夏まで大型dockへ据え置かない。

中央:
- first heavy-dock period: 1942-08中旬〜12月級
- 水中船体、大規模切戻し、replacement section接合を終えたら浮かせる
- 1943-01〜03は艤装岸壁中心
- 1943-03末〜04に2–3週級のfinal redockingを計画

dock occupancyとfitting-out laborを分離する。

## 8. 電気・航空艤装 — CLOSED planning rule

全船内配線を日本規格へ一律交換しない。

- essential generation / distribution backbone
- steering
- firemain / DC pump power
- combat radio / radar
- damage-control essential services

は日本側が責任を持って再構成する。

生存している:
- branch circuits
- motors
- elevators
- hydraulic equipment
- ventilation
- lighting
等はindividual surveyで再利用可否を決める。

外国製であることだけを理由に全交換して工期を膨張させない。

## 9. Enterprise再建の資源代償 — CLOSED principle / exact hull impact OPEN

無料の工業余力は発生しない。

中央で要求:
- **駆逐艦用52,000shp-class plant二艦分相当**
- carrier-size shaft forging / propeller / bearings
- heavy electrical machinery
- skilled shipfitters / machinists / boilermakers
- Kure fitting-out and engineering labor

原則:
- 既存量産系からallocationする
- その代償は後続駆逐艦の工程遅延として現れる
- 「Enterpriseがあるから国全体の造機能力も増える」としない
- どの駆逐艦が何か月遅れるかは、1942H2 production ledgerで別途CLOSEする

## 10. ミッドウェー後の修理・改装負荷監査 — CLOSED / OPEN separation

### 10.1 R3で史実型負荷が消えるもの
- **Mogami / Mikuma collisionは発生しない**
- Mogamiの史実型大修理は不要
- Mogamiの史実型aviation-cruiser conversionは中央では実施しない
- Asashio / Arashioの史実Midway battle-damage repairは不要
- 史実Midway由来のAkebono Maru torpedo repairはR3では発生しない
- CarDiv 5のR3損傷状態は史実Coral Sea損傷を自動継承しない

### 10.2 R3で新たに重くなるもの
- **Akagi:** Midway戦傷 major-yard repair
- **Kaga:** Midway戦傷 major-yard repair
- **Enterprise:** capture / reconstruction
- **Shinkoku Maru:** 6/17 R3 submarine torpedo damage
- Enterprise救難中のGenyo / Kokuyo / Akashi等の拘束

したがって「日本工廠が空く」と単純化しない。
R3は**史実の分散した複数修理・非常改装が減り、赤城・加賀・Enterpriseという大型案件へ負荷の形が変わる**。

## 11. Hyuga / Ise — CLOSED / OPEN

### Hyuga — CLOSED
Hyugaの1942-05砲塔爆発はMidway敗北と独立の問題として残る。

- No.5 turretを新品再建して元の戦艦へ戻すことを自動前提にしない
- **Hyugaのみ航空偵察戦艦化を確定維持**
- conceptは「空母代用品」より**大型Tone / Chikuma型のfleet reconnaissance / seaplane support battleship**
- 36cm砲後部2基を航空設備へ転換する案を中央
- 強化された水上機体系を活かし、search / ASW / artillery spotting / local reconnaissance / seaplane supportを主価値とする
- exact aircraft mix / facility design / scheduleは別途詰める

### Ise — OPEN
- Hyugaと自動的に同時改装しない
- Hyuga実績、艦隊需要、yard loadを見てfollow-onを判断

Fuso / Yamashiro等も自動的に航空戦艦へ振らない。

## 12. 「ミッドウェー改修」監査語の定義

以後「ミッドウェー改修」を単一の史実正式計画名のように扱わない。

監査上は以下を分離する:
1. battle-damage repair
2. battle lessonsによるAA / radar / fire-protection / DC改修
3. carrier-loss補填を目的としたemergency conversions
4. それらが拘束するrepair ships / oilers / escorts / yard labor

R3では1と3の相当部分が史実と変わる。
一方、米急降下爆撃・fighter direction・radar・hangar fire / fuel / ordnance handling等の戦訓自体は存在するため、**2を丸ごと消さない**。

## 13. 空母建造計画の読み方 — CLOSED policy

日本海軍の「大量建造」計画数を、同時に建造できるphysical capacityと混同しない。

- 計画数はpriority / authorization / continuation envelope
- 実際の起工・進水・竣工はdock / slip / machinery / skilled labor / material / repair interruptionで決まる
- 「大計画発令 = 建造速度が突然上がる」としない
- 「紙上15隻だから最初から8〜10隻へ削る」ともしない

### R3 policy
**史実級の全力空母建造計画を維持する。**

- 米国の公示済み大規模海軍拡張へ対抗する必要はMidway勝利後も消えない
- 米空母を撃沈しても米shipbuilding capacityそのものは消えず、cruiser hull / merchant hull等をcarrierへ再allocationする可能性を想定する
- 日本側も既定のcarrier construction priorityを緩めない
- Unryu-class 15隻級、modified Taiho-class 5隻級等の「全力計画枠」を、最初から直感で縮小しない
- ただし各艦の史実起工日・物理建造時間を理由なく大幅前倒ししない

R3 advantageは:
- 史実より損傷修理やemergency conversionの割込みが少ない場合
- 史実で後順位艦が中止・停止・大幅遅延した局面で
- **同じ計画のより奥まで消化できる可能性が上がる**
こととして現れる。

つまり:
- early hullsが魔法のように早く就役するのではない
- later hullsが起工・進水・竣工まで到達しやすくなる

## 14. Major carrier / conversion handling — planning status

CLOSED principle:
- Taiho等の既起工・既定carrier programは維持
- Unryu-family mass programをMidway勝利だけで縮小しない
- carrier productionは「victory dividend」で減速しない

OPEN / separate gate:
- Shinanoをcarrierへ転用するか
- Chitose / ChiyodaのCVL conversion timing
- Shinyo等のlate emergency merchant conversion
- Ise follow-on aviation conversion
- individual later Unryu-family hull allocation / cancellations

これらを「史実Midway敗北がない」だけで自動削除せず、それぞれyard load / fleet need / machinery availabilityで判定する。

## 15. Auxiliary continuity guard

Enterprise / Midwayで使用した補助艦艇を、作戦終了と同時に在庫へ瞬間復帰させない。

少なくとも現時点の継続状態:
- **Akashi:** Enterprise salvage / engineeringへ拘束
- **Genyo Maru:** Enterprise primary tow候補
- **Kokuyo Maru:** reserve tow / logistics
- **Shinkoku Maru:** 6/17被雷、reduced-speed withdrawal / repair requirement
- **Urakami Maru:** Kwajalein sheltered salvage支援、Enterprise出港後はlocal roleへ戻す
- Enterprise escort DD: tow / ASW duty終了時点を別途追跡
- Midway transport / seaplane-support assets: occupation / base maturationへ継続拘束し、作戦終了だけで本土在庫へ戻さない

## 16. 次のproduction / yard gate

次に艦艇生産を詰める際は、計画名称ではなく、以下の四列で追う:

1. historical scheduled / actual yard occupancy
2. R3で消えるrepair / conversion interruption
3. R3で新たに増えるrepair / reconstruction interruption
4. machinery / material / skilled-labor bottleneck

対象:
- Kure
- Sasebo
- Yokosuka
- Nagasaki
- Kobe / Kawasaki
- Maizuru

1942-07 → 1944のquarterly / major-gate単位で、
- Akagi
- Kaga
- Enterprise
- Hyuga
- Taiho
- Ryuho
- Unryu-family
- other major repairs / conversions
を並べる。

**原則: 史実起工日はまず基準として保持し、R3差分は遅延・中止・割込み・後続艦消化率に反映する。理由なくearly commissioning bonusを与えない。**
