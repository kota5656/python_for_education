import random
from cv2 import split

from numpy import mat

matrix = []

print("Welcome to Mine-Sweeper")
print("Choose the Matrix length: ", end="")
length = int(input())
print("Choose the amount of the mine: ", end="")
mine = int(input())

def matrix_printer():
    count = 0
    for i in matrix:
        for j in i:
            print(j, "", end="")
            if j: count += 1
        print()
    print("Amount of mine is:", count)


# matrix init
for i in range(length):
    row = []
    for i in range(length):
        row.append(0)
    matrix.append(row)

# first choice
print("Please open first tile: ", end="")
first_point = input().split(" ")
print(first_point)
if not len(first_point) == 2:
    exit()

# mine put
for i in range(mine):
    while True:
        x = random.randint(0,length-1)
        y = random.randint(0,length-1)
        if not matrix[y][x]: 
            matrix[y][x] = 1
            break

matrix_printer()

