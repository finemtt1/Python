#數字運算
#x=3+6
#print(x)
#x=3*6
#print(x)
#x=7/6
#print(x)
#x=7//6 #整除
#print(x)
#x=2**3 #次方
#print(x)
#x=7%3  #取餘數
#print(x)
#x=x+1 # 將變數中的數字+1
#print(x)
# x-=1 #x+=1 #x*=1 相當於變數-、+、*，為簡便寫法  

#字串運算
#字串會對內部的字元編號(索引).從0開始算起
#s="Hello" 
#print(s)
#s="Hell\"o" #\ :跳脫，字串內有雙引號需使用跳脫跟字串""區別
#print(s)   
#s="Hello"+"World" 
#print(s)
#s="Hello" "world" #+、空格 都是字串的串接
#print(s)
#s="Hello\nWorld" #\n 換行
#print(s)

# s="""Hello
# World"""  #""""可以任意換行
# print(s)
# #s="Hello"*3+"World"
# #print(s)
# s="Hello"
# #  01234
# print(s[0]) #g數字代表字串的位置
# print(s[1:4])
# print(s[1:])
# print(s[:4])
# print(s.index("l")) #如有重複的字回傳最前面的位置

# #字串的函式 小白補充
# phrase="Hello Mr.Lyu"
# print(phrase.lower())
# print(phrase.upper())
# print(phrase.isupper())
# print(phrase.islower())
# print(phrase.lower().islower())
# print(phrase.replace("Lyu","呂"))

# #數字的函式 小白補充
# number=-8
# print("會印出數字"+str(number))#str把數字轉成字串
# print(abs(number)) #絕對值
# print(pow(2,4)) #2的4次方
# print(max(2,3,88,100)) #回傳最大數
# print(min(2,3,88,100)) #回傳做小數
# print(round(4.6)) #四捨五入
# x=float(input("請輸入第一個數:"))) #str轉換成有小數的樹
# from math import * #引入數學模組，可以多數學函式用
# print (floor(4.6)) #無條件捨去
# print (ceil(4.6)) #無條件進位
# print(sqrt(4.6)) #開根號
