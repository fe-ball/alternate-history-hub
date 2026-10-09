# 日本側1942H2戦略整理・五号/FS/Arakan・航空機更新 handoff

> **Authority:** Relaunch R3 supporting / forward-analysis ledger
> **Status:** PROVISIONAL forward-analysis + next-session handoff
> **Canonical clock remains:** **1942-06-26 約18:00**
> 本稿は今回会話で進めた1942年後半〜1943年の作戦研究を、canonical future factへ昇格させずに再開可能な形で保存する。
> 実際の未来イベント・作戦成功・配備完了はまだCLOSEDではない。CLOSED / PROVISIONAL / OPENを分離する。
> **2026-10-04 update:** 本稿§0/§8の航空機OPEN agendaは [18-AIRCRAFT-FORCE-LEDGER-1942H2-1943-FORWARD.md](18-AIRCRAFT-FORCE-LEDGER-1942H2-1943-FORWARD.md) で再監査済み。競合時は18を優先し、active analytical frontierはFive-Go / FS-base / allocationへ戻る。

## 0. このhandoffの最重要事項

### 次回チャットの最優先論点 — OPEN / REQUIRED

**陸軍新型航空機を、名称を含めて改めて正式に詰める。**

特に:
1. 1942H2に量産立上げへ入る **O4系次期一般戦闘機（Ki-84-equivalent分析名）** の正式名称 / 制式呼称 / 命名時期
2. pilot production → service-trial unit → limited serial → first operational unit の時計
3. Ki-43 / Ki-44から何を継承し、何を切り捨てたか
4. 武装・防御・航続・高空性能・整備性の量産型での収斂
5. **Ki-45系の経験が他機種へ与えた影響**
   - 双発戦闘機
   - 長距離戦闘 / 護衛
   - bomber interception
   - ground / shipping attack
   - night-fighter方向
   - O4×2等の試験枝
6. Ki-45の**後継**をどう要求・分岐させるか
7. Ki-46、Ki-21 / Ki-49、次世代偵察・爆撃・襲撃機との技術 / 発動機 / 艤装共有
8. 1942H2の陸軍航空更新を、**機体名・制式名・部隊配備名まで含めて**閉じる

次回はまず [05-NAMING-DESIGNATION-POLICY.md](05-NAMING-DESIGNATION-POLICY.md)、[10-FIGHTER-DEVELOPMENT-1938-1940.md](10-FIGHTER-DEVELOPMENT-1938-1940.md)、[11-ENGINE-AIRCRAFT-ROADMAP-1940-1941.md](11-ENGINE-AIRCRAFT-ROADMAP-1940-1941.md) を再読してから開始する。

---

## 1. 1942H2世界波及 — 今回会話で得た中央像

16番台帳の世界波及監査を一巡した結果のPROVISIONAL central。

### 連合軍側

- 日本がPort Moresby、Midwayを確保し、Enterpriseを鹵獲、Hornetを喪失させたため、米太平洋の正規空母核は当面 **Saratoga + Wasp**。
- 日本側はSoryu / Hiryu / Shokaku / Zuikakuが健在、Akagi / Kagaは修理対象で、史実1942年夏より大幅に余裕がある。
- 米工業力が即月で空母不足を解決するわけではなく、Essex / Independence waveは1943年側の効果。
- Guadalcanal型の史実8/7攻勢は、この戦力差・Port Moresby日本領という幾何ではかなり危険。米側は基地航空・潜水艦・South Pacific defenseを優先しやすい。
- RNはOperation Cで **Indomitable喪失 / Formidable損傷**。Eastern Fleetの弱体化はMalta / Madagascar / Home Fleet / Torch / Arctic間の空母・護衛配分へ波及する。
- 欧州枢軸側は1942H2に多少利益: Malta補給 / offensive recoveryやAtlantic ASWの余裕が悪化し、Axis supply / U-boat / Arctic timingに小さな上振れ余地。
- ただしSuez / Stalingrad等の大勢を自動反転させない。
- Germany Firstは維持され、Torch自体は基本的に守られる中央。

