# #隨機選取
# import random #載入模組
# random.choice([0,1,5,8])#從列表中隨機選取1個資料
# random.sample([0,1,5,8],3)#從列表中隨機選取3個資料

# #隨機調換順序
# import random
# data=[0,1,5,8]
# random.shuffe(data)
# print(data)

# #隨機亂數
# import random
# random.random() #取0.0~1.0之間的隨機亂數
# random.uniform(0.0,1.0) #出現機率相同

# #常態分配亂數
# import random
# data=random.normalvariate(100,10)#取得平均數100，標準差10的常態分配亂數

# #統計模組
# import statistics
# statistics.mean([1,4,6,9]) #計算列表中的平均數
# statistics.median([1,4,6,9]) #計算列表中的中位數
# statistics.stdev([1,4,6,9]) #計算列表中的標準差

# #隨機模組
import random
# #隨機選取
# data=random.choice([1,5,6,10,20])
# data2=random.sample([1,5,6,10,20],3)
# print(data,data2)

# #隨機調換順序
# import random
# data=([1,5,8,20])
# random.shuffle(data)
# print(data)

# #隨機取得亂數
# data=random.random() #0.0~1.0之間的隨機亂數
# data2=random.uniform(0,60) 
# print(data2)

# #取得常態分配亂數
# data=random.normalvariate(100,10) #平均數100，標準差10
# print(data)

#統計模組
import statistics as stata
# data=stata.mean([1,2,3,4,5,8,100])
# data2=stata.median([1,2,3,4,5,8,100])
# data3=stata.stdev([1,2,3,4,5,8,100])
# print("平均數:",data,"中位數:",data2,"標準差:",data3)


print( random.sample(range(0, 10000),10000 ))
