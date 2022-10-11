import cv2
import numpy as np

'''
ここでのimread関数に入力するフォルダパスは、
opencv_tutorial.pyから見た相対パスではなく、
コマンド入力するターミナルのパスを見て判断します。
パスの入力に注意しましょう。
(あるいは絶対パスを打ってもOKです。)
'''

src = cv2.imread("./3_iteration_list/input/Lenna.bmp")

cv2.imshow('output_image', src)
cv2.waitKey()
cv2.destroyAllWindows()