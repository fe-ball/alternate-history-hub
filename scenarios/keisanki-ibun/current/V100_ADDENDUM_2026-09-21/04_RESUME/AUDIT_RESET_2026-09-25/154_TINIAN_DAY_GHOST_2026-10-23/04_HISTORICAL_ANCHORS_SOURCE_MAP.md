# 04 史実根拠と既存台帳の対応

## 1. テニアンの砲台配置と作戦可能区域
基準は既存[138](../138_TINIAN_BATTERY_RANGE_ARC_AND_SAIPAN_REACH_BOARD_v001.md)、[133](../133_TINIAN_CROSS_CHANNEL_FIRE_DURING_SAIPAN_CAMPAIGN_v001.md)、[134](../134_TINIAN_FORTIFICATION_AND_ARTILLERY_SURVIVABILITY_BASELINE_v001.md)、[150](../150_TINIAN_14JUN_OLDENDORF_CLOSE_BOMBARDMENT_AND_COUNTERBATTERY_v001.md)。

| 砲台/兵器 | 歴史級配置 | 南サイパンへの有効性 | 主な任務 |
|---|---:|---|---|
| Ushi 140mm | 3門 | 南サイパン・Aslito・海峡へ射程成立 | 南サイパン支援艦、揚陸・海峡、限定陸上射撃 |
| Ushi 120mm DP | 3門 | 射程成立、ただし対空任務と競合 | 艦・舟艇、対空、短時間砲撃 |
| Faibus 140mm | 3門 | 射程成立、実砲座の射界はOPEN | 西側艦艇、海峡、条件付き越海射撃 |
| Asiga 140mm | 4門 | 距離成立、砲座向き・地形遮蔽OPEN | 東海岸防御、条件付き海峡/南サイパン |
| Gurguan 120mm | 3門 | 南サイパン陸上深部は通常射程外 | 局地対艦、飛行場/対空 |
| Tinian Town 120mm | 4門 | サイパン陸地へ通常届かない | 西南港、対艦・局地防空 |
| Tinian Town 6インチ | 3門 | サイパン陸地へ届かない（射程約13.7km） | 港・町方面に近寄る巡洋艦/艦艇への重砲 |
| 移動式94式75mm山砲 | 約12門 | 7–8km級、配置次第で限定地域のみ | 島内機動防御、近距離海峡・上陸艇等 |
| Asiga 76.2mm | 3門 | 部分的な沿岸/近距離 | 東部防空・局地防御 |

基準幾何の代表例：Ushi→Agingan約6.9km、Aslito約9.9km、Nafutan約11.0km。Faibus→Aslito約15.6km。Tinian Town→Aslito約20kmで6インチ砲の射程外。射程があることは**砲座の可動角・火線・遮蔽・観測を自動保証しない**。

## 2. 史実による射撃能力校正（分岐へ自動移植しない）
- 6/14 Tinian沿岸砲：USS California BB-44、USS Braine DD-630が被弾、Cleveland CL-55が狭叉。米軍Oldendorf近接制圧下でも日本砲火が存在した。[150](../150_TINIAN_14JUN_OLDENDORF_CLOSE_BOMBARDMENT_AND_COUNTERBATTERY_v001.md)。歴史上の砲種識別には資料差があり、すべて140mm砲の個別戦果に固定しない。
- 6/15 USS Tennessee BB-43：Tinian砲兵の3発命中、戦死8・負傷25、5インチ連装砲1基停止。ただし艦全体の上陸支援は継続。直接命中3＝戦艦喪失ではない。これは**日本沿岸砲の損害様式校正**であって、分岐新規3命中ではない。[133](../133_TINIAN_CROSS_CHANNEL_FIRE_DURING_SAIPAN_CAMPAIGN_v001.md)、[151](../151_SAIPAN_DDAY_TINIAN_FIRE_SUPPORT_TAX_BRANCH_v001.md)。
- 6/18 USS Phelpsのサイパン西岸被弾、Waller/Pringleのサイパン東岸砲火・退避、20日夕Pringle→Renshaw交代は**サイパン砲火によるもの**。テニアンのB−Aへ足さない。個別帰属は[data/tinian_16_24_evidence_events.csv](data/tinian_16_24_evidence_events.csv)。
- 6/20米軍サイパン第531野戦砲兵大隊B中隊がテニアンへの155mm砲撃を開始。6/24ほか2個中隊も参加（歴史）。正確な分岐の砲位置・陣地完成時刻は別に再検証。既存[138](../138_TINIAN_BATTERY_RANGE_ARC_AND_SAIPAN_REACH_BOARD_v001.md)の引用では6/20–7/9 XXIV Corps砲兵のテニアン向け331任務/7,571発に及ぶため、米軍側を無力扱いしない。
- 6/25–26 DD Bancroftがテニアン港・町と舟艇を照明/射撃。6/26–27軽巡Birminghamと護衛艦が町・港を艦砲攻撃、7/6再び同方面へ砲撃。史実では舟艇損害があったが分岐へ自動コピーせず、攻撃の実在と日付・海域を**既存攻撃ゲート**に使う。今回B→米艦命中・撃沈は未裁定。
- 後のテニアン上陸戦で洞窟内6インチ砲が米戦艦Colorado・駆逐艦Norman Scottへ大きな被害を与えた史実は、砲台が高い生残性と対艦破壊能力を持つことの校正。ただし6月25日に同じ戦果が起きる証明にはならない。
- 7/6–7、史実のTinian砲火によるIsely/Aslitoへの攻撃と米海軍/陸上砲兵の反撃。後期サイパンの自力砲撃と混ぜない。

