# Name: Siddhesh Jadhav, Roll no: 08,  Batch: A1
import cv2 as cv
import numpy as np

img = cv.imread('doggy.jpg')
mask = np.array([[1/9,1/9,1/9],
                 [1/9,1/9,1/9],
                 [1/9,1/9,1/9]])

img_smt = cv.filter2D(img, -1, mask)
cv.imwrite('Smooth_doggy.jpg',img_smt)