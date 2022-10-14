import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("./3_iteration_list/input/Lenna.bmp")

dst = src.copy()
height, width, color = dst.shape
# ピクセルのスライド(指定画像, 動かすピクセ量, 縦(0)か横(1)か)
shift = 30
'''
all shift
'''
'''
dst = np.roll(dst, shift, axis=1)
# 空き部分を黒く塗り潰し
# dst(y, x, color)
dst[:, 0:shift, :] = np.array([0,0,0])
'''

'''
sin wave shift
'''
single_wave = 2 * np.pi
wave_amp_w = 8
wave_amp_h = 6
wave_phase_w = 30
wave_phase_h = 30
wave_freq_w = 4
wave_freq_h = 5

wave_width = np.sin((np.linspace(0, wave_freq_w*single_wave, height)) - wave_phase_w)
wave_height = np.sin((np.linspace(0, wave_freq_h*single_wave, width)) - wave_phase_h)

for i in range(height):
    wave = int(wave_amp_w*wave_width[i]) + wave_amp_w
    dst[i, :, :] = np.roll(dst[i, :, :], wave, axis=0)
    dst[i, 0:wave, :] = np.array([0,0,0])

for i in range(width):
    wave = int(wave_amp_h*wave_height[i]) + wave_amp_h
    dst[:, i, :] = np.roll(dst[:, i, :], wave, axis=0)
    dst[0:wave, i, :] = np.array([0,0,0])

cv2.imshow('input_image', src)
cv2.imshow('output_image', dst)
cv2.waitKey()
cv2.destroyAllWindows()