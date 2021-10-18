import cv2
import numpy as np
from matplotlib import pyplot as plt
# smoothing 降躁，邊緣模糊

# 讀取圖片→轉成灰階
img = cv2.imread("W_A1_0_3.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 圖片類型與大小
shape = img.shape
pix = img.size

# 定義圖片的高度與寬度
height = img.shape[0]
width = img.shape[1]

# 高斯模糊 (img,kernelsize,sigma) # RGB圖or灰階圖都可模糊
img_gauss = cv2.GaussianBlur(img, (5, 5), 0)
# cv2.imshow("gauss",img_gauss)
# cv2.waitKey(0)

# thresholding
# ADAPTIVE_THRESH_MEAN_C 算術平均二值化:(IMAGES,255,算法,閥值類型,參考局部大小,偏移量)
img_th1= cv2.adaptiveThreshold(img_gauss,255,cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY,5,2 )

# closing
# np.ones(shape,dtype)
kernel = np.ones((5,5),np.uint8)
img_closing = cv2.morphologyEx(img_th1,cv2.MORPH_CLOSE,kernel)
cv2.imwrite("HW.jpg", np.hstack((img, img_gauss, img_th1, img_closing)))
