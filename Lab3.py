import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('../Images/apple_1.jpg')
plt.imshow(img,cmap='gray')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray,cmap='gray')

def contrast(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1)*pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2

r1, r2 = 70, 140
s1, s2 = 0, 255
pixelVal_vec = np.vectorize(contrast)
contrast_stretched = pixelVal_vec(gray,  r1, s1, r2, s2)

fig = plt.figure(figsize=(10, 10))
rows = 1
columns = 2
images = [gray, contrast_stretched]
title = ["Gray", "Contrast Stretched"]
for i in range(len(images)):
  # Adds a subplot at the 1st position
  fig.add_subplot(rows, columns, i+1)
  # showing image
  plt.imshow(images[i], cmap='gray')
  plt.axis('off')
  plt.title(title[i])

c = 255/(np.log(1 + np.max(gray)))
log_transformed = c * np.log(1 + gray)

fig = plt.figure(figsize=(10, 10))
# setting values to rows and column variables
rows = 1
columns = 2

data = [gray, log_transformed]
title = ["Original Gray", "Log Transformed Image"]

for i in range(len(data)):
  # Adds a subplot at the 1st position
  fig.add_subplot(rows, columns, i+1)
  # showing image
  plt.imshow(data[i], cmap='gray')
  plt.axis('off')
  plt.title(title[i])

gammas = [0.1, 0.5, 1.5]

gamm_images = []
for gamma in gammas:
  gamm_images.append(255*(gray / 255) ** gamma)

# create figure
fig = plt.figure(figsize=(18, 18))
# setting values to rows and column variables
rows = 1
columns = 4

images = [gray, gamm_images[0], gamm_images[1], gamm_images[2]]
title = ["Original", "Gamma 0.1", "Gamma 0.5", "Gamma 1.5"]

for i in range(len(images)):
  # Adds a subplot at the 1st position
  fig.add_subplot(rows, columns, i+1)
  # showing image
  plt.imshow(images[i], cmap='gray')
  plt.axis('off')
  plt.title(title[i])

  