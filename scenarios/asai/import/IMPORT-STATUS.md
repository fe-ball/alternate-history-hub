# Import Status — 完全取り込み確認 2026-09-20 / authority metadata updated 2026-09-22

指定された原本ZIPと、その全ファイルをGit管理対象に取り込み済み。

- 原本: [ZIP](archives/ASAI-WORLDLINE-HANDOFF-2026-09-19-FULL-V22B-CHINA-PEACE-GERMAN-JET-BRANCH-GATE(1).zip)（20,996,153 bytes）
- SHA-256: `4bea918064d011331dfe5e0ba3ceed3994e59cc4d2187e84495e59719bc63307`
- 展開保存先: [source-v22b-full-exact/](source-v22b-full-exact/)
- ファイル: **1,122 / 1,122**
- 展開後容量: 27,856,505 bytes
- ZIP CRC検査: 全件合格
- 原本ZIPコピーおよび展開ファイル: 全件SHA-256一致
- [ファイル別パス・サイズ・SHA-256一覧](FULL-IMPORT-MANIFEST-2026-09-20.tsv)
- [検証結果](FULL-IMPORT-AUDIT-2026-09-20.json)

追加照合 fingerprint:
- archive Git blob: `c51075904e597ef5b37fb3917f2dd6b64e91f8e2`;
- 1,122 files;
- 27,856,505 bytes;
- sorted path + blob + size fingerprint `3f8dbee80b9473f3`.

## 保存範囲と現行正本

source mirrorはV22B時点の完全原本復旧層。旧版、監査履歴、バイナリ、入れ子ZIPを含めて保存し、収録自体はCANON昇格を意味しない。

**現行authorityは V25。**
読み始めは [シナリオREADME](../README.md) および [V25 entrypoint](../current/00-START-HERE-2026-09-22-FULL-V25.md)。

V24/V25は完全原本ZIPより後の会話authorityであり、元ZIPへ遡及的に含まれるものではない。

## Source recovery precedence

元V22B ZIPに実際に何が入っていたかを復元する際は **`source-v22b-full-exact/`** を忠実なsource mirrorとして使用する。

従来の `source-v22b-full/` は部分取り込み / 再構成層。同じ資料がexact mirrorに存在する場合、source recoveryの根拠としてpartial側を優先しない。

これはscenario authorityの順位とは別:
**V25 > V24 > route-compatible V23/V22B/V21 > referenced technical parents.**

## Current promoted-file integrity

2026-09-20監査ではV21/V22B/主要technical parentに実質的な本文破損は確認されていない。

完全原本へアクセスできなかった期間の会話推定は別問題であり、V25でも exact mirror / technical parent を優先して再監査する。
