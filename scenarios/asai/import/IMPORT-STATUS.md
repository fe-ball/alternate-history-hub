# Import Status — 完全取り込み確認 2026-09-20

指定された原本ZIPと、その全ファイルをGit管理対象に取り込みました。

- 原本: [ZIP](archives/ASAI-WORLDLINE-HANDOFF-2026-09-19-FULL-V22B-CHINA-PEACE-GERMAN-JET-BRANCH-GATE(1).zip)（20,996,153 bytes）
- SHA-256: `4bea918064d011331dfe5e0ba3ceed3994e59cc4d2187e84495e59719bc63307`
- 展開保存先: [source-v22b-full-exact/](source-v22b-full-exact/)
- ファイル: **1,122 / 1,122**
- 展開後容量: 27,856,505 bytes
- ZIP CRC検査: 全件合格
- 原本ZIPコピーおよび展開ファイル: 全件SHA-256一致
- [ファイル別パス・サイズ・SHA-256一覧](FULL-IMPORT-MANIFEST-2026-09-20.tsv)
- [検証結果](FULL-IMPORT-AUDIT-2026-09-20.json)

追加の対話内照合でも、アップロードされたZIPとGitHub exact mirrorについて、
- archive Git blob: `c51075904e597ef5b37fb3917f2dd6b64e91f8e2`;
- 1,122ファイル;
- 27,856,505 bytes;
- sorted path + blob + size fingerprint `3f8dbee80b9473f3`
が一致しました。

## 保存範囲と現行正本

旧版、監査履歴、バイナリ、入れ子ZIPを含め、元ZIP直下の全ファイルを保存しています。
入れ子ZIPはファイルとして原寸保存し、再帰展開はしていません。空ディレクトリの記録も原本ZIPに残ります。
展開時はZIP内の名前をそのまま使用し、元から含まれる文字化け名を推測で修正していません。
元ZIPから保存先への対応はmanifestに記録しています。

現行authorityは **V23** のままです。
旧資料の収録はCANONへの昇格を意味しません。各資料のsupersession・WORKING・OPEN・ARCHIVE等の状態を維持します。
現行の読み始めは [シナリオREADME](../README.md) を参照してください。

## Source recovery precedence

元V22B ZIPに「実際に何が入っていたか」を復元する際は、**`source-v22b-full-exact/` を唯一の忠実な展開mirrorとして使用する**。

従来の `source-v22b-full/` は、完全取り込み以前に作られた部分取り込み / 再構成層である。同じ資料がexact mirrorに存在する場合、source recoveryの根拠としてpartial側を優先してはならない。

ただしこれはscenario authorityの規則ではない。V23 > V22B > V21 > referenced technical parentsという正本順位は別に維持する。

## 既存の部分取り込みとの差分

従来の `source-v22b-full/` は43ファイルの部分取り込みで、ZIPと比較すると15ファイルは改行を除いて一致し、28ファイルには本文差があります。
その43ファイルは履歴・既存参照のprovenanceとして残します。
元ZIPの忠実な複製には **`source-v22b-full-exact/`** を使用してください。

- [既存取り込みとの比較一覧](PREVIOUS-IMPORT-COMPARISON-2026-09-20.tsv)

## Current promoted-file integrity check

2026-09-20の初回修復監査では、`scenarios/asai/current/` 49ファイルのうち42ファイルが元V22B sourceに直接対応しました。

- 38: 当初からbyte-identical;
- 4: 本文は同一で末尾改行/空白のみ差;
- 7: V23等、V22B ZIP以後に追加されたため元source counterpartなし。

4件の改行差はexact source blobへ復元しました。

現時点で、promotedされたV21/V22B/主要technical parentに**実質的な本文破損は確認されていません**。

ただし、完全原本へアクセスできなかった期間の**会話上の推定**は別問題です。特に通常航空機の台帳が存在しないとみなして史実値から再構成した議論は、exact sourceを読んで再監査します。
