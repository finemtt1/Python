# 載入 pandas 模組
import pandas as pd
# 篩選練習 - Sereis
# data=pd.Series([30,15,20])
# #condition=[True,False,True]
# condition= data>18 #透過比較運算得到布林值列表
# print(condition)
# filteredData=data[condition] #以布林值篩選條件
# print(filteredData)

# data=pd.Series(["你好","Python","Pandas"])
# #condition=[True,False,True]
# condition=data.str.contains("P")
# print(condition)
# filteredData=data[condition]
# print(filteredData)

# 篩選練習 -DataFrame
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
})
# print(data)
# condition=[True,False,True]
# condition=data["salary"]<=40000
condition=data["name"]=="Amy" #透過比較運算得到布林值列表
print(condition)
filteredData=data[condition] #以布林值篩選條件
print(filteredData)
