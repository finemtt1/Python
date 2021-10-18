import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("img1.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

kernel_size = 5
Filter_avg = np.ones((kernel_size, kernel_size), dtype=np.float32) / kernel_size**2
# print(filter_avg.shape,filter_avg.size , filter_avg) #(5x5), 25 , array

Img_shape = img.shape # 360*640*3(bgr)
Filter_shape = Filter_avg.shape #5*5

# zero padding : 在圖像的外圍加上0
Column = Img_shape[0]+Filter_shape[0]-1 #364
Row = Img_shape[1]+Filter_shape[1]-1 #644
# 製作0矩陣
Zero = np.zeros((Column,Row))

# 把原始圖片放進Zero矩陣, 原始圖片從矩陣第三行第三格開始，在python中是Zero[2,2]  ，因為0~2 = 3
for i in range(Img_shape[0]): #0~360
    for j in range(Img_shape[1]): #0~640    
        Zero[i+np.int32((Filter_shape[0]-1)/2),j+np.int32((Filter_shape[1]-1)/2)] = img_gray[i,j]

#print(Zero.shape,Zero.size,Zero) #(364, 644) , 234416 , array

# filter
for i in range(Img_shape[0]): #0~360
    for j in range(Img_shape[1]): #0~640
        # 364*644 的0矩陣中 抓取 filter大小的矩陣 令重疊的矩陣為K 
        K = Zero[i:i+Filter_shape[0], j:j+Filter_shape[1]] #像素移動 filter也會跟著動
        # 把捲積的結果替換回原始圖的1個像素
        img_gray[i,j] = np.sum(K * Filter_avg)
img_smooth = img_gray

# print(img_gray.shape)
# print((K * Filter_avg).shape)
# print(img_smooth.shape)

cv2.imshow("filter_avg",img)
cv2.waitKey(0)