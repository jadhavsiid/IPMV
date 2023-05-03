# Name: Siddhesh Jadhav, Batch: A1, Roll no: 08
import cv2 as cv
import numpy as np
from IPython.display import Image

r1 = 90
r2 = 170
s1 = 40
s2 = 205

img = cv.imread("lincoln.jpg", 0)
row, cols = img.shape
a1 = s1 / max(r1, 1)
bt = (s2 - s1) / (r2 - r1)
gm = (255 - s2) / (255 - r2)
c1 = s1 - bt * r1
c2 = s2 - gm * r2

d = img.copy()
for i in range(row):
    for j in range(cols):
        if img[i][j] < r1:
            d[i][j] = a1 * img[i][j]
        elif r1 <= img[i][j] < r2:
            d[i][j] = bt * img[i][j] + c1
        else:
            d[i][j] = gm * img[i][j] + c2

cv.imwrite('lincoln_contrast.jpg', d)

