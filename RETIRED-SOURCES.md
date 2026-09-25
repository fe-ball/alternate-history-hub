# 計算機異聞：旧資料の廃止（2026-09-25）

Status: **RETIRED / DO NOT RESTORE / NOT AUTHORITY**

ユーザー指示により、旧 FULL HANDOFF v003（1944-08-04T24）と、それを基礎とする2026-09-02作業・レビュー引き継ぎを廃止した。古い本文・ZIP・性能値・時計を現行資料へ戻してはいけない。

- 現行の入口は [仮想歴史総合の計算機異聞](https://github.com/fe-ball/alternate-history-hub/tree/main/scenarios/keisanki-ibun)。毎回その `README.md` と `scenarios.yaml` から読む。
- 廃止時点の正本は Branch B v100、時計は1944-06-16T14:15。今後の正本は中央registryの明示指定で確認する。
- 古いGit履歴、ブランチ、ローカル複製、ZIP、検索結果、会話引用からの復元・再取り込み・現行根拠への採用を禁止する。「不足資料」「以前の正本」「より未来の時計」を復活理由にしない。
- 現行側で明示的に保持された資料の効力は現行authority chainで判断する。この廃止により、現行側の保持済み正本やv097の由来資料全体を削除対象にしない。
- 2026-09-25の作業差分はWORKING / PROVISIONALのまま。廃止資料由来の主張は、現行正本で独立に確認できるまで根拠にしない。

再混入検査は `python scripts/check_retired_sources.py`。廃止した本文の代わりに識別用ハッシュだけを `retired-keisanki-sources.json` に保持する。同名パッケージと、改名された同一ファイルを検出する。push・PRでも実行する。
Git履歴自体の消去、外部キャッシュの消去、入れ子ZIPや書き換えられた複製の完全検出を行う仕組みではない。検査と禁止規則を併用し、検査を通すためにハッシュを削除しない。
