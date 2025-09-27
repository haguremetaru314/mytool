import math

def my_sum(a,N,X,R):
    if (N!=1) and ((a+X)*R/N>=1):
        b=math.floor(((a+X)*R/N)+X)*R*N
        nF=1
    else:
        b=(a+X)*R
        nF=0
    return b,nF

def probability_tool():
    while True:
        try:
            # 入力
            Ob = int(input("「オーバーヒート」を使用した回数を整数で教えてください\n使用していないなら「0」と入力してください: "))
            Oc =2**Ob-1

            N = int(input("「ねじれ触手」でダメージを分割できる回数を整数で教えてください\n使用していないなら「1」と入力してください: "))

            X = int(input("あなたの与えるダメージの増加量、相手の受けるダメージの増加量の合計を整数で教えてください\n使用していないなら「0」と入力してください: "))

            R = int(input("「羅刹の拳」によるダメージの倍率を整数で教えてください\n使用していないなら「1」と入力してください: "))

            # ダメージ計算
            rD,rDnF = my_sum(Oc+1,N,X,R)
            mD,mDnF = my_sum(rD*(Oc+4),N,X,R)
            aD=rD*(Oc+4)+mD

            # 出力
            if rDnF == 1:
                print("\n通常版「撫で斬り」の連撃は", rD/N, "ダメージを", (Oc+4)*N, "回")
            else:
                print("\n通常版「撫で斬り」の連撃は", rD, "ダメージを", (Oc+4), "回")

            if mDnF == 1:
                print("最後のダメージは", mD/N, "ダメージを",N, "回")
            else:
                print("最後のダメージは",mD, "ダメージ")

            print("合計",aD, "ダメージ")

            # 続行確認
            cont = input("\nEnterを押すと続行、それ以外の入力で終了します: ")
            if cont:  # 何か入力があれば終了
                print("終了します。")
                break

        except Exception as e:
            print("\n入力が正しくありません。もう一度入力してください。")
            continue

# 実行
probability_tool()
