# 浅井世界線 — 汎用リーディングガイド

このファイルは、チャット・モデル・人間が **浅井世界線を最初から誤読せずに再開するための固定入口** です。

個別セッションの版番号や戦況に依存しません。  
**最新版の版番号・canonical clock・active package は必ず `current/00-START-HERE-CURRENT.md` から取得してください。**

---

## 0. 最初に開くアドレス

### リポジトリ全体
- https://github.com/fe-ball/alternate-history-hub

### 浅井世界線トップ
- https://github.com/fe-ball/alternate-history-hub/tree/main/scenarios/asai

### この汎用ガイド
- https://github.com/fe-ball/alternate-history-hub/blob/main/scenarios/asai/00-READ-FIRST-GENERIC.md

### シナリオルール
- https://github.com/fe-ball/alternate-history-hub/blob/main/scenarios/asai/SCENARIO-RULES.md

### 現在状態のルータ
- https://github.com/fe-ball/alternate-history-hub/blob/main/scenarios/asai/current/00-START-HERE-CURRENT.md

### current ディレクトリ
- https://github.com/fe-ball/alternate-history-hub/tree/main/scenarios/asai/current

### 現行 technical
- https://github.com/fe-ball/alternate-history-hub/tree/main/scenarios/asai/current/technical

### 旧版から継承する exact source
- https://github.com/fe-ball/alternate-history-hub/tree/main/scenarios/asai/import/source-v22b-full-exact

---

## 1. 標準の読み順

原則として以下の順で読む。

1. **`SCENARIO-RULES.md`**
   - clock / backflow / knowledge-boundary / simulation guard を確認する。
   - ただしファイル冒頭の版番号・clockが古い場合は、最新版の版番号・clockについては次の current router を優先する。

2. **`current/00-START-HERE-CURRENT.md`**
   - 最新 authority
   - active package
   - canonical clock
   - 現在の frontier
   - 読むべき CURRENT package
   をここで確定する。

3. **current router が指定する最新 `00-START-HERE-*`**
   - その版の正式な入口を読む。

4. **active CURRENT package の `00-SESSION-HANDOFF-*`**
   - 現在戦況
   - 継承状態
   - actor knowledge
   - 作業上の境界
   を把握する。

5. **decision register**
   - `01-DECISION-REGISTER-*.tsv`
   - その後に同 package 内のより新しい working decision register / addendum がある場合は、CANON と WORKING を区別して読む。

6. **chronology / state snapshot**
   - `02-REPLAY-CHRONOLOGY-*`
   - 必要に応じて `03-*` 以降の状態ファイル。
   - chronological event と technical look-ahead を混同しない。

7. **open items / next gates**
   - `04-OPEN-ITEMS-AND-NEXT-GATES-*.tsv`
   - その後の working continuation がある場合、より新しい next-gate 指示を優先する。

8. **post-CURRENT working continuation**
   - 同じ CURRENT package 内の後発 `WORKING-HANDOFF`, `WORKING-DECISION-REGISTER`, addendum 等。
   - これらは **Vxx CANON を自動的に上書きしない**。
   - ただし post-canon 作業について、後発ファイルが明示的に WORKING-CLOSE した項目は、その後の作業状態として使う。

9. **具体論点だけ `current/technical/`**
   - 航空機
   - 発動機
   - 魚雷
   - 艦艇
   - 燃料
   - 生産
   - 兵站
   等、質問に必要な親だけを読む。

10. **不足するときだけ `import/source-v22b-full-exact/`**
    - 現行 technical が参照する親
    - supersession
    - package-state
    - 旧詳細
    を確認する。
    - exact source にファイルが存在すること自体は CANON を意味しない。

---

## 2. Authority / precedence の基本

### A. 現在戦況
原則:

`current router`
→ 最新 explicit CURRENT decision
→ 同枝の後発 working close
→ 非矛盾の親状態
→ technical parent
→ provenance / support source

### B. technical
より新しい明示的な technical closeout / supersession が古い値を上書きする。

古いファイルに
- CURRENT
- CANON
- CLOSED
と書かれていても、そのファイルが後で quarantine / superseded / provenance-only に落ちていれば現行 authority ではない。

### C. exact source
`source-v22b-full-exact` は **V22B source package の byte-exact recovery source**。

