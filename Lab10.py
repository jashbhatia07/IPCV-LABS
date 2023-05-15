import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('e.png', 0) 
plt.imshow(img, cmap='gray')

img.shape

filter1 = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
filter1

output1 = []
for r in range(img.shape[0]-2): 
  temp = []
  for c in range(img.shape[1]-2):
    lhs = img[r:r+3, c:c+3]
    ans = 0 
    for r_f in range(filter1.shape[0]): 
      for c_f in range(filter1.shape[1]):
        ans += lhs[r_f][c_f]*filter1[r_f][c_f] 
    temp.append(ans) 
  output1.append(temp)

fig=plt.figure(dpi=200)

fig.add_subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.title("Original")

fig.add_subplot(1,2,2)
plt.imshow(output1,cmap='gray')
plt.axis("off")
plt.title("F(X)")

filter2 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
filter2

output2 = []
for r in range(img.shape[0]-2): 
  temp = []
  for c in range(img.shape[1]-2):
    lhs = img[r:r+3, c:c+3]
    ans = 0 
    for r_f in range(filter2.shape[0]): 
      for c_f in range(filter2.shape[1]):
        ans += lhs[r_f][c_f]*filter2[r_f][c_f] 
    temp.append(ans) 
  output2.append(temp)

fig=plt.figure(dpi=200)

fig.add_subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.title("Original")

fig.add_subplot(1,2,2)
plt.imshow(output2,cmap='gray')
plt.axis("off")
plt.title("F (Y)")

filter_sum = filter1 + filter2 
output_sum = []
for r in range(img.shape[0]-2): 
  temp = []
  for c in range(img.shape[1]-2):
    lhs = img[r:r+3, c:c+3]
    ans = 0 
    for r_f in range(filter_sum.shape[0]): 
      for c_f in range(filter_sum.shape[1]):
        ans += lhs[r_f][c_f]*filter_sum[r_f][c_f] 
    temp.append(ans) 
  output_sum.append(temp)

fig=plt.figure(dpi=200)

fig.add_subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.title("Original")

fig.add_subplot(1,2,2)
plt.imshow(output_sum,cmap='gray')
plt.axis("off")
plt.title("F (X) + F (Y)")

fig=plt.figure(dpi=400)

fig.add_subplot(1,4,1)
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.title("Original")

fig.add_subplot(1,4,2)
plt.imshow(output1,cmap='gray')
plt.axis("off")
plt.title("F(X)")

fig.add_subplot(1,4,3)
plt.imshow(output2,cmap='gray')
plt.axis("off")
plt.title("F (Y)")

fig.add_subplot(1,4,4)
plt.imshow(output_sum,cmap='gray')
plt.axis("off")
plt.title("F (X) + F (Y)")

filter1 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
filter1

output1 = []
for r in range(img.shape[0]-2): 
  temp = []
  for c in range(img.shape[1]-2):
    lhs = img[r:r+3, c:c+3]
    ans = 0 
    for r_f in range(filter1.shape[0]): 
      for c_f in range(filter1.shape[1]):
        ans += lhs[r_f][c_f]*filter1[r_f][c_f] 
    temp.append(ans) 
  output1.append(temp)

fig=plt.figure(dpi=200)

fig.add_subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.title("Original")

fig.add_subplot(1,2,2)
plt.imshow(output1,cmap='gray')
plt.axis("off")
plt.title("F (X)")

filter2 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
filter2

output2 = []
for r in range(img.shape[0]-2): 
  temp = []
  for c in range(img.shape[1]-2):
    lhs = img[r:r+3, c:c+3]
    ans = 0 
    for r_f in range(filter2.shape[0]): 
      for c_f in range(filter2.shape[1]):
        ans += lhs[r_f][c_f]*filter2[r_f][c_f] 
    temp.append(ans) 
  output2.append(temp)

fig=plt.figure(dpi=200)

fig.add_subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.title("Original")

fig.add_subplot(1,2,2)
plt.imshow(output2,cmap='gray')
plt.axis("off")
plt.title("F (Y)")

filter_sum = filter1 + filter2 
output_sum = []
for r in range(img.shape[0]-2): 
  temp = []
  for c in range(img.shape[1]-2):
    lhs = img[r:r+3, c:c+3]
    ans = 0 
    for r_f in range(filter_sum.shape[0]): 
      for c_f in range(filter_sum.shape[1]):
        ans += lhs[r_f][c_f]*filter_sum[r_f][c_f] 
    temp.append(ans) 
  output_sum.append(temp)

fig=plt.figure(dpi=200)

fig.add_subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.title("Original")

fig.add_subplot(1,2,2)
plt.imshow(output_sum,cmap='gray')
plt.axis("off")
plt.title("F (X) + F (Y)")

fig=plt.figure(dpi=400)

fig.add_subplot(1,4,1)
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.title("Original")

fig.add_subplot(1,4,2)
plt.imshow(output1,cmap='gray')
plt.axis("off")
plt.title("F(X)")

fig.add_subplot(1,4,3)
plt.imshow(output2,cmap='gray')
plt.axis("off")
plt.title("F (Y)")

fig.add_subplot(1,4,4)
plt.imshow(output_sum,cmap='gray')
plt.axis("off")
plt.title("F (X) + F (Y)")