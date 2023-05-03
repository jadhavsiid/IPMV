# Name: Siddhesh Jadhav, Roll no: 08, Batch: A1
import numpy as np
import cv2 as cv
img = cv.imread('lady.jpg',0)
Kernel = np.ones((3,3), np.uint8)

im_d = cv.dilate(img,Kernel)
B_e = im_d - img

cv.imshow('Original image',img)
cv.waitKey(0)
cv.imshow('Dilated image',im_d)
cv.waitKey(0)
cv.imshow('Boundary_ext_lady.jpg',B_e)
cv.waitKey(0)
