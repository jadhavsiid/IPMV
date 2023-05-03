# Name: Siddhesh Jadhav, Roll no: 08, Batch:A1
import cv2 as cv
import numpy as np

a= cv.imread('lincoln.jpg',0)
cv.imshow('original image',a)
cv.waitKey(0)
b = 255-a;
cv.imshow('negative image',b)
cv.waitKey(0)

