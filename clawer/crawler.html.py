# #抓取 PTT 電影版的網頁原始碼(HTML格式資料)
# #盡可能讓程式模仿一個普通的使用者
# import urllib.request as req
# url="https://www.ptt.cc/bbs/movie/index.html"
# #建立一個Request物件，附加 Request Headers 的資訊
# #利用request物件打開網址，並且發送Headers，讓程式看起來像一般使用者
# request=req.Request(url,headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data=response.read().decode("utf-8")

# #解析原始碼. 取得每篇文章的標題
# import bs4
# root=bs4.BeautifulSoup(data,"html.parser") #BeautifulSoup 協助解析HTML文件
# print(root.title.string) #title是網頁的標籤
# titles=root.find_all("div",class_="title") #尋找所有class="title"的div標籤,class_="title為搜尋條件",底線是固定格式
# for title in titles:
#     if title.a !=None: #如果標題包含 a 標籤 (沒有被刪除)，則印出
#         print(title.a.string)


#連續抓取 PTT GOSSIPING 頁面實務 #新增cookies
import urllib.request as req
#把程式用函式def 做一個包裝，為了後面做很多頁面
def getdata(url):
    #Request headers增加一個cookie over18=1，告訴ptt已經按過已滿18
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        ,"cookie":"over18=1"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title")
    for title in titles:
        if title.a !=None:
            print(title.a.string)
    #抓取上頁的連結
    nextlink=root.find("a",string="‹ 上頁")#找到內文是 ‹ 上頁 的 a 標籤
    return nextlink["href"]
#主程序:抓取多個頁面的標籤
pageurl="https://www.ptt.cc/bbs/Gossiping/index.html" #第一頁
pages=0
#用while迴圈抓5頁
while pages<5:
     #把pageurl傳到getdata裡面呼叫函式getdata，函式getdata會returm上頁的連結覆蓋pageurl
    pageurl="https://www.ptt.cc"+getdata(pageurl)
    pages+=1

#------test----------
# # #抓取巴哈姆特-守望傳說-哈拉版(HTML)
# # import urllib.request as req
# # url="https://forum.gamer.com.tw/B.php?page=2&bsn=38113"
# # request=req.Request(url,headers={
# #     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36)"
# # })
# # with req.urlopen(request) as response:
# #     data=response.read().decode("utf-8")
# # import  bs4
# # root=bs4.BeautifulSoup(data,"html.parser")
# # titles=root.find_all("div",class_="b-list__tile")
# # for title in titles:
# #     if title.p !=None:
# #         print(title.p.string)

# import urllib.request as req
# def getdata(url):
#     request=req.Request(url,headers={
#         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36)"
#     })
#     with req.urlopen(request) as response:
#         data=response.read().decode("utf-8")
#     import  bs4
#     root=bs4.BeautifulSoup(data,"html.parser")
#     titles=root.find_all("div",class_="b-list__tile")
#     for title in titles:
#         if title.p !=None:
#             print(title.p.string)
#     #抓取下一頁連結
#     nextlink=root.find("a",class_="next")
#     return (nextlink["href"])
# pageurl="https://forum.gamer.com.tw/B.php?page=2&bsn=38113"
# pages=0
# while pages<3:
#     pageurl="https://forum.gamer.com.tw/B.php?"+getdata(pageurl)
#     pages+=1
    
