
# &#30446;&#27425;

1.  [Tweet検索スクリプト](#orgdebd08d)
    1.  [使用準備](#org6aeb94f)
    2.  [実行方法](#org1f6811b)
    3.  [その他](#orgc27bf77)



<a id="orgdebd08d"></a>

# Tweet検索スクリプト

指定した検索ワードでTwitterを検索して、スクリプト実行時以降に該当のツイートがあったら内容をLINEに通知してくれる


<a id="org6aeb94f"></a>

## 使用準備

[LINE notify API](https://notify-bot.line.me/ja/)と[Twitter API](https://developer.twitter.com/)からアクセストークンをもらってくる

以下のようなconfig.pyを用意

    CONSUMER_KEY = 'Twitter APIのCONSUMER KEY'
    CONSUMER_SECRET = 'Twitter APIのCONSUMER SECRET KEY'
    ACCESS_TOKEN = 'Twitter APIのACCESS TOKEN'
    ACCESS_TOKEN_SECRET = 'Twitter APIのACCESS TOKEN SECRET'
    
    LINE_ACCESS_TOKEN = "LINE notify APIのアクセストークン"

pipで以下をinstall

-   requests
-   argparse
-   requests-oauthlib


<a id="org1f6811b"></a>

## 実行方法

以下のように実行

    ./main.py -q "検索クエリ"


<a id="orgc27bf77"></a>

## その他

-   5分に一回該当ツイートを最新から5つ取ってくるので、5分の間に5個以上該当ツイートが投稿されていると追えない
-   デフォルトで"日本語のツイート"かつ"リツイートでないもの"しか対象としていない、設定を変えたかったら以下を変更
    
        query = query + " exclude:retweets lang:ja"

