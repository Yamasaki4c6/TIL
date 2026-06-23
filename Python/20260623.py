a, b, c, = input() .split() #三つの数字を取得し、三つに分割する。
#.splitは入力された文字列を分割するメソッド
#左辺と分割後が一致している必要がある。

q = int(a) #抽選者の人数
a_multiple = int(b) #当選A
b_multiple = int(c) #当選B

for q in range(1, q + 1): #1人目から順に処理をする。for文
    tousen_a = (q % a_multiple == 0) #順番に処理し、当選番号Aに当てはまるか割り算
    tousen_b = (q % b_multiple == 0) #同じくBで割り算。

    if tousen_a and tousen_b:
        print("AB")
    elif tousen_a:
        print("A")
    elif tousen_b:
        print("B")
    else:
        print("N")
