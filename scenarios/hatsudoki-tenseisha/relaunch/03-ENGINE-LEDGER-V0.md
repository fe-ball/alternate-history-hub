# 甲・乙 暫定技術台帳 v0

> **Status:** 甲の役割・乙の設計思想は CLOSED 寄り。寸法・出力・重量は PROVISIONAL。
> 旧 `current/航空発動機_工夫と発明_技術台帳.md` の135×152乙/丙系列を継承しない。

## 1. 共通気筒候補

現時点の第一候補:

**130 × 150 mm**

- 1気筒排気量: 約1.991 L
- 9気筒: 約17.92 L
- 14気筒: 約27.87 L

乙の目的を1935–40年へ限定すると、旧135×152より小径・軽量へ寄せられる。
130×145も検討したが、130×150は約3.4%の排気量増でBMEPを同程度下げ、87oct保証・長時間定格に余裕を返せる。
平均ピストン速度は乙2750rpmでも13.75m/s程度で、1930年代の設計として過大ではない。

## 2. 甲

### 2.1 商品目的

- 軍が普通に買いたくなる450hp級。
- 会社としての信頼・量産実績を得る。
- 乙用気筒を軍費で数千～数万本単位に量産し、L4の摩耗・熱・加工統計を稼ぐ。
- 甲を500–550hp商品へ過度に発展させず、1932–33年には人員を乙へ移す。

### 2.2 暫定仕様

| 項目 | 甲 |
|---|---|
| 構成 | 空冷単列9気筒 |
| bore × stroke | **130 × 150 mm** |
| 排気量 | **17.92 L** |
| valve | OHV 2-valve / cyl |
| ignition | dual ignition |
| compression ratio | 初期6.2–6.5候補 |
| supercharger | one-stage one-speed, low boost |
| propeller | **direct drive basic** |
| fuel | 当初通常航空燃料、後に80/87級へ |
| 甲0試作 | 350–400 hp級 |
| 甲11保証 | 400–420 hp / 2100–2150 rpm |
| **甲21成熟保証** | **450 hp / 2200 rpm** |
| 後期実証 | 約480 hp / 2300 rpm |
| 工場研究上端 | 約500 hp級。商品定格にはしない |
| dry mass | **285–305 kg** |
| diameter | **1.16–1.19 m級** |
| initial TBO | 150–200 h |
| mature TBO | **250–300 h級** |

450hp/2200rpmでBMEPは約10.2bar。
480hp/2300rpmでも約10.4bar。
機械的に無理をせず、乙用部品の量産学習へ余裕を振る。

### 2.3 甲→乙へ持ち越すもの

- cylinder barrel / head basic architecture
- chamber / plug placement
- piston / pin / ring pack
- valve / seat / guide
- cooling fins
- honing / bore geometry
- oil consumption control
- heat treatment / nitriding where appropriate
- tooling / gauges / inspection plan
- production statistical data

### 2.4 甲で共通化しないもの

- 7-cylinder master rod arrangement
- twin-row crankcase
- twin-row crankshaft
- reduction gear
- twin-row cooling architecture

これらは乙0で育てる。

## 3. 乙

### 3.1 商品目的

1935年の九六・九七式世代へ投入し、寿・光世代と正面競争する。
発動機単体の看板馬力ではなく、

- 小径
- 重量
- 87oct保証
- 30分高出力
- 冷却
- 量産全数保証
- 価格
- 将来92oct換金

を同時に成立させる。

### 3.2 暫定仕様

| 項目 | 乙・初期本線 |
|---|---|
| 構成 | 空冷複列14気筒、7×2 |
| bore × stroke | **130 × 150 mm** |
| displacement | **27.87 L** |
| valve | OHV 2-valve / cyl |
| ignition | dual ignition |
| compression ratio | **6.7–6.8 : 1 candidate** |
| supercharger | one-stage one-speed centrifugal |
| reduction ratio | **約0.68–0.70** |
| normal fuel | **87 oct** |
| experimental / special fuel | **92 oct** |
| **87 takeoff guarantee** | **900–920 hp / 2500 rpm** |
| 87 new-standard specimen | 930–950 hp級 |
| **92 special rating** | **980–1000 hp / 2550 rpm** |
| good specimen demo | 約1020–1030 hp / 2600 rpm候補 |
| **30-min class** | **850–880 hp級** |
| max continuous | 780–810 hp級 |
| initial rated altitude | 3.5–4 km級を狙う |
| dry mass | **520–535 kg** |
| diameter | **1.14–1.15 m級** |
| initial TBO | 200–250 h |

BMEP:

- 920hp / 2500rpm: 約11.8bar
- 1000hp / 2550rpm: 約12.6bar
- 1030hp / 2600rpm: 約12.8bar級

