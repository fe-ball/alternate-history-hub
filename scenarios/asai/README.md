# 浅井世界線

[汎用ガイド](00-READ-FIRST-GENERIC.md) → [現行軸・時計・次ゲート](current/ACTIVE-STATE.json) → [現行handoff](current/active/00-SESSION-HANDOFF.md)。開始文は [START-PROMPT.txt](START-PROMPT.txt)。

現行軸は中国戦継続V24→V25→V26→post-V26 WORKING。日米戦開戦済み・日ソ戦未開戦。V26正本時計は1941-12-07 14:30 HSTだが、継続作業は真珠湾/Enterprise→南方の局所検討→Wake/Saratoga→1941輸送航空WORKING-CLOSE→AT-3再監査まで進んだ。次は試作試験・1942調達トリガー。正本時計と最新作業点を同一視しない。

## 構造

- current/active：現在のhandoff・decision register・chronology/state・open items。
- current/ACTIVE-STATE.json：現行軸と四種類の時点を束ねるナビゲーション正本。原履歴を自動上書きしない。
- current/technical：具体的な技術論点の入口。歴史上の調達・配備・戦闘使用とは別。
- records：現行軸の原資料と親。記録本文・確定度は保存し、次の作業指示だけ現行ビューで解決する。
- archive：別歴史枝・旧入口。通常の探索対象外。
- navigation：旧パス解決・検証・保全記録。

シナリオルールは [SCENARIO-RULES.md](SCENARIO-RULES.md)。`keisanki-ibun`は別シナリオであり、版番号や更新日が新しくても浅井の継続先ではない。Libraryや古いexportのCURRENT自己申告より、同軸の実際の継続関係を照合する。

この整理はnavigationのみ。CANON、WORKING-CLOSE、WORKING、OPENを変更せず、importのexact sourceと技術正本も変更していない。
