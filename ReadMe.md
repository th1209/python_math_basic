## 概要

* 『Pythonからはじめる数学入門』の写経リポジトリ。

## 環境構築
* virtualenv (任意の環境名)
* source (任意の環境名)/bin/activate
* pip install jupyter
* pip install matplotlib
* pip install flake8
* pip install flake8-docstrings
* pip install flake8-import-order

## ルール
* 書籍の内容を学習する上で、補足が必要と感じた場合、appendixフォルダ以下に、ナレッジを貯めること。
* 全章で共通して使えそうなファイルは、utilitiesフォルダ以下にモジュールとして配置すること。
* .py形式のファイルは、flake8を使って構文チェックすること。

## TODO
* requirement.txtか、setup.pyを作成し、依存パッケージを明確にすること。