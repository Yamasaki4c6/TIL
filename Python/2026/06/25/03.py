#一行目に特定のワード、二行目にメールの件数、三行目以降からメールの題名が改行されて並ぶ。
#特定のワードで題名を検索をかけ、ワードが含まれていたらYes 含まれていなければNoと出力します。
#input()でワードと件数を取得し、for rangeで件数分処理を各題名を回して、if文でYesかNoかを出力する
#というようなコードを描こうとしています。 
#入力されたワードをまず取得する。
text = input()
#件数を取得
n = int(input())

for _ in range(n):
    mail = input()
    
    if text in mail:
        print("Yes")
    else:
        print("No")

#実用的だけど意外と簡単。Blenderの名前の検索とかリネームのアドオン作ったりできそう。


#ifで複数の条件を付ける時はandとかorとかで挟める。
a, b = (input().split())
a = int(a)
b = int(b)

if a > 24 and b < 41:
    print("No")

elif a > 24 or b < 41:
    print("Yes")
else:
    print("No")

#for文で計算を繰り返したいけど、計算一周ごとに元の数字に足していきたい処理
#自分のレベルと、相手のレベルを定義し、比べるコードをfor文で作る。
enemy_number, my_level = input().split()
enemy_number = int(enemy_number) #戦う数
my_level = int(my_level) #自分のれべる

#戦う数分、forで回す。
for _ in range(enemy_number):
    enemy_level = int(input())
    
    if my_level > enemy_level:
        my_level += int(enemy_level / 2)
        
    elif my_level < enemy_level:
        my_level = int(my_level / 2)
     
print(my_level)
