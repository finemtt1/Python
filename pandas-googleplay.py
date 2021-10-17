import pandas as pd
# 讀取資料
data=pd.read_csv("googleplaystore.csv") #把 csv 檔案讀取成一個 Dat把 csv 檔案讀取成一個 DataFrame
# 觀察資料
print("資料數量",data.shape)
print("資料欄位",data.columns)
print("===================================")

# 分析資料:評分的各種統計數據
# condition=data["Rating"]<=5 #資料清理，只取評分<=5的正常資料
# data=data[condition]
# print("平均數",data["Rating"].mean())
# print("中位數",data["Rating"].median())
# print("取得前1000個應用程式的平均",data["Rating"].nlargest(1000).mean())

# 分析資料:安裝數量的各種統計數據
# print(data["Installs"]) #安裝數是字串object，需轉換成數字才能統計
# print(data["Installs"][10472]) #怪異字串把它清掉
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))  #把str中的符號清掉，只留數字再用pd轉換成數字格式
# #print(data["Installs"])
# print("平均數",data["Installs"].mean())
# condition=data["Installs"]>100000
# # print("安裝數量大於100,000的應用程式",data[condition].shape) #shape(列,欄)
# print("安裝數量大於100,000的應用程式",data[condition].shape[0]) #shape(列)

# 基於資料的應用:關鍵字搜尋應用程式名稱
keyword=input("請輸入關鍵字:")
condition=data["App"].str.contains(keyword,case=False) #case=False:忽略大小寫
# print(data[condition]["App"])
print("包含關鍵字的數量",data[condition].shape[0])