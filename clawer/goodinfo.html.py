#從 goodinfo 抓取個股獲利資料 HTML/TEXT
import urllib.request as req
def getdata(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    # from bs4 import BeautifulSoup
    # #只要其中的txtFinDetailData資料
    # #select_one : id 前面 +# ; 類別前面 +. 
    import bs4
    root = bs4.BeautifulSoup(data,'html.parser').select_one('#txtFinDetailData')

    import pandas #表格用這個整理
    roots = pandas.read_html(root.prettify()) #prettify : 將內容依據html進行排版
    # result = roots[0].head(7) # 7rows
    with open("goodinfo.txt",mode="w",encoding="utf-8") as file:
        file.write(str(roots[0]))

number = int(input("請輸入股票代碼:"))
url = f"https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID={number}"
getdata(url)
print("成功建立:goodinfo.txt")


