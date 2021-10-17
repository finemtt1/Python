#載入內建的sys模組  #sys取得系統的相關資訊
#import sys  #import sys as s 用別名s來操作，方便辨認
#使用sys模組
# print(sys.platform) #印出作業系統  #print(s.platform)
# print(sys.maxsize) #印出整數型態的最大值
# print(sys.path) #印出搜尋模組的路徑
# pip 套件管理工具

#建立 geometry 模組，載入使用，把計算相關的程式獨立出來
# import geometry as gg
# result=gg.distance(1,1,5,5)
# print(result)
# result=gg.slope(4,4,1,2)
# print(result)

#調整搜尋模組的路徑
#python檔案名稱用數字開頭執行後會找不到路徑
import sys
#sys.path.append("moduels") #讓python增加一個模組的搜尋路徑
sys.path.append("C:\\python\\training\\backup\\moduels") #也可用絕對路徑搜尋，用\\
print(sys.path) #印出模組的搜尋路徑列表
print("----------------")
import geometry as gg
print(gg.distance(1,1,5,5))
