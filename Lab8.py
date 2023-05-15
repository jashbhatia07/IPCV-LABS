import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images.jpeg', 0) 
plt.imshow(img, cmap='gray')

m, n = img.shape

m

n

D0 = 50
F = np.fft.fft2(img)
Fshift = np.fft.fftshift(F)
H = np.zeros((m,n), dtype=np.float32)
for u in range(m):
    for v in range(n):
        D = np.sqrt((u-m/2)**2 + (v-n/2)**2)
        if D <= D0:
            H[u,v] = 1
        else:
            H[u,v] = 0

plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()

plt.imshow(H, cmap='gray')
plt.axis('off')
plt.show()

Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.show()

# Filter: High pass filter
H = 1 - H
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()

plt.imshow(H, cmap='gray')
plt.axis('off')
plt.show()

Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.show()

