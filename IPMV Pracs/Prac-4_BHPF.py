#Name: Siddhesh Jadhav
#Roll no: 08
#Butterworth HPF
import cv2
import numpy as np
import matplotlib.pyplot as plt
f = cv2.imread('doggy.jpg',0)
F = np.fft.fft2(f)
Fshift = np.fft.fftshift(F)
plt.imshow(np.log1p(np.abs(Fshift)), cmap='gray')
plt.axis('off')
plt.show()
M,N = f. shape
HPF = np.zeros( (M, N), dtype=np.float32)
D0 = 10
n = 1
epsilon = 1e-5 # adding a small value to avoid division by zero
for u in range (M) :
    for v in range(N) :
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        HPF[u, v] = 1 / (1 + (D0/(D+epsilon))**n)
plt. imshow (HPF, cmap='gray')
plt.axis('off')
plt.show()
Gshift = Fshift * HPF
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))
plt.imshow(g, cmap= 'gray')
plt.axis('off')
plt.show()
