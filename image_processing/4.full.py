import cv2
import numpy as np
import time

# 載入圖片
img = cv2.imread("D:\\Python\\trainnig\\W_A1_0_3.jpg")

# ----BGR2GRAY-------------------------------------
# 分離成單通道 b, g, r
b, g, r = img[:,:,0],img[:,:,1],img[:,:,2]

# 轉灰階圖 # Gray =  0.299 R + 0.587 G + 0.114 B
imgGray = np.uint8((0.3*r + 0.59*g + 0.11*b))



# ----Smooth-------------------------------------------------

filter_size = 5
#filter = np.array(([1,2,1],[2,4,2],[1,2,1])) / 16  # gaussuan 
filter = np.ones((filter_size, filter_size), dtype=np.float32) / filter_size**2   #averge

# 定義圖片寬高與filter寬高
h = imgGray.shape[0]
w= imgGray.shape[1] 
filter_h = filter.shape[0]
filter_w = filter.shape[1]

# # 以filter的中心點 定義迴圈範圍
x1 = np.int32((filter_h - 1)/ 2)
y1 = np.int32((filter_w - 1)/ 2)
x2 = np.int32(h - (filter_h - 1)/ 2)
y2 = np.int32(w - (filter_w - 1)/ 2)

# 計算開始時間
start1 = time.process_time()

# 掃描像素做捲積
for i in range(x1,x2):
    m = i- x1 # 0~
    for j in range(y1,y2):
        n = j- y1 # 0~

        #像素移動 filter也會跟著動
        K = imgGray[m: m+ filter_h, n: n+ filter_w]

        # 把捲積的結果替換回原始圖的1個像素
        imgGray[i,j] = np.sum(K * filter)

imgSmooth = imgGray # 圖片重新存成Smooth

end1 = time.process_time()
print("smooth time:",end1-start1)

# cv2.imwrite("full-smooth_gaussian_3x3.jpg",imgSmooth)
cv2.imwrite("smooth_avg_5x5.jpg",img)



#------------threshold--------------------------------------------------


# 定義閥值參數
a = 10
b = 0.5

# global mean 效果不好
# mean_global = np.mean(img)

start2 = time.process_time()

for i in range(x1,x2): # i 從 filter中心開始
    # 定義 filter範圍
    m = i - x1 # 從0開始

    for j in range(y1,y2):
        # 定義 filter範圍
        n = j -y1 #從0開始

        # 把 filter範圍內的值存進矩陣 L
        L = imgSmooth[m: m+ filter_h, n: n+ filter_w]

        # 對 filter內的所有像素取標準差與平均值，找出threshold
        mean = np.mean(L)
        stdv = np.std(L)
        t = a * stdv + b * mean # threshold value

        # 對每個點做二值化
        if (imgSmooth[m,n] > t):
            imgSmooth[m,n] = 255
        else:
            imgSmooth[m,n] = 0

imgBinary = imgSmooth

end2 = time.process_time()
print(("threshold time",end2-start2))

cv2.imwrite("full-threshold_variable_avg_a=10,b=0.5.jpg", imgBinary)


#-------------------closing------------------------------------------

kernel = np.ones((5,5),np.uint8)
img_closing = cv2.morphologyEx(imgBinary,cv2.MORPH_CLOSE,kernel)
cv2.imwrite("closing_cv_avg.jpg", np.hstack((imgBinary,img_closing)))
