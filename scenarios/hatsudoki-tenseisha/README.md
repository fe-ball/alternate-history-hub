# 発動機転生者

現代の自動車用ガソリンエンジン技術者が、名古屋の織機工場の家に生まれ、航空発動機事業を育てる世界線。
浅井世界線／計算機異聞とは別シナリオ。

> **Navigation status:** current router
> **Current authority:** Relaunch R3
> **Canonical historical clock:** **1942-06-04T18:45:00-10:30**
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

**1942-06-04 約18:45、ミッドウェー海戦夕刻。**

- 赤城・加賀は航空作戦不能だが船体は生存し、自航退避中。
- 蒼龍・飛龍・翔鶴・瑞鶴は健在。
- 米二空母の最終運命はCLOSED。
- **Enterprise:** 米側PhelpsのMk 15自沈斉射を受けても沈まず、日本側が18:45級に船体を完全確保。主機・操舵・main power dead、list 25–28°級。
- **Hornet:** abandoned / scuttle-damaged後、日本側が救艦不能と判定しfinish torpedo。最終沈没確定。
- 米surface forceはsurvivorsを抱えて東退。

## current frontier

Enterprise prizeの初夜生存はside-ledgerで先に監査済み。canonical clockは **1942-06-04 18:45** に据え置く。

次はMidway本体へ戻る。

1. 18:45以後の夕刻第二撃を出せるか
2. 夜間水上砲撃を行うか
3. 6/5 dawn carrier strikeの規模
4. occupation / support forceの前進
5. Enterprise prize protectionとの資源競合

Prize側の最低拘束は、筑摩＋DD4、dawn CAP 12–16級、fast oiler pair＋秋雲recall。これをMidway strikeへ二重計上しない。

## Authority / status規律

- **CLOSED:** 次の計算入力として採る
- **PROVISIONAL:** 現時点の最良案。監査で変更しうる
- **OPEN:** 未決
- **REFERENCE:** 旧体系・比較用

2026-09-21のリランチ以前の旧 `current/` / `archive/` は名前にかかわらずREFERENCE。
旧数値・旧製品系列・旧機体史は、リランチ正本で明示的に再採用しない限り自動継承しない。

[pre-relaunch参考資料索引](pre-relaunch/README.md) / [取り込み状況](import/IMPORT-STATUS.md) / [汎用セッション開始プロンプト](SESSION-START-PROMPT.md)
