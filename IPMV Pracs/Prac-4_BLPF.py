#Name: Siddhesh Jadhav
#Roll no: 08
#Butterworth LPF
import cv2
import numpy as np
import matplotlib.pyplot as plt
f = cv2.imread('doggy.jpg',0)
F = np.fft.fft2(f)
Fshift = np.fft.fftshift(F)
plt.imshow(np.log1p(np.abs(Fshift)), cmap= 'gray')
plt.axis('off')
plt.show()
M, N = f.shape
H = np.zeros((M,N),dtype=np.float32)
D0 = 30
n = 10
for u in range (M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        H[u,v] = 1 / (1 + (D/D0)**n)
plt.imshow(H, cmap='gray')
plt.axis('off')
plt.show()
Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.show()
