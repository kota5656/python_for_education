print("三角形の辺の長さを入力して、\n正三角形か二等辺三角形か不等辺三角形かを出力します。")

print("a: ", end="")
a = input()
a = float(a)
print("b: ", end="")
b = input()
b = float(b)
print("c: ", end="")
c = input()
c = float(c)

# 異常系の検出をする
if (a <= 0 or b <= 0 or c <= 0):
    print("辺は正の値を入力してください")
if (a+b < c or b+c < a or a+c < b):
    print("一つの辺が他の二辺よりも大きい場合、三角形が成立しません")

# 正常系が返ってきた場合
if (a==b and b==c):
    print("正三角形です")
elif (a==b or b==c or a==c):
    print("二等辺三角形です")
else:
    print("不等辺三角形です")
