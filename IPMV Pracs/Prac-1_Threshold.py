# Name: Siddhesh Jadhav, Batch: A1, Roll no: 08
import cv2 as cv
import numpy as np
from IPython.display import Image

T = 128
img = cv.imread("lincoln.jpg",0)
rows, cols = img.shape
d= img
for i in range(rows):
    for j in range (cols):
        if (img[i][j]<=T):
            d[i][j]=0
else:
    d[i][j]=255
    cv.imwrite("lincoln_threshold.jpg",d)
    Image('lincoln.jpg')
    Image('lincoln_threshold.jpg')