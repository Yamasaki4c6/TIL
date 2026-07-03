#月と日付がぞろ目なのを検知する問題。ぞろ目ならYesそうでないならNo
#if文で書けそうだけど、数字の各桁を検証する方法を知らなった。

a, b = input().split() #splitで分割
combined = a + b #文字列をがっちゃんこする

#lenはlengthの略、中のデータの数を数える機能
#set()は重複しているものを一つにまとめる機能
if len(set(combined)) == 1:
 print("Yes")

else:
 print("No")

#次の問題
#10文字ごとに改行するコード
#range()というまた便利なヤツがいるらしい。
#range(開始, 終了, 間隔)という書き方で
#[開始:終了]で切り取り
#print()関数は最後に改行してくれる。

a = input()
for i in range(0, len(a), 10): #25文字だった場合、0~25までを10毎に検知し、iに0,10,20と数字を入れる。
  print(a[i:i+10]) #0の時は0,10でprint、10の時は10,20でprintを字数が最後まで読み取るまで繰り返す。

#こういう裏技もある
#textwrapというツールがPythonには最初から入っているらしい（どこに？？）
#文章を指定した文字列で折り返すためだけのツール

import textwrap
text = input()

#10文字ずつで折り返して、改行(\n)でくっつける
result = '\n'.join(textwrap.wrap(text, 10))

print(result)
