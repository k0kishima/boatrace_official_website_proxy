# boatrace_official_website_proxy

## 概要

ボートレース公式サイトの proxy
<br>
以下を目的としている

- ファイルのキャッシングによるパフォーマンス向上
- インターフェースの統一による保守性の向上

### キャッシングに関して

毎回公式サイトへリクエストしてそれをスクレイピングするというアクションは、月次や年次の単位でやり直す際に以下のような問題が発生する。

- 前回と同じ量のリクエストが発生してしまう
  - 結果として、ホスト側に負荷がかかってしまう
  - ネットワークラウンドトリップがボトルネックとなってスクレイピング処理にかかる時間が長くなる

proxy がキャッシュを保持することで上記を解決する。

### インターフェースに関して

公式サイトはリニューアルされたら URL が変わってしまうが、proxy のインターフェースは変えないようにすれば保守性が高まる。

例えば公式サイトの開催スケジュールの URL は 2020 年時点で以下である。
<br>
https://boatrace.jp/owpc/pc/race/monthlyschedule?ym=202008

これは公式サイトがリニューアルされたら `https://boatrace.jp/events/2020/08` のような全然違う書式の URL になる可能性がある（前回のリニューアルでは実際そうなっている）

そこで、公式サイトへはこのリポジトリを経由してアクセスするようにしておけば上記の問題は解決できる。

例えば、開催スケジュールの URL は以下で統一する。
<br>
http://localhost:5000/file?month=8&page_type=event_schedule_page&version=1707&year=2020

クライアントは、公式サイトのバージョンが変わったらパラメータの version の値だけ変えればいい。
<br>
(実際はこのパラメータは省略すると最新のバージョンが既定値として適用されるのでコンテキストによってはそれも気にしなくていい)

## 使用例

### docker によるコンテナの実行

プロジェクトのルート（ここを基準にボリュームをマウントするため）で以下を実行

```bash
docker run --name boatrace_official_website_proxy --rm -it -v $PWD:/webapp -w /webapp --env PYTHONPATH="/webapp:$PYTHONPATH" -p 55000:5000 --network=default python:3.8 bash -c "pip3 install -r requirements.txt && python3 server.py"
```

※ 引数は適宜変更してください
