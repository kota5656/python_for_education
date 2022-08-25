import random
from cv2 import split

from numpy import mat

mine_matrix = []
mc_matrix = []

print("Welcome to Mine-Sweeper")
print("Choose the Matrix length: ", end="")
length = int(input())
print("Choose the amount of the mine: ", end="")
mine = int(input())

def matrix_printer(matrix):
    count = 0
    for i in matrix:
        for j in i:
            print(j, "", end="")
            if type(j) == int and j: count += 1
        print()
    print("Amount of mine is:", count)

def open_point():
    print("行: ", end="")
    y = input()
    y = int(y)
    print("列: ", end="")
    x = input()
    x = int(x)
    return y,x


def mine_checker(matrix, y, x):
    if matrix[y][x] == 1:
        '''
        print("BOMB!!!!!")
        mine_count_matrix[y][x] = "B"
        matrix_printer(mine_count_matrix)
        print("ゲームオーバー")
        '''
        return -1
    else:
        mine_count = 0
        if matrix[y-1][x-1] == 1: mine_count += 1
        if matrix[y][x-1] == 1: mine_count += 1
        if matrix[y+1][x-1] == 1: mine_count += 1
        if matrix[y-1][x] == 1: mine_count += 1
        # if matrix[y][x] == 1: pass
        if matrix[y+1][x] == 1: mine_count += 1
        if matrix[y-1][x+1] == 1: mine_count += 1
        if matrix[y][x+1] == 1: mine_count += 1
        if matrix[y+1][x+1] == 1: mine_count += 1
        return mine_count


# mine_matrix init
for i in range(length+2):
    row = []
    for i in range(length+2):
        row.append(0)
    mine_matrix.append(row)

# mine_count_matrix init
for i in range(length):
    row = []
    for i in range(length):
        row.append("_")
    mine_matrix.append(row)

# first choice
print("{length}×{length}のマインスイーパーを展開します。")
print("最初のマスの位置を決定してください。")
print("最初のマスを決定してください: ")
y, x = open_point()

# mine put
for i in range(mine):
    while True:
        x = random.randint(1,length-2)
        y = random.randint(1,length-2)
        if not mine_matrix[y][x]: 
            mine_matrix[y][x] = 1
            break

turn_count = 0
while(True):
    turn_count += 1
    print("ターン", turn_count)
    y, x = open_point()
    result = mine_checker(mine_matrix, y, x)
    # mine_count_matrix[y-1][x-1] = result
    matrix_printer(mc_matrix)
    
    if turn_count >= length * length - mine: break

matrix_printer(mine_matrix)
