# 経済マスタパラメータ・定数定義（暫定版）

> 修正版 2026-10-06。計算・参照・根拠不足を監査し、確定できない条件はOPENとした。変更根拠は [監査記録](../audit/DECISION-REGISTER.md)。

本資料は、シナリオ内の経済規模を一元管理するためのマスタデータである。各ドキュメントの「円・万円」記述は、本資料で定義されたコードを参照する形式で記述される。

---

## 【§0】ECNタグ・期区分運用規約（CANONICAL FOR FINANCIAL DATA）

**本節は資料群全体における財務データ運用の正典である。** 期区分の概念定義は `Phase_Analysis.md §0` を正典とし、本節は財務データ（価格・数量・売上・投資額・物価指数）の運用ルールと、ECNタグの参照箇所索引を定義する。

### §0.0 期区分との関係

> 本資料の期区分は `Phase_Analysis.md §0`（期区分の正典定義）に従う。財務期のラベル（第3期・第4〜5期前半・第5期後半〜第6期前半・第6期）は §0 の財務マッピング規約に従う。ECNタグ `REV_P3`〜`REV_P6` は財務ブロックを示し、概念フェーズ F3〜F6 と必ずしも1:1対応しない。具体的には、F3とF4は同一時間範囲の並列カテゴリのため財務的には合算（`REV_P3`）され、F5とF6は1936〜1940年でオーバーラップするため財務上は `REV_P4` (1934-37) と `REV_P5` (1937-41) の2ブロックに分割される。

### §0.1 ECNタグ運用ルール

本資料群における経済データの整合性を保つため、以下の5原則を遵守する。

#### 原則1：単一定義の原則（Single Source of Truth）

**各ECNタグの数値は、本資料 `Master_Parameters.md` で唯一定義される。** 他のすべての文書（Revenue_Model・Detailed_Growth_Simulation・Aviation_Fleet_List・Phase_Analysis 等）では、本資料の数値を**参照のみ**する。各文書で独立した点推定を記述してはならない。

例外：`Revenue_Model.md` は本資料と並ぶ「正典」だが、その役割は分担されている：
- `Master_Parameters.md` = タグ・数値の**定義**（タグ一覧・暫定値・命名規則）
- `Revenue_Model.md` = 数値の**根拠**（積み上げ計算・単価×数量・利益率の前提）

両者の数値が一致することを保証する責任は、双方の編集者にある。

#### 原則2：参照形式

文書本文で経済データを記述する際は、以下の形式で表記する：

```
[数値]{{ECN:CODE}}
```

例：「白金るつぼ調達 [2,500万円]{{ECN:CAPEX_PLATINUM}}」

これにより、(a) 読者は数値とコードを同時に参照でき、(b) 後で数値が改訂されても全文書の整合性が機械的に検証可能となる。

#### 原則3：レンジ表記の扱い

レンジ（例：`200〜500円`）を本文で表現する場合、ECNタグは**点推定値**（中間値・代表値）を持ち、レンジは備考欄または並記で示す。

```
○ 良い例：単価 [300円]{{ECN:PRICE_TANK_AVG}}（レンジ200〜500円・麻FRP/GFRPの混成平均）
× 悪い例：単価 [200〜500円]{{ECN:PRICE_TANK}}
```

ECNタグは集計の便宜上、機械可読な単一値を持つことを前提とする。

#### 原則4：タグ命名規則

ECNタグは以下のカテゴリ・命名規則に従う：

| カテゴリ | 接頭辞 | 用途 | 例 |
|:---|:---|:---|:---|
| 物価指数 | `INF_<年>` | 卸売物価指数（WPI）の年次値 | `ECN:INF_1935` |
| 製品単価 | `PRICE_<品目>` | 製品・部品の単価（円） | `ECN:PRICE_PROP_G` |
| 数量 | `QTY_<品目>_<単位>` | 年間生産量・供給量 | `ECN:QTY_TANK_SUPPLY` |
| 設備投資 | `CAPEX_<プロジェクト>` | 一回性の大型投資 | `ECN:CAPEX_PLATINUM` |
| 売上 | `REV_P<期>_<品目>` | 期別売上（万円） | `ECN:REV_P5_TANK` |
| 期別利益 | `REV_P<期>_PROFIT` | 期別税引前利益（万円） | `ECN:REV_P5_PROFIT` |
| 期別小計 | `REV_P<期>_<カテゴリ>` | カテゴリ集計値（万円） | `ECN:REV_P5_AVIA_BASE` |
| 期別総計 | `REV_P<期>` | 期間総売上（万円） | `ECN:REV_P5` |

期番号 `P1`〜`P6` は財務期を示す（§0.0 参照）。「期別小計」と「期別総計」を含む集計タグは、検算式の左辺・右辺で明示的に対応関係を示すこと（例：`REV_P5_AVIA_BASE + REV_P5_AVIA_COMP + 素材化学品小計 + REV_P5_STRATEGIC = REV_P5`）。

