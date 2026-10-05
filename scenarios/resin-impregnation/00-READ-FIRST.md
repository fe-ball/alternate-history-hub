# 樹脂含浸シナリオの参照入口

シミュレーションを再開する前に、ユーザー制約、領域基準、修正記録を読む。現在は39資料の回収と取り込み監査を終えた設計状態であり、単一の作中時計は指定されていない。

## 優先して読む資料

1. [運用規則](SCENARIO-RULES.md) と [User_Narrative_Constraints.md](current/User_Narrative_Constraints.md)。
2. [期区分](current/Phase_Analysis.md)、[経済マスタ](current/Master_Parameters.md)、[売上根拠](current/Revenue_Model.md)。
3. [監査記録](audit/DECISION-REGISTER.md) と [引継ぎ](current/active/00-SESSION-HANDOFF.md)。

## 今回の修正と保留

ECN値の誤記、単価×数量の桁、年次表、利益和、構成比、名目価格へのインフレ再乗算を修正した。ガラス繊維の流量・複合材質量・ホウ素源の換算も修正し、未実証の量産能力を開発目標に戻した。特許の研究年と公開日、国内秘匿と外国権利、成分秘匿と価格統制を区別した。

P3/P4の売上内訳未配賦、量産設備と販売量、資金残高、白金予算の費目、材料性能の再現性、顧客認定、国別の知財条件はOPEN。修正済みの式を、達成可能性まで検証した証拠とはしない。

## 分野別の資料

全39ファイルを以下に一度ずつ列挙する。本文の元ファイル名を維持し、分野別入口で再構成した。

### 目的と基準

- [User_Narrative_Constraints.md](current/User_Narrative_Constraints.md)
- [_00_INDEX_シナリオ設定資料集.md](current/_00_INDEX_シナリオ設定資料集.md)
- [00_シナリオ戦略改訂レポート.md](current/00_シナリオ戦略改訂レポート.md)
- [01_タイムライン.md](current/01_タイムライン.md)
- [Phase_Analysis.md](current/Phase_Analysis.md)
- [02_基幹技術データ集.md](current/02_基幹技術データ集.md)

### 財務と市場

- [Master_Parameters.md](current/Master_Parameters.md)
- [Revenue_Model.md](current/Revenue_Model.md)
- [Detailed_Growth_Simulation.md](current/Detailed_Growth_Simulation.md)
- [Economic_Refactoring_Logic.md](current/Economic_Refactoring_Logic.md)
- [Commercial_And_Financial_Strategy.md](current/Commercial_And_Financial_Strategy.md)
- [Product_Catalog_And_Demand_Matrix.md](current/Product_Catalog_And_Demand_Matrix.md)
- [GFRP需要シミュレーション草案.md](current/GFRP需要シミュレーション草案.md)
- [Industry_Improvement_Impact.md](current/Industry_Improvement_Impact.md)

### 材料と工程

- [Compreg_Markets_And_Lifecycle.md](current/Compreg_Markets_And_Lifecycle.md)
- [Furan_Resin_And_Furfurylated_Wood.md](current/Furan_Resin_And_Furfurylated_Wood.md)
- [Epoxy_Strategy.md](current/Epoxy_Strategy.md)
- [GFRP_Development.md](current/GFRP_Development.md)
- [GFRP_Mass_Production_Feasibility_Analysis.md](current/GFRP_Mass_Production_Feasibility_Analysis.md)
- [Interface_Solution.md](current/Interface_Solution.md)
- [CFRP_Complete.md](current/CFRP_Complete.md)
- [Carbon_Material_Hierarchy.md](current/Carbon_Material_Hierarchy.md)
- [Synthetic_Rubber_Route.md](current/Synthetic_Rubber_Route.md)

### 原料と協業

- [Chemical_Resource_Management.md](current/Chemical_Resource_Management.md)
- [Oji_Paper_Collaboration.md](current/Oji_Paper_Collaboration.md)
- [Taiwan_Bagasse_Furfural.md](current/Taiwan_Bagasse_Furfural.md)
- [Cooperation_Partners.md](current/Cooperation_Partners.md)
- [Sankyo_Amicable_Relationship.md](current/Sankyo_Amicable_Relationship.md)
- [Patent_Collision_Timeline.md](current/Patent_Collision_Timeline.md)
- [史実人物リスト.md](current/史実人物リスト.md)

### 製品と用途

- [Aviation_Fleet_List.md](current/Aviation_Fleet_List.md)
- [Propeller_Technology_Timeline.md](current/Propeller_Technology_Timeline.md)
- [Mitsubishi_Diesel_Aircraft_Feasibility.md](current/Mitsubishi_Diesel_Aircraft_Feasibility.md)
- [Seaplane_Strategy.md](current/Seaplane_Strategy.md)
- [Corrosion_Resistant_Business.md](current/Corrosion_Resistant_Business.md)
- [Composite_Armor.md](current/Composite_Armor.md)
- [Military_Applications.md](current/Military_Applications.md)
- [Radar_Proximity_Rocket.md](current/Radar_Proximity_Rocket.md)
- [Conductive_Fiber_Dispersal.md](current/Conductive_Fiber_Dispersal.md)

## 取得元の確認

回収した未編集本文は [取り込み控え](import/source-2026-10-06/) と [SOURCE-MANIFEST.json](import/SOURCE-MANIFEST.json)。矛盾を戻さないため、通常はcurrentの修正版を参照する。取得方法と未回収範囲は [IMPORT-STATUS.md](import/IMPORT-STATUS.md)。

原設定も含む監査は [SOURCE-AUDIT.md](audit/SOURCE-AUDIT.md)。完成機・化学品・合弁の財務収録範囲は [FINANCE-COVERAGE.md](audit/FINANCE-COVERAGE.md)。元の拡張案を限定財務ケースで縮めない。
