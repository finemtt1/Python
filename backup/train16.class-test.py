# #封裝變數與函數，統稱為類別(class)的屬性(變數與函數)
# #定義 Test 類別
# class Test:
#     x=3 #定義變數
#     def say(): #定義函式
#         print("Hello")
# #使用 Text 類別
# Test.x+3 #取得屬性 x 的資料 3
# Test.say() #呼叫屬性 say 函式

#定義類別、與類別屬性 (封裝在類別中的變數和函式)
#定義一個類別 IO，有兩個屬性 supportedSrcs 和 read
class IO:
    supportedSrcs=["console","file"] #定義變數
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("Read from",src)
#使用類別 (類別+屬性)
print(IO.supportedSrcs)
IO.read("file") #呼叫read把file傳進src，屬於supportedSrc，可印出
IO.read("internet") #把internet傳進src，不屬於supportedSrc