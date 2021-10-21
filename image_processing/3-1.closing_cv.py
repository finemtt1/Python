import cv2
import numpy as np
import os

# print(os.getcwd()) #顯示當前路徑

# os.chdir("/Python/trainnig/image_processing") #更改路徑

# print(os.getcwd()) #顯示當前路徑

# 載入binary圖片
img = cv2.imread("threshold_variable_a=3,b=0.3.jpg")

kernel = np.ones((5,5),np.uint8)
img_closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imwrite("closing_cv.jpg", np.hstack((img,img_closing)))
