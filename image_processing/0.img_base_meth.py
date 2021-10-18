import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. 讀取圖片→轉成灰階
img = cv2.imread("W_A1_0_3.jpg")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #0 is black ; 255 is white 0~255不同的灰

# 1-2. 直接讀取成灰階
# img = cv2.imread("W_A1_0_3.jpg", flags=cv2.IMREAD_GRAYSCALE)
# img = cv2.imread("W_A1_0_3.jpg",0) #直接讀取成單通道

# 2.顯示圖片
# cv2.imshow("result",img)
# cv2.waitKey(0)

# # 定義圖片的高度與寬度、中心
# height = img.shape[0]
# width = img.shape[1]
# center = (int(height/2),int(width/2))


# -------------------------------------------------------------------

# # 圖像屬性
# print(img.shape) # 3648*5472 3通道

# # 像素總數
# print(img.size)

# # 圖像類型
# print(img.dtype) #uint8


# # (x,y)位置的像素
# px = img[100,100]
# print(px) # 顯示 BGR[25 25 25]

# # 顏色讀取
# blue = img[100,100,0]
# green = img[100,100,1]
# red = img[100,100,2]
# print(blue,green,red)

# # 修改像素值
# img[100,100] = [255,255,255]
# print(img[100,100])


# # 圖像感興趣區域ROI
# ball = img[280:340, 330:390] #(280,340)到(330,390)框選矩形

# 拆分和合併圖像通道
# b,g,r = cv2.split(img)

# -------------------------------

# print(img_gray[100,100])

# # cv2 is BGR ; matplotlib is RGB
# # 做色彩轉換
# img_mat = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.imshow(img) #相反顏色
# plt.show()
# plt.imshow(img_mat) # 正確顏色
# plt.show()

# ----------------直方圖-----------------------


# # 畫第一個圖
# plt.subplot(221)
# img_mat = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #轉乘RGB
# plt.imshow(img_mat)

# # 畫第二個圖
# plt.subplot(222)
# img_gray = cv2.cvtColor(img_mat,cv2.COLOR_RGB2GRAY) # 轉成灰度
# plt.imshow(img_gray)

# # 畫第三個圖
# plt.subplot(223)
# plt.hist(img.ravel(),256),plt.title("hist") # img.ravel() 多維陣列轉一維; 畫素級: 256, 表示[0,255]

# # 畫第四個圖
# plt.subplot(224)
# plt.hist(img_gray.ravel(),256),plt.title("hist") 
# plt.show()

# -------------------cv2-------------------------------------------------

import cv2
import numpy as np


# # 1. 讀取圖片→轉成灰階
# img = cv2.imread("W_A1_0_3.jpg")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1-2. 直接讀取成灰階
# img = cv2.imread("W_A1_0_3.jpg", flags=cv2.IMREAD_GRAYSCALE)
# img = cv2.imread("W_A1_0_3.jpg",0)

# 2.顯示圖片
# cv2.imshow("result",img)
# cv2.waitKey(0)

# --------------------------------------------------------------------------------

# 讀取灰階圖片
img = cv2.imread("W_A1_0_3.jpg",0)

# 二值化
# cv2.threshold(img,閥值,填充色,閥值類型) #要讀取灰度圖
# ret要加
ret, Threshold1 = cv2.threshold(img,172,255,cv2.THRESH_BINARY)

# Otsu's閥值
ret2, Threshold2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# 11為block size(計算閥值的區域大小)，2為C值(閥值=平均值-C)
Threshold3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY,11,2 )
Threshold4 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY,11,2)

titles = ['original image', 'global thresholding (v=127)', 'otus thresholding','Adaptive mean thresholding', 'adaptive gaussian thresholding'] 
images = [img,Threshold1,Threshold2,Threshold3,Threshold4]

# matplotlib輸出
for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([]) #不畫X,y
plt.show()

# # cv2輸出
# cv2.imshow('Original', img)
# cv2.imshow('BINARY',Threshold1)
# cv2.imshow('OTSU', Threshold2)
# cv2.imshow('ADAPTIVE_THRESH_MEAN', Threshold3)
# cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN', Threshold4)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# --------------------------------------
# #讀取圖片
# img = cv2.imread('W_A1_0_3.jpg',flags=cv2.IMREAD_GRAYSCALE)
# iter_time = 1

# kernel = np.ones((3,3),np.uint8)
# closing_img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel,iterations=iter_time)

# cv2.imwrite('dao_closing_k5_iter%d.png'%(iter_time), np.hstack((img, closing_img)))
