Twitterlib
pythonで書かれたtwitterクライアント

##インストール

```
pip install https://github.com/koyuta/Twitterlib.git
```

##使い方

```python
from Twitterlib import TwitterClient

twitter_client = TwitterClient(
    consumer_key = 'consumer_key',
    consumer_secret = 'consumer_secret',
    access_token_key = 'access_token_key',
    access_token_secret = 'access_token_secret'
)
user_timeline = twitter_client.get_user_timeline(screen_name = 'screen_name', count = 100)
search_tweets = twitter_clinet.search_tweets(keyword = 'keyword', count = 100)
```

##パラメータ
基本的にはTwitterのapiのまんまです

```python
def get_user_timeline(self, screen_name, count = 20, include_rts = True, exclude_replies = False)
```

- screen_name : 表示されているユーザ名
- count：取得タイムライン件数
- include_rts：リツイートの有無（デフォルトではTrueで含む）
- exclude_replies：リプライの除外（デフォルトではFalseで除外しない）

```Pyhton
def search_tweets(self, keyword, count, result_type = 'mix')
```

- keyword：検索ワード
- count：取得タイムライン件数
- result_type：結果の並び順（デフォルトではmix）

##依存モジュール
OAuthのモジュールに依存しています
- [requests-oauthlib](https://github.com/requests/requests-oauthlib)
