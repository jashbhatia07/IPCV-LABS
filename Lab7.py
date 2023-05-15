import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/content/forest.jpg')

plt.imshow(img,cmap='gray')

grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(grey_img,cmap='gray')

hist,bin = np.histogram(grey_img.ravel(),256,[0,255])
plt.xlim([0,255])
plt.plot(hist)
plt.title('histogram')

def get_histogram(image, bins):
    histogram = np.zeros(bins)
    for pixel in image:
        histogram[pixel] += 1
    return histogram
# execute our histogram function
hist = get_histogram(grey_img, 256)

plt.plot(hist)

def cumsum(a):
    a = iter(a)
    b = [next(a)]
    for i in a:
        b.append(b[-1] + i)
    return np.array(b)

c = cumsum(hist)
plt.plot(c)

nj = (c - c.min()) * 255
N = c.max() - c.min()

c1 = nj / N

c1 = c1.astype('uint8')

plt.plot(c1)

img_new = c1[grey_img]

img_new = np.reshape(img_new, grey_img.shape)

print('Original Image')
plt.imshow(img,cmap='gray')

plt.imshow(img_new,cmap='gray')

hist1 = get_histogram(grey_img, 256)
hist2 = get_histogram(img_new, 256)

plt.title('Original Image Histogram')
plt.plot(hist1)
plt.show()

plt.title('Image Histogram After Histogram Equalization')
plt.plot(hist2)
plt.show()