### 日本側

最大の利益は領土そのものより:
- 1942年型熟練搭乗員・整備員・指揮官をMidway / Guadalcanalで大量消耗していない
- 駆逐艦・巡洋艦・空母航空隊が健康
- Enterprise鹵獲からF4F-4 folding wing、maintenance / paperwork、fighter direction、damage control等の研究を始められる
- Guadalcanal消耗がないため、1942H2に基地化・訓練・研究へ時間を再投資できる

## 2. 1942年夏の海上戦略 — 「決戦」より戦果の戦力化

### PROVISIONAL central

米側が無理な早期反攻を行わない限り、1942年7〜9月級は:
- Japanese carrier air-group rest / rebuild
- Akagi / Kaga major-yard repair
- Midway / Port Moresby / Solomons base maturation
- submarine / cruiser / selective carrier raids
- mutual reconnaissance
- Saratoga / Wasp concentration and defensive posture

が中心。

日本側は「どこを襲うか」を選びやすく、米側は「どこを守るか」を選ばされる。

### carrier use

- 四健在空母を毎週raidに出さない。
- 2個航空戦隊単位で即応 / 再訓練を交代するのが自然。
- large raidは敵輸送集中やcarrier location等の情報trigger時のみ。
- Akagi / Kagaは7月即復帰ではないが、修理時計は [15](15-ENTERPRISE-RECONSTRUCTION-AND-CARRIER-BUILDUP-1942.md) §25で再監査済み。**Kaga 1942Q4、Akagi 1942年末までのfirst-line return central**。

## 3. 五号作戦 / 四川作戦 — 根・編成・船腹

### 根の深さ

五号は1942年夏に突然思いつくものではない。
宜昌保持、重慶政権の抗戦基盤破壊、中国戦線兵力節減という1938–42年の連続問題の上にある。

R3では:
- 第11軍等の古参部隊が史実型大損を避けている
- reconnaissance / air observationにより大包囲・深追い事故の頻度が低い
- 1937型中核の摩耗が比較的小さく、実戦EDUが積み上がる
- 中国軍は人的には残る一方、火砲・車両・通信・昼間集中輸送の密度を累積的に失う

### 南京 / 華北系中国人組織

南京政府・華北系行政、地方警察、保安部隊、鉄道要員、荷役・商業・労務組織は:
- 日本軍戦闘師団の代替ではない
- 既占領地の駅・橋・倉庫・行政・荷役・交通統制等を肩代わりし、日本兵を前へ出す
- 特に工兵を警備任務から工事へ戻す効果が大きい
- 西へ進むほど有効性は低下し、新占領地では信用 / 行政能力とも低い

### 兵力構造

史実案の15個師団＋2旅団級の**攻撃正面幅は大きく削らない**中央。

理由:
- 中国軍の人的厚みは残る
- 地形・側面・兵站線の保持には面積を埋める歩兵が要る

一方、外部増援36万級はR3で:
- **29〜32万級をPROVISIONAL central band**
- 後方警備重複の圧縮
- infantryを単純削減するより engineers / transport / signals / maintenanceへ密度移行

を検討。

### 支援編成の方向

R3 working delta:
- road / bridge engineer: 史実案より +25〜35%方向
- motor transport: +15〜25%
- signals / maintenance: +15〜20%
- heavy artillery: 廃止せずarmy-level poolへ集中
- mountain / field gun / mortarは前線師団へ維持

効果:
- maximum speedより**minimum speedを底上げ**
- bridge / road destructionで一週間止まる事故を数日へ縮める
- 敵退却時に無理な追撃を避け、補給線を一緒に前進させる

### 情報封止

五号級では「大攻勢準備」は封止不能に近い。

