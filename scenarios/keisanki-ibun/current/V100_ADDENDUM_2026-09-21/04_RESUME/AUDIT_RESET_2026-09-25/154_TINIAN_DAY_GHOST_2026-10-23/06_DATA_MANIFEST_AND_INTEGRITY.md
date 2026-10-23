# 06 原データ登録簿・整合性チェック

**GitHubに登録する実データ**：当チャットで生成されたCSV12件とPython1件（合計13件）の中身を、data/ に UTF-8 テキストとして保存する。CSVは全列・全行を保持。GitHubのテキスト保存では改行がCRLF→LFへ正規化され得るので、下記SHA-256は**/mnt/dataに保存されていた生成原本（改行・バイト単位）**のものであり、Git上のテキストblob SHA-256と必ずしも一致しない。数値・行単位の同一性を主眼に置く。

| データファイル (data/以下) | 内容・地位 | ローカル原本SHA-256 |
|---|---|---|
| tinian_day15_events.csv | 6/15 T1/T2/T3射撃イベント・**説明用の時刻例** | 4dc1237de9bb73858a8768693ef0f9041f4a22d4aa7fb02c66d32a4b4751f393 |
| tinian_day15_scenarios.csv | 6/15各種米艦代替・荷役感度 | e28be7f547e812458174327476d33862a02f1f3ae706d0add838d7ee332f0e52 |
| tinian_day_event_model.py | 6/15条件計算の原本ソース | b6dd331d7489b71e423a169293ef22b3988c9ce77c8a91e3ecf92e8eaea5abe8 |
| tinian_16_20_daily.csv | 共通在庫型の旧5日試験 | f1f8ba35a8f20d35cdd600b999a3a89cea40dafcc944c063f0e5fe5af2e1d4bb |
| tinian_16_20_gunroll.csv | 6/16–20砲群別の旧台帳 | 8ac12f57ccfc719ad4fee7a14a0efaf753314c0b891b1e6f292af693c138f922 |
| tinian_16_24_evidence_events.csv | 日付付き史実艦艇交戦の帰属、追加戦果0と未確定の区別 | f2e341c390cd24108762fa55783682f55a04333bb1bb504c289203f5e82be697 |
| tinian_16_24_ghost_days.csv | 6/16–24 砲種別在庫・米軍日次復元・日別A/B | d767637e020b3f9d50102a4d08d5ce928ddcfcfd8a1d6aa367bd515f281ff6be |
| tinian_16_24_ghost_deltas.csv | 6/16–24 親子枝差・条件付き艦・分 | 01fb418e10c4818afe479449bc295a18e5cf830b563e901aa0e40eb2888eb0dc |
| tinian_16_24_ghost_guns.csv | 6/16–24 砲群/口径/弾薬残高・修復・射界係数 | 078e947a9cd87722922a048014f09eb234974ec6e96f2439d97ad986e49b7137 |
| tinian_25jul06_AB_deltas.csv | 6/25–7/6 9条件の日別A/B差、6インチ対艦窓 | d37b96fb7305705f9074b783ccd867826f6697317494d2feb088cc85afabdb8c |
| tinian_25jul06_day_ghost.csv | 6/25–7/6 米軍攻撃候補/圧力・日本残高 | f56342852c492929692063b1433716960fd70ad0103dc0f245421e4384589c57 |
| tinian_25jul06_gunroll.csv | 6/25–7/6 全砲群・全9条件の日次計算原行 | 9d49e8405fc2bdd3a2c4c23a91862ec0995d0ab3dfd131f97f30201840e8f7a7 |
| tinian_25jul06_summary.csv | 6/25–7/6 全9条件の累計と7/7朝残高 | fd3d50bf89e9769b3f60f27c1da00206eec6b34c4079cbc2ae5445549622d753 |

## チャット内の元Excel/ZIP・再実行スクリプト
以下のバイナリ原本は本チャットの添付物として存在し、**このGitHub編入コミットには含まない**（GitHubの登録にはテキストCSVを優先）。これを『バイナリ原本もGitHubへアップロード済み』と呼んではならない。再現コードのうち6/15 Pythonは data/ にあるが、後期模型のPython/JSON一式はZIP内に存在し、再計算時に以下の原本と照合する。

| チャット内原本 | SHA-256 / 用途 |
|---|---|
| tinian_day_only_event_audit.xlsx | 1d22a285fb4d09a238e62d7be7e0367cc98c7a5108045de15d247981226a3848 |
| tinian_16_20_day_ghost_audit.xlsx | 59565767953cf6fad341ace7b3abfec33272343b5201b2973a85fc741907c863 |
| tinian_16_20_repro_bundle.zip | 3ae3efdbc51e940db498e237b45d1e458b104601bb8347411cc8238d94c79b93 |
| tinian_16_24_ghost_day_extension.xlsx | 355912ce4c6d31ec80959f29f1c22b920c02e6a44eb18f8c633c5de687a4eb0c |
| tinian_16_24_ghost_repro.zip | 5130961b6fd2fa563945aff34312ac65575bf9cf00240d7d5288211828d35281 |
| tinian_25jul06_ghost_extension.xlsx | ebb838f3f86bbccc33844e48249e0893576c40a7d2760ac2fca598edeef12c8c |
| tinian_25jul06_repro.zip | 9bd819f1adbb2b3d8e26210f7e0958b11ab4c5249b5654fb86409f0956b4ca9b |

ZIP内部のソース（本コミットではGit登録対象外。ローカル原本のSHA）：
- tinian_16_20_ghost_increment_model.py: 16/20の共通在庫模型。ZIP tinian_16_20_repro_bundle.zip 内。
- tinian_16_20_parameters.json: 同上の入力。
- tinian_16_24_dualclock_model.py: 砲種別在庫日別二時計の再現用。
- tinian_16_24_ghost_assumptions.json: 同上入力。
- tinian_25jul06_replay.py: 25～7/6の実行コード。元Python SHA 81fb395281230417a580cef433f40606fa68d8e1b03ff732836699ac7942301c。
- tinian_25jul06_conditions.json: 同上条件入力。原本SHA 9694b54735de8d14e5ae73ef749d105fd5b8774fb0101c58de0bc444a81fd740。

**比較結果の再生成はこれらのZIPがある場合に最も容易。** GitHub内の日別CSVを使えば、砲群別の値・発射機会・A/B差分の独立検算と、以後の戦果監査は可能。ユーザー依頼への本編入は完全な音声/会話逐語アーカイブや未保存の試験途中計算を復元したという意味ではない。

## ユニット・不整合チェック
- 砲門数は「物理/即応/その日発砲」を分離。小数砲門＝期待値。
- 基準の15日Bの35+80艦・分は、16日以降のB−Aへ無条件足さない。1つの艦・分が機会費用・実損傷・荷役影響で重複しないよう別IDとする。
- データ列の extra_US_hulls_sunk、extra_US_dead、additional_JP_cargo_received_t が文字列の UNDETERMINED/NOT ESTABLISHED なら計算外として扱い、数値ゼロにキャストしない。
- 6/16–20の全口径共有在庫を6/16–24の砲種別在庫へ混合しない。
- 6/16–24 center+B は24日夜B残弾合計約1000.665、7/6朝B約767.796となるモデルを継承。実軍弾薬ではない。
- 6/25–7/6の『named ship mission』列はその日US艦対テニアン砲撃の史実日付を示し、日本砲側に確定目標機会を無料で創出するものではない。
- **適応の第2・第3段階はまだない**。米軍日次幽霊復元と日本テニアン継続残高のみ。
