import cv2
import numpy as np

# 載入圖片
img = cv2.imread("D:\\Python\\trainnig\\k-means\\img2.jpg")
h, w, c = img.shape

# 調整 image 矩陣 ; (-1)代表np由剩下的維度計算 (x,y)從2維改成一維
img = np.reshape(img,(-1,3)) 
'''
img 降成二維矩陣
axis = 0 列 row :bgr值  ， 每列分別運算處理
axis = 1 欄 col: b,g,r ，每欄分別運算處理
[[229 110   1]
 [229 110   1]
 [229 110   1]
 ...
 [ 25  47  29]]
'''

# 新圖片
img_kmeans = np.zeros((h * w, 3), dtype= np.uint8) # 圖片要還原成uint8 才能正常顯示

#------------------- 設定隨機數與初始值---------------------------------
# k聚類中心數量
k = 5
# rand = np.random.randint(low= 0, high=(h*w), size=k) # 隨機取K個數，範圍h*w 
# cluster = img[rand].copy()

# # 手動設定聚類中心
# cluster = np.zeros((k,3),dtype = np.uint8)
# cluster[0] = [255,146,0]
# cluster[1] = [255,255,255]
# cluster[2] = [45,86,58]
# cluster[3] = [161,154,75]
# cluster[4] = [8,195,115]

# # 隨機挑選K範圍
a = 255/k #51
rand1 = np.random.randint(low= 0, high=(a)) # 隨機取K個數，範圍h*w 
rand2 = np.random.randint(low= a, high=(a*2))
rand3 = np.random.randint(low= a*2, high=(a*3))
rand4 = np.random.randint(low= a*3, high=(a*4))
rand5 = np.random.randint(low= a*4, high=(a*5))
cluster = np.zeros((k,3),dtype = np.uint8)
cluster[0] = [rand1,rand1,rand1]
cluster[1] = [rand2,rand2,rand2]
cluster[2] = [rand3,rand3,rand3]
cluster[3] = [rand4,rand4,rand4]
cluster[4] = [rand5,rand5,rand5]


'''
cluster 把k值存成二維矩陣
[[b1  g1  r1]    k1 
 [b2  g2  r2]    k2
 [b3  g3  r3]    k3
 ...]
'''
print(cluster)

cluster_new = np.zeros((k,3),dtype=np.int32) # 新聚類中心    #(BGR值存放k個)     

Flag = np.zeros((h*w),dtype=np.int32) # 存放是哪個聚類

# 迴圈初始值
delta = 100

# --------------------------------------------------------------------------
# 重複迴圈直到 群集中心的差異收斂
while delta > 1:
        
        # Step1. 計算像素到每個聚類中心的距離
        for i in range(w*h): 
                distance = np.sqrt(np.sum((cluster - img[i])**2, axis=1))   # 距離 = 平方差相加開根號
        
                Flag[i] = np.argmin(distance)
                ''' 
                distance [d1 d2 d3 ... dn] 像素到每個聚類中心的距離 存成一維矩陣
                Flag[i] = 0~k 
                np.argmin 找出d1~dn最小值，並返回位置 0~k
                '''
                #print(distance,Flag[i])


        # 對每一個群取平均，找出新的平均值
        # 分別從群組0~群組2 進行平均
        for j in range(k):
                cluster_new[j] = np.mean( img[ Flag == j ], axis=0 ) # 對所有 Flag = 0~k 的群組分別 ; axis=0 ;分別將 b1~bn ,g1~gn , r1~rn 做平均 
                '''
                img[ Flag ==j ] :所有符合群組 j 的像素
                axis = 0 : 對每欄做平均,分別運算 b1~bn ,g1~gn , r1~rn ， 得到新的 B G R 平均
                cluster_new[j] : 存到新的聚類中心矩陣 # array(k,3)
                '''

        
        d1 = np.sum(cluster)
        d2 = np.sum(cluster_new)
        delta = np.abs(d1-d2)
        #print(d1,d2,delta)

        # 更新群集中心
        cluster = np.copy(cluster_new)

# 把分類完得聚類中心 BGR 值，丟回同一類的像素點
for i in range(k) :
        img_kmeans[Flag == i] = cluster_new[i]

# 還原圖片矩陣
img_kmeans = np.reshape(img_kmeans,(h, w, 3))

cv2.imshow("kmeans", img_kmeans)
cv2.waitKey(0)
