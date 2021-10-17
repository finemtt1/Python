#定義一個印出Hello的函式
# def sayHello():
#     print("Hello")
#呼叫上方定義的函式
# sayHello()

#定義可以印出任何訊息的函式
# def say(msg): #msg:函式參數的定義可以讓函是有彈性
#     print(msg)
# #呼叫上方定義的函式
# say("Hello Fumction")
# say("Hello Python")

#定義一個可以做加法的函式
def add(n1,n2):
    result=n1+n2
    print(result)
#呼叫上方定義的函式
add(3,4)
add(7,8)

#函式回傳 None
# def say(msg):
#     print(msg)
#     return  #回傳None
#呼叫函式，取的回傳值
# value=say("Hello Function")  #None=say("Hello Function") =value
# print(value)#印出 None

#函式回傳Hello
# def add(n1,n2):
#     result=n1+n2
#     return "Hello" #算出n1+n2但是回傳"Hello"
#呼叫函式，取得回傳值
# value=add(3,4)
# print(value) #印出Hello

#函式回傳 n1+n2的結果
# def add(n1,n2):
#     result=n1+n2
#     return result
#呼叫函式，取得回傳值
# value=add(3,4)
# print(value) #印出7 

#return 回傳函式內的結果，好處是可以把回傳值在函式外部繼續處理資料

#定義函式
#函式如沒有被呼叫，就不會執行
# def multiply(n1,n2):
#     print(n1*n2)
#呼叫函式
#multiply(5,9) #呼叫函式
# value=multiply(3,4) #回傳值=None，value=None
# print(value)

# def multiply(n1,n2):
#     print(n1*n2)
#     return n1*n2
#呼叫函式
# value=multiply(3,4)+multiply(10,5) #回傳值=n1*n2，value=n1*n2
# print(value)

#程式的包裝 函式最重要的用途
def calculate(n1,n2): #參數n1,n2定義在這
    sum=0
    for n in range(n1,n2+1):
        sum=sum+n
    print(sum)
calculate(1,10)
calculate(1,20)