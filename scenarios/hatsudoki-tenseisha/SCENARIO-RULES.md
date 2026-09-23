# 発動機転生者の固有ルール

## 1. シナリオ分離

- 主人公の現代の自動車用ガソリンエンジン技術者としての知識を認める。計算機異聞の「未来知識なし」と混ぜない。
- 浅井世界線とは別の人物・企業・技術台帳。機種、数値、戦史を相互に移植しない。
- 他シナリオから参照してよいのは **方法論・authority運用・因果監査規則のみ**。数値、製品、人物、戦史を移植しない。

## 2. 正本の優先順位

2026-09-21 のリランチ以後は次を優先する。

1. `relaunch/` のリランチ正本
2. 本 `SCENARIO-RULES.md`
3. `pre-relaunch/` から参照される旧 `current/` / `archive/` 資料

旧技術台帳・旧引き継ぎの数値、旧製品系列、旧機体史は **REFERENCE**。
リランチ正本で明示的に再採用しない限り、自動的に正準へ戻さない。
最大version、更新日の新しさ、記述年代の未来さだけでauthorityを決めない。

## 3. 検討案と確定事項

GitHubへ入ったことだけを理由に作者確定事項へ昇格させない。

- **CLOSED:** 今後の計算入力として採る。
- **PROVISIONAL:** 現時点の最良案。監査で変更しうる。
- **OPEN:** 未決。
- **REFERENCE:** 旧体系・比較用。

非標準ラベルは自動的にCLOSEDへ読み替えない。

## 4. 性能値の規律

- 出力は離昇・30分定格・常用最大・巡航・開発試験上端・条件付き値を区別する。
- 公称定格は指定燃料・吸気条件・回転数/過給圧・温度条件で試験認定された使用上限として扱う。「最悪条件まで最低値を保証するため大幅に寝かせる」モデルを自動採用しない。
- 回転数、燃料、過給、水メタノール、耐久、使用時間と一緒に扱う。
- exhaust thrust、cooling drag、propeller efficiencyなどの搭載利得をshaft hpへ混ぜない。
- 技術利得を単純な「+%」で全部加算しない。同じknock / thermal / filling / mechanical marginを二重計上しない。
- 出力へ使わなかった技術余裕は消さず、定格時間、燃料耐性、寿命、重量、抗力、燃費、量産再現性、成長余地へ配分する。
- prototype best / official rating / production center / production dispersion / field-usable power を分離する。

## 5. future-CAD benchmark と idea / physical gate

未来知識は未来工場を召喚しない。

その年の日本の、

- 材料・燃料
- 工作機械・工員
- 計測器・試験設備
- 工場・電力・資金・調達
- supplier capacity
- qualificationに必要な実時間

を固定し、その条件で現代級の設計・解析・生産技術を使ったときの最善を100% benchmarkとする。

すべての技術で **idea / answer-selection gate** と **physical / industrial gate** を分離する。
主人公は前者を非常に強く開けるが、未知係数、加工、材料、耐久、寿命、量産歩留まり等の後者は現地で払う。

史実の発明年・制式年は能力上限ではない。
早期成立を否定・縮小する場合は、材料、加工、計測、試験、寿命、供給、重量、容積、搭載等の具体的な未払いゲートを示す。
「史実より早い」「数字が強すぎる」だけで史実中央値へ巻き戻さない。

## 6. 主人公の未来視の有限性

主人公は万能な年代別製品表を頭に持っているわけではない。

- 甲設計時には乙を強く見通してよい。
- 乙設計時には寿・光世代に対する明確な性能優位を狙い、とくに寿に対しては重量増という選択コストが残りうることも含めて設計する。乙の発展系列では、その後数年の栄級要求を明確に上回ることまで強く意識してよい。
- 甲より前から誉・ハ43級、1944年要求までを完成仕様として完全逆算しない。
- 後世の大型発動機系列は、その時点で育った会社・試験・生産能力、新しい軍要求、会社側の自主研究から改めて設計する。

