# 仮想歴史総合

複数の仮想歴史シナリオの**中央ルータ**。

ここで管理するのは、各世界線の本文そのものより、

- どのシナリオが存在するか
- 現在のauthorityは何か
- 歴史時計はどこか
- 時計が進行中か凍結中か
- 次に何を処理するか
- どこから読むか
- 元資料がGitHubへどこまでimportされているか

という「現在地」。

機械可読の正本一覧は [scenarios.yaml](scenarios.yaml)。

## 現在のシナリオ

| Scenario | Status | Authority | Canonical clock | Clock state | Current frontier |
|---|---|---|---|---|---|
| [浅井世界線](scenarios/asai/README.md) | active | V26（正本）＋post-V26 WORKING | 1941-12-07T14:30:00-10:30 | 正本時計と最新継続点を分離 | [現行manifest](scenarios/asai/current/ACTIVE-STATE.json) → [最新handoff](scenarios/asai/current/active/00-SESSION-HANDOFF.md) |
| [計算機異聞](scenarios/keisanki-ibun/README.md) | active | Branch B v100 | 1944-06-16T14:15 | OPEN / EVENT-SIMULATION（以後はWORKING） | 艦艇装備・6月出撃配置・空母防空の再監査。正本化前にTF58 ASW監査 |
| [発動機転生者](scenarios/hatsudoki-tenseisha/README.md) | active | Relaunch R3 | 1942-06-26T18:00:00-10:30 | Enterprise Kwajalein sheltered salvage・Midway radar-assisted base | 6/27–7/3 repair/tow decision → Saratoga/Wasp concentration → Midway maturation |
| [豊国IF](scenarios/toyokuni-if/README.md) | active | v3＋執筆規律 | 一律の確定時計は未指定 | 派生叙述は1613年まで、提言採否はOPEN | 呂宋統治・後金問題・国内政治 |
| [樹脂含浸シナリオ](scenarios/resin-impregnation/README.md) | active | Claude現行39文書（2026-10-06回収） | 単一時計は未指定 | 年表・試算と確定進行を分離 | 取り込み完了。次の検討対象はユーザー指定待ち |

## 読み方

1. scenarios.yaml で対象世界線の current authority / clock / frontier を確認。
2. 各 scenarios/<id>/README.md を読む。
3. 各 SCENARIO-RULES.md で、その世界線固有の知識・因果ルールを確認。
4. authority entrypoint から本体へ入る。

**最大version、最新作成日、最も未来の歴史時刻を自動的にcurrentとはみなさない。**

シナリオを将来独立repositoryへ移しても、scenario idは維持し、scenarios.yaml の repository / path を更新する。

## 共通原則

- [Simulation Method](principles/simulation-method.md)
- [Causality](principles/causality.md)
- [Authority / Evidence Status](principles/evidence-status.md)

共通原則と、各シナリオ固有のepistemic ruleを混ぜない。

例:
- 浅井世界線では、正本で認められた先行知識・技術優位の伝播範囲を追う。
- 計算機異聞では未来知識を置かず、計算・測定・試験feedbackの高速化から分岐を導く。

## 永続化ルール

通常の会話・検討は GitHub へ自動反映しない。

ユーザーの「GitHubに投げろ」「ここまでGitHub反映」等を永続化トリガーとする。

詳細:
- [Persistence Policy](conventions/persistence-policy.md)
- [Scenario Status Convention](conventions/scenario-status.md)
- [Scenario Registry Convention](conventions/scenario-registry.md)

AIの推論、ユーザー指定、未確定案、superseded事項を可能な限り区別し、誤解釈が判明した場合は履歴を隠さず修正する。

## ディレクトリ

- scenarios.yaml — 中央registry
- principles/ — 複数シナリオ共通の方法論
- conventions/ — authority / status / persistenceの運用規約
- scenarios/ — 現在のシナリオ配置

## 元ZIPの完全保存 — 2026-09-20

- [浅井世界線 V22B: 原本ZIPと全1,122ファイル](scenarios/asai/import/IMPORT-STATUS.md)
- [計算機異聞 v097: 原本ZIPと全2,071ファイル](scenarios/keisanki-ibun/import/IMPORT-STATUS.md)

取り込み時点で全件CRC・SHA-256検証済み。当時の正本V23 / v098と歴史時計を維持した記録。現在の正本は scenarios.yaml を参照。

## PC資料の追加統合 — 2026-09-20

- [計算機異聞：物語・設定解説の全文と整合性注記](scenarios/keisanki-ibun/current/06_READER_GUIDE/README.md)
- [発動機転生者：2原稿を独立シナリオとして編入](scenarios/hatsudoki-tenseisha/README.md)
- [豊国IF：38文書と原本ZIP2本を回収・分類](scenarios/toyokuni-if/README.md)

原文保全と現行の読み順を分離。最大版番号ではなく明示的な正典指定を優先し、提案・未決・旧稿を自動的に確定設定へ昇格させない。

## Claude資料の追加取り込み — 2026-10-06

- [樹脂含浸シナリオ：コンテキスト全39文書](scenarios/resin-impregnation/README.md) — 木材加工・樹脂化学・複合材料の技術経営シミュレーション。元テキスト保全・修正版・監査記録を分離。数値と量産条件等を修正し、未解決事項を明示。
- 回収範囲・テキスト取得方法・検証上の限界は [取り込み記録](scenarios/resin-impregnation/import/IMPORT-STATUS.md)。
