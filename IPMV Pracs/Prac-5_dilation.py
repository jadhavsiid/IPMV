#  Name: Siddhesh Jadhav, Batch: A1, Roll no: 08
import numpy as np
import cv2 as cv
img = cv.imread('lady.jpg')
kernel = np.ones((5,5),np.uint8)

im_dil = cv.dilate(img,kernel)

cv.imshow('original image',img)
cv.waitKey(0)
cv.imshow('dilated_lady.jpg',im_dil)
cv.waitKey(0)