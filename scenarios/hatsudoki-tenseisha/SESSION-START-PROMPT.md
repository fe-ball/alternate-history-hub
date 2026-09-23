# 発動機転生者 — セッション開始テキスト R2

発動機転生者世界線の議論を再開する。

このシナリオでは、現在の製品・機体・性能表を静的な完成状態として読むのではなく、**その時点までに何を知り、何を試し、何を作り、何を失い、何を学び、その結果として次の要求・研究枝・製品計画・作戦行動がどう発生したか**を最優先で追うこと。

技術・組織・軍要求・会社戦略だけでなく、戦役を跨ぐ人員・兵器・熟練・輸送能力・航空可動率も正本の状態量として扱う。前の会戦で失ったものを、次の会戦で理由なく復活させない。

---

## 1. authority の解決

まず GitHub の `fe-ball/alternate-history-hub` を参照し、中央案内 `scenarios.yaml` から `hatsudoki-tenseisha` の現在状態を取得する。

以下の順序で読む。

1. `scenarios.yaml`
2. `scenarios/hatsudoki-tenseisha/README.md`
3. `scenarios/hatsudoki-tenseisha/SCENARIO-RULES.md`
4. registry が指定する authority entrypoint
5. authority が指定する capability / history / engine / thermal / aircraft / naming / war-ledger parent
6. 必要に応じて `pre-relaunch/` と import status
7. 旧 `current/` と `archive/` は、現行authorityが明示的に再採用した事項を除き REFERENCE としてのみ読む

最大version、最新作成日、最も未来の歴史時刻を自動的にcurrentと判断しない。

2026-09-21リランチ以前の旧135×152mm共通気筒、旧乙/丙系列、旧機体史・生産史・戦史はpre-relaunch REFERENCEである。古いディレクトリ名だけを理由に旧台帳を復帰させない。

`authority_version`、`canonical_clock`、`clock_state`、`frontier` は独立して確認する。

現在は **Relaunch R2**、canonical historical clock は **1938-05-21T00:00** である。
1938-05-21より未来の発動機・機体計画が正本に書かれていても、それはその時点までに開始済みの研究・要求・計画であり、未来の実績をactor knowledgeへ逆流させない。

---

## 2. 世界線の最上位前提

主人公は現代の自動車用ガソリンエンジン技術者である転生者で、当時としては未来知識を持つ。ただし万能ではない。

無料に近く得られるものは主として、

- 正しい方式・設計枝の選択
- 後世に失敗すると分かっている枝の回避
- 何を測るべきか
- failure mode の先取り
- 実験計画・DOE
- 設計空間探索
- 量産設計・工程設計
- SPC・品質管理・変更管理
- 後世に有効と分かっている技術を、現地条件で成立可能な形へ早期提案する能力
- 長時間研究・耐久・工程成熟の必要性を早く認識し、合理的なら早く時計を開始する能力

である。

無料で生成しないもの:

- 存在しない材料
- 当時作れない合金・熱処理
- 加工不能な形状
- 未存在の工作機械
- 未測定係数
- 実際に回していない長時間耐久
- 疲労・摩耗・腐食の実時間
- 未成熟な量産歩留まり
- 軍予算
- 工場能力
- 機体工場
- 搭乗員・整備員
- 燃料・補給網
- 歴史上存在しなかった輸送capacity

---

## 3. 史実年代は能力上限ではない

史実の発明年、初飛行年、制式年、量産年を能力上限として使わない。

「史実より早い」「当時として高度すぎる」「日本ではまだ存在しなかった」「数字が強すぎる」という理由だけで性能や開発時期を史実へ巻き戻さない。

遅らせる場合は、

- 材料・熱処理
- 加工・公差
- 計測
- 試験設備
- flow / thermal / vibration map
- fatigue / wear / corrosion
- endurance duration
- 重量・容積
- 搭載
- supplier capacity
- 量産歩留まり
- 整備・兵站

等の具体的未払いゲートを示す。

逆にゲートが払われているなら、史実から離れた結果であること自体を弱体化理由にしない。

---

## 4. idea gate と physical gate

すべての新技術・新製品について、

**idea / answer-selection gate**
と
**physical / industrial gate**

を分ける。

主人公の未来知識は前者を非常に強く開くが、後者は現地で払う。

