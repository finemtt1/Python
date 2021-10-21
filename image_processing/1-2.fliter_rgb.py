import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("img1.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

kernel_size = 3
filter_avg = np.ones((kernel_size, kernel_size), dtype=np.float32) / kernel_size**2
Filter_shape = filter_avg.shape
Img_shape = img.shape

# zero padding : 在圖像的外圍加上0
Column = Img_shape[0]+Filter_shape[0]-1
Row = Img_shape[1]+Filter_shape[1]-1
Zero = np.zeros((3,Column,Row))


# 把原始圖片放進Zero矩陣, 原始圖片從矩陣第三行第三格開始，在python中是Zero[2,2]  ，因為0~2 = 3  
for m in range(3):
    for i in range(Img_shape[0]): #0~360
        for j in range(Img_shape[1]): #0~640
            Zero[m,i+np.int32((Filter_shape[0]-1)/2),j+np.int32((Filter_shape[1]-1)/2)] = img[i,j,m]

# filter
for m in range(3):
    for i in range(Img_shape[0]): #0~360
        for j in range(Img_shape[1]): #0~640
            # 364*644 的0矩陣中 抓取 Filter大小的矩陣 令重疊的矩陣為K 
            K = Zero[m,i:i+Filter_shape[0], j:j+Filter_shape[1]] #像素移動 filter也會跟著動
            # 把捲積的結果替換回原始圖的1個像素
            img[i,j,m] = np.sum(K * filter_avg)

cv2.imshow("G8",img)
cv2.waitKey(0)