#### 原則5：タグの追加・変更プロセス

新規ECNタグを導入する際は、以下の順序を遵守する：

1. **本資料に追加**：`Master_Parameters.md` の該当節（§1〜§5）にタグと暫定値を追加
2. **§0.2 索引を更新**：参照箇所索引に新タグを追記
3. **`Revenue_Model.md` で根拠を記述**：単価×数量・利益率前提などの計算根拠を追加
4. **他文書から参照**：参照する文書では `[数値]{{ECN:CODE}}` 形式で記述

既存タグの数値変更は、本資料の値を改訂した上で `Revenue_Model.md` の整合を確認する。タグ名の変更（リネーム）は影響が大きいため、§0.2 索引で全参照箇所を確認した上で一括変更する。

### §0.2 ECNタグ参照箇所索引

本資料群で使用される全ECNタグの**定義箇所**と**参照箇所**を一覧する。`(M)` = Master_Parameters（定義元）、`(R)` = Revenue_Model（根拠）、その他は参照のみ。各タグの末尾に主要な使用文書を記載。本索引は主要な参照先の手動一覧であり、修正後の実参照箇所は [ECN-REFERENCES.json](../audit/ECN-REFERENCES.json) で確認する。機械検証した数値参照をファイル名・行番号付きで記録し、例示コードと暗黙参照は分ける。

#### §0.2.1 物価指数（ECN:INF_*）

定義元：本資料 §1。参照は現状なし（本資料内のみで完結）。

| タグ | 値 | 参照箇所 |
|:---|:---:|:---|
| `INF_1930` | 0.85 | (M) のみ |
| `INF_1935` | 1.00 | (M) のみ。Detailed_Growth_Simulation §4 に「実質価値（1935年基準）」記述あり（タグ参照なしの暗黙参照） |
| `INF_1938` | 1.25 | (M) のみ |
| `INF_1941` | 1.80 | (M) のみ |
| `INF_1944` | 3.50 | (M) のみ |

#### §0.2.2 製品・部品単価（ECN:PRICE_*）

定義元：本資料 §2。

| タグ | 値 | 参照箇所 |
|:---|:---:|:---|
| `PRICE_TRAINER_P5` | 45,000円 | (M), (R), Aviation_Fleet_List |
| `PRICE_LIAISON_P5` | 120,000円 | (M), (R), Aviation_Fleet_List |
| `PRICE_PATROL_P6` | 250,000円 | (M), (R) |
| `PRICE_PROP_C` | 800円 | (M), Aviation_Fleet_List |
| `PRICE_PROP_G_EARLY` | 2,500円 | (M), Aviation_Fleet_List |
| `PRICE_PROP_G` | 5,500円 | (M), (R), Aviation_Fleet_List |
| `PRICE_FLOAT_C` | 2,500円 | (M), Aviation_Fleet_List, Seaplane_Strategy |
| `PRICE_FLOAT_G` | 12,000円 | (M), Aviation_Fleet_List, Seaplane_Strategy |
| `PRICE_BOAT_PANEL` | 50,000円 | (M), Seaplane_Strategy |
| `PRICE_TANK_L` | 250円 | (M), Aviation_Fleet_List, Military_Applications |
| `PRICE_TANK_G` | 600円 | (M), Aviation_Fleet_List |
| `PRICE_TANK_AVG` | 300円 | (M), (R), Aviation_Fleet_List。P5混成平均の暫定値 |
| `PRICE_AMMO_BOX` | 25円 | (M), Military_Applications |
| `PRICE_GEAR_PIECE_AVG` | 5円 | (M), Military_Applications |
| `PRICE_REPAIR_KIT` | 45円 | (M), Military_Applications |
| `PRICE_RADIO_SEAL` | 15円 | (M), Military_Applications |
| `PRICE_VARNISH_KG` | 3〜8円 | (M) のみ。**※レンジ表記。原則3に従い点推定タグ追加検討** |
| `PRICE_ACETATE_DOPE_KG` | 2〜4円 | (M) のみ。**※レンジ表記。同上** |
| `PRICE_PMMA_SHEET` | 15〜40円 | (M) のみ。**※レンジ表記。同上** |
| `PRICE_PVB_SQM` | 8〜15円 | (M) のみ。**※レンジ表記。同上** |
| `PRICE_FURFURAL_TON` | 300〜500円 | (M) のみ。**※レンジ表記。同上** |

#### §0.2.3 数量（ECN:QTY_*）

定義元：本資料 §3。