「正解を知る」ことと「量産可能な航空発動機として完成」を同一視しない。

---

## 5. future-CAD benchmark

future-CAD benchmark は未来工場召喚ではない。

対象年の日本で使える、

- 材料・燃料
- 工作機械
- 工員・技能
- 計測器
- 試験設備
- 工場・電力
- 資金
- supplier
- qualificationに必要な時間

を固定する。

その条件で、現代級の設計知識・解析・生産技術・故障知識を持つ専門家集団が作れる最善の設計、工程、公差、検査、試験計画、failure-mode一覧、trade studyを100% benchmarkとする。

---

## 6. Gp / Gd / Gq、L0–L4、余裕通貨

能力を一つの倍率にしない。

- Gp: performance gain capture
- Gd: development gain capture
- Gq: quality gain capture

問題クラス:
- L0: 方式選択・系列構成
- L1: 基本寸法・CR・減速比・基本熱収支
- L2: port、混合分配、点火、過給機map、冷却ΔP
- L3: 捩り振動、動弁、熱変形、過渡
- L4: 疲労、摩耗、腐食、焼付き、軸受寿命、量産歩留まり

技術項目の+%を単純加算しない。

- knock
- filling
- thermal
- mechanical / rpm
- friction
- weight
- cooling drag
- exhaust energy
- life
- production variance

等の物理財布へ集約し、peak power、離昇、30分、常用、巡航、高空、燃料耐性、寿命、重量、抗力、BSFC、量産再現性、成長余地へ配分する。

同じ余裕を二重計上しない。

---

## 7. 生産・試験・品質を設計性能と同格に扱う

当時日本を「ヤスリで一個ずつ仕上げる未近代工業」とみなさない。

史実日本の近代的工作・治具・検査・量産能力を基礎に、

- DFM
- tolerance allocation
- datum / setup design
- fixture strategy
- gauges
- SPC / process capability
- change control
- supplier quality
- failure feedback
- standard work
- test planning

の早期体系化を主人公の強みに置く。

---

## 8. 発展は並行工程

製品史を、

「甲完成 → 乙を考える → 乙完成 → 丙を考える」

という直列工程にしない。

各枝について少なくとも、

1. idea / paper
2. trade study
3. budget / personnel
4. rig / coupon / single-cylinder / mock-up
5. prototype
6. ground / endurance
7. flight installation
8. qualification
9. military requirement / company proposal
10. adoption
11. serial production
12. allocation / serviceability / unit deployment

を区別する。

次期製品起点は、

- COMPANY-ORIGIN
- MILITARY-ORIGIN
- MIXED

の三種を認める。

---

## 9. 要求 → 試作 → 実測 → 新要求

基本ループ:

**要求・仮説 → 設計 → rig / prototype → 実測 → failure / margin発見 → 要求修正 → 次の枝**

未来知識で方式選択・試験項目・instrumentation・failure-mode想定は大きく改善してよい。

ただし実測は答え合わせだけではない。材料品質、加工ばらつき、冷却分布、振動、機体搭載、軍運用結果は新要求を生む。

---

## 10. 長い時計の先払い

疲労、摩耗、腐食、軸受、冷却、過給機、工程能力、field return、専門技術者育成は実時間を要する。

主人公が必要性を早く認識し、

- research decision
- budget
- people
- rig
- specimen
- prototype
- accumulated running time

を実際に投入したなら、その時点から時計を進める。

後年必要になった時点でゼロへ戻さない。

---

## 11. 獲得済み能力を巻き戻さない

一度獲得した、

- test facilities
- dynamometer / instrumentation
- failure taxonomy
- design procedures
- tolerance / process design
- gauge / fixture
- SPC
- heat-treatment know-how
- supplier management
- teardown / field-return analysis
- engineering teams
- combustion / ring / lubrication / cooling data

は因果的に共通する限り次製品へ継承する。

低下させる場合は、設備破壊、人材喪失、材料品質低下、supplier崩壊等の具体的因果を置く。

---

## 12. capability / procurement / deployment / effect を分離

最低でも、

technical capability
→ research / requirement
→ physical prototype
→ qualification
→ adoption
→ serial production
→ allocation
→ serviceability
→ unit deployment
→ tactical effect
→ operational effect
→ strategic effect

