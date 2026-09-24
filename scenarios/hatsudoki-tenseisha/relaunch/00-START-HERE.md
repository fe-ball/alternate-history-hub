# 発動機転生者・リランチ正本

> **Authority:** Relaunch R2
> **Canonical historical clock:** **1939-10-11T00:00**
> 旧 `current/`・`archive/` はpre-relaunch REFERENCE。
> 2026-09-21以後の正本は本 `relaunch/` ディレクトリ。
> canonical clockより未来の計画は、その時点で開始済みのresearch / requirement / planningとしてのみ保持し、後年結果をactor knowledgeへ逆流させない。

## 目的

主人公の未来知識を「完成品を無料取得する能力」ではなく、正しい研究枝、測定項目、failure mode、試験計画、量産設計を早く選べる能力として扱う。

技術史・生産史・戦史を共通の状態遷移として追い、
- capability
- research / requirement
- prototype
- qualification
- production
- allocation
- serviceability
- deployment
- tactical / operational effect
を分離する。

戦役を跨ぐ人員・熟練・兵器・輸送・航空可動率を継続在庫として扱い、会戦ごとにリセットしない。

## 現在の正準範囲

### 技術・企業

CLOSED core:
- O1 / 旭
- O2 / 暁一一
- O2B / 暁一二
- O2C / 暁二一
- O2D / 暁二二
- O3 / 岳
- O4 / 昴

O5 / 峰はroadmap・初期targetがPROVISIONAL。

O2Dは「実用不能」ではなく、TBO 120–180h / 50h級inspectionを払う **usable super-limit bridge**。主力量産baselineにはしない。

1939暁family mixの後続監査中央:
- O2B 約80
- O2C 約450
- O2D 約85
- total 600基強級
詳細bandは `07` / `10`。

### 航空機

1937基準は `04`、1937H2–1939全体は `07`。

1939-10-11までに追加で閉じた中心:
- Ki-43相当はO2C主力、1938 Sep前後first flight、1939 H1増加試作、夏pilot lot、秋low-rate serial / China operational trial
- 1939年formal adoption中央なら世界線制式名は **九九式戦闘機**
- Ki-43初期武装は nose sync 2×7.7 + wing unsync 2×7.7
- 第四案・九六三号でretract / closed canopy / constant-speed prop / rearward exhaust / wing-gun integrationの多くを先払い
- Ki-44はO2D先行・O4/昴本命
- O2D Ki-44は少数実用・高速技術実証として有効だが、九九戦が既に550km/h級主力なのでmass attractionは弱い
- 1939 H2のO2D Ki-44は12–18 practical aircraft級、O4型は1939 Q3 flight中央、1940に本採用価値を再判定

詳細は `10-FIGHTER-DEVELOPMENT-1938-1940.md` を優先。

### 戦史

`08` が1938-05-21まで、`09` が1939-10-11までを継続正本化。

CLOSED / central:
- 黄河決壊は発生し、鄭州直進軸を閉じる。R2差は日本側重装備退避等の損失軽減で、決壊防止ではない
- 武漢陥落日は大差なし。Wanjialingでは10月2以降の位置修正と学習で106師団の組織崩壊を軽減
- 武漢・宜昌疎開ではcritical machine toolsの多くを保存する一方、一般設備・原料・補機・輸送に追加損失
- 1939深部航空戦ではescort radiusが独立gate。蘭州・重慶は戦闘機護衛の届かない空間を残す
- 南昌・随県棗陽では人的殲滅より中国側の砲・通信・車両・馬匹等希少装備損失がやや増える
- ノモンハンはソ連・蒙古側の明確な作戦勝利を維持。ただし日本23師団の組織・support cadre保存率は改善
- ノモンハンへの航空抽出が史実相当より軽く、中国方面は1939 Sepにserviceable-equivalent +50〜70機級の余力
- 第一次長沙では日本側が誘致後退をより早く認識し、9月29〜30日頃に作戦終了判断。主力は10月7〜9日頃までに新墻河北方へ復帰
- 長沙防衛・失地回復という中国側成功は残るが、日本側撤退損失は史実相当より軽い

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
10. [支那事変台帳 1938-05-21まで](08-CHINA-WAR-LEDGER-TO-1938-05-21.md)
11. [支那事変台帳 1938-05-21→1939-10-11](09-CHINA-WAR-LEDGER-1938-05-21-TO-1939-10-11.md)
12. [Ki-43 / Ki-44 / O2D / 昴 戦闘機開発台帳](10-FIGHTER-DEVELOPMENT-1938-1940.md)
13. [pre-relaunch 参考資料索引](../pre-relaunch/README.md)
14. [セッション開始テキスト](../SESSION-START-PROMPT.md)

## 状態ラベル

- **CLOSED:** 次の計算入力として採用
- **PROVISIONAL:** 現在の最良監査値
- **OPEN:** 未決
- **REFERENCE:** 旧体系・比較

古いplanningが後続正本と競合する場合、後続正本の明示的なsupersessionを優先する。

## 発展史ガード

史実年代を能力上限にしない。
未来知識はidea / answer-selection gateを強く開くが、材料・加工・試験・耐久・量産・supplier・予算・搭乗員・兵站等のphysical / industrial gateを無料では開かない。

逆に既に支払ったgateは「史実より早い」という理由で巻き戻さない。

## 現在frontier

**1939-10-11。第一次長沙会戦 / 贛湘作戦の作戦台帳を閉じた直後。**

次は **1939年末中国の国家戦争台帳** を作る。

最低限、
- organized personnel
- rifles / ammunition
- LMG / HMG
- mortar
- field / mountain artillery
- AT
- radio / signal
- trucks / tractors
- horses / carts
- trained officers / NCO / mechanics
- domestic arms production by category
- migrated factory restart / throughput
- Soviet / French Indochina / Burma import
- fiscal mobilization / inflation
- rail / river / motor transport
- aircraft / pilots / engine hours / spares
を、

**全国保有 / front-serviceable availability / monthly replenishment**

に分ける。

その台帳を入力として **1939年冬季攻勢** を再演する。
