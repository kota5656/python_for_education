a = 10
b = 4

plus = a + b # 足し算
minus = a - b # 引き算
mul = a * b # 掛け算
div = a / b # 割り算(小数あり)
divint = a // b # 割り算(小数なし)
rem = a % b # 割り算の余り(剰余)
pow = a ** b # 累乗(aのb乗)

# ちなみに、この時の割り算についてだが、
# 小数ありの方は、divデータ内で計算できる極限の
# 小数桁まで計算してくれる。
# 一方で、小数なしの方についてだが、実は四捨五入してくれる
# わけじゃない。実は、小数以下の値は全部切り捨てられる。

# 全部の数値を出力
print("a?b =", plus, minus, mul, div, divint, rem, pow )

# div(小数あり)の結果、小数点以下の出力桁数が多くなりすぎてしまった
# この場合、divを以下のように書き換えると、小数桁を制限できる。
print("a?b =", plus, minus, mul, '{:.2f}'.format(div), divint, rem, pow )
