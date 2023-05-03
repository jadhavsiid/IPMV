#  Name: Siddhesh Jadhav, Batch: A1, Roll no: 08
import numpy as np
import cv2 as cv
img = cv.imread('lady.jpg')
kernel = np.ones((5,5),np.uint8)

im_er = cv.erode(img, kernel)
op = cv.dilate(im_er,kernel)

cv.imshow('original image',img)
cv.waitKey(0)
cv.imshow('opened_lady.jpg',op)
cv.waitKey(0)