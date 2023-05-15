import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('/content/lowconstrast.jpg')

plt.imshow(img,cmap='gray')

img.shape

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(img,cmap='gray')

img_grey

contrast = img_grey.std()
contrast

colors = ("red", "green", "blue")

# create the histogram plot, with three lines, one for
# each color
plt.figure()
plt.xlim([0, 256])
for channel_id, color in enumerate(colors):
    histogram, bin_edges = np.histogram(
        img[:, :, channel_id], bins=256, range=(0, 256)
    )
    plt.plot(bin_edges[0:-1], histogram, color=color)

plt.title("Color Histogram")
plt.xlabel("Color value")
plt.ylabel("Pixel count")

img_grey.shape

img_grey.min()

new_img  = img_grey.copy()

for i in range(img_grey.shape[0]):
  for j in range(img_grey.shape[1]):
    new_img[i][j] = ((img_grey[i][j]-img_grey.min())/(img_grey.max()-img_grey.min()))*255

plt.imshow(new_img,cmap='gray')

img_grey

new_img

print("Öriginal Image")
plt.imshow(img,cmap='gray')
plt.show()
print("GreyScale Converted Image")
plt.imshow(img_grey,cmap='gray')
plt.show()
print("Histogram Stretched Image")
plt.imshow(new_img,cmap='gray')
plt.show()

hist,bin = np.histogram(img_grey.ravel(),256,[0,255])
plt.xlim([0,255])
plt.plot(hist)
plt.title('histogram')

hist,bin = np.histogram(new_img.ravel(),256,[0,255])
plt.xlim([0,255])
plt.plot(hist)
plt.title('histogram')