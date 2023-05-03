#Siddhesh Jadhav
#TE EXTC(A1)
#Roll No: 08
#<------Gaussian HPF------------->
import cv2
import numpy as np
import matplotlib.pyplot as plt
#open the image f
f = cv2.imread('doggy.jpg',0)
plt.figure(figsize=(5,5))
plt.imshow(f, cmap='gray')
plt.axis('off')
plt.show()

#transform the image into frequecy domain, f-->F

F=np.fft.fft2(f)
Fshift = np.fft.fftshift(F)
plt.figure(figsize=(5,5))

plt.imshow(np.log1p(np.abs(F)), cmap='gray')
plt.axis('off')
plt.show()

plt.figure(figsize=(5,5))

plt.imshow(np.log1p(np.abs(Fshift)), cmap='gray')
plt.axis('off')
plt.show()
#Create Gaussian Filter : high passFilter 
M,N =f.shape
H= np.zeros((M,N), dtype=np.float32)
D0 =200
for u in range(M):
    
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        H[u,v]=np.exp(-D**2/(2*D0*D0))
HPF=1-H
plt.figure(figsize=(5,5))
plt.imshow(HPF, cmap='gray')
plt.axis('off')
plt.show()
#Image Filters
Gshift =Fshift*HPF
G=np.fft.ifftshift(Gshift)
g=np.abs(np.fft.ifft2(G))
plt.figure(figsize=(5,5))
plt.imshow(g,cmap='gray')
plt.axis('off')
plt.show()
plt.figure(figsize=(5,5))
plt.imshow(np.log1p(np.abs(Gshift)), cmap='gray')
plt.axis('off')
plt.show()