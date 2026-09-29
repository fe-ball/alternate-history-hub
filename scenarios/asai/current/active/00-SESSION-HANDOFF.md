# 浅井世界線 — 現行継続handoff

Status: NAVIGATION-ONLY / SOURCE-BOUND ROLLUP / NO CANON PROMOTION

## 現在地

対象は scenarios/asai の中国戦継続軸（V24 → V25 → V26 → POST-V26 WORKING）。asai-china-war-v24-v26-post-v26 はナビゲーション識別子で、Git branch名や新しい歴史決定ではない。

**正本はV26、正本時計は1941-12-07 14:30 HST（当時のUTC−10:30）。正本時計そのものは進めない。**
日米戦は開戦済み、中国戦は継続、日ソ戦はV25の非開戦状態を継承し、後続で開戦を指定した記録はない。

一方、POST-V26 WORKINGでは戦役ごとのreplay-local時計を用いており、最新の議論frontierは **1942-04-16夕刻のMO枝** まで進んでいる。これは全世界時計でもCANON promotionでもない。

## 実際の作業の流れ

真珠湾・Enterprise → 南方作戦局所監査 → Wake第一次・第二次とSaratoga戦 → 1941航空輸送WORKING-CLOSE → AT-3技術再監査 → 第一次インド洋作戦と西方基地航空・水雷艇需要 → Doolittle型空襲の実行条件 → 前倒しMOのTulagi / Coral Sea / Port Moresby進入replay。

最新の大きなWORKING状態は V26:12 にまとめた。

- 第一次インド洋作戦は当面一区切り。
- Doolittle型作戦は構想・訓練を残すが、歴史日付へ自動固定しない。
- MOは4月8日級Tulagiから開始するreplay-local枝。
- 4月9～16日の空母戦・基地航空・China Strait進入をWORKINGで進めた。
- 4月16夕刻時点でSaratogaとYorktownはMOから事実上排除方向、Shokakuも航空運用不能、Zuikaku / Shoho / Rabaul-Lae航空とMO船団はまだ作戦を継続。
- 次の決定点はCrace型連合軍水上部隊と日本輸送船団護衛の水上接触。

## いま再開する論点

**1942-04-16夕刻以後のMO水上戦。**

ただし、次回は戦闘結果を先に置かない。

最初に以下を監査する：

1. 日本側の実際の護衛OOB（Yubari、駆逐艦、CruDiv 6から何隻がどこにいるか、Shoho損傷後の速度・航空運用）。
2. 連合軍Crace型部隊のこの早い4月時点の実際の集中可能艦。
3. 九三式魚雷の艦別発射管・再装填・射撃指揮。
4. 艦別FCS、夜間光学、通信、電探の有無。
5. 損傷・弾薬・燃料・乗員疲労。
6. 月齢・視程・天候・海況。
7. 輸送船団の位置、速度、隊形と、護衛が船団からどこまで離脱できるか。

九三式については現行技術正本を確認済み。弾体性能はほぼ史実どおりで、世界線差は発射・再装填・FCS・夜間光学/通信・編隊同期の統合側。15 kmを約9.7分、20 kmを約13分で走るため、長距離では目標の針路・速力誤差が支配的。

**連合軍が1942年4月に九三式の長射程挙動を正しく理解していたとは未確定。** 次回、偶然の変針で雷撃線を外した場合は、明示的な魚雷発見・情報・戦訓がない限り「九三式を理解して意図的に回避」としない。

日本側の発射後変針も、「撃っていないように見せる」より、自艦安全、編隊整理、自軍魚雷航跡との干渉回避、再装填・次斉射・砲戦位置、敵雷撃回避、船団保護を優先する。具体的変針は接触時の方位・発射角・隊形から計算する。

## 根拠と次の読み順

ファイル番号は ACTIVE-STATE.json の sources で解決する。

まず：
- V26:12 = 最新POST-V26 WORKING handoff（西方 / Doolittle / early MO / surface-next-gate）
- V26:07 = Wake / Saratoga / carrier repair and regeneration
- V26:05 = Enterprise / Southern / first Wake provenance
- V26:08–11 = airlift / AT-3 technical work

水上戦技術は次に：
- 85-CURRENT-2026-09-12-NAVAL-CRP-CONSOLIDATION-V17/06-SURFACE-TYPE93-EMPLOYMENT-AND-SHIP-INTEGRATION-CLOSEOUT-V1.md
- 71-CURRENT-TECHNICAL-CONTROL-V9/04-NAVAL-COMPUTATION-FCS-INTEGRATION-CLOSURE-V9.md
- 71-CURRENT-TECHNICAL-CONTROL-V9/07-NAVAL-FCS-CLASS-CLOSEOUT-V9.md

この要約と原記録が食い違ったら、同軸の更新を調べる。旧枝・別シナリオの未来時刻で解決しない。
