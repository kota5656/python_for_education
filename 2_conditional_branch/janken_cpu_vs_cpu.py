import random

'''
手順1: a,bさんの出す手をランダムで1~3を出してもらう。
手順2: 1~3の数を、それぞれグーチョキパーに置き換える。
手順3: ジャンケンの勝敗を判別するアルゴリズムを作成する。
'''

# 手順1
a = random.randint(1,3)
b = random.randint(1,3)

# 手順2
'''
出した手(1,2,3)をそれぞれグーチョキパーに変換するにも、
いくらか方法があります。今回はその中でも一番泥臭い
3番目の方法を使いますが、他の方法もいずれ学習しますので、
よければ予習として覚えておくと👍です。
'''

# やり方1: 連想配列(辞書型)を使う
'''
hand = {
    1: 'グー',
    2: 'チョキ',
    3: 'パー'
}

print('aは',hand[a], 'bは', hand[b])
'''

# やり方2: 関数を使う
'''
def hand(x):
    if x == 1:
        return 'グー'
    elif x == 2:
        return 'チョキ'
    else: 
        return 'パー'
    
print('aは',hand(a), 'bは', hand(b))
'''

# やり方3: そのまま解く。
# (これでは人数が増えるほどにプログラムも増えまくるのでオススメしない)
hand_a = ''
if a == 1:
    hand_a = 'グー'
elif a == 2:
    hand_a = 'チョキ'
else: 
    hand_a = 'パー'

hand_b = ''
if b == 1:
    hand_b = 'グー'
elif b == 2:
    hand_b = 'チョキ'
else: 
    hand_b = 'パー'

print('aは',hand_a, 'bは', hand_b)

# 手順3
if a == b:
    print('aとbはあいこです。')
elif b-a == 1 or b-a == -2:
    print('aの勝ちです。')
else: print('bの勝ちです。')