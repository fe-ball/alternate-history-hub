# 発動機転生者 — 汎用セッション開始プロンプト

発動機転生者世界線の議論を再開する。
この文面だけを固定正本として扱わず、**毎回GitHub上のauthorityを先に解決し、最新の正本台帳から再開状態を復元すること。**

## 1. 最初にauthorityを解決する

GitHub repository:
`fe-ball/alternate-history-hub`

最初に:
1. `scenarios.yaml` の `hatsudoki-tenseisha`
2. `scenarios/hatsudoki-tenseisha/README.md`
3. `scenarios/hatsudoki-tenseisha/SCENARIO-RULES.md`
4. registryが指す `authority_entrypoint`
5. authority entrypointのreading orderで必要なengine / aircraft / naming / war-ledgerを読む

を実行する。

**最大version、最も新しい作成日、最も未来の日付を勝手にcurrentとみなさない。**
`authority_version`、`canonical_clock`、`clock_state`、`frontier` をそれぞれ確認する。

旧 `current/`、`archive/`、pre-relaunchは、現authorityが再採用した事項を除きREFERENCE。

## 2. 基本方法論

この世界線では「史実年表を少し前倒しする」のではなく、

**その時点で何を知っているか
→ 何を要求するか
→ 何を設計するか
→ 何を試すか
→ 実測で何が分かるか
→ 何が量産可能になるか
→ 何を配備できるか
→ 何を失うか
→ その結果、次に何を要求するか**

を連続的に追う。

主人公は現代の自動車用SIガソリンエンジン技術者。
強い領域:
- combustion / knock
- mixture / ignition
- piston / ring / bore
- valvetrain
- lubrication / friction
- cooling / thermal
- failure analysis
- DFM / process / QC / SPC

隣接領域:
- centrifugal supercharging
- reduction gear
- nacelle aero
- aviation metallurgy
- large radial crank / master rod

隣接領域はtest / expert gateを払う。

未来知識はidea / answer-selection gateを強く開くが、材料、工作機械、熱処理、公差、測定、耐久、疲労、量産歩留まり、supplier、予算、機体工場、搭乗員、燃料、輸送を無料では生成しない。

史実年代は能力上限ではない。
遅らせるなら具体的な未払いphysical / industrial gateを示す。
既に払ったgateは「史実より早い」だけで巻き戻さない。

## 3. 状態量を会戦ごとにリセットしない

地上戦:
- present / organized personnel
- veteran officer / NCO
- rifle / LMG / HMG
- mortar / infantry gun
- field / mountain artillery
- AT
- truck / tractor
- horse / cart
- radio / signal
- ammunition / fuel
- cohesion
- rail / river / motor / animal transport

航空:
- total aircraft
- serviceable
- immediate ready
- reserve / repair
- pilots
- mechanics
- spare engines
- allowable engine / airframe hours
- forward fuel / bombs
- sustainable sorties/day

を継続在庫として扱う。

aircraft count ≠ serviceable ≠ immediate sortie。
人員補充 ≠ 元の師団能力回復。

## 4. 兵站を万能ブレーキにも無料道路にも使わない

分ける:
- trunk rail / river
- railhead
- last-mile road
- bridges
- trucks
- horses
- engineer clock
- specialist / locomotive / signal
- enemy resistance
- weather
- forward airfield / aviation freight

敵抵抗・弾薬消費・車両損耗が下がれば、浮いたcapacityを道路・橋・鉄道・通信整備へ回してよい。
ただしlarge bridge、locomotive、specialist work等の物理時計は残す。

## 5. CLOSED / PROVISIONAL / OPENを守る

- **CLOSED:** 次の計算入力
- **PROVISIONAL:** 現在の最良監査band
- **OPEN:** 未決
- **REFERENCE:** 比較・旧体系

後の議論で新証拠・物理矛盾が出れば再監査してよいが、理由なくCLOSEDを史実値へ戻さない。
古いplanningと後続正本が競合する場合、明示的なsupersessionを優先する。

## 6. actor knowledgeを守る

canonical clockより未来の正本記述があっても、
- その時点までに開始済みのresearch
- military requirement
- company proposal
- production plan
として読む。

後年の成功・失敗・戦果を過去のactorへ逆流させない。

## 7. 史実確認

史実の部隊配置、作戦目的、天候、移動、工場移転、生産、援助、政治決定等が因果に効く場合は、その都度外部資料で確認する。

特に、
- 「史実でも既にやっていたこと」をR2独自効果にしない
- 後世の俗説・誤った損害数字を採用しない
- 一つの史料の誤認をscenario factへ直結させない
- 史料事実とscenario audit estimateを明示的に区別する

こと。

## 8. 現checkpoint — 2026-09-24更新

authority version: **Relaunch R2**
canonical historical clock: **1939-10-11T00:00**

必読の後続正本:
- `relaunch/09-CHINA-WAR-LEDGER-1938-05-21-TO-1939-10-11.md`
- `relaunch/10-FIGHTER-DEVELOPMENT-1938-1940.md`

現在までに閉じた大筋:
- 黄河決壊、武漢、Wanjialing、南昌、随県棗陽、ノモンハン裏番組、第一次長沙まで連続再生済み
- 第一次長沙は中国側の長沙防衛成功を維持する一方、日本第11軍は誘致後退をやや早く認識して撤退損失を軽減
- 中国側は人員を残す一方、砲・AT・radio・vehicle・horse・熟練等の希少戦力が相対的に薄い
- 武漢疎開のcritical machineryは大半を保存するが、一般設備・原料・補機・輸送損失により後方工業の立上がりが弱る
- 日本側はノモンハンで敗北するが、staff / support cadreと中国方面航空availabilityを史実相当より多く保存
- Ki-43は1939秋にpilot / early serial実用段階。1939 formal adoption中央なら九九式戦闘機
- Ki-44はO2D少数実用・O4/昴本命
- 1939 O2Dは70–100基、中央約85へ下方監査。O2Cへ生産mixを寄せる

## 9. 次にやること

current frontier:
**1939年末中国の国家戦争台帳を閉じ、その台帳から1939年冬季攻勢を再演する。**

中国について最低限、
- organized personnel
- rifles / ammunition
- LMG / HMG / mortar
- field / mountain artillery / AT
- radio / signal
- truck / tractor / horse / cart
- officer / NCO / mechanic quality
- domestic arms production by category
- migrated factory restart / throughput
- Soviet / French Indochina / Burma imports
- fiscal mobilization / inflation
- rail / river / motor transport
- aircraft / pilots / engine hours / spares

を、

**全国保有量
/ front-serviceable availability
/ monthly replenishment capacity**

へ分ける。

「中国にまだ武器がある／ない」の二値にしない。
小銃・小銃弾のような再生しやすい品目と、砲・AT・radio・truck・precision equipmentのような希少品目を分ける。

## 10. 回答スタイル

新規チャット最初の回答では、単なるファイル一覧ではなく、
- authority / clock / frontier
- 今までの主要因果
- 技術・航空機の現在状態
- 日本・中国の累積戦力差
- CLOSED / PROVISIONAL / OPEN
- 今回の作業入力

を短く再構成し、すぐ議論を再開できる状態にする。

既存GitHub資料から分かることをユーザーへ聞き返さない。
不確実なら合理的bandを置き、根拠とgateを示す。

## 11. GitHub write policy

会話中の推論を自動でGitHubへ書かない。
ユーザーが「GitHubへ反映」「GitHub化」「編入」等と明示した場合だけ永続化する。

その際にcanonical clock / clock_state / frontierが変わるなら、`scenarios.yaml` とauthority entrypointも同時に更新する。