を別々に確認する。

---

## 13. 発動機・搭載・定格

監査名、社内型式、世界内名称を混同しない。

現行R2の主要系列は、

- O1 / 旭
- O2 / 暁一一
- O2B / 暁一二
- O2C / 暁二一
- O2D / 暁二二
- O3 / 岳
- O4 / 昴
- O5 / 峰

である。

正確な寸法、排気量、mass、diameter、fuel、ratings、thermal、TBO、development stateは現authorityの `03A` / `06` を読む。

87octと92octを分離する。

離昇、30分、常用最大、巡航を用途別に使う。

exhaust thrust、cooling drag、prop efficiency、intake loss、cowl dragをshaft hpへ混ぜない。

prototype best、公称定格、量産中央値、量産ばらつき、field-usable powerを混同しない。

---

## 14. 主人公個人・組織能力・技術伝播

主人公本人が知ることと、尾張発動機が再現できることを分ける。

組織化済みの試験体系、設計手順、QC、failure analysis、工程設計、文書、gauge、fixture、supplier managementは会社能力として残る。

主人公しか知らない未文書化未来知識を社員へ自動コピーしない。

軍、航空廠、機体メーカー、他社への伝播には、

- actual hardware
- drawings
- interface specification
- test records
- engineers
- joint tests
- suppliers
- license
- field feedback

等の具体的経路を必要とする。

---

## 15. 後年結果の逆流を禁止

後に成功した製品、量産値、戦訓、部隊評価があるからといって、早期checkpointの人物が知っていることにはしない。

1938-05-21より先のKi-43 / Ki-44 / Ki-45 / Ki-46 / 十二試艦戦 / 岳・昴生産などの正本記述は、「当時までに合理的に立っている計画・要求・開発時計」として使い、後年の成功を既知事実にしない。

---

## 16. 機体側も同じ発展規律

要求
→ prototype
→ comparison
→ measurement
→ doctrine / requirement change
→ next aircraft

を追う。

史実相当機は史実のprototype number / abbreviation / service designationを優先し、発動機換装だけで新番号を作らない。

海軍の一号/二号/三号は1930年代の制度として相当に異なる枝を許す。
後年の二桁model notationを1936–37へ遡及しない。

---

## 17. R2の1937-07-07発動機・機体基準

現authorityから必ず確認する。

重要なR2訂正:
- 暁family累計 **約470基**
- O2 / 暁一一 約405
- O2B / 暁一二 **約65**
- installed engines 約282
- reserve 約95
- tests 約50
- depot/company/overhaul 約43

主要機体中央:
- A4N暁 16
- 九六二号 約100
- 九六三号 約40
- Ki-11 O2 約27
- 陸軍第四案 約18
- Ki-15暁 約60
- B4Y暁 4
- B5N暁 3
- G3M暁 compare 2 aircraft
- Ki-21暁 compare 2 aircraft
- Owari testbeds 6

旧正本の「三号研究5機」「O2B数基試験」は廃止されている。

九六三号の詳細、陸軍第四案、armament、fuel/range、exhaust等は `04` / `07` から取得する。

---

## 18. R2の発動機系列状態

### 暁一二 / O2B
CLOSED。one-stage one-speed mature type。
1937-07-07までに約65基、low-rate production。

### 暁二一 / O2C
CLOSED。one-stage two-speed、reduction約0.60。
暁14として健康に使える最後の主力。
高空高速戦闘機・司偵・高速双発へ優先。

### 暁二二 / O2D
CLOSED。high-boost two-speed bridge。
1250hp級を可能にするがTBOを払い、次世代基幹にはしない。

### 岳 / O3
CLOSED basic architecture。
145×160×14、large-cylinder、large-aircraft long-duration。
Ki-21が最初の大口顧客。

### 昴 / O4
CLOSED product target。
130×150×18、1500hp級、next high-speed fighter main。
O1 9-cylinder + O2 high-load cylinder / supercharge + new long-crank / torsion / rear-coolingの統合。

### 峰 / O5
PROVISIONAL。
145×160×18、future 1750–2100hp healthy range。
まだ今の歴史時点で完成結果へ固定しない。

---

## 19. 1937後半～39年の機体計画

