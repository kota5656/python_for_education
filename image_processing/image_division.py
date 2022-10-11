import cv2
import numpy as np
import os

'''
ここでのimread関数に入力するフォルダパスは、
opencv_tutorial.pyから見た相対パスではなく、
コマンド入力するターミナルのパスを見て判断します。
パスの入力に注意しましょう。
(あるいは絶対パスを打ってもOKです。)
'''

src = cv2.imread("./3_iteration_list/input/nc149853.png")
src_width, src_height, color = src.shape
print("元画像の横幅:", src_width, "元画像の縦幅:", src_height)

cv2.imshow("input_image", src)
cv2.waitKey()

print("出力画像名を入力してください: ", end="")
name = input()

print("横に並ぶ画像の枚数を入力してください: ", end="")
row_length = input()
row_length = int(row_length)
print("縦に並ぶ画像の枚数を入力してください: ", end="")
col_length = input()
col_length = int(col_length)
print("xの初期座標を入力してください: ", end="")
x0 = input()
x0 = int(x0)
print("yの初期座標を入力してください: ", end="")
y0 = input()
y0 = int(y0)
print("一枚画像の横幅を決めてください: ", end="")
width = input()
width = int(width)
print("一枚画像の縦幅を決めてください: ", end="")
height = input()
height = int(height)

dst_list = []

for col in range(col_length):
    for row in range(row_length):
        dst_list.append(src[y0+col*height:y0+(col+1)*height, x0+row*width:x0+(row+1)*width])
        # print("ok")

print(len(dst_list))
count = 0
for dst in dst_list:
    count += 1
    cv2.imwrite("./3_iteration_list/output/"+name+str(count)+".png", dst)

cv2.destroyAllWindows()