| タグ | 値 | 参照箇所 |
|:---|:---:|:---|
| `QTY_TRAINER_YEAR` | 100機 | (M) のみ |
| `QTY_LIAISON_YEAR` | 20機 | (M) のみ |
| `QTY_PATROL_YEAR` | 5機 | (M) のみ |
| `QTY_PROP_SUPPLY` | 3,000本 | (M) のみ |
| `QTY_WING_SUPPLY` | 700機分 | (M), (R) |
| `QTY_TANK_SUPPLY` | 25,000個 | (M), (R) |

#### §0.2.4 設備投資（ECN:CAPEX_*）

定義元：本資料 §5。

| タグ | 値 | 参照箇所 |
|:---|:---:|:---|
| `CAPEX_DR980` | 120万円 | (M), (R), Phase_Analysis |
| `CAPEX_RESIN_PLANT` | 80万円 | (M), (R), Phase_Analysis |
| `CAPEX_PLATINUM` | 2,500万円 | (M), (R), Phase_Analysis |
| `CAPEX_PLAT_SELF` | 800万円 | (M), (R), Phase_Analysis |
| `CAPEX_AVIA_FACTORY` | 150万円 | (M), (R) |

#### §0.2.5 売上（ECN:REV_P1〜P6_*）

定義元：本資料 §4。期別総計は本資料、品目別内訳の根拠は (R) で詳述。

**第1期 (1910-17)**

| タグ | 値（万円） | 参照箇所 |
|:---|:---:|:---|
| `REV_P1` | 80 | (M), (R), Phase_Analysis |
| `REV_P1_LUMBER` | 50 | (M), (R) |
| `REV_P1_PLYWOOD` | 30 | (M), (R) |

**第2期 (1917-26)**

| タグ | 値（万円） | 参照箇所 |
|:---|:---:|:---|
| `REV_P2` | 400 | (M), (R), Phase_Analysis |
| `REV_P2_PROFIT` | 80 | (M), (R) |
| `REV_P2_SHUTTLE` | 200 | (M), (R) |
| `REV_P2_INSUL` | 100 | (M), (R) |
| `REV_P2_GEAR` | 50 | (M), (R) |
| `REV_P2_PROP` | 15 | (M), (R) |
| `REV_P2_LUMBER` | 35 | (M), (R) |

**第3期 (1926-34)** — F3+F4の財務出力合算

| タグ | 値（万円） | 参照箇所 |
|:---|:---:|:---|
| `REV_P3` | 1,200 | (M), (R), Phase_Analysis |
| `REV_P3_PROFIT` | 240 | (M), (R) |
| `REV_P3_SHUTTLE` | 500 | (M), (R) |
| `REV_P3_COMP_JOINT` | 150 | (M), (R) |
| `REV_P3_COMP_PROP` | 150 | (M), (R), Aviation_Fleet_List |
| `REV_P3_AVIA_FLOAT` | 20 | (M), Aviation_Fleet_List, Seaplane_Strategy |
| `REV_P3_AMMO_BOX` | 150 | (M), Military_Applications |
| `REV_P3_REPAIR_KIT` | 30 | (M), Military_Applications |
| `REV_P3_RADIO_SEAL` | 40 | (M), Military_Applications |
| `REV_P3_INSUL` | 200 | (M), (R) |
| `REV_P3_GEAR` | 100 | (M), (R) |
| `REV_P3_LINING` | 50 | (M), (R) |
| `REV_P3_EPOXY` | 50 | (M), Aviation_Fleet_List |
| `REV_P3_OTHER` | 10 | (M), (R) |

**第4〜5期前半 (1934-37)** — F5前半

| タグ | 値（万円） | 参照箇所 |
|:---|:---:|:---|
| `REV_P4` | 3,500 | (M), (R), Phase_Analysis |
| `REV_P4_MID` | 3,000 | (M), (R) |
| `REV_P4_PROFIT` | 530 | (M), (R) |
| `REV_P4_SHUTTLE` | 150 | (M), (R) |
| `REV_P4_COMP_ALL` | 800 | (M), (R) |
| `REV_P4_INSUL` | 400 | (M), (R) |
| `REV_P4_CHEM` | 300 | (M), (R) |
| `REV_P4_AVIA` | 1,500 | (M), (R) |
| `REV_P4_PROP` | 250 | (M), Aviation_Fleet_List |
| `REV_P4_TANK` | 50 | (M), Aviation_Fleet_List, Military_Applications |
| `REV_P4_GEAR_ALL` | 120 | (M), Military_Applications |
| `REV_P4_EPOXY` | 250 | (M), Aviation_Fleet_List |
| `REV_P4_ARMOR_INIT` | 50 | (M), Aviation_Fleet_List |
| `REV_P4_ARMOR` | 120 | (M), Aviation_Fleet_List |
| `REV_P4_PMMA_INIT` | 50 | (M), Aviation_Fleet_List |
| `REV_P4_OTHER` | 130 | (M), (R) |

**第5期後半〜第6期前半 (1937-41)** — F5後半+F6前半