用途:
- 消えた親資料を回収する
- supersession を確認する
- 旧詳細を再監査する

用途ではないもの:
- 全ファイルを自動CANON化
- sibling branch の未来を current branch へ逆流
- 古い性能表・調達表を無条件復活

### D. partial import
`import/source-v22b-full/` は古い partial / reconstructed import。

exact counterpart がある場合、復元元として使わない。

---

## 3. CANON / WORKING / OPEN の読み分け

### CANON / INHERIT
現在枝で確定している履歴・決定。

### WORKING-CLOSE
次の作業へ入力として使ってよい閉鎖値。
ただし正式な版更新で CANON 昇格したとは限らない。

### WORKING
中心値・帯・暫定経路。
後続監査で変更可能。

### OPEN
まだ決めていない。
古い結果、史実結果、会話上便利な値で勝手に埋めない。

### ANALYSIS-ONLY
思考実験。
履歴やOOBへ入れない。

---

## 4. 時間と因果のルール

必ず以下を分ける。

- technical feasibility
- prototype
- factory accepted
- service released
- unit assigned
- serviceable
- forward deployed
- immediately operational
- actual combat presence
- combat result

性能が存在しても、部隊に存在するとは限らない。

また:

- 後の戦訓を前のactorへ与えない
- sibling branch の未来結果を current branch へ逆流させない
- later historical outcome を理由に earlier decision を自動最適化しない
- geography / weather / runway / fuel / maintenance / trained crews を無視しない

---

## 5. 史実名称の機体・装備を読むとき

同じ名称でも史実と同一hardwareとは限らない。

必ず:

1. designation identity
2. date / lot / variant
3. installed system
4. production / QC state
5. service / maintenance state
6. historical anchor already including later improvement or not
7. actual allocation

を確認する。

史実機数を使う場合も:

`historical count -> worldline configuration -> serviceable -> forward -> combat-present`

の順に通す。

---

## 6. 新設機・旧枝復元のルール

旧枝・quarantine・support資料から機体を復活させる場合:

1. current propulsion / materials で H→A 再監査
2. development-history plausibility
3. customer requirement / institutional sponsor
4. prototype / formal program gate
5. nomenclature gate
6. production / service gate
7. allocation / combat replay gate

後段が成立しているからといって前段を遡って成立させない。

---

## 7. チャットへ最初に渡す最小アドレス集

新しいチャットへは、最低限これを渡せばよい。

- 汎用ガイド  
  https://github.com/fe-ball/alternate-history-hub/blob/main/scenarios/asai/00-READ-FIRST-GENERIC.md

- current router  
  https://github.com/fe-ball/alternate-history-hub/blob/main/scenarios/asai/current/00-START-HERE-CURRENT.md

- current directory  
  https://github.com/fe-ball/alternate-history-hub/tree/main/scenarios/asai/current

- current technical  
  https://github.com/fe-ball/alternate-history-hub/tree/main/scenarios/asai/current/technical

- exact inherited source  
  https://github.com/fe-ball/alternate-history-hub/tree/main/scenarios/asai/import/source-v22b-full-exact

---

## 8. 新しいチャットへの短い指示文

そのまま貼れる形:

> 浅井世界線を連続的に把握してから回答してください。  
> 最初に汎用ガイド → current/00-START-HERE-CURRENT.md → そこが指定する最新CURRENT packageのsession handoff → decision register → chronology/state → open items/next gates の順に読んでください。  
> post-CURRENT working continuation が同packageにあれば CANON と区別して後発working stateとして取り込んでください。  
> 具体的論点だけ current/technical を読み、不足時のみ source-v22b-full-exact の該当親へ降りてください。  
> sibling branch の未来や旧provenanceをcurrentへ逆流させず、factory accepted / service released / assigned / serviceable / forward / combat-present を分離してください。

---

## 9. このファイル自身の更新方針

このガイドは版番号を固定しない。

更新が必要なのは:
- ディレクトリ構造が変わったとき
- authority model が変わったとき
- exact source の場所が変わったとき
- CANON / WORKING / provenance の読み方が変わったとき

V27 / V28 等へ進んでも、単に版番号が変わっただけならこのファイルの基本構造はそのまま使う。
