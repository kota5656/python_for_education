bank_deposit = 12000 # 銀行預金
print("現在の預金額は、", bank_deposit, "円です。")

print("お金を何円おろしますか？: ", end="¥")
withdraw = input() # お金を入力する
withdraw = int(withdraw) # input()は文字列型なので、整数型に変換する。

# withdrawの入力値が適切であるか
if (withdraw == 0):
    print("0円は引き出せません")
elif (withdraw < 0):
    print("マイナス円は引き出せません")
else: # つまり正常パターン
    if (withdraw > bank_deposit):
        print("預金よりも多くのお金は引き出せません。")
        print("預金: ", bank_deposit, "引き出し額: ", withdraw)
    else:
        print(withdraw, "円を引き出しました。")
        bank_deposit -= withdraw
        print("現在の預金額: ", bank_deposit)
