# mlab-preseminar

これは融合知能デザイン研究室2021年度プレセミナー用のリポジトリです。

## ファイル・フォルダ構成

- check.py：クレンジングプログラムです。無効なURLを持つデータセットを除外します
- cleansing.py：下処理用のプログラムです。無効なCSV形式のデータを除外します

## 実行方法

poetry install
poetry run python **.py

## 参考URL

- https://zenn.dev/monry/scraps/64055c787ed6aa
- https://github.com/icoxfog417/baby-steps-of-rl-ja

## 実験実績

### データセットのエラー率

全体に対して、以下のようにデータセットに無効なデータが含まれていた。
Kaggleのデータセットが必ずしも使い物にはならないという事例を示す形となった。

BMW:
Error count of BMW's data: 1048.0 9.6306%

TOYOTA:
Error count of Toyota's data: 4169.0 21.409%

TOYOTAのデータセットについては20%もの無効データが混入していた。