この有限性は **思考禁止ではない**。
甲で乙より先を固定しない理由は、主人公が将来を全く知らないからではなく、会社規模、軍の信頼、資金、工場、将来要求がまだ不確定で、そこまで製品仕様へ固定する合理性がないためである。

乙の開発が始まった後は、乙の成熟と並行して乙改・高度性能枝・post-O2 architecture studyを検討するのが自然である。
「乙完成後に初めて次を考える」という直列史にしない。

## 7. 発展史は並行工程として扱う

現行品量産、故障改修、次期改良、次世代architecture study、軍向け提案、社内基礎研究は時間的に重なりうる。

各枝について少なくとも次を区別する。

1. idea / paper study
2. trade study
3. 人員・予算付与
4. rig / coupon / single-cylinder / mock-up
5. prototype
6. ground / endurance test
7. flight installation
8. qualification
9. military requirement / company proposal
10. adoption
11. serial production
12. allocation / serviceability / unit deployment

未来知識で思いつけるからといって、すべての枝に物理的開発時計が存在することにはしない。

## 8. 次期製品の起点

後続製品の起点を一種類に固定しない。

- **COMPANY-ORIGIN:** 主人公・尾張発動機が未来需要、O2の成長限界、市場機会を見て自主研究を開始する。
- **MILITARY-ORIGIN:** O1/O2の実績で信頼した陸海軍が、出力、高度、径、重量、長時間定格、燃料条件等の要求を出す。
- **MIXED:** 会社が先行して持っていた研究枝へ軍要求が接続し、正式計画へ昇格する。

軍要求が出るまで何も考えないことも、主人公が未来を知るから軍要求・予算なしで全て量産されることも避ける。

## 9. 要求 → 試作 → 実測 → 新要求

開発史の基本ループは、

**要求・仮説 → 設計 → rig / prototype → 実測 → failure / margin発見 → 要求修正 → 次の枝**

とする。

未来知識によって方式選択、試験順序、instrumentation、failure-mode想定、失敗枝回避は大幅に改善してよい。
一方、実測結果は主人公の予想を単に確認するだけでなく、新しい要求や分岐を発生させる。

後年の成功型が存在するからといって、その完成仕様や戦訓を早期checkpointのactor knowledgeへ逆流させない。

## 10. 長い時計の先払いと能力の非巻き戻し

疲労、摩耗、腐食、軸受、冷却、過給、工程能力、field-return、専門技術者育成等の長い時計は、主人公が必要性を早く認識し、実際に研究決定・予算・人員・rig・試験を投入した時点から開始してよい。
後年必要になった時点から自動的にゼロスタートさせない。

一度、日時を持つ開発・試験・量産・組織学習で獲得した、

- 試験設備
- 計装
- failure taxonomy
- 設計手順
- 公差・工程設計
- gauge / fixture
- SPC
- supplier quality
- teardown / field-return解析
- 技術者集団
- 燃焼・リング・潤滑・冷却データ

は因果的に共通する限り次製品へ継承する。
史実日本の平均へ自然減衰させない。
低下させる場合は設備破壊、人材喪失、材料品質低下、supplier崩壊等の具体的因果を置く。

## 11. 能力・製品・採用・戦果を分離する

最低でも次を別軸に扱う。

`technical capability`
→ `company research / military requirement`
→ `physical prototype`
→ `qualification`
→ `adoption`
→ `serial production`
→ `allocation`
→ `serviceability`
→ `unit deployment`
→ `tactical effect`
→ `operational effect`
→ `strategic effect`

これは唯一の固定時系列ではない。会社試作が軍要求より先に来てもよい。
ただし後段を主張する場合は必要な中間ゲートを飛ばさない。

## 12. 生産知識

