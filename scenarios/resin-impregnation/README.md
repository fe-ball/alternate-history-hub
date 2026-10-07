# 樹脂含浸シナリオ

1910年代の日本で、歴史・化学等の未来知識を持つ転生者が、名古屋港の木材商家を基盤に木材加工・樹脂化学・複合材料の事業を構築するシミュレーション。日本を有利にして敗戦を避けることを上位目標とし、技術・原料・設備・需要・資金と他者の反応を追う。

Claudeプロジェクトの全39文書を新規シナリオとして回収し、計算・参照・推論の不整合を修正した。読み始めは [00-READ-FIRST.md](00-READ-FIRST.md)。運用は [SCENARIO-RULES.md](SCENARIO-RULES.md)、修正内容と未解決事項は [監査記録](audit/DECISION-REGISTER.md) を参照する。

## 保存構成

| 保存先 | 用途 |
|:---|:---|
| [00-READ-FIRST.md](00-READ-FIRST.md) | 優先順位、分野別の読み順、保留事項 |
| [current](current/) | 修正版39文書。元のファイル名と相互参照を維持 |
| [current/active/00-SESSION-HANDOFF.md](current/active/00-SESSION-HANDOFF.md) | 次回検討への引継ぎ |
| [audit](audit/) | 修正根拠、未解決事項、検証結果、修正版ハッシュ |
| [import/source-2026-10-06](import/source-2026-10-06/) | 回収した39文書の未編集スナップショット。現行判断には使わない |
| [import/IMPORT-STATUS.md](import/IMPORT-STATUS.md) | 取得範囲と忠実性の限界 |

現行整理版は `source-audit-2`（2026-10-06）。`canonical_clock` は未指定。1942年等の年表・将来試算を、その年まで進行が確定した証拠とは扱わない。需要草案・オプション・試算は未確定のまま維持する。

元の [Claudeプロジェクト](https://claude.ai/project/019d16ee-963d-7207-86ee-448111dd18a6) と [2026-05-06の更新確認](https://claude.ai/chat/39562d1e-fc57-42e3-b9c2-d0041cc62a59) を取得元・現行性の根拠として記録した。GitHubの修正はClaude側の文書には反映していない。

追加監査では元設定の工場年代・比弾性率・原価・燃料費/物量・合弁会計を訂正し、完成機40%構想とPAN研究を条件付きで保持した。[原設定監査](audit/SOURCE-AUDIT.md) と [財務収録範囲](audit/FINANCE-COVERAGE.md) から再開できる。

2026-10-07に航空材料・推進・機体統合のWORKINGを [current/active/Aviation_Composite_Integration_1933_1942.md](current/active/Aviation_Composite_Integration_1933_1942.md) へ追加した。PAN長繊維の航空主系化、短シャンク/広弦プロペラ、水上高速機、零戦期の他社導入、大型機波及をまとめる。これはsource-audit-2の39文書監査を置換せず、その上に載る継続検討層である。