現authority `07-AIRCRAFT-PRODUCTION-1937H2-1939.md` を読む。

重要な方向:
- 九六三号は1937末約120機のupper first-lineへ
- Ki-15暁も1937末約120
- 陸軍第四案は約48へ
- Ki-21は岳integrationへ
- Ki-43-equivalent = 暁二一主力
- Ki-44-equivalent = 暁二二先行、昴本命
- Ki-45 = 暁二一×2のearly heavy fighter
- Ki-46 = 暁二一×2が非常に有力
- Ki-48 = 暁なら強いがopportunity costでHa-25 mass branch
- 十二試艦戦 = O2C/O2D暫定、昴本命
- 海軍次期陸攻 = 岳比較はするが三菱大型発動機mass main central

これらの1939–40結果を、1938-05-21の人物が確実に知ることにはしない。

---

## 20. 戦役を跨ぐ状態量 — 最重要

今後の戦史で絶対に「会戦リセット」をしない。

会戦・撤退・疎開のたびに、

前回残高
+ reinforcement / production / import
- combat losses
- non-combat losses
- capture / abandonment
± transfer
= next balance

で閉じる。

最低限追うもの:
- total present
- organized combat personnel
- veteran officers / NCO
- rifles
- LMG
- HMG
- mortar / infantry gun
- field / mountain artillery
- AT guns
- trucks / tractors
- horses / carts
- communications
- ammunition / fuel
- cohesion
- rail / river / motor / animal transport capacity

人員が補充されたから「元の師団」に戻ったと扱わない。
砲・車両・通信・熟練がなければ、頭数だけ多いlight infantryになりうる。

失われた装備が倉庫から理由なく湧いて再び失われる描写は禁止。

---

## 21. 航空も別在庫

aircraft count ≠ serviceable ≠ immediate sortie。

最低でも、
- assigned aircraft
- serviceable
- immediate ready
- reserve
- under repair
- trained pilots
- replacement pilots
- mechanics
- spare engines
- allowable flying hours
- forward-base fuel / bombs
- sustainable sorties/day
を分ける。

中国・ソ連側の「存在するだけで護衛を強制する」戦略は認めるが、その存在にもfuel / engine hours / maintenance / pilot attrition / base / spare aircraftの継続支払いがある。

日本側が相手を何度もscrambleさせることで、撃墜しなくても存在戦略の支払いを増やすことを認める。

---

## 22. 兵站を万能ブレーキにも無料道路にもするな

「兵站だから史実の日まで一歩も動けない」としない。
「航空が強いから無限に進める」ともしない。

分ける:
- trunk rail / river capacity
- railhead
- last-mile road condition
- bridges
- trucks
- horses
- aviation fuel / bombs
- enemy resistance
- weather
- engineer / specialist clock

敵抵抗が弱く、砲弾・車両損耗が減った場合、その輸送余裕の一部を、
- rail
- sleepers
- bridge material
- cement
- gravel
- road repair
- signal / telephone
へ投資し、後日のcapacityを増やしてよい。

ただしlarge bridge、locomotive、signal、specialist workは材料だけで無限短縮しない。

航空基地は幹線capacityを食う一方、railheadより先のenemy artillery / reinforcement / transportを弱め、地上末端の弾薬消費・車両損耗・工事妨害を減らす。

**安定兵站圏の少し前に、数日だけ維持可能な「航空支援された暫定突出圏」が存在してよい。**
その突出から生還したstaff / logistics / engineer / NCOは経験を蓄積し、次作戦へ持ち越す。

検証困難な細部は、無理に数値を作らず「現時点では効果ゼロとして扱う／OPEN」としてよい。

---

## 23. 1937–38年中国政治・社会のactor knowledge

この論点では後世の中華人民共和国・台湾・日本の記憶政治を1937–38年の人物へ流し込まない。

史実ベースラインとして同時に存在するもの:
- anti-Chiang factions
- peace factions
- warlord self-preservation
- active collaboration with Japan
- participation in collaborationist administrations
- political ambition / acquisition of office
- commercial opportunity / profit
- anti-Communism / localism
- coercion / survival
- dual dealing
- regional resentment toward Nationalist government / army

対日協力者をすべて「生活のため仕方なく」に縮減しない。
反対に、協力者が存在するから抵抗・被害・反日感情が存在しないとも扱わない。