| タグ | 値（万円） | 参照箇所 |
|:---|:---:|:---|
| `REV_P5` | 8,500 | (M), (R), Phase_Analysis |
| `REV_P5_PROFIT` | 1,400 | (M), (R) |
| `REV_P5_AVIA_BASE`（小計） | 940 | (M), (R) |
| `REV_P5_AVIA_TRAINER` | 450 | (M) のみ |
| `REV_P5_AVIA_LIAISON` | 240 | (M) のみ |
| `REV_P5_AVIA_PATROL` | 125 | (M) のみ |
| `REV_P5_AVIA_SPARE` | 125 | (M) のみ |
| `REV_P5_AVIA_COMP`（小計） | 3,660 | (M), (R) |
| `REV_P5_AVIA_COMP_PROP` | 1,650 | (M), (R), Aviation_Fleet_List |
| `REV_P5_GFRP_WING` | 560 | (M), (R), Aviation_Fleet_List |
| `REV_P5_GFRP_OTHER` | 200 | (M), (R) |
| `REV_P5_RADOME` | 100 | (M), (R) |
| `REV_P5_AVIA_FLOAT` | 250 | (M), (R), Aviation_Fleet_List, Seaplane_Strategy |
| `REV_P5_BOAT_PANEL` | 150 | (M), (R), Seaplane_Strategy |
| `REV_P5_TANK` | 750 | (M), (R), Aviation_Fleet_List |
| `REV_P5_COMP` | 800 | (M), (R), Economic_Refactoring_Logic |
| `REV_P5_FIELD_BRIDGE`（内訳） | 10 | (M), (R), Economic_Refactoring_Logic |
| `REV_P5_HARBOR`（内訳） | 10 | (M), (R), Economic_Refactoring_Logic |
| `REV_P5_EPOXY` | 1,100 | (M), (R), Aviation_Fleet_List |
| `REV_P5_SELF_PROT_AMMO`（内訳） | 3 | (M), (R), Economic_Refactoring_Logic |
| `REV_P5_INSUL` | 550 | (M), (R) |
| `REV_P5_HF_BOARD` | 50 | (M), (R), Economic_Refactoring_Logic |
| `REV_P5_VARNISH` | 200 | (M), (R), Economic_Refactoring_Logic |
| `REV_P5_ACETATE` | 100 | (M), (R), Economic_Refactoring_Logic |
| `REV_P5_PMMA` | 150 | (M), (R), Aviation_Fleet_List |
| `REV_P5_PVB` | 50 | (M), (R), Economic_Refactoring_Logic |
| `REV_P5_STRATEGIC`（小計） | 900 | (M), (R) |
| `REV_P5_ARMOR` | 350 | (M), (R), Aviation_Fleet_List |
| `REV_P5_RUBBER` | 130 | (M), (R), Economic_Refactoring_Logic |
| `REV_P5_SELFSEAL` | 50 | (M), (R), Economic_Refactoring_Logic |
| `REV_P5_ROCKET` | 20 | (M), (R), Economic_Refactoring_Logic |
| `REV_P5_CARBON` | 150 | (M), (R), Economic_Refactoring_Logic |
| `REV_P5_FURFURAL` | 100 | (M), (R), Economic_Refactoring_Logic |
| `REV_P5_LINING` | 100 | (M), (R) |

**第6期 (1942-)** — F6後期

| タグ | 値（万円） | 参照箇所 |
|:---|:---:|:---|
| `REV_P6` | 12,500 | (M), (R), Phase_Analysis |
| `REV_P6_PROFIT` | 1,875 | (M), (R) |
| `REV_P6_AVIA_BASE` | 1,200 | (M), (R) |
| `REV_P6_PROP` | 2,200 | (M), (R) |
| `REV_P6_FRP_STRUCT` | 1,200 | (M), (R) |
| `REV_P6_WING_SPAR_CF`（内訳） | 50 | (M), (R), Economic_Refactoring_Logic |
| `REV_P6_FLOAT` | 500 | (M), (R) |
| `REV_P6_TANK` | 1,000 | (M), (R) |
| `REV_P6_EPOXY` | 1,500 | (M), (R) |
| `REV_P6_SELF_PROT_AMMO`（内訳） | 5 | (M), (R) |
| `REV_P6_COMP_INSUL` | 1,200 | (M), (R) |
| `REV_P6_FIELD_BRIDGE`（内訳） | 15 | (M), (R) |
| `REV_P6_HARBOR`（内訳） | 30 | (M), (R) |
| `REV_P6_OPTICAL` | 300 | (M), (R) |
| `REV_P6_ARMOR` | 500 | (M), (R) |
| `REV_P6_STRATEGIC` | 1,100 | (M), (R) |
| `REV_P6_CONDUCTIVE_FIBER`（内訳） | 30 | (M), (R), Economic_Refactoring_Logic |
| `REV_P6_DIESEL_CAST` | 50 | (M), (R) |
| `REV_P6_CFRP` | 500 | (M), (R) |
| `REV_P6_RADOME` | 200 | (M), (R) |
| `REV_P6_SELFSEAL` | 150 | (M), (R) |
| `REV_P6_ROCKET` | 100 | (M), (R) |
| `REV_P6_OTHER` | 800 | (M), (R) |

