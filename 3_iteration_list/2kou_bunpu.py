import math

n = 30 # 試行回数
p = 0.008 # SR当選確率

sum = 0

for i in range(n+1):
    pi = math.comb(n, i) * (p**i) * ((1-p)**(n-i))
    print(i, "回当たる確率: ", pi)
    sum += pi

print("合計確率: ", sum)