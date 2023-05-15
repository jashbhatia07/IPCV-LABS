import cv2
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

img = cv2.imread('../Images/real_00026.jpg')
plt.imshow(img,cmap='gray')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray,cmap='gray')

gray.shape

img.shape

gauss_noise=np.zeros((600,600),dtype=np.uint8)
cv2.randn(gauss_noise,64,5)

gauss_noise.shape

plt.imshow(gray,cmap='gray')
plt.show()
plt.imshow(gauss_noise,cmap='gray')
plt.show()

noisy_img = cv2.add(gray,gauss_noise)
plt.imshow(noisy_img,cmap='gray')

noisy_img

mask=1/9*np.array([[1,1,1],[1,1,1],[1,1,1]])
mask

ret_img=[]
for i in range(len(noisy_img)-2):
  t=[]
  for j in range(len(noisy_img[i])-2):
    temp=noisy_img[i:i+3,j:j+3]
    ans=0
    for k in range(3):
      for l in range(3):
        ans+=temp[k][l]*mask[k][l]
    t.append(ans)
  ret_img.append(t)
ret_img=np.array(ret_img)
ret_img.shape

print('Original Image')
plt.imshow(gray,cmap='gray')
plt.show()
print('Image with Gaussian Noise')
plt.imshow(noisy_img,cmap='gray')
plt.show()
print("Image after removing noise using Average Filter")
plt.imshow(ret_img,cmap='gray')
plt.show()

copy=img.copy()
copy.shape
plt.imshow(copy,cmap='gray')

copy

for _ in range(135):
  x = random.randint(0,copy.shape[0]-1)
  y = random.randint(0,copy.shape[1]-1)
  copy[x][y]=255
for _ in range(135):
  x = random.randint(0,copy.shape[0]-1)
  y = random.randint(0,copy.shape[1]-1)
  copy[x][y]=0
print('Adding Salt and Pepper Noise to Image')
plt.imshow(copy,'gray')

median_fil=[]
for i in range(len(copy)-2):
  t=[]
  for j in range(len(copy[i])-2):
    temp=copy[i:i+3,j:j+3]
    val=[]
    for k in range(3):
      for l in range(3):
        val.append(temp[k][l])
        # val.sort()
    t.append(val[4])
  median_fil.append(t)
median_fil=np.array(median_fil)
median_fil.shape

print('Salt and Pepper Noise Image')
plt.imshow(copy)
plt.show()
print("Image after applying Median Filtering")
plt.imshow(median_fil)
plt.show()