### §0.3 索引メンテナンス上の留意

- **本索引で `(M) のみ` または `(M), (R) のみ` のタグは、他文書から参照されていない単独定義タグである。** 将来的に参照される可能性に備えて定義は維持するが、不要が確認できれば削除して構わない。
- **レンジ表記タグ（`PRICE_VARNISH_KG` 等5件）** は原則3への例外として残されている。レンジが本質的に意味を持つ品目（用途差で価格幅が大きい絶縁ワニス等）については、点推定値を持つ派生タグ（例：`PRICE_VARNISH_KG_AVG = 5円`）を別途定義し、本タグの値はレンジ表現として備考に留める運用が望ましい。
- **暗黙参照**（タグなしの数値直書き）は機械的整合性検査の対象外となる。`Detailed_Growth_Simulation.md` §3 の品目別積み上げ等が該当し、これらは可読性を優先した結果として生数値で示されている。新規記述では `[数値]{{ECN:CODE}}` 形式の使用を推奨し、暗黙参照を増やさない。
- **新タグ追加時** は §0.2 の該当カテゴリ表に追記し、参照箇所一覧も更新する。
- **教訓**：本資料群の整合性事故は、複数文書を同一年・同一商品・同一原料で読み比べたときに初めて姿を現す性質を持つ。横串の検算は ECN タグの単一定義原則と参照箇所索引によって構造的に防がれるが、各編集者は数値変更時に索引で全参照箇所を確認する習慣を維持すること。

---

## 1. 経済ベースライン・インフレ係数 (ECN:INF)
1934-36年（昭和9-11年）を **1.0** とした指数。

| 年度符号 | 指数コード | 指数値 (暫定) | 備考 |
|:---|:---|:---:|:---|
| **1930年** | `ECN:INF_1930` | 0.85 | デフレ・昭和恐慌期 |
| **1935年** | `ECN:INF_1935` | 1.00 | 戦前基準（安定期） |
| **1938年** | `ECN:INF_1938` | 1.25 | 日中戦争激化・インフレ開始 |
| **1941年** | `ECN:INF_1941` | 1.80 | 太平洋戦争開戦・軍需爆発 |
| **1944年** | `ECN:INF_1944` | 3.50 | 大戦末期・激しいインフレ |

---

## 2. 製品・部品単価 (ECN:PRICE)
※価格はすべて当時の額面（インフレ反映済み想定）。

### 2.1 航空機完成機
| 製品名 | コード | 単価 (暫定) | 備考 |
|:---|:---|:---:|:---|
| **練習機（公開・初練）** | `ECN:PRICE_TRAINER_P5` | 45,000円 | 史実赤とんぼ（2万）の2.2倍相当。複合材プレミアム |
| **連絡機（DR連絡）** | `ECN:PRICE_LIAISON_P5` | 120,000円 | 複合材・ディーゼルプレミアム反映 |
| **哨戒機（四号・D哨）** | `ECN:PRICE_PATROL_P6` | 250,000円 | 高性能哨戒機・大型 |

### 2.2 航空コンポーネント (部品)
| 製品名 | コード | 単価 (暫定) | 備考 |
|:---|:---|:---:|:---|
| **木製/コンプレグプロペラ** | `ECN:PRICE_PROP_C` | 800円 | 初期・固定ピッチ |
| **コンプレグプロペラ (前期)** | `ECN:PRICE_PROP_G_EARLY` | 2,500円 | |
| **GFRP/CFRPプロペラ** | `ECN:PRICE_PROP_G` | 5,500円 | 可変ピッチ対応ブレード |
| **コンプレグフロート (対)** | `ECN:PRICE_FLOAT_C` | 2,500円 | 水上機用 |
| **GFRPフロート (対)** | `ECN:PRICE_FLOAT_G` | 12,000円 | 軽量・耐海水 |
| **飛行艇艇体パネル** | `ECN:PRICE_BOAT_PANEL` | 50,000円 | |
| **麻FRP落下増槽** | `ECN:PRICE_TANK_L` | 250円 | 使い捨て |
| **GFRP落下増槽** | `ECN:PRICE_TANK_G` | 600円 | 航続距離延長用 |
| **落下増槽の混成平均（P5）** | `ECN:PRICE_TANK_AVG` | 300円 | 750万円÷25,000個から導出。構成比・実受注は未確定 |
| **コンプレグ弾薬箱** | `ECN:PRICE_AMMO_BOX` | 25円 | |
| **歩兵装備樹脂部品(平均)** | `ECN:PRICE_GEAR_PIECE_AVG` | 5円 | |
| **航空機補修キット** | `ECN:PRICE_REPAIR_KIT` | 45円 | |
| **無線機ポッティング封止** | `ECN:PRICE_RADIO_SEAL` | 15円 | |

