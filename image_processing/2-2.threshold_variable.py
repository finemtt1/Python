import cv2
import numpy as np
import time

# 載入灰階圖片
img = cv2.imread("smooth.jpg",0)

# 建立filter
filter_size = 17
filter = np.zeros((filter_size,filter_size),dtype= np.float16) 

# 定義圖片寬高與filter寬高
h = img.shape[0]
w= img.shape[1] 
filter_h = filter.shape[0]
filter_w = filter.shape[1]

# 區分 local 區塊
x = h//filter_h 
y = w//filter_w 

# # 以filter的中心點 定義迴圈範圍
x1 = np.int32((filter_h - 1)/ 2)
y1 = np.int32((filter_w - 1)/ 2)
x2 = np.int32(h - (filter_h - 1)/ 2)
y2 = np.int32(w - (filter_w - 1)/ 2)

# 定義閥值參數
a = 3
b = 0.5

# # global mean
# global_mean = np.mean(img)

start = time.process_time()

# 掃描每個local block
for i in range(x1,x2,filter_h):
    m = i - x1 #0~
    for j in range(y1,y2,filter_w):
        n = j - y1 #0~

        L = img[m:m+filter_h,n:n+filter_w] # 存到矩陣 L

        mean = np.mean(L) # local 平均
        stdv = np.std(L) # local 標準差
        t = a * stdv + b * mean # threshold value


        # 掃描local內的每個點做閥值判斷
        for r in range(m,m+filter_h):
            for c in range(n,n+filter_w):
                if(img[r,c] > t):
                    img[r,c]=255 
                    
                else:
                    img[r,c]=0

end = time.process_time()
print((end-start))

cv2.imwrite("threshold_variable_a=30,b=1.5.jpg", img)
