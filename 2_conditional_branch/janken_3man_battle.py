import random

'''
手順1: a,b,cさんの出す手をランダムで1~3を出してもらう。
手順2: 1~3の数を、それぞれグーチョキパーに置き換える。
手順3: ジャンケンの勝敗を判別するアルゴリズムを作成する。
'''

# 手順1
a = random.randint(1,3)
b = random.randint(1,3)
c = random.randint(1,3)


# 手順2
'''
3人ともなると、プログラムが長くなってしまうので、
僕は連想配列で書くことにします。
使い慣れてみると、その便利さが分かりますよ。
'''

hand = {
    1: 'グー',
    2: 'チョキ',
    3: 'パー'
}

print('a',hand[a], 'b', hand[b], 'c',hand[c])

# 手順3
if a == b == c or (a != b and b != c and a != c):
    print('aとbとcはあいこです。')
else: 
    '''
    3人以上でジャンケンの勝敗が決まる場合は、
    全員の手が一緒にならない、またはグーチョキパーに
    分かれない場合。つまりは2つの手に決まる場合で
    ある。これをxとyに分け、x,yのどっちが勝ちかを判別する。
    '''
    x = a
    if b != x: y = b
    if c != x: y = c
    
    if y-x == 1 or y-x == -2: # つまりxの勝ち
        if x == a: print('a', end="")
        if x == b: print('b', end="")
        if x == c: print('c', end="")
        print('の勝ちです。')
    else: # つまりyの勝ち
        if y == a: print('a', end="")
        if y == b: print('b', end="")
        if y == c: print('c', end="")
        print('の勝ちです。')