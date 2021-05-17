# SQLMaker
GUI Application with the minimun required functions

package
-tkinter
-sqlite

#目的
Python上でのSQLへのデータ保存のやり方について学ぶために作成した．

#__init__.py
setpu.pyを呼び出している．これによってわざわざsetup.pyを走らせなくとも初期設定を行うことができるらしい．

#setup.py
sqlファイルの作成を行う．テーブル名はEnglish, 属性名はSentence，Descriptionを定義している．

#ListMaker.py
メインのアプリケーション．Tkinterのレイアウトが大半を占めている．setup.pyをインポートに記述することでsetup.pyを走らせることができる．

#db2csv.py
データベースをCSVとして出力する．ListMakerに組み込んでも良かったが，何度も使うわけではないし面倒だったのでそのままにしている．

#あとがき
新たな発見もあったので頃合いをみて検索機能等も追加していきたい．