南京で日本軍による大規模な殺害・暴行・略奪等が発生したことは史実として扱う。
しかし、それを「対日和平・協力政治は以後成立不能」という万能な政治変数にしない。史実にはその後も維新政府・汪兆銘政権等が成立している。
同様に、国府軍による焦土・徴発・防衛・撤退等への住民側反感も、具体的局面で普通に存在しうる。

センシティブな歴史事象を、現在の問いに直接因果関係がないのに毎回長く挿入しない。
必要なときだけ、その時代の資料・actor knowledge・政治利害として扱う。

---

## 24. 1937後半から1938-05-21までの戦史状態

現authority `08-CHINA-WAR-LEDGER-TO-1938-05-21.md` を必ず読む。

大筋:

### 上海
日本側航空は史実以上に機体・熟練搭乗員を温存。
8月に航空優勢、9月に中国側昼間航空活動を強く制限、10月に後方交通への継続的圧力。

### 上海撤退
杭州湾上陸・地上側面進撃が撤退の主因。
撤退が始まると目標が塹壕からroad / rail / bridge / artillery / truck / horse transportへ変わり、航空効果が非線形に増える。
中国側は人員より重装備・通信・輸送を多く失う。

### 南京
政府・重要軍需設備の疎開はかなり成功しうる。
守備軍・敗残軍は人間が逃げても重装備が逃げにくい。
最重要工作機械が西遷できたことと、軍の装備崩壊を混同しない。

### 1938初頭
中国地上軍は人員を比較的早く補充するが、砲・車両・通信・熟練の回復は遅い。
ソ連援助によって中国航空だけは比較的早く新品戦闘単位を再建する。

### 台児荘
史実型の日本大敗は成立しない。
Linyi reinforcementは航空偵察・阻止を受け、5th Divisionは完全拘束されない。
Tang Enbo maneuverも早期発見され、包囲輪が閉じにくい。
ただしSeya-type dangerous protrusion自体は残る。
日本側は危険な突出から多数のexperienced staff / NCOを生還させ、補給・航空連携・追撃限界の実測を次へ持ち越す。

### 徐州
中国側は史実よりやや早く撤退。
日本側は完全包囲殲滅に失敗する。
悪天候・夜間分散は依然として中国側の大脱出を助ける。
ただし人員を救う代価として師団形態・重装備・車両・通信を史実以上に失う。

canonical clock:
**1938-05-21、徐州陥落直後。**

---

## 25. 1938-05-21 current force picture

絶対数の史料幅が大きいため、詳細は `08` のaudit bandを使う。

中国第五戦区撤退対象について、withdrawal-start equipmentを100とした6月初頭見込み中央帯:
- alive/recovered 75–82
- organized combat 60–68
- rifles 65–72
- LMG 55–62
- HMG 45–53
- mortar/infantry gun 43–52
- field/mountain artillery 30–40
- AT 32–42
- vehicles/tractors 22–32
- horse/cart 45–55
- communications 32–42
- immediate ammunition/supply 28–38

additional vs historical-equivalent path:
- Chinese KIA/captured/missing +2～4万人級 audit
- temporarily dispersed / unavailable as formed unit +3～5万人級
- Japanese effective strength carried into pursuit +5,000～8,000人級

これらはscenario audit rangeであり、史料上の一点確定値と偽装しない。

---

## 26. 日本側学習能力を故意に無能化しない

日本軍の攻撃性・独断・突出傾向は残してよい。
しかし「玉砕志向だから兵站も軍規も学習も存在しない」とはしない。

部隊が壊滅を免れれば、
- staff
- regimental/battalion commanders
- artillery observers
- engineers
- signals
- logistics officers
- drivers
- veteran NCO
が経験を持ち帰る。

危険な突出から生還すれば、
- railheadからの実用距離
- daily ammunition need
- road capacity
- aviation support条件
- weather failure
- emergency motor transport allocation
等の実測が蓄積する。

軍規・命令・補給手順も経験に応じ改善しうる。
必ず守られるとは限らないが、「敗北しなければ学習ゼロ」ともしない。

---

## 27. 他社発動機を消さない

尾張が高性能戦闘機・司偵需要を取っても、中島・三菱等の工場設備・人員が消滅するわけではない。

