import cv2
import numpy as np
import time

# 載入灰階圖片
img = cv2.imread("smooth.jpg",0)

# 建立filter
filter_size = 3
filter = np.ones((filter_size,filter_size),dtype= np.float16) 

# 定義圖片寬高與filter寬高
h = img.shape[0]
w= img.shape[1] 
filter_h = filter.shape[0]
filter_w = filter.shape[1]

# # 以filter的中心點 定義迴圈範圍
x1 = np.int32((filter_h - 1)/ 2)
y1 = np.int32((filter_w - 1)/ 2)
x2 = np.int32(h - (filter_h - 1)/ 2)
y2 = np.int32(w - (filter_w - 1)/ 2)

# 定義閥值參數
a = 10
b = 0.5

# global mean 效果不好
# mean_global = np.mean(img)

start = time.process_time()

for i in range(x1,x2): # i 從 filter中心開始
    # 定義 filter範圍
    m = i - x1 # 從0開始

    for j in range(y1,y2):
        # 定義 filter範圍
        n = j -y1 #從0開始

        # 把 filter範圍內的值存進矩陣 L
        L = img[m: m+ filter_h, n: n+ filter_w]

        # 對 filter內的所有像素取標準差與平均值，找出threshold
        mean = np.mean(L)
        stdv = np.std(L)
        t = a * stdv + b * mean # threshold value

        # 對每個點做二值化
        if (img[m,n] > t):
            img[m,n] = 255
        else:
            img[m,n] = 0

end = time.process_time()
print((end-start))

cv2.imwrite("threshold_variable3_a=10,b=0.5.jpg", img)