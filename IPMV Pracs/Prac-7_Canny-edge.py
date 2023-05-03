# Name: Siddhesh Jadhav
# Batch: A1
# Roll no: 08

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('cat.png',0)
edges = cv.Canny(img,250,250)
plt.subplot(121), plt.imshow(img,cmap='gray')
plt.title('Original Image'), plt.xticks([]),plt.yticks([])
plt.subplot(122), plt.imshow(edges,cmap='gray')
plt.title('Canny_edge_detection'), plt.xticks([]),plt.yticks([])
plt.show()