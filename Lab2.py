import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('../Images/background.jpg')
plt.imshow(img1)

gray_img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

plt.imshow(gray_img,cmap='gray')

negative_img  = 255-gray_img
print(negative_img)

plt.imshow(negative_img,cmap='gray')
plt.title('Negative Image')

gray_img.shape

print(gray_img[0])

print(gray_img)

def thresholding(img,threshold,mode):
    thres_img = gray_img.copy()
    if mode=='Binary':
        for i in range(gray_img.shape[0]):
        #     print(gray_img[i])
            for j in range(gray_img.shape[1]):
                if(gray_img[i][j]>threshold):
                    thres_img[i][j] = 0
                else:
                    thres_img[i][j] = 255
    if mode=='Binary_Inverse':
        for i in range(gray_img.shape[0]):
        #     print(gray_img[i])
            for j in range(gray_img.shape[1]):
                if(gray_img[i][j]>threshold):
                    thres_img[i][j] = 255
                else:
                    thres_img[i][j] = 0
    return thres_img

thres_img_bin = thresholding(gray_img,45,'Binary')
plt.imshow(thres_img_bin,cmap='gray')
plt.title('Binary')

thres_img_inv_bin = thresholding(gray_img,45,'Binary_Inverse')
plt.imshow(thres_img_inv_bin,cmap='gray')
plt.title('Binary Inversion')

def gray_level_slicing(img,t1,t2):
    img_thresh_back = np.zeros((img.shape[0],img.shape[1]), dtype = int)   
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if t1 < img[i,j] < t2: 
                img_thresh_back[i,j]= 255
            else:
                img_thresh_back[i,j] = img[i,j]
    return img_thresh_back

gray_sliced = gray_level_slicing(gray_img,20,45) 

plt.imshow(gray_sliced,cmap='gray')
plt.title('Gray Level Sliced Image')