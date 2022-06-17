# 迷路の自動生成と探索

## 概要
Pythonを使った迷路の自動生成と探索。  
スクリプトとして実行すると迷路を出力します。

「generate.py」――迷路の自動生成  
「search.py」――迷路の探索  

アルゴリズム「**穴掘り法**」を使い、迷路の壁を「'#'」と通路を「' '」とし、自動で生成します。  
例
```
['#', '#', '#', '#', '#', '#', '#']
['#', ' ', ' ', ' ', ' ', ' ', '#']
['#', '#', '#', '#', '#', ' ', '#']
['#', ' ', ' ', ' ', '#', ' ', '#']
['#', ' ', '#', ' ', '#', ' ', '#']
['#', ' ', '#', ' ', ' ', ' ', '#']
['#', '#', '#', '#', '#', '#', '#']
```

探索は、深さ優先探索でゴールまで探索した順にステップ数を書き込み、幅優先探索ならスタートからゴールまでの距離を出します。

## モジュールとしての使い方
1. インポートします。
1. インスタンス作成時、迷路の幅と高さを渡します。幅と高さともに**5以上の奇数**に設定してください。
1. GenerateMaze.mazeが作成した迷路です。

## スクリプトとしての使い方

### generate
```
$ python3 generate.py 
迷路を出力します
幅と高さが5以上の奇数を入力
Width = 11
Height = 11
# # # # # # # # # # # 
#                   G 
#   # # # # # # #   # 
#   #               # 
# # #   # # # # # # # 
#       #           # 
#   # # # # # # #   # 
#   #               # 
#   #   # # # # #   # 
S       #           # 
# # # # # # # # # # # 
```

### search
```
$ python3 search.py 
迷路を出力します
幅と高さが5以上の奇数を入力
Width = 11
Height = 11
# # # # # # # # # # # 
#       #           G 
#   #   #   # # #   # 
#   #   #   #       # 
#   # # # # #   # # # 
#   #       #       # 
#   #   #   # # #   # 
#   #   #       #   # 
#   #   # # #   #   # 
S       #           # 
# # # # # # # # # # # 
1.深さ優先探索 2.幅優先探索 3.最短経路 4.プログラムの終了
番号を入力 = 3
# # # # # # # # # # # 
#       #         . G 
#   #   #   # # # . # 
#   #   #   # . . . # 
#   # # # # # . # # # 
#   # . . . # . . . # 
#   # . # . # # # . # 
#   # . # . . . # . # 
#   # . # # # . # . # 
S . . . #     . . . # 
# # # # # # # # # # # 
1.深さ優先探索 2.幅優先探索 3.最短経路 4.プログラムの終了
番号を入力 = 4
```