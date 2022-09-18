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

list_tmp = []
list_tmp.append(src[48:100, 0:72])

print(list_tmp[0])