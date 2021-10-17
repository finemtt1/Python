#有序可變動列表 List
grades=[12,60,15,70,90]
#print(grades)
#print(grades[0])
#grades[0]=55 #把55放到列表中的第一個位置
#print(grades[0])

#print(grades[1:4])
#grades[1:4]=[]#連續刪除列表中從編號1到編號4(不包含4)的資料
#print(grades)

#grades=grades+[12,33]
#print(grades)

#length=len(grades)#取得列表的長度 len(列表資料)
#print(length)

#data=[[3,4,5],[6,7,8]]
#print(data)
#print(data[0])
#print(data[0][1]) #槽狀列表
#data[0][0:2]=[5,5,5] #資料取代
#print(data[0])

#有序不可變動列表 Tuple
data=(3,4,5)
print(data[2])
#data[0]=5 #error:Tuple object does not support item assignment
#print(data)