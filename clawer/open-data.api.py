# #下載特定網址資料
# import urllib.request as request
# with request.urlopen(網址) as response:
#     data=response.read()
# print(data)

#網路連線
# import urllib.request as request
# src="http://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") #取得台大網站的原始碼 (HTML CSS JS)
# print(data)
#串接、擷取公開資料
import urllib.request as request #載入網路連線模組urllib.request，as request縮寫
import json #載入json模組
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:  #開啟網路資料request.urlpoen(src), as response 縮寫
    data=json.load(response) #利用 json 模組處理 json 資料格式
#將公司名稱列表出來，首先觀察資料的格式
clist=data["result"]["results"] #網頁上的api格式是兩個result，data是字典，取得字典中的result，result也是字典在取得下一層的results
with open("data.txt",mode="w",encoding="utf-8") as file: #開啟一個文字檔案寫入
    for company in clist: #company分別是每一筆資料，都是字典1對1
        file.write(company["公司名稱"]+"\n") #公司名稱是字典，讀取字典的Value並寫入文字檔案

with open("data2.txt",mode="w",encoding="utf-8") as file: 
    for company in clist: 
        file.write(company["公司名稱"]+"  "+company["公司地址"]+"\n") #以+把不同的"文字"資料串起來，不是用,


#--------------test-------------------
# #載入網頁模組，縮寫as
# import urllib.request as request
# #指定網頁，令變數src
# src="https://nbk.acad.ncku.edu.tw/netcheckin/index.php?c=quall_rwd&m=qu"
# #request為網頁模組縮寫,urlopen(src)為開啟網頁,as縮寫
# with request.urlopen(src) as response:
#     #令變數data=respinse.read()讀取
#     data=response.read().decode("utf-8")
# print(data)

# #台北市水利處雨量站
# import urllib.request as request
# import json
# src="https://wic.heo.taipei/OpenData/API/Rain/Get?stationNo=&loginId=open_rain&dataKey=85452C1D"
# with request.urlopen(src) as response: #用網頁模組開啟src
#     data=json.load(response) #json.load 開始json格式的response
# clist=data["data"] #令變數clist=data裡面的字典，藍色的data=上面的程式，紅色的data為api內的字典名稱
# with open("rains taipei.txt",mode="w",encoding="utf-8") as file:
#     for rains in clist: #令變數rains，逐筆找資料
#         file.write(rains["stationName"]+"    "+str(rains["rain"])+"\n") #rain是數字資料要用str把int轉換成文字

# #桃園市空氣品質
# import urllib.request as request
# import json
# src="https://data.tycg.gov.tw/api/v1/rest/datastore/99431803-9c5a-477d-9c95-4c061acbe04b?format=json"
# with request.urlopen(src) as response:
#     data=json.load(response)
# airlist=data["result"]["records"]
# with open("air condition in Taoyuan.txt",mode="w",encoding="utf-8") as file:
#     for air in airlist :
#         file.write(air["County"]
#         +"  "+air["ItemName"]
#         +"  濃度"+str(air["Concentration"])
#         +" "+air["ItemUnit"]
#         +"  "+str(air["MonitorDate"])
#         +"\n")

# #桃園市工廠排放即時監測
# import urllib.request as request
# import json
# src="https://data.tycg.gov.tw/api/v1/rest/datastore/28bc4efa-a1c3-4d2e-8705-2010237b82ed?format=json"
# with request.urlopen(src) as response:
#     data=json.load(response)
# airlist=data["result"]["records"]
# with open("air condition in Taoyuan.txt",mode="w",encoding="utf-8") as file:
#     for air in airlist :
#         file.write(air["ABBR"]    
#         +"  "+air["M_YEAR"]+air["M_MONTH"]+air["M_DAY"]
#         +"  "+str(air["M_VAL"])+" "+air["UNIT"]
#         +"  "+air["STATUS"]
#         +"\n")