### 2.3 素材・化学品単価
| 製品名 | コード | 単価 (暫定) | 備考 |
|:---|:---|:---:|:---|
| **電気絶縁ワニス (1kg缶)** | `ECN:PRICE_VARNISH_KG` | 3〜8円 | 重電・通信機向け。用途で価格差大 |
| **セルロースアセテートドープ (1kg)** | `ECN:PRICE_ACETATE_DOPE_KG` | 2〜4円 | 航空機布張り用。乾留酢酸の下流 |
| **PMMA板 (1枚・標準サイズ)** | `ECN:PRICE_PMMA_SHEET` | 15〜40円 | 風防・計器窓用 |
| **PVB中間膜 (1㎡)** | `ECN:PRICE_PVB_SQM` | 8〜15円 | 合わせガラス用。艦艇舷窓 |
| **フルフラル原料 (1トン)** | `ECN:PRICE_FURFURAL_TON` | 300〜500円 | 合成ゴム原料として理研系合弁等へ出荷 |

---

## 3. 市場需要・生産規模 (ECN:DEMAND)
※1941年前後のピーク時想定。

| カテゴリ | コード | 数量 | 備考 |
|:---|:---|:---:|:---|
| **自社練習機 年産** | `ECN:QTY_TRAINER_YEAR` | 100機 | 公開・初練 |
| **自社連絡機 年産** | `ECN:QTY_LIAISON_YEAR` | 20機 | DR連絡 |
| **自社哨戒機 年産** | `ECN:QTY_PATROL_YEAR` | 5機 | 四号・D哨（少量） |
| **他社供給プロペラ 年産** | `ECN:QTY_PROP_SUPPLY` | 3,000本 | 陸海軍全体の数割をカバー |
| **他社供給翼パネル等** | `ECN:QTY_WING_SUPPLY` | 700機分 | 三菱・中島向け。日本全生産の約14% |
| **他社供給増槽 年産** | `ECN:QTY_TANK_SUPPLY` | 25,000個 | 一任務一投棄の消耗品。戦線拡大で急増 |

---

## 4. 企業マクロ規模 (ECN:MACRO・REV)

### 第1期 (1910-17)
- `ECN:REV_P1`: 80万円 (総計)
- `ECN:REV_P1_LUMBER`: 50万円
- `ECN:REV_P1_PLYWOOD`: 30万円

### 第2期 (1917-26)
- `ECN:REV_P2`: 400万円 (総計)
- `ECN:REV_P2_PROFIT`: 80万円
- `ECN:REV_P2_SHUTTLE`: 200万円
- `ECN:REV_P2_INSUL`: 100万円
- `ECN:REV_P2_GEAR`: 50万円
- `ECN:REV_P2_PROP`: 15万円
- `ECN:REV_P2_LUMBER`: 35万円

### 第3期 (1926-34)
※`Phase_Analysis.md §0` に従い、F3（主業務：コンプレグ・樹脂自社合成）とF4（次素材探索：ガラス繊維着目）の財務出力を合算。
- `ECN:REV_P3`: 1,200万円 (総計)
- `ECN:REV_P3_PROFIT`: 240万円
- `ECN:REV_P3_SHUTTLE`: 500万円
- `ECN:REV_P3_COMP_JOINT`: 150万円
- `ECN:REV_P3_COMP_PROP`: 150万円
- `ECN:REV_P3_AVIA_FLOAT`: 20万円
- `ECN:REV_P3_AMMO_BOX`: 150万円
- `ECN:REV_P3_REPAIR_KIT`: 30万円
- `ECN:REV_P3_RADIO_SEAL`: 40万円
- `ECN:REV_P3_INSUL`: 200万円
- `ECN:REV_P3_GEAR`: 100万円
- `ECN:REV_P3_LINING`: 50万円
- `ECN:REV_P3_EPOXY`: 50万円
- `ECN:REV_P3_OTHER`: 10万円

