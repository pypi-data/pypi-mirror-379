# easy-modal
[![PyPI - Version](https://img.shields.io/pypi/v/easy-modal.svg)](https://pypi.org/project/easy-modal)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/easy-modal.svg)](https://pypi.org/project/easy-modal)

コマンドラインに不慣れなユーザーでも直感的に操作できるよう、ファイル選択、メッセージ表示、簡単な入力などの機能を提供するシンプルなGUIライブラリです。


## **ユーザーフレンドリーな入力**と**迅速なスクリプト開発**の両立
GUI版はTkinterのラッパーライブラリとなっており、Tkinterの記法やウィンドウ描画等の知識ゼロでも1行でモーダルを表示できるようになっています。

TUI版ではGUI版の一部モーダルが実装されており、ASCII文字列で分かりやすいウィンドウ風ダイアログボックスを表示します。

## ライセンス
MIT LICENSEを使用しています。

このライブラリ自体は標準ライブラリ+1ファイルで完結する仕様となっているため、pipでインストールしなくても直接ファイルを開発中のソースフォルダに入れることで機能します。  
[GUI版](src/easy_modal/gui.py)と[TUI版](src/easy_modal/tui.py)のうち、必要なソースファイルだけを直接ダウンロードして、ドロップインでお使いいただくことも可能です。


## 使い方
>[!NOTE]
>ドキュメント作成予定