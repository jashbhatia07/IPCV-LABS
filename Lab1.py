import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('Image.jpg')
plt.imshow(img)

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(grayscale_img,cmap='gray')
plt.show()

grayscale_img

print(img.shape)
crop_img = img[0:250,50:450]
plt.imshow(crop_img)

img2 = cv2.imread('cat.jpg')
plt.imshow(img2)

img2.shape

img2 = cv2.resize(img2, (509,339))
plt.imshow(img2)

weightedSum_img = cv2.addWeighted(img, 0.5, img2, 0.5, 1)
plt.imshow(weightedSum_img)

img_100 = np.ones(img.shape, dtype = "uint8") * 100
result_add = cv2.add(img,img_100)
result_sub = cv2.subtract(img,img_100)
plt.imshow(result_add)
plt.show()
plt.imshow(result_sub)
plt.show()

sq_img = cv2.imread('square.png')
cir_img = cv2.imread('circle.png')

plt.imshow(sq_img)
plt.show()
plt.imshow(cir_img)
plt.show()

dest_and = cv2.bitwise_and(sq_img, cir_img, mask = None)
plt.imshow(dest_and)

dest_or = cv2.bitwise_or(sq_img, cir_img, mask = None)
plt.imshow(dest_or)

dest_xor = cv2.bitwise_xor(sq_img, cir_img, mask = None)
plt.imshow(dest_xor)

sq_not = cv2.bitwise_not(sq_img, mask = None)
cir_not = cv2.bitwise_not(cir_img, mask = None)

plt.imshow(sq_not)
plt.show()
plt.imshow(cir_not)
plt.show()