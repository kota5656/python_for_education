import cv2
import numpy as np
from perlin_noise import PerlinNoise

name = 'output'
width = 640
height = 480
color = 3
src = np.zeros((height, width, color), np.uint8)
# src[0:height, 0:width, 0:color] = 255 # white
# src[0:height, 0:width, 0] = 255

print("done")

noise1 = PerlinNoise(octaves=3)
noise2 = PerlinNoise(octaves=6)
noise3 = PerlinNoise(octaves=12)
noise4 = PerlinNoise(octaves=24)
scale = 100

print("done")

for y in range(height):
    for x in range(width):
        noise = 0
        noise += noise1([y/scale, x/scale])
        noise += 0.5 * noise2([y/scale, x/scale])
        noise += 0.25 * noise3([y/scale, x/scale])
        noise += 0.125 * noise4([y/scale, x/scale])
        src[y, x, 0:color] = noise
    if y % (height/10) == 0: print("drawn percentage line")

# src[0:height, 0:width, 0] = 255

dst = src

cv2.imshow(name, dst)
cv2.waitKey(0)
cv2.destroyAllWindows()