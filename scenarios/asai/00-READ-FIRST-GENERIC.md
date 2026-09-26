# 浅井世界線 — 汎用リーディングガイド

このガイドは読む手順だけを定める。固定パス、最大版番号、最も未来の歴史日付、最新mtimeを無条件の現行authorityにしない。

## 1. 最初に現行軸を同定する

[SCENARIO-RULES.md](SCENARIO-RULES.md) と [current/ACTIVE-STATE.json](current/ACTIVE-STATE.json) を読み、scenario_id・history_branch・日米/日ソ/中国の戦争状態・正本時計・直近戦役・working到達点・discussion frontierを照合する。旧current routerはこのmanifestへ戻す互換入口で、歴史を決定しない。

対象はscenarios/asai。まずmanifestが列挙した同軸のhandoff、register、checkpoint、progressを確認する。必要ならLibraryの引継ぎを照合するが、広域検索で拾った旧枝・別シナリオを読書起点にしない。会話とmanifestに矛盾があれば同軸のより新しい実行記録を探し、署名・明示的な継承/上書き・根拠を確認してから採用する。

manifestのverified_source_commitとsourcesのblob SHAは照合基準。新しいファイルや変更があれば未同期を疑い、読まずに「新しいものはない」としない。technical更新だけで歴史時計を進めない。

## 2. 標準の読み順

現行軸確定後はmanifestのdefault_read_orderどおり、**session handoff → decision register → chronology/state → open items/next gates**。

current/activeは原記録に結び付いた現在ビュー。source_statusは原資料の確定度、navigation_roleは今の読み方であり別属性。履歴の採用状態を変える台帳ではない。必要箇所をrecordsの原handoff/registerで確認する。source idはmanifestで解決する。

古いnext gateの保存は、そのゲートが現在も未着手という意味ではない。現行registerのSUPERSEDED-NEXTを確認し、個別OPENまで一括で消さない。新しいworking結果をCANONへ自動昇格させない。

## 3. 時間・状態を分離する

正本時計、戦役のworking到達点、局所ケーススタディ、将来の修理/調達/技術計画、会話の検討順は別。全世界のworking時計が明示されていなければ勝手に一日時へ統合しない。

各対象を日付・variant/lot・用途・場所とともに、capability / physical article / qualification / adopted / factory accepted / service released / assigned / serviceable / forward / combat-presentで区別する。これは自動昇格する階段ではない。未確認は0ではなく未確認。combat-presentと戦果も別。

## 4. 技術と旧資料の範囲

具体的論点だけcurrent/technicalを読む。不足時のみ、その正本が指定する該当親へ降りる。source-v22b-full-exactは復元用の正確な資料で、全体が現行CANONではない。partial importをexact counterpartより優先しない。

現行枝で変更されていない技術正本・試験方法・材料能力はbranch-neutralな基盤として扱える。技術成立を、その枝での開発完了・発注・受領・配備・戦闘使用へ自動変換しない。旧provenanceや別枝の歴史結果は逆流させない。

archiveは通常探索から外す。明示的な比較か具体的な親証拠の不足時だけ開く。旧URLに到達したら[navigation/SOURCE-ROUTES.json](navigation/SOURCE-ROUTES.json)で解決する。原資料の旧相対パス・コード内パスは、元のscenario-root文脈とこの対応表を使う。

## 5. 更新時

同軸の継続記録を追加したらmanifest・active四文書・中央scenarios.yamlの浅井欄を同じ変更で同期する。新しいnext gateを原registerの具体的な行に結び付ける。単なるナビゲーション修正でCANONを昇格させない。

`python scenarios/asai/navigation/validate_active_axis.py`で入口・source inventory・旧URL・対象枝境界を検査する。検査は歴史/工学的正しさやLibrary外部コピーの消去を保証しない。
