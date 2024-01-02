# fastapi-introduction

- Fast APIについて
    - Pythonの標準である型ヒントに基づいて Python3.6以降でAPIを構築するのでモダンで, 高速なwebフレームワーク
    - 今後の学習は 公式 Documentをちゃんと読む: https://fastapi.tiangolo.com/
    - 自動ドキュメント生成機能がある.
    - type hints でエラーを表示してくれる. -> Pydanticというツールが validation周りの処理を行なっている.

- 気になる
    - 非同期処理
    - オリジン間リソース共有
    - GraphQL
    - WebSocket

- memo 
    - デコレータ: 関数を受け取り関数を返す
    - asyncとは?: 非同期処理, 1つの処理を実行中でも他の処理を実行できる. 
    - swagger: RESTful APIを記述するための標準format, swagger uiは api documentであり, fast apiでは自動で生成される. 規格が決まっているから其れに沿ってapiを作ってるのかな? 
    - Path parameterは上から優先的に処理される. 
    - query parameterは path parameterにない変数を関数上で定義すると, 自動的にquery parameterになる. path parameter と組み合わせ利用もできる.
    "http://127.0.0.1:8000/countries/?country_name=America&country_no=3"
    - "Optional[str]" で typehintsを定義するとnullでもokにできる.

- APIのデプロイ
    - AWS: サーバーを常に用意する, 機械学習や高頻度で利用する場合はこちらが良い.
    - AWS lambda (サーバーレス): 楽, requestsを投げるだけで良い, 回数課金, 低頻度での利用に向いている
→ API ゲートウェイ

- detaは こちらのdocumentを確認
https://deta.space/docs/en/quickstart-guides/python


local 経由と web経由でres.json() の 挙動が違う?? 

- local

```
TakutonoMacBook-Air:fastapi_intro takuto$ python sample_deploy_api.py 
{'result': 12}
```

- web 経由だと 'content-type': 'text/plain' になっていることがある. response classを指定する? webのdocsで確認すると jsonになっている.

```
raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

https://intellectual-curiosity.tokyo/2019/11/02/python%E3%81%AErequests%E3%81%A7%E3%80%8Cjson-decoder-jsondecodeerror-expecting-value-line-1-column-1-char-0%E3%80%8D%E3%82%A8%E3%83%A9%E3%83%BC%E3%81%8C%E5%87%BA%E5%8A%9B%E3%81%95%E3%82%8C/