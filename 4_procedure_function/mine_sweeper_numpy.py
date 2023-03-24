import numpy as np
import cv2

print("マインスイーパーの範囲を選択してください: ", end="")
length = input()
length = int(length)
print("マインの個数を選択してください: ", end="")
mines = input()
mines = int(mines)

mine_matrix = np.zeros((length+2, length+2), dtype=int)
print(mine_matrix[1:length+1, 1:length+1])

for i in range(mines):
    while True:
        x = np.random.randint(1, length+1)
        y = np.random.randint(1, length+1)
        if mine_matrix[y, x] != -1:
            mine_matrix[y, x] = -1
            break
print(mine_matrix[1:length+1, 1:length+1])