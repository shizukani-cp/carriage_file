# carriage_file
## 概要
名前のように、ユーザーをファイルのある場所へ移動させる、CUIのソフトです。
ただし、Windowsのエクスプローラーのようなファイラーの機能も持っています。
## 使い方
### 実行ファイル化
リポジトリには、実行ファイルは含まれていません。ですので、ご自身で実行ファイル化してください。
例を示します。
```shell
$ python -m pip install pyinstaller
$ git clone https://github.com/shizukani-cp/carriage_file.git
$ cd carriage_file
$ pyinstaller cf.py --onefile
$ cd dist
$ set PATH=%PATH%;%CD%
$ cf
```
### 実行ファイル化せずに直接実行する場合
```shell
$ git clone https://github.com/shizukani-cp/carriage_file.git
$ cd carriage_file
$ python cf.py
```
### 起動
```shell
$ cf
```
### 最初のディレクトリを指定しての起動
```shell
$ cf 最初のディレクトリ
```
### ディレクトリへの移動
```
> 表示されているディレクトリの番号
```
### vimでファイルを開く
```
> 表示されているファイルの番号
```
### ファイルのコピー
```
> c c ファイルの番号
```
### ファイルの切り取り
```
> c x ファイルの番号
```
### コピー・切り取りしたファイルのペースト
```
> c v
```
### ファイル名の変更
```
> rename ファイルの番号 新しいファイル名
```
### ファイル・ディレクトリの削除
```
> del ファイルの番号
```
### 現在のカレントディレクトリへ移動するコマンドのコピー
```
> chdir
```
### シェルコマンドを実行
```
> shell シェルでのコマンド
```