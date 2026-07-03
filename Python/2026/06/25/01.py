#じゃんけん結果検出コード
#defというヤツと、for文というヤツを理解する
#defはdefineの略で、オリジナルの関数を作れるというもの。CreateAttributeSOP的なやつかな。
#これを使って、あいこ、勝ち、負けのルールを定義する。
#
#
#改行ごとに勝敗を判断するコードを書く
#1行目はintで取得し、二行目以降をその回数分処理を繰り返すfor文
num = int(input())

    
#次にやるのは、ルールを定義して各セットを比べる。
def janken_rule(my_hand, enemy_hand):
    #defの形式はdef 定義したいルール名(比べるもの) 処理 という順番
    if my_hand == enemy_hand:
        return "draw"
     
    if (my_hand == "G" and enemy_hand == "C") or \
       (my_hand == "C" and enemy_hand == "P") or \
       (my_hand == "P" and enemy_hand == "G"):
           return "win"
           
    else:
        return "lose"
        
#対戦結果を羅列。
for _ in range(num):
    my_hand, enemy_hand = input().split()
    
#結果を出力。    
result = janken_rule(my_hand, enemy_hand)
print(result)

#↑なんか一行しか結果が出ない！！！
#と思ったら最後の二行がfor文に入っておらず、一回しか処理されてなかったみたい。
#戒めのためにそのままにしておきます。
