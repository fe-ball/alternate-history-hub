# NEXT CHAT — 紫雲・母艦・索敵資産と資料継承の再接続

Status: **WORKING / PROVENANCE AUDIT / NOT AUTHORITY / NO CLOCK ADVANCE**

正本は **Branch B v100 / 1944-06-16T14:15** のまま。Saipan地上の独立した承認済み前線は **6/16夜明け** まで。全体時計を地上閉鎖時計へコピーしない。

## 今回の入口

1. [発掘監査・訂正・未閉鎖項目](PROVENANCE_RECOVERY_2026-09-25/README.md)
2. [回収原文の対照表](PROVENANCE_RECOVERY_2026-09-25/SOURCE_INDEX.md)
3. [保全・走査検証](PROVENANCE_RECOVERY_2026-09-25/SCAN_VERIFICATION.json)
4. [同時更新された廃止資料規則との関係](PROVENANCE_RECOVERY_2026-09-25/CONCURRENT_POLICY_CHECK.md)
5. 必要な原文だけを [RETAINED_SOURCE_NOT_CURRENT](PROVENANCE_RECOVERY_2026-09-25/RETAINED_SOURCE_NOT_CURRENT/README.md) から読む。
6. 既存 [17日夕刻再開メモ](00_NEXT_CHAT_17JUN_EVENING_REGEN_ROTATION_I400_TF58_2026-09-24.md) と [艦隊監査snapshot](FLEET_HULL_ESCORT_REAUDIT_WORKING_SNAPSHOT_2026-09-23.md) へ接続する。

## 先に直す取り違え

現行repoは `fe-ball/alternate-history-hub/scenarios/keisanki-ibun`。以前の会話が暫定差分を書いた `fe-ball/--1/計算機異聞/WORKING_DELTAS_2026-09-25` とは別。旧repoで検索不発だったことは現行資料不存在の証明ではない。旧private repoの会話差分全文は今回公開複製していない。廃止された旧8月時計／9月2日作業を根拠へ復帰させない。

v097外側全2,071ファイルの原文・元パスから再計算したGit treeは、現行importのtreeと一致。資料バイトの欠落と、参照・継承・機種別監査の欠落を区別する。

## 次の順序

大淀の既存役割と他戦域派遣履歴を先に接続し、紫雲の要求・試験・採用・生産・搭載実態を監査する。並行して瑞雲・彩雲・D4Y偵察・旧来水偵・日米飛行艇を、型式／母艦・基地／乗員／機材／通信／可動／即応に分解する。

その後に6/16→6/18の配置・消耗・回復を通し、18日午後の発見時刻、触接更新、報告遅延、攻撃見送り、夜間幾何を再評価する。必要なら同じ前提に依存する17日以前へも影響を追う。全部を無条件に巻き戻さず、暫定結果を守るため不一致を無視もしない。

TF58全体系ASWメタ監査はpost-14:15昇格前の必須gateとして維持。今回の原文回収も、旧本文のcanonical/closed表記も、現行への自動昇格ではない。