mean piston speed:

- 2500rpm: 12.5m/s
- 2550rpm: 12.75m/s
- 2750rpm later development: 13.75m/s

乙初期の強さを高BMEPだけで作らない。

## 4. 87 / 92の扱い

**CLOSED principle**

乙のnormal operationは87で成立させる。
92対応のために87側のCR・燃費・寿命を犠牲にしない。

92は主に、

- boost limit
- ignition schedule
- mixture schedule

を通じて追加性能へ換金する。

初期軍用表示では、
**87を正式保証、92を試験・特認**
とする。

## 5. valve / head

乙初期は4-valve化しない。

2500–2600rpm・BMEP 12–13bar級では、130mm boreに良好な2-valve headで足りる。
4-valveの流量利得より、

- head simplicity
- fewer parts
- exhaust-seat cooling
- production repeatability
- maintainability

へ余裕を配る。

dual ignition, compact chamber, controlled squish, hotspot removal, mixture distribution, ignition mappingを一つのknock-walletとして扱い、個別利得を加算しない。

## 6. supercharger

乙初期は一段一速。

狙い:

- production adiabatic efficiencyを堅実に上げる
- impeller/diffuser matchingをcut-and-tryから設計＋rig testへ移す
- tip clearance / gear / seal / drive durabilityを閉じる

二速過給は後期乙で復活可能なgrowth item。
初期商品へ将来装備の重量・複雑さを前払いしない。

## 7. cooling

巨大なfin areaで解くのではなく、

- fin placement
- exhaust-side concentration
- inter-cylinder baffle
- rear-row flow
- pressure recovery
- cowl outlet

を一体系で設計する。

乙は裸のengineではなく、
**指定baffle / cooling pressure-drop / cowl-interfaceを含む搭載package**
として機体屋へ渡す。

cooling marginは全てhpへ換金せず、

- 30-min rating
- 87oct margin
- hot-day guarantee
- lower cooling drag
- valve / head life

へ配る。

## 8. exhaust

軸出力定格と分離。

初期乙では、

- short individual pipes
- low back pressure
- rearward orientation
- several nozzle-area A/B tests

を標準思想とする。

初期候補:

**net exhaust thrust 15–25 kgf class**

これはPROVISIONALであり、機体速度・pipe geometry・back pressure試験で閉じる。
engine hpへ加算しない。

ejector cooling shroudはresearch item。
高速戦闘機の初期標準装備にはしない。

## 9. production / price

「当時日本が職人手仕上げしかできない」前提を置かない。
既存の近代工業へ、modern automotive production engineeringを先回り適用する。

主な原価レバー:

- relaxed non-functional tolerances
- datum unification
- fewer setups
- fixture design
- repeated cylinder-module production
- SPC / process drift detection
- less rework / scrap / sorting
- common part design
- supplier process control

現時点では、
**軍が光級と比較して普通に買う価格に入れば十分**
とし、絶対単価を正準化しない。

乙は光とほぼ同重量帯で、小径かつ高出力となるため、多少の価格premiumがあっても商品性を損なわない。

## 10. 1932 capability snapshot（監査座標）

数値はPROVISIONAL。完成品性能倍率ではない。

| 系 | 1932状態 | O目安 |
|---|---|---:|
| K design/search | trade study・failure thinking・DOE的試験順序 | 90–95% |
| E test/measurement | dyno・single-cylinder・CHT・valve/vibration・blower rig | 70–80 |
| P production/quality | gauges・route sheet・control chart・lot records | 75–85 |
| M materials/process | heat treat・nitriding・honing・early peening trials | 60–70 |
| C combustion/knock | chamber・dual ignition・CR・timing integrated | 80–90 |
| F fuel/mixture | carb/distribution strong; pressure/injection experimental | 65–75 |
| G gas exchange | valve/cam/port with flow & dyno correlation | 70–80 |
| S supercharging | single centrifugal understood, efficiency still maturing | 60–70 |
| T thermal | head/fins/baffle/cowl integrated test | 70–80 |
| D mechanics | balance/valve surge/master-rod/torsion anticipated | 65–80 |
| L lubrication/friction | dry sump/oil/rings/honing systematic | 70–80 |
| X exhaust | low-backpressure/rearward thrust concept known | 70–85 |
| R control/instrument | mechanical schedules / CHT-based limits | 60–70 |
| O maintenance | failure return / preventive replacement / teardown records | 80–90 |
| I installation | engine+cowl+prop treated as one interface | 70–80 |

1932の最大のチートは個別部品ではなく、
**design → rig → measurement → failure attribution → redesign → endurance → process capability → production → field return**
を高速で回す開発ループそのもの。
