# 浅井世界線

Status: **active**

Authority: **V23**

Canonical clock: **1946-06-30T24:00級**

Clock state: **1946年一般休戦まで history working-close / source-repair + 1939–1941 retro-audit OPEN**

Current frontier: **完全収録されたV22B原本を基準に、部分取り込み期に生じた可能性のある破損・誤推定を監査修復し、1939–1941の技術・生産・配備状態を回収する。1941年5月台帳を閉じた後、中国戦継続・仏印進駐・改装空母論点へ戻る。**

## Scenario rule

最初に [SCENARIO-RULES.md](SCENARIO-RULES.md) を確認する。

浅井側の先行知識・技術優位は、正本で認められた伝播経路を越えて他国・他組織へ自動コピーしない。

また、1945–46年に閉じた結果を1939–41年の主体知識・物理在庫・制度成熟へ逆流させない。

## 読み順

1. [00-START-HERE-2026-09-19-FULL-V23.md](current/00-START-HERE-2026-09-19-FULL-V23.md)
2. [V23 session handoff](current/91-CURRENT-2026-09-19-CHINA-PEACE-SECOND-CLOSE-V23/00-SESSION-HANDOFF-V23.md)
3. [Import-recovery / technology-recovery handoff](current/91-CURRENT-2026-09-19-CHINA-PEACE-SECOND-CLOSE-V23/05-IMPORT-RECOVERY-TECH-RECOVERY-HANDOFF-V23.md)
4. V23 decision register / chronology / armistice stop-line / retro frontier
5. For source recovery, use **[source-v22b-full-exact/](import/source-v22b-full-exact/)**. Do not use the old partial `source-v22b-full/` when an exact counterpart exists.
6. V22B branch package for inherited 1940–44 German-jet-transfer state
7. V21 year-end handoff for non-conflicting inherited state
8. technical / essence parents referenced by V22B/V21

## Precedence

V23明示決定 > V22B明示決定 > V21の非矛盾部分 > 参照されるV10/V9/V8技術親。

V23は、V22BでOPENだった1945年以降の中心枝を1946年一般休戦までworking-closeする。V23が明示していない技術値はV22B/V21/technical parentを継承する。

**source-v22b-full-exact は原本復旧用の忠実なsource mirrorであり、その収録自体は旧資料をCANONへ昇格させない。** 同時に、元ZIPの内容を確認する場合は部分取り込み・再構成物よりexact mirrorを優先する。

GitHub 上のファイル配置、最大version、作成日、最も未来の記述だけではauthorityを決めない。

## Clock semantics

Canonical clockは歴史再演がworking-closeされた最終地点を示す。

Current frontierは次に議論する対象を示す。V23では両者を意図的に分離し、**canonical clockは1946年、active discussionは1939–41年の修復・技術回収へ戻る**。

## Import status

- [Source package](import/SOURCE-PACKAGE.md)
- [Import status](import/IMPORT-STATUS.md)

V22B source ZIPのprovenanceは保持し、2026-09-20に原本ZIPと全展開ファイルの収録を完了した。V23はこの会話で承認された日中和平ルート第二弾の追加authorityであり、元ZIPへ遡及的に含まれるものではない。

元ZIPに含まれる旧版・監査履歴・ネストした過去ZIP・XLSX等は、`import/source-v22b-full-exact/` に全件保存済み。収録によってcurrentへ自動昇格させない。
