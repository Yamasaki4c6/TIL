i = input()

print("Hello " + i + "!") #シンプルなHello input !

print("Hello " + i + " !") #+でも繋げられる

print(f"Hello {i} !") #便利なf文字列

#f文字列「フォーマット済み文字列リテラル」
#文字と変数をつなげる際、手軽にできる
#入力　太郎　20

a, b, = input() .split() #入力された二つのデータをsplitで分割する。
name = a #inputで受け取ったデータはデフォルトで文字列として扱われるのでstr()にしなくて結構。
age = int(b)

print(f"私の名前は{a}です。年齢は{b}歳です。") #f文字列。{}が全角になっていて一敗。
