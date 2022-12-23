import random
import numpy as np
from scipy.spatial import *
import cv2

# make black image
size = 320
img = np.zeros((size, size, 3))

# generate biome center point
n = 10
points = np.random.randint(0, size, (n, 2))
print(points)

voronoi = Voronoi(points)
fig = voronoi_plot_2d(voronoi)
fig.savefig('./image_processing/voronoi.png')

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()