import random

'''
手順1: あなたの出す手を1~3で入力する。(文字列型でも結構だが)
手順2: cpuの出す手をランダムで1~3を出してもらう。
手順3: 1~3の数を、それぞれグーチョキパーに置き換える。
手順4: ジャンケンの勝敗を判別するアルゴリズムを作成する。
'''

print("あなたの出す手を選択してください: ", end="")
you = input()
you = int(you)

# 手順2
cpu = random.randint(1,3)

# 手順3
hand_you = ''
if you == 1:
    hand_you = 'グー'
elif you == 2:
    hand_you = 'チョキ'
elif you == 3: 
    hand_you = 'パー'

hand_cpu = ''
if cpu == 1:
    hand_cpu = 'グー'
elif cpu == 2:
    hand_cpu = 'チョキ'
else: 
    hand_cpu = 'パー'

print('youは',hand_you, 'cpuは', hand_cpu)

# 手順3
if you == cpu:
    print('あいこです。')
elif cpu-you == 1 or cpu-you == -2:
    print('あなたの勝ちです。')
else: print('CPUの勝ちです。')