### 第4〜5期前半 (1934-37)
※`Phase_Analysis.md §0` に従い、F5前半（エポキシ・GFRP事業の立ち上げ期）に対応する財務ブロック。日華事変（1937）末で年率3,500万円。
- `ECN:REV_P4`: 3,500万円 (総計)
- `ECN:REV_P4_MID`: 3,000万円
- `ECN:REV_P4_PROFIT`: 530万円（利益率約17.7%）
- `ECN:REV_P4_SHUTTLE`: 150万円
- `ECN:REV_P4_COMP_ALL`: 800万円
- `ECN:REV_P4_INSUL`: 400万円
- `ECN:REV_P4_CHEM`: 300万円
- `ECN:REV_P4_AVIA`: 1,500万円
- `ECN:REV_P4_PROP`: 250万円
- `ECN:REV_P4_TANK`: 50万円
- `ECN:REV_P4_GEAR_ALL`: 120万円
- `ECN:REV_P4_EPOXY`: 250万円
- `ECN:REV_P4_ARMOR_INIT`: 50万円
- `ECN:REV_P4_ARMOR`: 120万円
- `ECN:REV_P4_PMMA_INIT`: 50万円
- `ECN:REV_P4_OTHER`: 130万円

### 第5期後半〜第6期前半 (1937-41)
※`Phase_Analysis.md §0` に従い、F5後半（GFRP本格量産・軍需全開）と F6前半（CFRP研究水面下進行）をまたぐ財務ブロック。日華事変（1937）から太平洋戦争開戦（1941）までの軍需爆発期を含む。1938年は連続線上で内挿される（前後年の補間値）。1941年末で年率8,500万円。
- `ECN:REV_P5`: **8,500万円** (総計)
- `ECN:REV_P5_PROFIT`: **1,400万円**（利益率16.5%。価格統制反映）

#### 航空完成機
- `ECN:REV_P5_AVIA_TRAINER`: 450万円（練習機100機 × 4.5万円）
- `ECN:REV_P5_AVIA_LIAISON`: 240万円（連絡機20機 × 12万円）
- `ECN:REV_P5_AVIA_PATROL`: 125万円（哨戒機5機 × 25万円）
- `ECN:REV_P5_AVIA_SPARE`: 125万円（自社機向け補用品・整備支援）
- **小計 `ECN:REV_P5_AVIA_BASE`**: **940万円**

#### 航空コンポーネント
- `ECN:REV_P5_AVIA_COMP_PROP`: 1,650万円（プロペラ3,000本 × 5,500円）
- `ECN:REV_P5_GFRP_WING`: 560万円（翼パネル700機分 × 8,000円）
- `ECN:REV_P5_GFRP_OTHER`: 200万円（その他GFRP構造材。レドームは別タグ計上）
- `ECN:REV_P5_RADOME`: 100万円（GFRPレドーム航空機用・艦載用。電探の実用化に連動）
- `ECN:REV_P5_AVIA_FLOAT`: 250万円（GFRPフロート）
- `ECN:REV_P5_BOAT_PANEL`: 150万円（飛行艇艇体パネル）
- `ECN:REV_P5_TANK`: 750万円（増槽25,000個 × 平均300円）
- **小計 `ECN:REV_P5_AVIA_COMP`**: **3,660万円**（検算：1,650+560+200+100+250+150+750=3,660 ✓）

#### 素材・化学品
- `ECN:REV_P5_COMP`: 800万円（コンプレグ板材・弾薬箱・歩兵装備・小物自明置換品等。野戦橋梁・港湾設備は下記内訳参照）
  - うち `ECN:REV_P5_FIELD_BRIDGE`: 10万円（野戦用運搬橋梁。工兵本部向け）
  - うち `ECN:REV_P5_HARBOR`: 10万円（港湾設備一式：桟橋踏板・係船柱カバー・水上機スロープ・係留ブイ等。海軍設営隊向け）
- `ECN:REV_P5_EPOXY`: 1,100万円（接着剤・封止・シーラント。価格統制の扱いはOPEN。成分秘匿だけで免除されない）
  - うち `ECN:REV_P5_SELF_PROT_AMMO`: 3万円（自己防護型弾薬コンテナ）
- `ECN:REV_P5_INSUL`: 550万円（積層板・絶縁材）
- `ECN:REV_P5_HF_BOARD`: 50万円（高周波エポキシ-ガラス積層板。電探回路基板用。芝浦・海軍技研向け）
- `ECN:REV_P5_VARNISH`: 200万円（絶縁ワニス・塗料）
- `ECN:REV_P5_ACETATE`: 100万円（セルロースアセテートドープ）
- `ECN:REV_P5_PMMA`: 150万円（PMMA風防・計器窓）
- `ECN:REV_P5_PVB`: 50万円（PVB合わせガラス中間膜）
- **小計**: **3,000万円**

#### 装甲・戦略物資
- `ECN:REV_P5_ARMOR`: 350万円（複合装甲パネル）
- `ECN:REV_P5_RUBBER`: 130万円（合成ゴム原料・特殊ゴム部品の本体。セルフシーリング用ゴムシートは分離して下記計上）
- `ECN:REV_P5_SELFSEAL`: 50万円（セルフシーリング燃料タンク用ゴムシート。三菱・中島への供給）
- `ECN:REV_P5_ROCKET`: 20万円（噴進弾構造部品試作・少量供給）
- `ECN:REV_P5_CARBON`: 150万円（炭素電極・活性炭）
- `ECN:REV_P5_FURFURAL`: 100万円（フルフラル原料の合弁等への出荷）
- `ECN:REV_P5_LINING`: 100万円（耐蝕ライニング）
- **小計 `ECN:REV_P5_STRATEGIC`**: **900万円**

