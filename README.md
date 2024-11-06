# ASMRMetaFLAC
DLSiteで購入してからダウンロードしたwav形式のASMRファイル群を、flacに変換してメタデータを付与し、自動でアートワークを取得して付与するプログラム

## 環境
### Python
- Python 3.x
- 必要なPythonライブラリ
  - requests
  - beautifulsoup4
  - mutagen
  - Pillow
  - pydub
    - pydubの実行にはffmpegが必要です。

## 実行 
```shell
git clone https://github.com/Hayabusa1601/ASMRMetaFLAC.git
cd ASMRMetaFLAC
python main.py
```

## 操作
1. 以下の指示に従い、ASMRのwavファイルが格納されているフォルダパスを入力して下さい。
```
folder path?:
```
2. 作品ID(RJxxxxxxx)を入力して下さい。
(例)
```
id?(RJxxxxxxx) : RJ00000000
```

3. タイトルとURLが表示されます。問題なければメタデータの入力を行っていきます。順にアーティスト名、アルバムアーティスト名、ジャンル名を入力して下さい。入力する必要がなければ空欄で問題ないです。

```
artist name?: 
album artist name?:
genre name?: 
```

4. ファイル名が順に表示されるため、トラック番号を半角数字で入力してください。
```
tracknumer?: 
```

5. wavからflacに変換され、メタデータとアートワークが付与されたファイルが生成されています。

