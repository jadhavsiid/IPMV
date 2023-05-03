#  Name: Siddhesh Jadhav, Batch: A1, Roll no: 08
import numpy as np
import cv2 as cv
img = cv.imread('lady.jpg')
kernel = np.ones((5,5),np.uint8)

im_dil = cv.erode(img, kernel)
cl = cv.erode(im_dil,kernel)

cv.imshow('original image',img)
cv.waitKey(0)
cv.imshow('closed_lady.jpg',cl)
cv.waitKey(0)