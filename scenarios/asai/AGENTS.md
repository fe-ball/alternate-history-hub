# ASAI scope guidance

対象はscenarios/asai。まず00-READ-FIRST-GENERIC.md、current/ACTIVE-STATE.jsonを読む。current/activeの00→01→02→03が標準順。原記録はrecords、旧枝はarchive、旧パスはnavigation/SOURCE-ROUTES.jsonで解決する。

最大version・最新mtime・未来の歴史日付で枝を選ばない。keisanki-ibunは別シナリオ。歴史状態とtechnical authorityを混ぜず、source_statusとnavigation_roleも分ける。manifestはナビゲーション正本で、矛盾する新しい同軸の実行記録を隠す権威ではない。

新しいhandoff/register/checkpoint/progress追加時にはACTIVE-STATEとactive四文書、中央registryの浅井欄を同一変更で同期する。原記録のstatusや戦果を、入口修正の名目で変更しない。

検査：python scenarios/asai/navigation/validate_active_axis.py
