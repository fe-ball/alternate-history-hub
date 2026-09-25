# NEXT CHAT — 航空機・共通生産監査、紫雲／大淀、陸戦取消し

Updated: 2026-09-25, after explicit user audit/reset instruction
Status: **USER-INSTRUCTION RECORD / WORKING AUDIT / NOT EVENT PROMOTION**

正本は **Branch B v100 / 1944-06-16T14:15** のまま。Saipan地上の独立した承認済み前線は **6/16夜明け** まで。今回の会話で作ったその後の陸戦進行・人数・死傷・補給・予備・Aslito見通しは、ユーザー承認により取消し。次の初期値として使わない。

## 最初に読む

1. [今回の指示・取消範囲・大淀の系譜判定](AUDIT_RESET_2026-09-25/00_DECISIONS_AND_OYODO_LINEAGE.md)
2. [全機種群の未閉鎖項目と先行整理・共通生産枠](AUDIT_RESET_2026-09-25/01_AIRCRAFT_GAPS_AND_SHARED_PRODUCTION.md)
3. [紫雲・大淀を丸めず深掘りする専用監査仕様](AUDIT_RESET_2026-09-25/02_SHIUN_OYODO_DEEP_AUDIT_SPEC.md)
4. [前回の発掘監査](PROVENANCE_RECOVERY_2026-09-25/README.md)、[原文対照表](PROVENANCE_RECOVERY_2026-09-25/SOURCE_INDEX.md)、[検証](PROVENANCE_RECOVERY_2026-09-25/SCAN_VERIFICATION.json)。前回の解釈と今回の訂正が競合する場合は今回を優先。
5. 必要な原文だけを [RETAINED_SOURCE_NOT_CURRENT](PROVENANCE_RECOVERY_2026-09-25/RETAINED_SOURCE_NOT_CURRENT/README.md) から読む。旧本文のcanonical/currentは現行への採用証明ではない。

## 先に固定する訂正

- 現行repoは `fe-ball/alternate-history-hub/scenarios/keisanki-ibun`。ユーザーは旧 `--1` 側を他エージェントで除去済みと通知した。復元・再取り込みしない。
- 大淀＋4DDの1月インド洋派遣案／3月継続は旧ベンガル実行系統へ接続する。特に3月表はチッタゴン喪失を前提とする。現行6月の拘束・帰還義務の根拠から除外する。
- 除外の反動で大淀や4DDをトラック／マリアナへ自動配置しない。現行の実所在・命令・整備はOPEN。
- 瑞雲・紫雲以外にも、彩雲、百式司偵、D4Y偵察、旧来水偵、B5N/B6N、飛行艇、夜間・対潜・輸送／教育、米側各種を分離する。
- 既存の型別性能・実戦化時計・空地分離・母艦間再配分・人員還流は、現行根拠を確認した部分から再接続する。史実値へ暗黙復帰させない。
- 生産は誉の5需要を含む共通発動機・工場・修理予備・教育枠で照合。月間生産を日付以前の現地即応へ変換しない。
- 紫雲は「少し良い判断でほどほどに改善」に丸めない。専用の一チャットで要求・機構・実測・採否・大淀適合を掘ってよい。

## 次の順序

機種別の未閉鎖整理と先行訂正 → 紫雲／大淀専用監査と共通生産／受領／修理／配備 → 日米の索敵・防空・ASW・海戦・再生監査 → 別途の陸戦再演。

航空機と生産の作業は往復可能。海戦監査で地上支援・輸送・飛行場・観測へ変更が出れば陸戦へ戻す。地上再演が再び航空作戦を変えれば、そのフィードバックも拒まない。

「CVEが十分いる」だけで日本側の積極的な航空関与を消さない。日本の対地・観測・CVE／輸送／砲撃艦攻撃、米のCAP/ASW/SAR/回収処理、実際に届くCAS・艦砲・荷役・後送を同じ時間線で追う。成功も失敗も先取りしない。

18日午後の日本側先行発見、攻撃見送り、19日朝の幾何は監査の目標値ではない。必要なら17日以前の依存点も再確認する。正本へ及ぶ訂正は根拠と範囲を明示し、黙って上書きしない。

TF58全体系ASWメタ監査はpost-14:15昇格前の必須gateとして維持。[17日夕刻メモ](00_NEXT_CHAT_17JUN_EVENING_REGEN_ROTATION_I400_TF58_2026-09-24.md) と [艦隊監査snapshot](FLEET_HULL_ESCORT_REAUDIT_WORKING_SNAPSHOT_2026-09-23.md) はこの訂正と合わせて読む。