**内訳検算**：940 + 3,660 + 3,000 + 900 = **8,500万円** ✓

### 第6期 (1942〜)
※`Phase_Analysis.md §0` に従い、F6後期（CFRP実戦配備期）に対応する財務ブロック。
- `ECN:REV_P6`: **12,500万円** (総計)
- `ECN:REV_P6_PROFIT`: **1,875万円**（利益率15%。戦時統制本格化）

#### 第6期の内訳概要
| カテゴリ | コード | 金額 | 備考 |
|:---|:---|:---:|:---|
| 完成機 | `ECN:REV_P6_AVIA_BASE` | 1,200万円 | 練習機増産 + 哨戒機 |
| プロペラ | `ECN:REV_P6_PROP` | 2,200万円 | 4,000本/年へ拡大 |
| 翼パネル・GFRP/CFRP構造材 | `ECN:REV_P6_FRP_STRUCT` | 1,200万円 | CFRP一部導入 |
| うち 翼スパー(ピッチ系CF) | `ECN:REV_P6_WING_SPAR_CF` | 50万円 | 量産機の比弾性率対策 |
| フロート・艇体 | `ECN:REV_P6_FLOAT` | 500万円 | |
| 増槽 | `ECN:REV_P6_TANK` | 1,000万円 | 30,000個超 |
| エポキシ消耗品 | `ECN:REV_P6_EPOXY` | 1,500万円 | 全軍拡大供給 |
| うち 自己防護型弾薬コンテナ | `ECN:REV_P6_SELF_PROT_AMMO` | 5万円 | |
| コンプレグ・積層板・絶縁材 | `ECN:REV_P6_COMP_INSUL` | 1,200万円 | |
| うち 野戦用運搬橋梁 | `ECN:REV_P6_FIELD_BRIDGE` | 15万円 | 工兵本部向け |
| うち 港湾設備一式 | `ECN:REV_P6_HARBOR` | 30万円 | 海軍設営隊向け |
| ドープ・PMMA・PVB | `ECN:REV_P6_OPTICAL` | 300万円 | |
| 装甲パネル | `ECN:REV_P6_ARMOR` | 500万円 | 陸海軍本格採用 |
| 戦略物資（ゴム・炭素・フルフラル） | `ECN:REV_P6_STRATEGIC` | 1,100万円 | 合成ゴム本格化 + 炭素電極増産 |
| うち 導電性繊維散布兵器 | `ECN:REV_P6_CONDUCTIVE_FIBER` | 30万円 | 5弾種（一号〜五号型）合計 |
| CFRP素材（新規） | `ECN:REV_P6_CFRP` | 500万円 | 実戦配備開始 |
| GFRPレドーム | `ECN:REV_P6_RADOME` | 200万円 | 電探の全軍展開に連動 |
| セルフシーリング用ゴムシート | `ECN:REV_P6_SELFSEAL` | 150万円 | 新型機への標準採用拡大 |
| 電感噴進弾構造部品 | `ECN:REV_P6_ROCKET` | 100万円 | 月産500発体制 |
| ディーゼル添加剤・鋳造バインダー | `ECN:REV_P6_DIESEL_CAST` | 50万円 | フルフリルエーテル＋鋳造用フラン樹脂 |
| その他（ワニス・ライニング・治具等） | `ECN:REV_P6_OTHER` | 800万円 | |

**内訳検算**：1,200 + 2,200 + 1,200 + 500 + 1,000 + 1,500 + 1,200 + 300 + 500 + 1,100 + 500 + 200 + 150 + 100 + 50 + 800 = **12,500万円** ✓
（「うち」行は親カテゴリの内訳分解のため集計には含まない）

---

## 5. 主要投資・資産支出 (ECN:CAPEX)

| 項目 | コード | 金額 | 備考 |
|:---|:---|:---:|:---|
| **DR-980エンジン一括購入** | `ECN:CAPEX_DR980` | 120万円 | 1931年 |
| **樹脂合成施設建設** | `ECN:CAPEX_RESIN_PLANT` | 80万円 | |
| **航空量産工場拡張** | `ECN:CAPEX_AVIA_FACTORY` | 150万円 | |
| **白金るつぼ調達 (総額)** | `ECN:CAPEX_PLATINUM` | **2,500万円** | 1934前後 |
| **自社負担分白金** | `ECN:CAPEX_PLAT_SELF` | 800万円 | 3年分割想定 |
