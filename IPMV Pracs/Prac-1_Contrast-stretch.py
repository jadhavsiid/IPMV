# Name: Siddhesh Jadhav, Batch: A1, Roll no- 08
import cv2 as cv
import numpy as np
def pixelVal(pix, r1,s1,r2,s2):
    if(0<= pix and pix <=r1):
        return(0.8)*pix
    elif(r1<pix and pix <=r2):
         return 1.70 * (pix-r1) + s1
    else:
        return 0.83 * (pix -r2) + s2

img = cv.imread('Einstein.jpg',1)
r1 = 70
s1 = 130
r2 = 170
s2 = 245

pixelVal_vec = np.vectorize(pixelVal)
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)
cv.imwrite('contrast_stretched.jpg', contrast_stretched)