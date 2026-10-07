# 浅井世界線

[汎用ガイド](00-READ-FIRST-GENERIC.md) → [現行軸・時計・次ゲート](current/ACTIVE-STATE.json) → [現行handoff](current/active/00-SESSION-HANDOFF.md)。開始文は [START-PROMPT.txt](START-PROMPT.txt)。

現行軸は中国戦継続V24→V25→V26→post-V26 WORKING。日米戦開戦済み・日ソ戦未開戦。**V26正本時計は1941-12-07 14:30 HSTのまま**であり、1942年の検討はreplay-local WORKINGとして扱う。

現行のresume authorityは固定READMEではなく [current/ACTIVE-STATE.json](current/ACTIVE-STATE.json) と active 4文書。旧entrypoint、古いnext gate、最も未来の日付だけから再開位置を決めない。

## 最新WORKING原文

- [V26:25 fleet-equipment integration](records/V26/25-POST-V26-FLEET-EQUIPMENT-INTEGRATION-WORKING-HANDOFF-2026-10-07.md)
- [V26:26 matching decision register](records/V26/26-POST-V26-FLEET-EQUIPMENT-INTEGRATION-WORKING-DECISION-REGISTER-2026-10-07.tsv)
- [V26:27 MI escort / radar / ASW allocation](records/V26/27-POST-V26-MI-ESCORT-RADAR-ASW-WORKING-HANDOFF-2026-10-07.md)
- [V26:28 matching decision register](records/V26/28-POST-V26-MI-ESCORT-RADAR-ASW-WORKING-DECISION-REGISTER-2026-10-07.tsv)
- [V26:29 FT tactical-doctrine integration](records/V26/29-POST-V26-FT-TACTICAL-DOCTRINE-INTEGRATION-WORKING-HANDOFF-2026-10-07.md)
- [V26:30 matching decision register](records/V26/30-POST-V26-FT-TACTICAL-DOCTRINE-WORKING-DECISION-REGISTER-2026-10-07.tsv)
- [V26:31 spring-1942 ordnance stock / MI allocation](records/V26/31-POST-V26-SPRING-1942-ORDNANCE-STOCK-MI-ALLOCATION-WORKING-HANDOFF-2026-10-07.md)
- [V26:32 matching decision register](records/V26/32-POST-V26-SPRING-1942-ORDNANCE-STOCK-MI-ALLOCATION-WORKING-DECISION-REGISTER-2026-10-07.tsv)
- [V26:33 Apr29 Shokaku hit/damage/repair](records/V26/33-POST-V26-APR29-SHOKAKU-HIT-DAMAGE-REPAIR-WORKING-HANDOFF-2026-10-07.md)
- [V26:34 matching decision register](records/V26/34-POST-V26-APR29-SHOKAKU-HIT-DAMAGE-REPAIR-WORKING-DECISION-REGISTER-2026-10-07.tsv)

V26:21-24 remain required predecessors for repair/MO/Lexington/Doolittle/MI-AL planning, but they no longer define the latest next gate by themselves.

## 最新中央の要点

- Enterprise: no-I-75 working branch、late-Mar戦列復帰計画
- Saratoga: Wake損傷修理がApr下旬まで延び、Apr10 MO不在
- Yorktown: Apr9 mission kill、deep repair
- 旧Apr10 Saratoga/Shokaku戦はSUPERSEDED
- Crace: Apr12 Chicago=FT/HE+Type91、Australia=FT-IR/SAP、Crace後退
- Doolittle型: Enterprise+Hornet、Apr21-23級 / center Apr22
- Port Moresby: Apr15 Taurama → Apr18 physical capture
- Lexington: Apr11南下、Apr27 H7Y接触、Apr29 CarDiv5戦
- Lexington lost central
- **Shokakuの旧1000lb級2発固定mission-kill結果はSUPERSEDED。V26:33-34で1x1000lb級 direct hit centralを採用し、forward-starboard/island-adjacent flight deck→upper hangar hit、battle-day aviation mission kill、frontline return Jun9-11 center、MI不参加中央までWORKING-CLOSE**
- Zuikaku hull combat-effective central。air-group attrition / regenerationはOPEN
- MIはALと分離して先行。Shokaku復帰は待たない
- Zuikakuは再編航空隊でMI参加中央、Ryujoはfighter-heavy CAP/search/torpedo-support carrier
- MI carrier-supportはNagara + 16 DD。Arashi / Urakaze / Kazagumoを中央DD surface-radar picketとする
- Type21-line carrier air-warning中央3基、Type22-line surface-search中央7基
- FTはFT-G / FT-GR / standard FT / FT-GR-IR / FT-IRを別familyとして扱い、HE/SAPを別軸管理する

FTの厳密speed / acceleration / release range / TOF / fuel / fuse / penetrationはparallel technical OPEN。これらを理由にMI force-state作業を停止しない。

## 現在のnext gate

**V26:33-34でApr29 Shokaku central damage/repairまでWORKING-CLOSE。Apr29 air-loss ledgerから再開する。**

1. Apr29双方のairframe / aircrew loss ledgerを閉じる
2. Zuikaku等のcarrier-air-group regenerationを閉じる
3. MI final one-sheet OOBへ統合
4. 上記が閉じた後にのみMI combat replayへ進む

## 構造

- current/active：現在のhandoff・decision register・chronology/state・open items。
- current/ACTIVE-STATE.json：現行軸、正本時計、working frontier、次ゲートを束ねるナビゲーション正本。
- current/technical：具体的な技術論点の入口。技術成立と歴史上の調達・配備・戦闘使用は別。
- records：現行軸の原資料と親。原statusを保存する。
- archive：別歴史枝・旧入口。通常探索から外す。
- navigation：旧パス解決・検証・保全記録。
- import：原資料復旧・完全性監査。**scenario resume authorityではない。**

シナリオルールは [SCENARIO-RULES.md](SCENARIO-RULES.md)。`keisanki-ibun`は別シナリオ。

この整理はnavigationのみ。CANON、WORKING-CLOSE、WORKING、OPENを混同しない。
