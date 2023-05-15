import cv2
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

img = cv2.imread('../Images/apple_2.jpg')
plt.imshow(img,cmap='gray')

filter=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
filter

rows, cols = img.shape[0],img.shape[1]
highpassfil_img = np.zeros((rows-2, cols-2), dtype=np.uint8)

for i in range(1, rows-1):
    for j in range(1, cols-1):
        neighborhood = img[i-1:i+2, j-1:j+2]
        convolution = (neighborhood * filter).sum()
        highpassfil_img[i-1, j-1] = max(convolution, 0)

plt.imshow(highpassfil_img,cmap='gray')

filter=np.array([[-1,-1,-1],[-1,8.9,-1],[-1,-1,-1]])
filter

def highboost(img):
  hb=[]
  for i in range(len(img)-2):
    t=[]
    for j in range(len(img[i])-2):
      temp=img[i:i+3,j:j+3]
      ans=0
      for k in range(3):
        for l in range(3):
          ans+=temp[k][l]*filter[k][l]
      t.append(ans)
    hb.append(t)
  hb=np.array(hb)
  return hb

highboost_img= highboost(img)
plt.imshow(highboost_img,cmap='gray')

print("Original Image")
plt.imshow(img,cmap='gray')
plt.show()
print("Image After High Pass Filtering")
plt.imshow(highpassfil_img,cmap='gray')
plt.show()
print("Image After High Boost Filtering")
plt.imshow(highboost_img,cmap='gray')
plt.show()

