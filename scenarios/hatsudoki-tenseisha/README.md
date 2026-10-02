# 発動機転生者

現代の自動車用ガソリンエンジン技術者が、名古屋の織機工場の家に生まれ、航空発動機事業を育てる世界線。
浅井世界線／計算機異聞とは別シナリオ。

> **Navigation status:** current router
> **Current authority:** Relaunch R3
> **Canonical historical clock:** **1942-06-26T18:00:00-10:30**
> **Authority entrypoint:** [relaunch/00-START-HERE.md](relaunch/00-START-HERE.md)
> **Current war ledger:** [relaunch/14-WAR-LEDGER-1941-12-07-TO-1942-06-04-MIDWAY-CHECKPOINT.md](relaunch/14-WAR-LEDGER-1941-12-07-TO-1942-06-04-MIDWAY-CHECKPOINT.md)
> **Forward planning ledger:** [relaunch/15-ENTERPRISE-RECONSTRUCTION-AND-CARRIER-BUILDUP-1942.md](relaunch/15-ENTERPRISE-RECONSTRUCTION-AND-CARRIER-BUILDUP-1942.md)
> **Next-session world ripple ledger:** [relaunch/16-WORLD-STRATEGY-RIPPLE-1942H2.md](relaunch/16-WORLD-STRATEGY-RIPPLE-1942H2.md)

機械可読のauthority / clock / frontierはリポジトリ直下の `scenarios.yaml` を正とする。
このREADMEと競合した場合は、`scenarios.yaml` が指す `authority_entrypoint` と、その入口が明示するsupersessionを優先する。

## 読み順

1. [固有ルール](SCENARIO-RULES.md)
2. [現行authority入口](relaunch/00-START-HERE.md)
3. authority入口の **現在の読み順** に従い、必要なengine / aircraft / naming / war-ledgerを読む
4. 現行論点では特に [14 — 真珠湾後〜ミッドウェー午後チェックポイント](relaunch/14-WAR-LEDGER-1941-12-07-TO-1942-06-04-MIDWAY-CHECKPOINT.md) を優先する
5. Enterprise再建・工廠負荷・空母建造の6/26時点forward planは [15 — Enterprise再建・ミッドウェー後工廠負荷・空母建造計画](relaunch/15-ENTERPRISE-RECONSTRUCTION-AND-CARRIER-BUILDUP-1942.md) を参照する
6. 1942年後半へ時計を進める前の世界波及監査は [16 — 世界戦略波及 1942H2](relaunch/16-WORLD-STRATEGY-RIPPLE-1942H2.md) を参照する

最大version、更新日の新しさ、記述年代の未来さだけでauthorityを決めない。

## 現checkpoint

**1942-06-26 約18:00、Enterprise Kwajalein sheltered salvage・Midway radar-assisted base。**

- 赤城・加賀は航空作戦不能だが船体は生存し、自航退避中。
- 蒼龍・飛龍・翔鶴・瑞鶴は健在。
- 米二空母の最終運命はCLOSED。
- **Enterprise:** 米側PhelpsのMk 15自沈斉射を受けても沈まず、日本側が18:45級に船体を完全確保。主機・操舵・main power dead、list 25–28°級。
- **Hornet:** abandoned / scuttle-damaged後、日本側が救艦不能と判定しfinish torpedo。最終沈没確定。
- 米surface forceはsurvivorsを抱えて東退。

## current frontier

1942-06-26 約18:00。

CLOSED central:
- Enterprise:
  - 6/23 Mk14 contact dud
  - 6/25 Kwajalein lagoonへ安全入泊
  - Akashi + Urakami Maru sheltered salvage
  - list 7–9°
  - main propulsion / steering / ship main power dead
  - 5kt-class next towはPROVISIONAL
- Midway:
  - fighters 42–46、central 44
  - B5N 12–15
  - D3A 8–12
  - land-attack 6級
  - fixed early-warning radar 1基 operational
  - radar-assisted forward base
- Saratoga = Hawaii
- Wasp = 6/24–25 San Diego発Pearl向けへ転用
- selected Enterprise photos already public
- foreign physical inspectionはKwajaleinでは行わない

次は、
0. 1942H2 world ripple audit — Ironclad / Pedestal / PQ18 / Torch / CVE / Atlantic / Persian Corridor
1. 6/27–7/3 Enterprise sheltered repair / Truk tow decision
2. Saratoga + Wasp Pearl concentration
3. Midway fuel / radar / land-attack maturity
4. Akagi / Kaga major-yard repair timeline
5. Enterprise technical / propaganda exploitation second stage

Forward-plan CLOSED central:
- EnterpriseはKwajalein → Truk → Kureを中央線とする
- Kureでは米式四軸原状復旧を中央にせず、日本式6缶・104,000shp-class・4軸plantと大型replacement sectionsで再建する
- 改装工程は中庸を中央とし、1943-08級limited operational readinessをplanning centerとする
- Hyugaのみ航空偵察戦艦化を確定維持、IseはOPEN
- carrier mass-production planは史実級の全力枠を維持し、R3差分は後続艦の中止・遅延・割込み減少として扱う
- 詳細は [15](relaunch/15-ENTERPRISE-RECONSTRUCTION-AND-CARRIER-BUILDUP-1942.md)

## Authority / status規律

- **CLOSED:** 次の計算入力として採る
- **PROVISIONAL:** 現時点の最良案。監査で変更しうる
- **OPEN:** 未決
- **REFERENCE:** 旧体系・比較用

2026-09-21のリランチ以前の旧 `current/` / `archive/` は名前にかかわらずREFERENCE。
旧数値・旧製品系列・旧機体史は、リランチ正本で明示的に再採用しない限り自動継承しない。

[pre-relaunch参考資料索引](pre-relaunch/README.md) / [取り込み状況](import/IMPORT-STATUS.md) / [汎用セッション開始プロンプト](SESSION-START-PROMPT.md)
