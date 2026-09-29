# 発動機転生者

現代の自動車用ガソリンエンジン技術者が、名古屋の織機工場の家に生まれ、航空発動機事業を育てる世界線。
浅井世界線／計算機異聞とは別シナリオ。

> **Navigation status:** current router
> **Current authority:** Relaunch R3
> **Canonical historical clock:** **1942-06-04T13:30:00-10:30**
> **Authority entrypoint:** [relaunch/00-START-HERE.md](relaunch/00-START-HERE.md)
> **Current war ledger:** [relaunch/14-WAR-LEDGER-1941-12-07-TO-1942-06-04-MIDWAY-CHECKPOINT.md](relaunch/14-WAR-LEDGER-1941-12-07-TO-1942-06-04-MIDWAY-CHECKPOINT.md)

機械可読のauthority / clock / frontierはリポジトリ直下の `scenarios.yaml` を正とする。
このREADMEと競合した場合は、`scenarios.yaml` が指す `authority_entrypoint` と、その入口が明示するsupersessionを優先する。

## 読み順

1. [固有ルール](SCENARIO-RULES.md)
2. [現行authority入口](relaunch/00-START-HERE.md)
3. authority入口の **現在の読み順** に従い、必要なengine / aircraft / naming / war-ledgerを読む
4. 現行論点では特に [14 — 真珠湾後〜ミッドウェー午後チェックポイント](relaunch/14-WAR-LEDGER-1941-12-07-TO-1942-06-04-MIDWAY-CHECKPOINT.md) を優先する

最大version、更新日の新しさ、記述年代の未来さだけでauthorityを決めない。

## 現checkpoint

**1942-06-04 約13:30、ミッドウェー海戦中。**

- 第一機動部隊は赤城・加賀・蒼龍・飛龍・翔鶴・瑞鶴の六空母集中。
- 赤城は中〜大破、加賀は大破で、両艦とも航空作戦不能。ただし最終的な船体運命は未確定。
- 蒼龍・飛龍・翔鶴・瑞鶴は健在。
- 米Enterprise/Hornetは二度の日本空襲でmission killまで進んだが、放棄・自沈・撃沈・拿捕は **OPEN**。
- 以前の「米側が放棄・自沈し、日本側追撃隊が夕刻撃沈」という展開は現行正本では採用しない。

## current frontier

次の順で閉じる。

1. Enterprise/Hornet個艦ごとの13時台損傷状態と曳航可能性
2. 米側が空母救援のため重巡・駆逐艦screenをどこまで危険に残すか
3. 日本側が追加航空雷撃・水上追撃・拿捕／曳航のどれを選ぶか
4. 赤城・加賀退避、Midway第二撃、残存航空兵力との競合
5. その後にのみ夕刻／夜戦と米二空母の最終運命を進める

## Authority / status規律

- **CLOSED:** 次の計算入力として採る
- **PROVISIONAL:** 現時点の最良案。監査で変更しうる
- **OPEN:** 未決
- **REFERENCE:** 旧体系・比較用

2026-09-21のリランチ以前の旧 `current/` / `archive/` は名前にかかわらずREFERENCE。
旧数値・旧製品系列・旧機体史は、リランチ正本で明示的に再採用しない限り自動継承しない。

[pre-relaunch参考資料索引](pre-relaunch/README.md) / [取り込み状況](import/IMPORT-STATUS.md) / [汎用セッション開始プロンプト](SESSION-START-PROMPT.md)
