print('ロト7を何回買いますか: ', end="")
n = input()
n = int(n)

number_last = 37 # ロト7の番号の数
fill_number = 7 # ロト7の番号を埋める数

all_pettern = 1
# for文。ここで気をつけて欲しいのは、0から始まること。
for i in range(fill_number):
    print(i, number_last-i)
    all_pettern *= number_last-i
print(all_pettern)

p = 1
for i in range(n):
    '''
    1等でないパターン(つまりその大当たりの1通り以外全部)を
    引き続ける確率を計算する。
    つまり、ハズレ続ける確率を計算する。
    n回で1等を当てる確率は、1等を全部外す確率の裏返し。
    pの初期値を1にしたのは、一度も買わなければ100%
    当たらないためである。
    '''
    p *= ((all_pettern-1)/all_pettern)

p = 1-p # ロト7を外し続ける確率から、当てる確率に返す。
p *= 100 # パーセンテージに直したいので100倍する

print(n,'回のロト7の挑戦で1等を当てる確率は',p,'です。')