# 発動機転生者・リランチ正本

> **Authority:** Relaunch R2
> **Canonical historical clock:** **1938-05-21T00:00**
> 旧 `current/` 技術台帳・`archive/` 引き継ぎはpre-relaunch REFERENCE。
> 2026-09-21以後の正本は本ディレクトリ。
> 1938-05-21より未来の発動機・機体計画は「その時点までに開始済みの研究・要求・計画」として保持し、後年結果をactor knowledgeへ逆流させない。

## 目的

旧体系の「1944年の18気筒要求から1932年の気筒寸法を逆算する」方式を破棄し、
主人公が各時点で持つ未来知識、会社能力、軍要求、実測、戦訓、当時の産業条件から製品・航空機・戦史を再生成する。

今後は技術史だけでなく、戦役を跨ぐ
- 人員
- 熟練
- 兵器
- 車両・馬匹
- 通信
- 弾薬
- 輸送capacity
- aircraft serviceability / pilots / spare engines / sorties
を状態量として繰り越す。

## 現在の正準範囲

### 技術・企業

- O1 / 旭
- O2 / 暁一一
- O2B / 暁一二
- O2C / 暁二一
- O2D / 暁二二
- O3 / 岳
- O4 / 昴
- O5 / 峰（PROVISIONAL）

O2B/C/D、岳、昴の基本構成はCLOSED。
峰はroadmapと初期targetがPROVISIONAL。

尾張織機製作所は姉妹会社として存続し、航空側の生産技術が逆伝播するが、航空critical partsの自動qualified sourceにはしない。

### 航空機

1937-07-07の暁family 470基、うちO2B約65基を新基準とする。
九六三号、陸軍第四案、Ki-15暁、Ki-21岳integration等は `04` / `07` を参照。

1938後半～39年のKi-43 / Ki-44 / Ki-45 / Ki-46 / 十二試艦戦等は、current clockから見た要求・開発・生産planning。後年結果として固定しない。

### 戦史

1937-07-07から1938-05-21までの主要因果を `08-CHINA-WAR-LEDGER-TO-1938-05-21.md` に継続台帳化。

current:
- 上海・南京を経て中国華東軍は人員以上に重装備・通信・輸送・熟練を損耗
- ソ連援助で中国航空は1938年前半に再建されるが、日本側航空優勢を全面的に奪回しない
- 台児荘史実型の大捷は成立せず、日本側は危険な突出から生還して学習を蓄積
- 徐州は1938-05-18夕～19頃に占領
- 中国主力の完全包囲殲滅には失敗するが、史実より多くの重装備を剥離し、多数の部隊を一時解体
- current clockは **1938-05-21、徐州陥落直後の西方追撃開始**

## 発展史ガード

技術は
1. idea / paper
2. trade
3. budget / people
4. rig / coupon / single-cylinder / mock
5. prototype
6. endurance / ground
7. flight
8. qualification
9. proposal / requirement
10. adoption
11. production
12. allocation / serviceability / deployment
を分ける。

未来知識はidea gateを強く開くがphysical / industrial gateを無料では開かない。
一方、払済みの物理・産業ゲートを「史実より早い」という理由だけで巻き戻さない。

戦史でも同様に、
- capability
- procurement
- deployment
- serviceability
- sortie generation
- tactical effect
- operational effect
を分ける。

## 読み順

1. [固有ルール](../SCENARIO-RULES.md)
2. [能力収斂・余裕配分フレーム](01-CAPABILITY-FRAMEWORK.md)
3. [リランチ史・甲から乙初期](02-HISTORY-TO-1935.md)
4. [甲・乙 暫定技術台帳](03-ENGINE-LEDGER-V0.md)
5. [O2初期定格・熱監査](03A-O2-RATING-THERMAL-AUDIT-V1.md)
6. [1937-07-07 航空機基準台帳](04-AIRCRAFT-LEDGER-TO-1937.md)
7. [名称・会社・制式呼称](05-NAMING-DESIGNATION-POLICY.md)
8. [暁後期・岳・昴・峰 発動機系列](06-ENGINE-FAMILY-GROWTH-TO-1939.md)
9. [1937H2–1939 航空機・生産・配備](07-AIRCRAFT-PRODUCTION-1937H2-1939.md)
10. [支那事変・戦力在庫・兵站台帳 1938-05-21まで](08-CHINA-WAR-LEDGER-TO-1938-05-21.md)
11. [pre-relaunch 参考資料索引](../pre-relaunch/README.md)
12. [セッション開始テキスト](../SESSION-START-PROMPT.md)

## 状態ラベル

- **CLOSED:** 次の計算入力として採用
- **PROVISIONAL:** 現在の最良監査値
- **OPEN:** 未決
- **REFERENCE:** 旧体系・比較

未来計画を記録してもcanonical historical clockは進まない。

## 現在frontier

**1938-05-21。徐州陥落直後。**

次は日単位で、
- 商丘
- 蘭封
- 開封
- 中牟 / 鄭州
への追撃速度を再構築する。

同時に中国側の黄河決壊について、
- political decision clock
- Zhao口等の施工試行
- 現場到達
- 工兵・人夫
- 河況
- 施工地点変更
- 日本航空偵察・地上先頭との距離
を別時計で追う。

「日本軍が3日早いから花園口も3日早い」と比例させない。
日本軍の高速化は決壊判断を早めうる一方、施工物理時計・適地・天候は別律速である。

また、速い日本軍がより早く補給限界・洪水等の非常ブレーキへ突っ込む可能性も常に残す。
