# 浅井世界線

[汎用ガイド](00-READ-FIRST-GENERIC.md) → [現行軸・時計・次ゲート](current/ACTIVE-STATE.json) → [現行handoff](current/active/00-SESSION-HANDOFF.md)。開始文は [START-PROMPT.txt](START-PROMPT.txt)。

現行軸は中国戦継続V24→V25→V26→post-V26 WORKING。日米戦開戦済み・日ソ戦未開戦。V26正本時計は1941-12-07 14:30 HSTのまま。

POST-V26の1942年時計はreplay-local。最新の議論ではFT damage/repair監査から早期MOを再伝播し、**旧Apr10 Saratoga/Shokaku戦をsupersede、Apr18 Port Moresby physical capture、Apr29-class Lexington vs CarDiv5戦**まで進んでいる。

最新WORKING原文：
- [V26:21 FT repair / MO / Lexington handoff](records/V26/21-POST-V26-FT-REPAIR-MO-LEXINGTON-WORKING-HANDOFF-2026-10-06.md)
- [V26:22 decision register](records/V26/22-POST-V26-FT-REPAIR-MO-LEXINGTON-WORKING-DECISION-REGISTER-2026-10-06.tsv)

## 最新中央の要点

- Enterprise: no-I-75枝、late-Mar戦列復帰
- Saratoga: Wake損傷修理がApr下旬まで延び、Apr10 MO不在
- Yorktown: Apr9 mission kill、深修理
- 旧Apr10 Saratoga/Shokaku戦は削除
- Crace: Apr12 Chicago FT/HE+Type91、Australia FT-IR/SAP
- Doolittle型: Enterprise+Hornet、Apr21-23級
- Port Moresby: Apr15 landing → Apr18 physical capture
- Lexington: Apr11南下、Apr27 H7Y接触、Apr29 CarDiv5戦
- Lexington lost central
- Shokaku mission kill / withdraw
- Zuikaku hull combat-effective
- Shoho combat-effective

FTの厳密speed/range/TOF/fuelはOPENだが、SAP kinetic/internal damage、secondary-fire、miss原因分解、Crace reaction correctionはWORKINGとして反映済み。

## 現在のnext gate

post-Apr29 carrier-force stateから：
1. Shokaku修理時計
2. Zuikaku航空隊損耗/再生
3. Saratoga late-Apr readiness
4. Enterprise/Hornet Doolittle帰還
5. 米太平洋空母balance
6. 日本のMI/AL/FS/other次作戦

FT厳密数値モデルはparallel technical follow-up。

## 構造

- current/active：現在のhandoff・decision register・chronology/state・open items。
- current/ACTIVE-STATE.json：現行軸と正本時計・複数WORKING frontierを束ねるナビゲーション正本。
- current/technical：具体的な技術論点の入口。歴史上の調達・配備・戦闘使用とは別。
- records：現行軸の原資料と親。記録本文・確定度は保存し、次の作業指示だけ現行ビューで解決する。
- archive：別歴史枝・旧入口。通常の探索対象外。
- navigation：旧パス解決・検証・保全記録。

シナリオルールは [SCENARIO-RULES.md](SCENARIO-RULES.md)。`keisanki-ibun`は別シナリオ。

この整理はnavigationのみ。CANON、WORKING-CLOSE、WORKING、OPENを混同しない。