封止可能性:
- 四川 / 重慶が大戦略目標: 低〜中
- 北 / 南の正確な主攻比率: 中〜高
- 各方面の正確な兵力: 中
- artillery / engineer重点: 中〜高
- H-hour: 高
- 第一段階後どこで止まるか / 成功軸をどこまで拡張するか: 非常に高

狙いは完全奇襲でなく:
**中国予備を北 / 南 / 中央に数日〜数週間長く分散させること。**

### 作戦時計 — forward simulation only

今回会話ではfuture simulationとして:
- 1943-03下旬級発動
- 潼関 / 黄河渡河
- 西安 4月上旬〜中旬級
- 宝鶏 4月中〜下旬
- 漢中 5月末〜6月上旬
- 広元 7月中旬級
- 南路は宜昌→巴東→奉節→万県方向へ並進

というWORKING CENTRALを試した。

**これはcanonical future factではない。**
次回以後、航空機・資源・敵配置の再監査で変更可。

### 船腹

重要なのは「五号中ずっと30万トン級を貼る」ではないこと。

PROVISIONAL working model:
- 第一集中徴傭: **22〜28万総トン級、central 25万級**
- 45〜60日級
- その後8〜15万級まで低下
- 第二集中徴傭: **18〜25万総トン級**
- 45〜75日級
- 本攻開始後: 5〜10万級の補充輸送へ低下

特徴:
- 人・車・工兵・備蓄を大陸へ降ろした船は返せる
- 満洲 / 朝鮮→北支は可能な限り大陸鉄道を使用
- 五号は**一時的ton-day負担**
- FS / NCは攻略後もtanker / escort / base cargoを永久拘束

## 4. FS — 中止ではなく発動保留 / 再設計

### PROVISIONAL central

R3でFSを史実同様に完全中止する理由はない。
しかし原7月のNC / Fiji / Samoa連続攻略案は、敵情見積が甘すぎる。

今回の議論では:
- 1942夏: **旧実施案を凍結**
- 目的・研究・部隊・上陸能力は保持
- Solomons / Port Moresby基地線を先に成熟
- NC / Fiji / Samoaを反復偵察
- 一般貨物船は期限付きで五号第一波へ
- fleet oiler / DD / CA / landing craft等のFS固有資産は保持
- 秋にFS再判定

という陸海軍妥協が自然とした。

### 秋のFS再判定

原三島同時案は、実守備兵力・長距離補給から魅力低下。

比較:
- A: original FS — NC + Fiji + Samoa
- B: NC限定攻略
- C: non-occupation FS — Solomons / PM base line + submarines + selective raids

今回の中央:
- **Aは実質廃棄方向**
- Bはcontingencyとして残す
- **Cがcentral**
- Saratoga / Waspの一方が失われる、NC守備が抜かれる等のopportunityが出ればBを再評価

### NC限定の負担

秋のNCは待つほど硬くなる。
WORKING:
- ground invasion force: 3.5〜6万級
- initial shipping: 20〜30万総トン級もあり得る
- carrier cover: 4〜6 carrier級の一時拘束
- occupation sustainment: 5〜10万総トン級相当の恒常能力 + tanker / escort
- five-go second wave: 最低3〜6週遅延、難航時2〜3か月

このため「敵にNCを守らせるだけで相手に恒常費用を払わせる」C案の費用対効果が高い。

## 5. 小〜中規模の基地化 / 追加進出

FS延期中でも、Five-Goのような一時輸送を済ませた後は、大上陸でなければ動く余地がある。

### Solomons / Oceania

PROVISIONAL central:
- Guadalcanal / Tulagiの完成・成熟
- Shortland / Faisi
- Buin / Kahili
- Buka
- New Georgia / Mundaを史実より早く測量・着工
- Nauru / Ocean Islandの史実型占領は高確率
- Milne Bay / Samaraiは有力な追加小進出候補
  - Port Moresby東側面保護
  - Coral Sea東部 reconnaissance
  - Louisiadesへのstep
  - 史実型の小兵力突撃ではなく、敵情を見て連隊〜旅団級＋建設隊等で実施

