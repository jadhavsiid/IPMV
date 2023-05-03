# Name: Siddhesh Jadhav, Batch: A1, Roll-no: 08
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("doggy.jpg",0)
hist = cv.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.show()

equ = cv.equalizeHist(img)
res = np.hstack((img,equ))
cv.imwrite("doggy_histogram.jpg",res)
hist = cv.calcHist([res],[0],None,[256],[0,256])
plt.hist(res.ravel(),256,[0,256])
plt.show()
