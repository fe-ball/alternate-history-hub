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
- 「史実でも既にやっていたこと」をこの世界線固有の効果にしない
- 後世の俗説・誤った損害数字を採用しない
- 一つの史料の誤認をscenario factへ直結させない
- 史料事実とscenario audit estimateを明示的に区別する

こと。

## 8. 現checkpointはこのファイルへ固定しない

この汎用プロンプトは、authority version / canonical clock / clock state / frontier の可変スナップショットを保持しない。

毎回必ず、
- `scenarios.yaml` の `hatsudoki-tenseisha`
- そこが指す `authority_entrypoint`
- authority entrypointが指定するcurrent war ledger / technical ledger

から現在地を復元する。

このファイル内の説明とregistry / authority entrypointが競合した場合は、**registryとauthority entrypointを優先**する。

## 9. authority解決直後にやること

current ledgerから、
- authority / canonical clock / frontier
- 艦艇・航空機・発動機・搭乗員・整備・燃料・弾薬の継続在庫
- CLOSED / PROVISIONAL / OPEN
- 直前戦役から持ち越す損傷・疲労・学習
- 次に閉じるdecision gate

を再構成する。

過去checkpoint専用の再開プロンプトはREFERENCEとして扱い、現行authorityの代用にしない。

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
