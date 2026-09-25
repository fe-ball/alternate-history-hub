# 回収原文対照表 — 参照復元であって正本昇格ではない

原文16本は既存 `import/source-v097-full` 内のGit blobをそのまま参照し、バイトを変更せず読めるパスへ複製した。原本もそのまま保持する。元パスには文字化けが含まれるため、ファイル名だけでなく下記blob SHAを出所識別子とする。

旧本文の CURRENT / AUTHORITATIVE / CLOSED は当時のラベルである。現在はv100 > v099 > v098 > v097 > v096 > 非競合の継承資料。旧later-clockのforce-stateは復活させない。

| 原文コピー | 原本Git blob SHA | 回収目的／留保 |
|---|---|---|
| [巡洋艦監査](RETAINED_SOURCE_NOT_CURRENT/BRANCH_B_JAPANESE_CA_CL_CLASS_AUDIT_PROVISIONAL_v001.md) | f553b3b90c8809a195b93890696ed4c4529e02d2 | 大淀I-O/水偵handlingとE15K問題の切分け。旧PROVISIONAL感度 |
| [船体差異watchlist](RETAINED_SOURCE_NOT_CURRENT/BRANCH_B_SURFACE_HULL_DIFFERENCE_WATCHLIST_v001.md) | 4ed4433c7c1dbac9cdc04fb0d5abab2aea53946c | E15K運用と大淀旗艦化の別因果gate |
| [インド洋派遣v006](RETAINED_SOURCE_NOT_CURRENT/JAPAN_INDIAN_OCEAN_REINFORCEMENT_CANDIDATES_1944-01_WORKING_v006.json) | 49eb689db5462e64dbd9add80cbc78ae73b9edc6 | 大淀＋4DDの旧WORKING派遣と太平洋配分控除 |
| [航路監査](RETAINED_SOURCE_NOT_CURRENT/JAPAN_INDIAN_OCEAN_ORIGIN_ROUTE_AUDIT_1944-01_WORKING_v001.md) | d8bb6eb9b63c4b73be6e16288b4c15a4bad8ecac | 派遣原位置・給油・到着時間。現行への継承確認前 |
| [3/8並行戦域](RETAINED_SOURCE_NOT_CURRENT/PARALLEL_THEATER_STATE_1944-03-08T24_WORKING_v001.json) | 8e0992d36f02564c5062c16207bef2f08313f6de | 大淀群が接触後利用予備。June所在確定には使わない |
| [水上航空ドクトリン](RETAINED_SOURCE_NOT_CURRENT/SEAPLANE_TACTICS_LEDGER_1943-10-01_v001.json) | bed16d4a817f6f5bf0a3e8962ce9470fe54d3ec9 | 再捜索・高速確認・触接更新・夜間条件・二重加算禁止 |
| [Marshall水上航空網](RETAINED_SOURCE_NOT_CURRENT/MARSHALL_WATER_AVIATION_NETWORK_1944-02-02_WORKING_v001.json) | 06d40aaf7716f8167317725a20030eb5f917e0f1 | 日米飛行艇・水偵・母艦・陸上哨戒を分離。旧局地数はJuneへ加算禁止 |
| [NC水上航空閉鎖](RETAINED_SOURCE_NOT_CURRENT/BRANCH_B_NC_1942_11_11_GROUND_WATER_AIR_CLOSURE_v001.json) | 4a90faacc05b70f44d749269aca8b92217bb58e6 | KAMIKAWA MARU中間支援層の記録。June稼働とは別 |
| [Santo前進配置訂正](RETAINED_SOURCE_NOT_CURRENT/CURRENT_BRANCH_B_V081_SANTO_DPLUS1_WATER_AIR_FORWARD_STAGING_CORRECTION_v001.md) | 6927353a2ebe1e21e7b896047f7d19bb3f86ca77 | 滑走路時計と水上航空時計、移送元控除の既存訂正 |
| [CATCHPOLE旧台帳](RETAINED_SOURCE_NOT_CURRENT/CATCHPOLE_ENIWETOK_1944-04-18_24_SETTLEMENT_v001.md) | 774030005809c008d7505edb24240f974bece717 | 瑞雲ready分母の先例。旧日付・イベントの権威を戻さない |
| [1944初夏戦力再監査v3](RETAINED_SOURCE_NOT_CURRENT/1944初夏戦力_再監査v3起点.md) | 224e48438e3aa991ffb040dc3fc6e94040fd606e | v097 cleanにはあるが現行同名cleanにはない。後続overlay優先 |
| [31 魚雷・水雷戦](RETAINED_SOURCE_NOT_CURRENT/31_魚雷・水雷戦_魚雷本体・射撃指揮・再装填・運用.md) | 591df5bad203aed3b4e2858c67d14e050399eb2e | 再装填・射撃指揮・任務回転の継承参照 |
| [61 技術派生・戦術サイクル](RETAINED_SOURCE_NOT_CURRENT/61_技術からの自然な軍事的派生_戦術サイクル・任務階級・戦史再監査.md) | f78c395161f26dd3f4a88fb1f04a9a3e1f3e7314 | 既存機種性能を任務体系へ接続する原則 |
| [機種別防護配分](RETAINED_SOURCE_NOT_CURRENT/BRANCH_B_AIRCRAFT_TYPE_ARMOR_DEPLOYMENT_DOCTRINE_1944-04-25_v001.md) | e5c29af9b9d40141c537b8ba0357d1b6873a589d | 機種ごとの重量・防護・配備。全機同率bonus禁止 |
| [I400 readiness](RETAINED_SOURCE_NOT_CURRENT/I400_SEIRAN_READINESS_GATE_1944_v001.md) | 5fd9c35cef0211a5b012a37060d8eba6cb61fc26 | 初回実戦化時計。初陣後の予備・補給を証明する資料ではない |
| [4/30兵器監査](RETAINED_SOURCE_NOT_CURRENT/WEAPONS_AUDIT_1944-04-30_v001.md) | e6b93e542aea396aa1a11b544303223fb33ab87d | 短い瑞雲20–30行は分母を確認し、Juneへ自動roll-forwardしない |

現行の優先参照は [scenario rules](../../../../SCENARIO-RULES.md)、[v099航空監査](../../../V099_ADDENDUM_2026-09-20/03_SESSION_UPDATES/01_AIRCRAFT_AUDIT_AND_HOMARE_POOL_1944H1.md)、[v098生残・非改装](../../../V098_ADDENDUM_2026-09-19/03_SESSION_UPDATES/01_PERSONNEL_FLEET_SURVIVAL_AND_NONCONVERSION_SETTLEMENT.md)、[v100艦隊snapshot](../FLEET_HULL_ESCORT_REAUDIT_WORKING_SNAPSHOT_2026-09-23.md)、[Saipan承認済み地上](../../03_SESSION_UPDATES/01_SAIPAN_DDAY_TO_16JUN_DAWN_APPROVED.md)。