低payoff用途や自社機では、
- Ha-25 family
- Kinsei
- Mitsubishi large engine
等が普通に増産されうる。

尾張の存在による日本航空工業の増加は、
「全部尾張発動機になる」
ではなく、
**尾張が高性能用途を肩代わりした結果、既存メーカーが別用途へより厚く供給できる**
という形も重視する。

---

## 28. 状態ラベルと不確実性

- CLOSED: 今後の入力として採用済み
- PROVISIONAL: 現時点の最良案
- OPEN: 未決
- REFERENCE: 比較・旧体系

証拠・物理監査不足なら史実へ自動復帰しない。

- bandを広げる
- PROVISIONAL維持
- OPEN
- 効果ゼロとして保留
- 次に閉じるgate提示

のどれかにする。

細部を無限に台帳化せず、major bottleneckを優先する。

---

## 29. 過去資料との監査

旧値残存、二重計上、古いauthority、manifest不整合、参照切れがあれば抽出する。

旧135×152系列、旧乙/丙定格、旧機体性能、旧生産・戦史をR2へ自動継承しない。

R1の以下はR2で明示的に上書き済み:
- O2Bが1937.7に数基試験だけ
- 九六三号が高速研究5機だけ
- O2実機搭載約260 / 二号約125等の旧配分
- canonical clock 1937-07-07

---

## 30. 最初の回答

最初の回答は単なるファイル一覧にしない。

少なくとも、

1. authority_version / canonical_clock / clock_state / frontier
2. 主人公の知識境界と会社能力
3. O1→O2→O2B/C/D、岳、昴、峰の状態
4. 1937-07-07 aircraft / engine baseline
5. 1937 H2生産・配備の主要変化
6. 1938-05-21までの戦役による人員・装備・熟練・輸送の累積差
7. 中国・ソ連航空再建と日本側の適応
8. 台児荘・徐州で何が史実から変わったか
9. current Japanese / Chinese force-quality asymmetry
10. logistics current state
11. future aircraft / engine projects that are already started but not yet historical outcomes
12. current OPEN / PROVISIONAL items
13. 次に閉じるfrontier

を、議論をそのまま再開できる密度でまとめる。

既存資料から得られることをユーザーへ聞き返さず、自分で読む。

---

## 31. 次の作業 — current frontier

**1938-05-21。徐州陥落直後。**

次は1938年5月19日頃から6月15日頃までを日単位寄りで連続再生する。

見るもの:

### 日本側
- Xuzhou後の5th / 10th / 14th / 16th等の実際の残存戦力
- 商丘 → 蘭封 → 開封 → 中牟 / 鄭州のadvance
- road / rail / bridge repair
- trunk vs last-mile supply
- artillery expenditure
- motor / horse availability
- forward airfields
- Ki-15 reconnaissance
- fighter / bomber sortie generation
- どこまで「航空支援された暫定突出圏」を維持できるか
- 速く進んだ結果、どこで補給・洪水等の非常ブレーキへ早く衝突するか

### 中国側
- 徐州から逃げた部隊のorganized strength
- Henan reinforcement / rear guard
- remaining artillery / AT / transport
- rail/road evacuation
- Yellow River dike breach decision process
- 4月以来の「以水代兵」案の存在
- 5月末～6月のpolitical / operational decision
- Zhao口等の初期施工
- failure / site change
- labor / engineer / explosives
- river conditions
- Japanese approach / air reconnaissance pressure

### 禁止する単純化
- 「日本が3日早いから決壊も3日早い」
- 「花園口は史実日付に固定」
- 「日本軍が速いので決壊不能」
- 「兵站だから日本軍は史実線を一歩も越えない」

decision clock、construction clock、hydrological effect clock、日本軍advance clockを別々に走らせ、どこで交差するかを見る。

---

## 32. GitHubへの反映

会話中の推論・暫定案を自動でGitHubへ書かない。

ユーザーが、

- 「GitHubに投げろ」
- 「ここまでGitHub反映」
- 「GitHubへ編入」

等と明示した場合のみ永続化する。

authority、canonical clock、clock_state、frontierが変化するなら `scenarios.yaml` も同時に更新する。

未承認事項・暫定推論を勝手にCLOSED/CANONへ昇格させない。
