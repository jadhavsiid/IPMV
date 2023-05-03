# Name: Siddhesh Jadhav, Roll-no: 08, Batch: A1

# Low Pass Filtering

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('lincoln.jpg',0)
dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
rows, cols = img.shape
rr = int(rows/2)
rc = int(cols/2)
mask = np.zeros ((rows,cols,2),np.uint8)
mask [rr-30 : rr+30, rc-30 : rc+30]= 1
fshift = dft_shift*mask
f_shift = np.fft.ifftshift(fshift)
lpimg = cv.idft(f_shift)
lpimg = cv.magnitude(lpimg[:,:,0],lpimg[:,:,1])
plt.subplot(121),plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(lpimg, cmap='gray')
plt.title('Blurred Image'), plt.xticks([]), plt.yticks([])
plt.show()