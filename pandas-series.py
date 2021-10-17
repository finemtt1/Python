# 數字運算:數學統計相關
# import pandas as pd
# data=pd.Series([3,10,20,5,-12])
# print(data.sum(),data.max(),data.prod()) #prod全部相乘
# print(data.mean(),data.median(),data.std()) #mean:avg
# print(data.nlargrest(3),data.nsmallest(2))

# 字串運算:
# import pandas as pd
# data=pd.Series(["你好","Python","Pandas"])
# # 各種字串操作，都定義在 str 底下
# print(data.str.lower(),data.str.upper(),data.str.len())
# print(data.str.cat(sep=","),data.str.contains("P")) #cat(sep=)把字串串起來
# print(data.str.replace("你好","Hello"))

# 載入 pandas模組
import pandas as pd
# 資料索引
# data = pd.Series([5,4,-2,3,7])
# print(data)
# data2 = pd.Series([5,4,-2,3,7],index=["a","b","c","d","e"])
# print(data2)

# 觀察資料 
# print("資料型態",data2.dtype)
# print("資料的數量",data2.size)
# print("資料的索引",data2.index)

# 取得資料: 根據順序、根據索引
# print(data2[2],data[0]) 
# print(data2["c"],data2["a"])

# 數字運算: 基本、統計、順序
# print("最大值",data2.max())
# print("總和",data2.sum())
# print("標準差",data2.std())
# print("中位數",data2.median())
# print("最大的三個數",data2.nlargest(3))

# 字串運算: 基本、串接、搜尋、取代
data=pd.Series(["你好","Python","Pandas"])
# print(data.str.lower()) 小寫
# print(data.str.upper()) 大寫
# print(data.str.len()) 字串長度
# print(data.str.cat(sep="阿")) 把字串串起來，可自訂符號
# print(data.str.contains("P")) 判斷每個字串是否包含特定的字元
print(data.str.replace("你好","Hello"))