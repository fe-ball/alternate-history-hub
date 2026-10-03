# 浅井世界線

[汎用ガイド](00-READ-FIRST-GENERIC.md) → [現行軸・時計・次ゲート](current/ACTIVE-STATE.json) → [現行handoff](current/active/00-SESSION-HANDOFF.md)。開始文は [START-PROMPT.txt](START-PROMPT.txt)。

現行軸は中国戦継続V24→V25→V26→post-V26 WORKING。日米戦開戦済み・日ソ戦未開戦。V26正本時計は1941-12-07 14:30 HSTのまま。

POST-V26には複数のreplay-local枝がある。既存MO枝はPort Moresby攻略後の1942-04-30夕刻carrier-contactまで保存されているが、現在の議論フロンティアはFT再監査で過去へ戻り、1942Q1の対艦損耗・Saratoga修理時計・第一次インド洋作戦を再評価した結果、**1942-04-05午後のForce A接触→日本第一撃判断**へ移っている。MO枝は削除せず凍結し、後で差分を伝播する。

最新WORKING原文は：
- [V26:17 FT/Q1/Indian Ocean handoff](records/V26/17-POST-V26-FT-Q1-INDIAN-OCEAN-WORKING-HANDOFF-2026-10-04.md)
- [V26:18 decision register](records/V26/18-POST-V26-FT-Q1-INDIAN-OCEAN-WORKING-DECISION-REGISTER-2026-10-04.tsv)

## 現在のnext gate

1942-04-05 15:32級、B5N索敵機が英Force Aを発見した中央WORKING枝から、日本側第一撃の時刻・規模・兵装・攻撃軸を決める。

「夜間IRを使いたい」という案は、一部士官・技術者の面白い技術的欲望として記録済みだが、IRの識別能力・夜間航法・編隊・発着艦/回収負担から、**意図的に夜を狙う中央作戦案にはしない**。次回はこの論点を再オープンせず第一撃から進める。

## 構造

- current/active：現在のhandoff・decision register・chronology/state・open items。
- current/ACTIVE-STATE.json：現行軸と正本時計・複数WORKING frontierを束ねるナビゲーション正本。
- current/technical：具体的な技術論点の入口。歴史上の調達・配備・戦闘使用とは別。
- records：現行軸の原資料と親。記録本文・確定度は保存し、次の作業指示だけ現行ビューで解決する。
- archive：別歴史枝・旧入口。通常の探索対象外。
- navigation：旧パス解決・検証・保全記録。

シナリオルールは [SCENARIO-RULES.md](SCENARIO-RULES.md)。`keisanki-ibun`は別シナリオであり、版番号や更新日が新しくても浅井の継続先ではない。

この整理はnavigationのみ。CANON、WORKING-CLOSE、WORKING、OPENを混同せず、最大version/最新日付/最も未来の時計を自動currentにしない。
