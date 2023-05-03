# Name: Siddhesh Jadhav, Roll no: 08,  Batch: A1
import cv2 as cv
import numpy as np

img = cv.imread('doggy.jpg')
mask = np.array([[-1,-1,-1],
                 [-1,8.9,-1],
                 [-1,-1,-1]])

img_hbf = cv.filter2D(img, -1, mask)
cv.imwrite('hbf_doggy.jpg',img_hbf)