### Aleutians

R3ではMidwayも保持するため、Kiska / Attuの観測・牽制基地価値が史実より高い。

中央:
- **Kiska本格基地化**
- **Attu本格基地化**
- Adak追加攻略は低優先
- 1942中は水上機 / reconnaissance / submarine support / radar / AA / fuel / wintering中心
- 天候・tundra・工事能力を無視して大航空基地を即完成させない

> **2026-10-09 operational continuity restored from prior user-established storyline in [23]:** [23](23-ARAKAN-1942-COUNTERATTACK-1943-WINTER-AMPHIBIOUS-OPTIONS.md) にて、旧会話で既決の**1942年末前後の高速補給・舟艇機動による日本軍反撃→Cox's Bazarの日本軍取得→次の冬季作戦までの膠着**を復旧。史実とは異なるR3既決分岐であり、正確な占領日・戦力内訳・損害等は未転記の詳細監査とする。以下のlow/middle/highは**選択肢の説明**であり、1943年春にそのままChittagongまで進んだ確定戦果ではない。冬季作戦は英軍新攻勢の有無を発動条件とせず、Chittagongの港湾・市街への上陸/攻略は後段の別判定。

## 6. Indian Ocean / Arakan — 研究→準備→英攻勢→反撃拡張

### 基本整理

第一次Arakan攻勢は、Eastern Fleetの強弱だけでは開始が消えにくい。
本質はIndia Commandの陸上反攻:
Chittagong → Cox's Bazar → Maungdaw / Buthidaung → Akyab。

R3の海軍優勢は:
- 英攻勢そのものを自動中止させるより
- **沿岸安全度を悪化**
- 日本側の舟艇側背機動を可能にする

方向に効く。

### 研究段階 — 1942夏

FS延期により余る:
- Daihatsu / landing craft
- amphibious staffs / cut-out assault units
- some transports
- naval support assets

をArakan contingency研究へ回す余地。

研究対象:
- Akyab港 / airfield
- Rangoon–Akyab coastal supply
- Maungdaw / Buthidaung
- Cox's Bazar landing beaches
- Chittagong port / airfields
- tide / monsoon / coastal waterways
- RAF / small craft / submarine / mine threat
- Port Blair / Andaman support
- joint Army-Navy air cover

### 準備段階 — 8〜10月

- Akyab base improvement
- landing craft forward stock
- coastal reconnaissance
- Cox's Bazar / Chittagong photo reconnaissance
- Port Blair / Akyab seaplane support
- local air / submarine / cruiser reconnaissance

### 英Arakan攻勢が進んだ場合

三段階以上の日本側option:

1. **low:** naval / air raid only
2. **middle-A:** 55 Division front + inland flanking + 1〜数個大隊級 coastal landing to enemy rear
3. **middle-B:** 5,000〜10,000級でCox's Bazar完全着上陸
4. **high:** existing 55 Division + mainland reinforcement division級でChittagong攻略
5. **maximum:** Calcutta地上攻略 — 別主作戦級、現段階では低確率 / gate後

中央:
- **middle-A〜Bが最も自然**
- Chittagongは成功時のrealistic upper branch
- Calcutta地上侵攻は自動継続しない
- Chittagong / Calcuttaへのair raid / Bay of Bengal raidは高確率

### 海上戦力の意味

Eastern Fleetの大型艦不足は:
- 日本が海岸に永久に居座れる、ではない
- RAF / submarines / small craft / minesは残る
- しかし **大型英艦隊による即時介入riskが低く、夜間・短時間の沿岸舟艇機動がかなりやりやすい**

という程度が中央。

## 7. 日進・水上機 — 今回の掘り直し

### 日進

日進を「水上機が増えたからIndian Ocean seaplane tender」と固定しない。

