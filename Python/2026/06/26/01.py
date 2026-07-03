a, b = input().split()
a = int(a) #買い物する回数
b = int(b) #目当てのポイント数

value = list(map(int, input().split())) #買うものの値段をリスト化し、int型に変形。

print(value) #ここまでは想定通り

#for文で回数分処理を回す
#値段//100をint型で。

for i in range(a):
    point = value[i] // 100
    get_point = [point] #各買い物ごとにもらえるPointをリスト化
    
print(a, get_point) #ここがおかしい。
    
my_point = 0 #一旦手元のポイント数を定義
for p in get_point: #こうすることで、get_pointのリストをpで一個ずつint型で取り出せる。
    my_point + p
    
    print(my_point, p)

#いろいろ惜しい。
#16行目はループするたびに上書きしてしまっている。
#int型はlist化できないらしい。
#でもがんばってかけた


a, b = input().split()
a = int(a) #買い物する回数
b = int(b) #目当てのポイント数

value = list(map(int, input().split())) #買うものの値段をリスト化し、int型に変形。


#for文で回数分処理を回す
#値段//100をint型で。

get_point = [] #カラのリストを先に用意。

for i in range(a):
    point = value[i] // 100
    get_point.append(point) #各買い物ごとにもらえるPointをリスト化
    
    
my_point = 0 #一旦手元のポイント数を定義
for p in get_point: #get_pointのリストをpで一個ずつint型で取り出せる。
    my_point += p
    

if b > my_point:
    print((b - my_point) * 100)
    
else:
    print(0)

#見直してもっと短くなるように書き直した

#買い物回数と欲しい商品のポイント数を取得
buy_count, goal_point = map(int, input().split()) 

#買うものの値段をリスト化
value = list(map(int, input().split()))

#手持ちのポイントを定義
my_point = 0

#for文で各買い物で得られるポイントを計算し、ポイントを足していく
for p in value:
    my_point += p // 100 

#目標ポイントと手元のポイントをif文でくらべる
if goal_point > my_point:
    print((goal_point - my_point) * 100)
else:
    print(0)

    
#goal_Pointは使わないのでけして良かったかも。
#Pythonは割とforとifとlistゴリ押せる文法なのかな。
