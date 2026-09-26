# 浅井世界線 — 現行継続handoff

Status: NAVIGATION-ONLY / SOURCE-BOUND ROLLUP / NO CANON PROMOTION

## 現在地

対象は `scenarios/asai` の中国戦継続軸（V24 → V25 → V26 → POST-V26 WORKING）。`asai-china-war-v24-v26-post-v26` は今回の整理で付けたナビゲーション識別子で、Git branch名や新しい歴史決定ではない。

**正本はV26、正本時計は1941-12-07 14:30 HST（当時のUTC−10:30）。作業の続きは真珠湾へ戻さない。**
日米戦は開戦済み、中国戦は継続、日ソ戦はV25の非開戦状態を継承し、後続で開戦を指定した記録はない。

## 実際の作業の流れ

真珠湾・Enterprise → 南方作戦を局所的に確認 → Wake第一次・第二次とSaratoga戦 → 1941年航空輸送を再監査してWORKING-CLOSE → AT-3大型輸送機の技術再監査。

最新の戦役上の明示的なWORKING-CLOSEはWakeの12月23日午後陥落。後発資料には年末輸送台帳と修理・再生・翌年計画が含まれるが、一つの全世界working時計にはまとめない。南方の後日ケーススタディも全戦域の時計を進めない。

## いま再開する論点

**AT-3の試作構造・ランプ・脚・E6搭載試験、および1942年調達を発動する条件。**
AT-3再監査を未着手としてやり直さない。1941年航空輸送の監査対象における阻害OPEN=0は継承するが、AT-3の試験・調達ゲートまで閉じたという意味ではない。

元資料の確定度を保つ。Enterpriseの修理日程はWORKING、Wake陥落はWORKING-CLOSE、航空輸送とAT-3の各採用値にもそれぞれの原statusがある。V26より後を一括でCANONにしない。

## 根拠と次の読み順

ファイル番号は [ACTIVE-STATE.json](../ACTIVE-STATE.json) の `sources` で解決する。
V26:00–04＝正本アンカー、05–06＝Enterprise・南方・第一次Wake、07・09＝第二次Wake/Saratoga、08・09＝航空輸送、10・11＝AT-3。

次に [decision register](01-DECISION-REGISTER.tsv) → [chronology/state](02-CONTINUITY-STATE.md) → [open items/next gates](03-OPEN-ITEMS-AND-NEXT-GATES.tsv)。原handoffは [05](../../records/V26/05-POST-V26-WORKING-HANDOFF-2026-09-26.md) と [07](../../records/V26/07-POST-V26-WAKE-SARATOGA-CARRIER-WORKING-CONTINUATION-2026-09-26.md)、最新原registerは [11](../../records/V26/11-AT3-WORKING-DECISION-REGISTER-2026-09-26.tsv)。

この要約と原記録が食い違ったら同軸の更新を調べる。旧枝・別シナリオの未来時刻で解決しない。
