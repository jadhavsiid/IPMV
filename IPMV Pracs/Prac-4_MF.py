#Name : Siddhesh Jadhav  Roll no.: 08 Batch : A1
import cv2
import numpy as np
from skimage.util import random_noise
from matplotlib import pyplot as plt

#load the image
img=cv2.imread('lady.jpg',0)
img=img/255
#print(img.shape)
rows,col=img.shape
#Add salt-and-pepper noise to the image.
"""imp_noise=np.zeros((rows,col),dtype=np.uint8)
cv2.randu(imp_noise,0,255)
imp_noise=cv2.threshold(imp_noise,245,255,cv2.THRESH_BINARY)[1]
n_img=cv2.add(img,imp_noise)"""
#blank image
x,y=img.shape
g=np.zeros((x,y), dtype=np.float32)
#salt and pepper amount
pepper=0.1
salt=0.95
#create salt and peppr image
for i in range(x):
    for j in range(y):
        rdn=np.random.random()
        if rdn < pepper:
            g[i][j] =0
        elif rdn>salt:
            g[i][j]=1
        else:
            g[i][j]=img[i][j]
            
#The above function returns a floating point image
#on the range [0,1], thus we changed it 'uint8'
#and from [0,255]
#noise_img=np.array(255*noise_img,dtype='uint8')
median=cv2.medianBlur(g,5)

#Display the noise image
fig=plt.figure(dpi=300)
fig.add_subplot(1,3,1)
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.title('original')
fig.add_subplot(1,3,2)
plt.imshow(g,cmap='gray')
plt.axis('off')
plt.title('Salt Pepper')
fig.add_subplot(1,3,3)
plt.imshow(median,cmap='gray')
plt.axis('off')
plt.title("median Filter")
plt.show()