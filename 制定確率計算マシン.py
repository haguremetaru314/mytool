import math

# 順列の計算
def my_sum_P(x, y):
    if x <= y:
        return 0
    return math.factorial(x) / math.factorial(x - y)

# 確率計算とループ処理
def probability_tool():
    while True:
        try:
            # 入力
            a, b = input("通常版「制定の盾」、強化版「制定の盾」の枚数をコンマ(,)で区切って入力してください（例: 1,2）: ").split(",")
            a = int(a)
            b = int(b)
            c = int(input("目当てのルールの数を入力してください（例: 1）: "))

            # 確率計算
            n = 1 - (my_sum_P(11-c,b)) * (my_sum_P(12-c-b,a)) / (my_sum_P(13,a+b))
            m = round(n * 100, 1)

            # 結果表示
            print(f"特定の {c} つのルールが選択肢に現れる可能性は {m}% です。")

            # 続行確認
            cont = input("Enterを押すと続行、それ以外の入力で終了します: ")
            if cont:  # 何か入力があれば終了
                print("終了します。")
                break

        except Exception as e:
            print("入力が正しくありません。例: 1,2  のように入力してください。")
            continue

# 実行
probability_tool()
