# #實體物件的建立與使用
# #類別的兩種用法
# # 1.類別與類別屬性
# # 2.類別與實體物件、實體屬性
# class Point:
#     #定義初始化函式
#     def __init__(self,x,y):
#         self.x=x #實體屬性跟類別屬性是分開的概念
#         self.y=y #實體屬性跟類別屬性是分開的概念
# #建立實體物件，並取得實體屬性資料
# #此物件包含 x y 兩個實體屬性
# #建立時，可直接傳入參數資料
# p=Point(1,5) #呼叫初始化函式
# print(p.x+p.y)  #實體物件.屬性名稱

# #Point 實體物件的設計:平面座標上的點
# class Point: #類別Point
#     def __init__(self,x,y):
#         self.x=x #實體屬性 X
#         self.y=y
# #建立第一個實體物件 p1
# p1=Point(3,4)
# print(p1.x,p1.y)
# #建立第二個實體物件 p2
# p2=Point(5,6)
# print(p2.x,p2.y)
# #FullName 實體物件的設計: 分開紀錄姓、名資料的全名
# class FullName:
#     def __init__(self,first,last):
#         self.first=first
#         self.last=last
# name1=FullName("LYU","YINGLI") #實體屬性:封裝在實體物件中的變數
# print(name1.first,name1.last)
# name2=FullName("GG","ininder")
# print(name2.first,name2.last)

#實體方法 (封裝在實體物件中的函式)
# class 類別名稱:
#     #定義初始化的函式
#     def __init__(self):
#         封裝在實體物件中的變數
#     def 方法名稱(self,更多自訂參數):
#         方法主體，透過self操作實體物件
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def show(self):
#         print(self.x,self.y)
# p=Point(1,5)#建立實體物件
# p.show()#呼叫實體方法

# # Point 實體物件的設計:平面座標上的點
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     #定義實體方法
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetX,targetY):
#         return(((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
# p1=Point(3,4)
# p1.show() #呼叫實體方法 / 函式
# result=p1.distance(0,0) #計算座標 3,4 和座標 0,0 之間的距離
# print(result)

# File 實體物件的設計: 包裝檔案讀取的程式
class File:
    # 初始化函式
    def __init__(self,name):
        self.name=name
        self.file=None #尚未開啟檔案:初期是None
    # 實體方法
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8") #開啟檔案的函式，得到一個檔案物件，放在實體屬性file裡
    # 實體方法
    def read(self):
        return self.file.read() #把上面得到的檔案物件 self.file 做 read 並且 return
#讀取第一個檔案
f1=File("backup//train.17//data1.txt") #建立實體物件放在變數f1
f1.open() #利用變數f1代表實體物件，呼叫實體方法 open
data=f1.read() #呼叫實體方法 read 放到變數 data
print(data)
#讀取第二個檔案
f2=File("backup//train.17//data2.txt")
f2.open()
data=f2.read()
print(data)