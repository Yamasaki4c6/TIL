#二人のお小遣いを足す問題。
#一見成立するように見えるが、入力された二つの値が空白で仕切られているのではなく改行で仕切られていた場合、一行目のみを読み込んでしまい、ValueError (not enough values to unpack)が発生する。

a, b = input().split()

a = int(a)
b = int(b)

print(a + b)

#対策としては、input()を二回呼び出す。

a = int(input())
b = int(input())

print(a + b)

#カンマで仕切られている場合は、split内部で区切り文字を指定する。

a, b = input().split(',')

a = int(a)
b = int(b)

print(a + b)

#慣れたら一発で使い分けられるもんなんですか？？
