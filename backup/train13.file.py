#基本語法
#絕對路徑 ex:C:/python/training/backup/tain13.file.py #斜線要反過來
#相對路徑 以程式的位置做延伸　ex:123.txt

#開啟檔案
    #檔案物件=open(檔案路徑，mode=開啟模式)
        #開啟模式-r(讀取)，-w(複寫)，-r+(讀寫),-a(附加)
#讀取檔案
    #檔案物件.read() #讀取全部文字
        #for 變數 in 檔案物件: #一行一行讀取
            #從檔案依序讀取每行文字到變數中
#讀取 json 格式
    #import json
    #讀取到的資料=json.load(檔案物件)
#寫入檔案
    #檔案物件.write(字串)  #換行符號/n
#寫入 json 格式
    #import json
    #json.dump(要寫入的資料，檔案物件)
#檔案關閉
    #檔案物件.close()
#最佳實務
#with open(檔案路徑，mode=開啟模式) as 檔案物件:
    #讀取或寫入檔案的程式  #以上區塊會安全且自動的關閉檔案。

#儲存檔案
# file=open("data.txt",mode="w",encoding="utf-8") #開啟  #encoding="utf-8"為中文格式
# file.write("Hello File\nSecond Line\n中文測試") #操作
# file.close() #關閉
#最佳實務
# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("Hello File\nSecond Line\n中文測試")

#讀取檔案 文字檔案
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     data=file.read()
#     print(data)

#Example 讀取文字檔案中的數字並計算總合
# with open("data2.txt",mode="w",encoding="utf-8") as file : #file是自訂的變數
#     file.write("5\n3") 
# sum=0
# with open("data2.txt",mode="r",encoding="utf-8") as file:
#     for line in file: #一行一行讀取，line是自訂的變數
#         sum+=int(line) #把字串轉成整數並且加起來
# print(sum)
#-----------------------------------------------------        
#JSON格式介紹(javaScript 物件表示法)
#jSON格式{
    # "成員名稱1":成員資料,
    # "成員名稱2":成員資料,
    # "成員名稱3":function(){
    #  alert(this.成員名稱1+","+this.y);
    #}
#};
    #JSON用大括號可以製造物件
    #function是函式，成員資料是物件
    #JSON.stringify(物件);將物件轉換成json格式的字串，但會忽略函式
    #JSON.parse(JSON格式字串);將字串轉換成物件結構
#-------------------------------------------------------
#使用 JSON 格式讀取，複寫檔案
# import json
# with open("config.json",mode="r") as file:
#     data=json.load(file)
# print(data) #data 是一個字典資料
# print("name:",data["name"])
# print("version:",data["version"])

#從檔案中讀取JSON資料，放入變數data裡面
import json
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data) #data 是一個字典資料，因config內的資料是字典資料
data["name"]="New Name2" #修改變數中的資料
#把最新的資料複寫回檔案中
with open("config.json",mode="w") as file:
    json.dump(data,file) #dump(資料,檔案物件)