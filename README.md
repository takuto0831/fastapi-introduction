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
    - Path parameterは上から優先的に処理される