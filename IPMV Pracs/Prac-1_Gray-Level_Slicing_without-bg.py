# Name: Siddhesh Jadhav, Roll no: 08, Batch: A1

# with background
import cv2 as cv
import numpy as np
from IPython.display import Image
min_range = 30
max_range = 100
img = cv.imread("doggy.jpg",0)
row,column = img.shape
img2 = img
for i in range(row):
    for j in range (column):
        if img[i,j]> min_range and img[i,j]<max_range:
            img2[i,j] = 255

cv.imwrite("sliced-img1.jpg",img2)
cv.waitKey(0)