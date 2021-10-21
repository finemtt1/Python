import cv2
import numpy as np
  
img = cv2.imread("W_A1_0_3.jpg",0)

Filter_avg = np.ones((5, 5), dtype=np.float32) /25

Img_shape = img.shape 

Filter_shape = Filter_avg.shape #5*5


# zero padding : 在圖像的外圍加上0
Row = Img_shape[0]+Filter_shape[0]-1 
Column = Img_shape[1]+Filter_shape[1]-1 
Zero = np.zeros((Row,Column))



# 把原始圖片放進Zero矩陣, 原始圖片從矩陣第三行第三格開始，在python中是Zero[2,2]  ，因為0~2 = 3
for i in range(Img_shape[0]): 
    filter_i = i+np.int32((Filter_shape[0]-1)/2)
    for j in range(Img_shape[1]): 
        Zero[filter_i,j+np.int32((Filter_shape[1]-1)/2)] = img[i,j]


# filter
for i in range(Img_shape[0]):
    m = i+Filter_shape[0]
    for j in range(Img_shape[1]): 
        K = Zero[i:m, j:j+Filter_shape[1]] # 像素移動 filter也會跟著動
        img[i,j] = np.sum(K * Filter_avg)  # 把捲積的結果替換回原始圖的1個像素 #np.sum 把矩陣所有元素相加
img_smooth = img


cv2.imwrite("smooth.jpg", img_smooth)
