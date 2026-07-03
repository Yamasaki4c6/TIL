#Python六日目
#一昨日はAtCoder初参加で、昨日はゲーム会社のインターンのweb試験があった
#AtCoderはA問題が解けて上々だが、
#インターンは難しすぎて半分も取れなかった
#アルゴリズムの知識が無さすぎ。
#ただ、Houdini,Mayaの開発での実務を考えるとアルゴリズムの理解はそこまで深くなくてよさそう。
#Pythonは基本文法でもそれなりのツール開発ができそうだし、時間を取られるリスクがでかい
#アルゴリズム周りと3DCGの処理はやっぱりC++みたいなのでちょっとずつC++も始めよう

#23 34 67 21 45のような入力があったとき、あとでfor文で計算回せるようにリスト化する処理がまだ不慣れ
#一行でやりたい。

a = 0
test_list = [int(s) for s in input().split()]  

#[]の中にforもint(s)とかが入る歪さ。慣れない。
#Pythonを数日触って思ったけど、構文がかなり暗記頼りで思ってたプログラミングとイメージが違うかも。
#アルゴリズムも良い構図の方法論を個別具体として暗記しつつ、それの組み合わせで作っていく絵みたいな感じ。
#ここから、aにfor文でリストの端から足していく。

total = 0
test_list = [12, 5, 82, 10, 31]

for num in test_list: #for文はここではnumにリストの端から順に代入されて処理される。
  #合計値を出したい場合は
  total += num










num = input() #買い物の回数
a, b = input().split() #aがボーダーの値段、bが合計の値段
a = int(a)
b = int(b)

num_buy_list = [int(s) for s in input().split()] #各買い物の値段を取得

total = 0
total_border = False

for bought in num_buy_list: #買い物の合計がボーダーを超えているか
    total += bought
    
if 3000 < total:
    total_border = True #買い物の合計が3000円を超えていたらTrue
    
    
judge_list = []

for particle_bought in num_buy_list: #各買い物の値段がボーダーを超えているか
    if particle_bought > a:
        judge_list.append(True)
    else:
        judge_list.append(False)
        
if total_border == True and judge_list.count(True) >= 3:
    print("silver")
else:
    print("bronze")
        
