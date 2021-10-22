import cv2
import numpy as np

#----------------------圖片載入-----------------------------

# 載入圖片
img = cv2.imread("D:\\Python\\trainnig\\k-means\\img1.jpg")
h, w, c = img.shape

# 分離 BGR影像
b, g, r = img[:,:,0],img[:,:,1],img[:,:,2]

# 調整 image 為三維 b,g,r的灰階值  (-1)代表np由剩下的維度計算 (x,y)改成1維
img = np.reshape(img,(-1,3)) #(230400,3) b,g,r的灰階值
imgB = np.reshape(b,(-1,1))  #(230400,1)


#------------------- 設定隨機數---------------------------------
# k聚類中心數量
k = 3

rand = np.random.randint(low= 0, high=(h*w), size=k) # 隨機取K個數，範圍h*w
clustering = imgB[rand] # k個灰階值 存入列表，當成聚類中心
cluster_new = np.zeros((k,1),dtype=np.int32) # 新聚類中心
#print(clustering[0],clustering[1],clustering[2]) # 初始聚類中心

#---------------------設定初始值---------------------------
# 存放距離與灰階值
Distances = np.zeros((h*w),dtype=np.float16)
Flag = np.zeros((h*w),dtype=np.int32)

# 距離判斷初始值
temp_distance = 257

# 存放群組的灰階值
group1 = []
group2 = []
group3 = []

# 迴圈初始值
delta = 100

#--------------------------------------------------------------------------
# 重複迴圈值到 群集中心的差異收斂
while delta > 1:
# 掃過整張圖的像素
    for i in range(h*w):

        for j in range(k): # Step1. 計算像素到每個聚類中心的距離
        
            distance = np.sqrt((clustering[j]-imgB[i])**2)  # 距離 = 平方差開根號  (算每個像素與聚類中心灰階值的差異)
            if distance < temp_distance: # 找出最短距離
                temp_distance = distance # 存入距離到暫存繼續判斷用
                flag = j # 存入最短距離是哪群
        
        Distances[i] = distance # 存入距離到像素位置   
        Flag[i] = flag # 記錄像素的群族
        temp_distance = 257 # 初始化距離



    # Step2 .分類每個像素點
    for i in range(h*w):
    
        # 分類群組 存入灰階值
        if np.int32(Flag[i]) == 0:
            group1.append(imgB[i])  # 整數灰階值存入group群組
     
        elif np.int32(Flag[i]) == 1:
            group2.append(imgB[i])

        elif np.int32(Flag[i]) == 2:
            group3.append(imgB[i])

    # Step3. 找出新的聚類平均值
    cluster_new[0] = np.nan_to_num(np.mean(group1)) # 遇到警告 Mean of empty slice. 把nan→0
    cluster_new[1] = np.nan_to_num(np.mean(group2))
    cluster_new[2] = np.nan_to_num(np.mean(group3))
    print(cluster_new[0],cluster_new[1],cluster_new[2])

    # 計算新舊群聚中心的差異
    d1 = np.sum(clustering) #舊
    d2 = np.sum(cluster_new) #新
    delta = np.abs(d2- d1) 
    #print(d1,d2,delta)

    # 更新群集中心
    clustering = np.copy(cluster_new)

    
print("end",delta)