R3 central role候補:
- **fast heavy transport / amphibious logistics**
- Daihatsu
- engineers
- field / mountain artillery
- light tanks / vehicles
- ammunition
- signals / fuel

をRangoon / Port Blair / Akyab、さらに条件が良ければCox's Bazar上陸部隊へ高速前送する。

水上機ISRそのものは他資産で分担した方が安い。

### Bengal Bay seaplane system

史実侵攻戦で実績のある特設水上機母艦＋前進泊地方式を採る。

候補構成のWORKING:
- E13A: 8〜12
- F1M: 8〜12
- A6M2-N: 4〜8
- 合計20〜30機級から開始

役割:
- E13A: long-range search / convoy / coastal ISR / ASW
- F1M: short-range patrol / landing craft cover / light attack
- A6M2-N: limited fighter cover
- H6K/H8K: outer long-range reconnaissance

base chain:
Penang → Port Blair → Akyab → 必要なら沿岸泊地。

R3ではGuadalcanal消耗がないため、史実ならSolomonsへ集中した水上機・搭乗員の一部をBengal Bayへ回す余地がある。

## 8. 1942H2航空機更新 — 現在の暫定像

### IJN

#### Fighter
- 第一線標準: **昴二一零戦**
- 昴二二1650PS branch: 1942Q1 qualification → initial production
- 1942H2は二一→二二の **gradual production-standard shift** が自然
- 昴三一 high-altitude: small / specialized、全面標準化しない
- next carrier fighter / 烈風equivalent: 1942Q3 first-flight central。まだ試作・試験
- Raiden-equivalent: B-17/B-24基地防空需要でpriority上昇余地、まだ大量配備ではない

#### Carrier attack / dive
- B5N: still mainline
- B6N: 1942H2 advanced test / possible limited initial service, full replacement later
- D3A: still mainline
- D4Y: reconnaissance-first / structural qualificationを飛ばさず、bombing version一斉更新はしない

#### Land attack / seaplane
- G4M mainline
- G3M pushed to second-line / patrol / training / transport roles
- E13A増勢
- F1M近距離任務
- A6M2-N限定防空
- H8K長距離ISR

### IJA

#### Existing mainline
- 九九式戦闘機 / Ki-43-equivalent: mature mass mainline
- Ki-44 O4 high-speed branch: interceptor specialization
- Ki-45: twin-engine multirole / interception / long-range / ground-sea attack branches
- Ki-46: mature strategic / operational reconnaissance
- Ki-21 main quantitative bomber
- Ki-49 increasing as newer line

#### O4 next-main fighter — OPEN naming / service closure

Current R3 technical state:
- study 1940Q2
- first flight 1941Q2
- increased prototypes / service trial 1941H2
- late prototype / service trial at 1941-12-07
- 1942H1 pilot production possible

1942H2 working expectation:
- Q2 pilot production
- Q3 first service-trial / operational-evaluation unit
- Q4 limited serial / some first-line unit conversion

**Exact production numbers, first operational unit, service date, and official name remain OPEN.**

This is the next chat's first target.

## 9. 次回読む順

1. 05-NAMING-DESIGNATION-POLICY.md
2. 10-FIGHTER-DEVELOPMENT-1938-1940.md
3. 11-ENGINE-AIRCRAFT-ROADMAP-1940-1941.md
4. 必要なら 07-AIRCRAFT-PRODUCTION-1937H2-1939.md
5. 本稿の §8
6. その後にArakan / Five-Go / base-allocationへ戻す

## 10. Next-session resume line

**Canonical clockは1942-06-26 18:00据置。最初に陸軍1942H2新型航空機を、名称・制式呼称・量産時計・初配備まで含めて再監査する。特にO4系次期一般戦闘機の正式名称を閉じ、Ki-45系の経験が双発戦闘機・長距離戦闘・迎撃・襲撃・夜戦方向や後継機へどう伝播したかをもう一度見る。Ki-46、Ki-21/Ki-49等の関連系列も同じ発動機・武装・防御・radio/ISR・production gateの中で再整理する。その後、更新済み航空戦力を入力としてArakan / Bengal Bay研究→準備→英攻勢反応、およびFive-Go / FS保留 / 基地化配分へ戻る。**