当時日本を「ヤスリで一個ずつ仕上げる未近代工業」とみなさない。
史実日本の近代的工作・治具・検査・量産能力を基礎とし、主人公の現代自動車技術者としての強みは、

- DFM
- tolerance allocation
- datum / setup design
- fixture strategy
- SPC / process capability
- change control
- supplier quality
- failure feedback
- standard work

などを早期に体系化する点に置く。

設計性能、生産技術、試験能力、品質管理を同格の能力軸として扱う。

## 13. 技術伝播

主人公個人の未来知識と、尾張発動機という組織が再現できる能力を分ける。

主人公が試験体系、設計手順、QC、工程設計、文書、fixture等として組織化したものは会社能力として残る。
未文書化の主人公個人の未来知識を社員へ自動コピーしない。

軍、航空廠、機体メーカー、他社への技術伝播は、

- 実機
- 図面
- interface specification
- 試験記録
- 技術者
- joint test
- supplier
- license
- field feedback

等の具体的経路を必要とする。

## 14. 名称

機体・発動機の世界内名称は `relaunch/05-NAMING-DESIGNATION-POLICY.md` を参照する。
甲/乙等の監査ラベルを制式名称へ侵入させない。
史実相当機は史実の試作番号・略符号・制式名称を優先し、発動機換装だけで新しい機体番号を作らない。


## 15. 戦役を跨ぐ状態量・在庫の非リセット

会戦・撤退・疎開を跨いでも、人員・兵器・熟練・輸送能力を新品へ戻さない。

最低でも、
- 在隊人員 / organized combat personnel
- veteran cadre / NCO
- rifles / LMG / HMG
- mortar / infantry gun
- field / mountain artillery / AT
- vehicle / tractor
- horses / carts
- communications
- ammunition / fuel
- cohesion
- rail / river / motor / animal transport capacity
- aircraft / serviceable aircraft / pilots / mechanics / spare engines / sortie generation
を前回残高から繰り越す。

人員補充は重装備、熟練、凝集を自動回復しない。
失われた砲・車両・通信・馬匹は、具体的な生産・輸入・転用・捕獲がない限り復活しない。

## 16. 兵站は単一の史実日付ロックではない

「兵站があるから史実日まで動けない」と一括処理しない。

幹線容量、鉄道末端、道路状態、橋梁、車両、馬匹、航空基地へのfuel/bomb、敵抵抗、天候を分ける。

敵抵抗が弱く弾薬・車両損耗が減った場合、その余裕の一部をrail / sleeper / bridge / cement / gravel / road / signal等へ再配分し、transport capacity investmentが後続の末端容量を増やすことを認める。

一方、large bridge / locomotive / signal / specialist engineeringの物理時計を無料で短縮しない。

航空は幹線貨物を消費するが、末端より先のenemy artillery / reinforcement / transportを弱めることで地上側の弾薬消費・損耗・補修妨害を減らせる。
一時的な「航空支援された突出圏」を許容するが、無限進撃にはしない。

## 17. 1930年代中国政治・占領社会のactor-knowledge規律

1937–38年の人物へ、後世の中華人民共和国・台湾・日本の記憶政治や宣伝体系を逆流させない。
同時代のactorが知り得る軍事・政治・社会状況から判断させる。

史実ベースラインとして、
- 反蒋派
- 和平派
- 軍閥の自己保存
- 対日協力者・協力政権参加者
- 商業的・政治的機会を積極的に求める者
- 強制・保身・二股
- 国府軍・国民政府への地域的反感
が存在することを認める。

日本軍による残虐行為が存在したことから「対日協力政治は成立不能」と自動推論しない。
逆に、協力者が存在したことから被害・反日感情・抵抗が存在しないとも推論しない。
動機を一律に「生活のため仕方なく」に縮減せず、権力・反蒋・和平思想・利権・地方主義・反共・保身・強制などを具体的に分ける。

後に汪兆銘政権が成立したという史実は、早期時点で結果が必然・既知であることを意味しない。
