# Name: Siddhesh Jadhav, Batch: A1, Roll no: 08
# without background
import cv2 as cv
import numpy as np
from IPython.display import Image
min_range = 20
max_range = 80
img = cv.imread("doggy.jpg",0)
row,column = img.shape
img1 = img
for i in range(row):
    for j in range (column):
        if img[i,j]> min_range and img[i,j]<max_range:
            img1[i,j] = 255
        else: img1[i,j] = 0

cv.imwrite('sliced-img.jpg',img1)
cv.waitKey(0)
