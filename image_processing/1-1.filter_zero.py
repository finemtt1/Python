import cv2
import numpy as np
import time

img = cv2.imread("W_A1_0_3.jpg",0)

kernel_size = 3
#Filter_gaussian = np.array((
# [1,2,1],
# [2,4,2],
# [1,2,1])) / 16
Filter_avg = np.ones((kernel_size, kernel_size), dtype=np.float32) / kernel_size**2

Img_shape = img.shape 
Filter_shape = Filter_avg.shape 

# zero padding : 在圖像的外圍加上0
Column = Img_shape[0]+Filter_shape[0]-1 #364
Row = Img_shape[1]+Filter_shape[1]-1 #644
# 製作0矩陣
Zero = np.zeros((Column,Row))

start = time.process_time()

# 把原始圖片放進Zero矩陣
for i in range(Img_shape[0]): #0~360
    for j in range(Img_shape[1]): #0~640    
        Zero[i+np.int32((Filter_shape[0]-1)/2),j+np.int32((Filter_shape[1]-1)/2)] = img[i,j]


# filter
for i in range(Img_shape[0]): 
    for j in range(Img_shape[1]):
        # 364*644 的0矩陣中 抓取 filter大小的矩陣 令重疊的矩陣為K 
        K = Zero[i:i+Filter_shape[0], j:j+Filter_shape[1]] #像素移動 filter也會跟著動
        # 把捲積的結果替換回原始圖的1個像素
        img[i,j] = np.sum(K * Filter_avg)

end = time.process_time()
print(end-start)
# cv2.imwrite("smooth_gaussian_3x3.jpg",img)
cv2.imwrite("smooth_avg_3x3.jpg",img)


