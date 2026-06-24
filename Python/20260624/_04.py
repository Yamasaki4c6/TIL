#入力された数字が、2の累乗かどうかを調べる問題
#入力された数字をintで扱い、if文で2の累乗かどうかを調べる。
#2の累乗は2で割り続けていくと最後は1になる。
#0,やマイナスを弾く。
n = int(input())
if n <= 0: #入力された数字が0以下ならNG
    print("NG")
        
else:
    while n % 2 == 0: #%は、割り算の余りを示し、whileは条件を満たす間その処理をし続けるもの。
        n = n // 2 #//は小数点以下を出さずに割る記号（なにそれ）nを上書き。
    
    if n == 1: #nが1なら、入力された数字は2の累乗。そうでないなら違う。
        print("OK")
    else:
        print("NG")

#難しい～～～～
#Geminiがほかの回答案を教えてくれました。
def is_power_of_two_loop(n):
    if n <= 0:
        return False
        
    # 2で割り切れる間は割り続ける
    while n % 2 == 0:
        n = n // 2
        
    # 最終的に1になれば2の累乗
    if n == 1:
        return True
    else:
        return False
  #あるいは
  
      def check_power_of_two():
    try:
        # ユーザーから数字を入力してもらう
        user_input = input("数字を入力してください: ")
        n = int(user_input)
        
        # if文で2の累乗かどうかを判定
        if n > 0 and (n & (n - 1)) == 0:
            print(f"{n} は2の累乗です！")
        else:
            print(f"{n} は2の累乗ではありません。")
            
    except ValueError:
        print("有効な整数を入力してください。")

# 実行
check_power_of_two()

#難しい～～～～～～～～～～～～～～～～
