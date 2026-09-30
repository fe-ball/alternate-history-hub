# 発動機転生者

現代の自動車用ガソリンエンジン技術者が、名古屋の織機工場の家に生まれ、航空発動機事業を育てる世界線。
浅井世界線／計算機異聞とは別シナリオ。

> **Navigation status:** current router
> **Current authority:** Relaunch R3
> **Canonical historical clock:** **1942-06-07T18:00:00-10:30**
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

**1942-06-07 約18:00、Midway初期基地復旧。**

- 赤城・加賀は航空作戦不能だが船体は生存し、自航退避中。
- 蒼龍・飛龍・翔鶴・瑞鶴は健在。
- 米二空母の最終運命はCLOSED。
- **Enterprise:** 米側PhelpsのMk 15自沈斉射を受けても沈まず、日本側が18:45級に船体を完全確保。主機・操舵・main power dead、list 25–28°級。
- **Hornet:** abandoned / scuttle-damaged後、日本側が救艦不能と判定しfinish torpedo。最終沈没確定。
- 米surface forceはsurvivorsを抱えて東退。

## current frontier

1942-06-07 約18:00。

CLOSED central:
- Midway 6/6 tactical capture
- 11th / 12th Construction Units surviving work force ~1,900–2,200
- Eastern 3,500–4,000ft narrow fighter lane provisional-operational
- first 4–6 Japanese fighters ashore
- Sand fuel system badly damaged / sabotaged
- US SCR-270 not restored to service
- Enterprise: Shinkoku tow 2.8–3.2kt、list 20–22°、Chikuma released
- Saratoga direct Midway reliefなし、US immediate offensive emphasisはsubmarines / PBY reconnaissance

次は、
1. 6/8–6/10 Midway self-defense transition
2. Enterprise repair-team / Akashi rendezvous
3. Saratoga / submarine / PBY US counteraction
4. Akagi / Kaga / four-carrier post-MI disposition

## Authority / status規律

- **CLOSED:** 次の計算入力として採る
- **PROVISIONAL:** 現時点の最良案。監査で変更しうる
- **OPEN:** 未決
- **REFERENCE:** 旧体系・比較用

2026-09-21のリランチ以前の旧 `current/` / `archive/` は名前にかかわらずREFERENCE。
旧数値・旧製品系列・旧機体史は、リランチ正本で明示的に再採用しない限り自動継承しない。

[pre-relaunch参考資料索引](pre-relaunch/README.md) / [取り込み状況](import/IMPORT-STATUS.md) / [汎用セッション開始プロンプト](SESSION-START-PROMPT.md)
