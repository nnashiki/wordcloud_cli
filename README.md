# wordcloud_cli
wordcloud_cli


参考:

- フォント
    - https://moji.or.jp/ipafont/ipaex00401/
    - https://github.com/fontworks-fonts/Klee/tree/master/fonts/ttf
- [MeCabを使って、テキスト中に含まれる品詞をカウントしてみよう！ - Qiita](https://qiita.com/yonedaco/items/27e1ad19132c9f1c9180)
- [Word Cloudで文章の単語出現頻度を可視化する。[Python] - Qiita](https://qiita.com/kenmatsu4/items/9b6ac74f831443d29074)
- [Python による日本語自然言語処理](http://www.nltk.org/book-jp/ch12.html)
- python-mecab
    - [SamuraiT/mecab-python3: mecab-python. you can find original version here //taku910.github.io/mecab/](https://github.com/SamuraiT/mecab-python3#common-issues)
    - [mecab-python3 · PyPI](https://pypi.org/project/mecab-python3/)
- word cloud
    - [amueller/word_cloud: A little word cloud generator in Python](https://github.com/amueller/word_cloud#examples)
    - [mask][word_cloud/masked.py at master · amueller/word_cloud](https://github.com/amueller/word_cloud/blob/master/examples/masked.py)
  
# venv で作る際の手順 

```
python3 -m venv venv
. venv/bin/activate
pip install wordcloud
pip install mecab-python3
pip install unidic-lite
# IPAフォントipaexm.ttf を保存
python example.py
```

# poetry した際の手順
- `poetry search wordcloud-cli-for-japanese`
  - [パッケージ命名規則](https://www.python.org/dev/peps/pep-0008/#package-and-module-names)
- `poetry new --src wordcloud-cli-for-japanese`
- `cd wordcloud-cli-for-japanese`
- `tree .`

```
.
├── README.rst
├── pyproject.toml
├── src
│   └── wordcloud_cli_for_japanese
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_wordcloud_cli_for_japanese.py

3 directories, 5 files
```

- `poetry shell`
- `which python`

```
wordcloud_cli/wordcloud-cli-for-japanese/.venv/bin/python
```

- `poetry install`
  - デフォルトで dependencies に入っているやつを install
  - lock が作成される

```
$ poetry install
Updating dependencies
Resolving dependencies... (1.2s)

Writing lock file

Package operations: 8 installs, 0 updates, 0 removals

  • Installing pyparsing (2.4.7)
  • Installing attrs (20.3.0)
  • Installing more-itertools (8.6.0)
  • Installing packaging (20.8)
  • Installing pluggy (0.13.1)
  • Installing py (1.10.0)
  • Installing wcwidth (0.2.5)
  • Installing pytest (5.4.3)

Installing the current project: wordcloud-cli-for-japanese (0.1.0)
```

- `pytest`
  - ここらで1回テストしてみる
- `poetry add wordcloud mecab-python3 unidic-lite click`
  - 開発に必要なパッケージを全て足す
- `core.py(cli関数のみ)作成して呼び出してみる`
  - `poetry run python src/wordcloud_cli_for_japanese/core.py`
- `[tool.poetry.scripts]` に追加しておく
  - `wordcloud_cli_for_japanese` cliになった際の名称になる
  - `poetry run wordcloud_cli_for_japanese`
- `poetry publish --build` でパッケージ化してみる
  - wheel と tar.gz が作成される
  - 別 venv から install してみる
      - `pip install wordcloud-cli-for-japanese/dist/wordcloud_cli_for_japanese-0.1.0-py3-none-any.wh`
  
```
$ wordcloud_cli_for_japanese
this is wordcloud_cli_for_japanese
```

- 実装
  - 実装
  - IPAフォントダウンロード
  - pyproject.toml に `include = ["data/*"]` を追加
- 実行
  - `poetry run python src/wordcloud_cli_for_japanese/core.py  --target ./src/wordcloud_cli_for_japanese/data/sample.txt --out sample.png`
  
- install (ファイルシステム)
  - `pip install wordcloud-cli-for-japanese/dist/wordcloud_cli_for_japanese-0.9.0-py3-none-any.whl`
  - `wordcloud_cli_for_japanese --target wordcloud-cli-for-japanese/src/wordcloud_cli_for_japanese/data/sample.txt --out sample.png`
- install (git)
  - `pip install git+https://git@github.com/nnashiki/wordcloud_cli#subdirectory=wordcloud-cli-for-japanese`
  - `wordcloud_cli_for_japanese --target sample.txt --out sample.png`
