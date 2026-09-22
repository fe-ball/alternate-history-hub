# Import Status — 完全取り込み確認 2026-09-20 / current pointer repaired 2026-09-23

指定された原本ZIPと、その全ファイルをGit管理対象に取り込み済みです。

- 原本: [ZIP](archives/計算機異聞_BRANCH_B_v097_FULL_HANDOFF_1944-04-30T2400_AIRCRAFT_HISTORY_NEXT_2026-09-19(1).zip)（27,078,890 bytes）
- SHA-256: `29e2d71e234cfdfab108b15054c3ad1014c6f68ad7778d67d591d110950e40fb`
- 展開保存先: [source-v097-full/](source-v097-full/)
- ファイル: **2,071 / 2,071**
- 展開後容量: 51,813,460 bytes
- ZIP CRC検査: 全件合格
- 原本ZIPコピーおよび展開ファイル: 全件SHA-256一致
- [ファイル別パス・サイズ・SHA-256一覧](FULL-IMPORT-MANIFEST-2026-09-20.tsv)
- [検証結果](FULL-IMPORT-AUDIT-2026-09-20.json)

## 保存範囲

旧版、監査履歴、バイナリ、入れ子ZIPを含め、元ZIP直下の全ファイルを保存しています。
入れ子ZIPはファイルとして原寸保存し、再帰展開はしていません。空ディレクトリの記録も原本ZIPに残ります。
展開時はZIP内の名前をそのまま使用し、元から含まれる文字化け名を推測で修正していません。
元ZIPから保存先への対応はmanifestに記録しています。

## 現行authorityとの関係

Import package itself is a **v097 source/provenance snapshot**.

Current scenario identity is controlled by the central registry and current authority entrypoint, not by this import directory:

- Current authority: **Branch B v100**
- Canonical clock: **1944-06-16T14:15**
- Authority entrypoint: [00_READ_FIRST_CURRENT_V100_2026-09-21.md](../current/00_CURRENT_AUTHORITY/00_READ_FIRST_CURRENT_V100_2026-09-21.md)

Authority chain:
**v100 > v099 > v098 > v097 > v096 > older retained authority where non-conflicting.**

旧資料の収録はCANONへの昇格を意味しません。各資料のsupersession・WORKING・OPEN・ARCHIVE等の状態を維持します。
旧い later-clock force ledgers も、時計が先という理由だけでは current に復帰しません。

The import audit records the authority that was current **at import time**. Current authority must be read from `scenarios.yaml` and the authority entrypoint.