外部一次/準一次資料の照合先例：US Navy DANFS Tennessee BB-43, Braine DD-630, California BB-44, Phelps DD-360, Waller DD-466, Pringle DD-477, Bancroft DD-598, Birmingham CL-62 の艦歴；USMC Saipan/Tinian Official Histories；[153の未閉鎖一次資料リスト](../153_NEXT_CHAT_TINIAN_GUNFIRE_SHIP_DAMAGE_OPTICS_SESSION_CLOSE_2026-10-16_v001.md)。艦の日付や被害詳細は艦ごと再確認してから分岐へ反映する。

## 3. サイパン自身の力を忘れない
[36](../36_SAIPAN_PRE_FORTIFICATION_AND_COMBAT_REWORK_LEDGER_v001.md)、[39](../39_SAIPAN_ARTILLERY_SURVEY_FIRE_DATA_LEDGER_v001.md)、[59](../59_SAIPAN_PRE_VS_AIR_INTEGRATED_PAIRED_DELTA_15_16JUN_v001.md)、[101](../101_PHASE1_SAIPAN_DDAY_15JUN_REAUDIT_v001.md)、[102](../102_PHASE2_3_SAIPAN_16_19JUN_REAUDIT_v001.md)、[103](../103_PHASE4_20_21JUN_RELIEF_BOMBARDMENT_COUNTERLANDING_REAUDIT_v001.md)、[104](../104_PHASE5_21_25JUN_CONVERSION_AND_REINFORCEMENT_BRANCH_AUDIT_v001.md)、[117](../117_SAIPAN_NUMERIC_CURVE_TO_FINAL_OPERATION_v001.md)。

15日上陸戦～19日Aslito西/中央へ米軍が進入しても、日本側東・南東の観測・迫撃砲・残存砲兵で使用阻止が続く。終盤の高地観測・射撃諸元再取得と近傍迫撃砲を保持。強化テニアンはこれに上乗せするのであって、サイパンの砲群をテニアンへ移すわけではない。米軍のCVE・艦砲・陸上砲兵をアスリート不稼働だけで失った扱いにしない。

## 4. 航空の接続ゲート
[91 地域航空](../91_10JUN_MARIANAS_AIR_POWER_ISR_BASE_PROTECTION_RESET_CLOSEOUT_v001.md)の6/10地域MR420–520（Saipan155–185、Tinian140–170、Guam100–125、残り島々20–30等）は旧MR92–118に置換。6/15 [152 テニアン航空](../152_TINIAN_15JUN_DAWN_LOCAL_AVIATION_STATE_POST_91_v001.md)ではTinian MR全機種50–68・戦闘機28–40・即時32–45。15日島別MRをつなぐには日本機の修理・フェリー・退避・現地残留・新決戦の選択・米CVE/空母の固有機/ソーティを航空台帳で合算する必要があり、**本陸上砲兵模型では航空を別建てで増減させない**。

## 5. 海上輸送と救援受入れ
[83](../83_20JUN_SAIPAN_RECEPTION_SECTORS_LOCAL_CRAFT_WALLET_WORKING_v001.md)、[100](../100_PHASE0_SAIPAN_LOCAL_CRAFT_STARTING_WALLET_GATE_v001.md)、[110](../110_PHASE7_LOCAL_CRAFT_EVACUATION_WALLET_GATE_v001.md)、[104](../104_PHASE5_21_25JUN_CONVERSION_AND_REINFORCEMENT_BRANCH_AUDIT_v001.md)、[90](../90_10JUN_MARIANAS_SEA_BOARD_B_FAST_LIFT_PREPOSITION_CLOSEOUT_v001.md)。両島に艇はあるが実艦状態/満載/往復時間/着岸・陸上受入れを検証。テニアンTown南西港を安全な資材倉庫とはしない。砲兵による米海軍迎撃妨害の**潜在荷役時間**と日本の**実到着トン**を常に区別する。20/21、25/26の輸送は別WORKING比較枝を合算しない。

## 6. 追加監査の停止線
射界・実目標接触・射撃許可・日本砲座の位置・観測・弾薬が閉じない限り**特定米艦への命中率から撃沈艦数を確定しない**。実艦の修理時間・任務欠損・米上陸海兵への影響は相互に重複するため、艦・分→死傷を直接換算しない。日本軍の空軍とサイパン自身の火力は本領域で再発明しない。
