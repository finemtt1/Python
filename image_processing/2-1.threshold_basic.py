import cv2
import numpy as np
import time

img = cv2.imread("smooth.jpg",0)
h = img.shape[0]
w = img.shape[1] 

t= 130
t_new=0
delta = abs(t_new- t)

start = time.process_time()

# 找出閥值
while delta> 1:
    group1 = []
    group2 = []
    for i in range(h):
        for j in range(w):
            if(img[i,j] < t):
                group1.append(img[i,j])

            elif(img[i,j] >= t):
                group2.append(img[i,j])

    m1 = np.mean(group1)
    m2 = np.mean(group2)
    t_new= (m1+m2)/2
    delta = abs(t_new-t)
    t = t_new

end = time.process_time()
print(t_new,(end-start))

# 二值化
for i in range (h):
    for j in range(w):
        if(img[i,j] < t_new):
            img[i,j]=0  
        elif(img[i,j] >= t_new):
            img[i,j]=255
           
img_binary = img
cv2.imwrite("binary_basic.jpg", img_binary)