## 11. 2026-10-04 forward discussion update — aircraft closure / operational context

### aircraft
Detailed closure is in [18](18-AIRCRAFT-FORCE-LEDGER-1942H2-1943-FORWARD.md).

Key results:
- IJA next-main air-cooled fighter project = **Ki-63 / 二式戦闘機**; 「疾風」official nickname is PROVISIONAL central.
- Ki-63 1942 production 180–240級、1943にmain-successor ramp。
- O4 Ki-44 new mass-production priority declines; 峰Ki-44 remains limited specialist interceptor branch.
- IJN bridge = 昴二二零戦; A7M / 烈風equivalent first flight 1942Q3 central、1943H2 limited first-line conversion.
- B6N / D4Y mature earlier without deleting carrier / structural gates.
- B7A / 流星 keeps historical requirement and 1942-05 first-flight lineage; 峰 + maturation / carrier-system work makes 1943H2 limited operational existence plausible.
- Enterprise exploitation primarily advances folding / arresting / dive-release / maintenance / fighter-direction / DC / EMI maturity, not wholesale US-design copying.
- practical radio 1941 is reinterpreted as weight / power / installation-enabled usefulness, not full EMI solution; 1942H2 shielding / bonding / filtering standards and 1943 design-in EMC follow.

### Arakan / Chittagong conditional forward line

Still **PROVISIONAL conditional**, not canonical fact:
- British First Arakan offensive remains likely.
- Japanese prepared defense can transition middle-A → middle-B; if British forces remain committed, Chittagong becomes realistic high branch.
- Chittagong high branch uses 55 Division + reinforcement division-class (38 Division central candidate), temporary Bay-of-Bengal naval escalation, and forward air pressure.
- objective is not automatic Calcutta land advance. Chittagong is the more natural strategic stop / wedge.
- Bose / Azad Hind political use of actual Indian territory becomes a summer-1943 conditional branch; civil sovereignty can be granted while Japanese operational military control remains.

### Aleutians winter closure

Through winter 1942–43, central preparation:
- Kiska / Attu both treated as real long-hold bases, not disposable pickets.
- FS freeze frees enough shipping / construction margin to pre-stock substantial bulk, but Midway occupation cargo is not double-counted.
- working additional delivered cargo across H2 / winter = **4–6万t級 actual cargo**.
- Kiska: ~7,000–8,000 personnel-class, mature AA/coast-defense / power / workshop / storage / water / roads / seaplane support.
- Attu: ~3,200–4,000 personnel-class, earlier continuous construction and limited airstrip development.
- water-air emphasis remains A6M2-N / E13A; huge land-air regiment is not generated.
- re-open at 1943 March maritime interdiction / Komandorski gate; US May Attu landing is not pre-fixed.

### South / Central Pacific

- both sides increasingly base-up rather than immediately escalate.
- Japanese inner line matures around Rabaul / Port Moresby / Solomons / Midway.
- original FS three-island occupation remains effectively displaced by base-network / ISR / submarine / selective-raid strategy.
- Milne Bay / Samarai exact 1942H2 campaign remains a priority audit before final 1943 spring base map closure.


## 12. successor forward ledger

1943 summer convergence / Five-Go Phase-II pre-X state has moved to:
[19-1943-SUMMER-PRE-X-STRATEGIC-CONVERGENCE.md](19-1943-SUMMER-PRE-X-STRATEGIC-CONVERGENCE.md).

This file remains the 1942H2 Five-Go / FS / Arakan source ledger.  
For 1943 summer decisions, use 19 together with the aircraft counts / X-day air reservation in [18](18-AIRCRAFT-FORCE-LEDGER-1942H2-1943-FORWARD.md).
