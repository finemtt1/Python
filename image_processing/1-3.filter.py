import cv2
import numpy as np
import time

img = cv2.imread("W_A1_0_3.jpg",0)

filter_size = 3
filter = np.array(([1,2,1],[2,4,2],[1,2,1])) / 16
# filter = np.ones((filter_size, filter_size), dtype=np.float32) / filter_size**2

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


start = time.process_time()

# filter
for i in range(x1,x2):
    m = i- x1
    for j in range(y1,y2):
        n = j- y1

        #像素移動 filter也會跟著動
        K = img[m: m+ filter_h, n: n+ filter_w]

        # 把捲積的結果替換回原始圖的1個像素
        img[i,j] = np.sum(K * filter)

end = time.process_time()
print(end-start)
cv2.imwrite("smooth_gaussian_3x3.jpg",img)
# cv2.imwrite("smooth_avg_3x3.jpg",img)

# cv2.imshow("hh",img)
# cv2.waitKey(0)
