#參數 msg 預設資料為"Hello"
# def say(msg="Hello"):
#     print(msg)
#印出 Hello Function
# say("Hello Function") #印出Hello Function
# say() #印出預設資料 Hello

##定義一個可以做加法的函式
# def devide(n1,n2):
#     result=n1/n2
#     print(result)
##呼叫函式，以參數名稱對應資料
# devide(2,4)#印出0.5
# devide(n2=2,n1=4) #印出2.0 #可指定參數的名稱不管順序

#函式接受無限參數msgs
# def say(*msgs): #前面加*
#     #以Tuple的方式處理
#     for msg in msgs:
#         print(msg)
#呼叫函式，傳入三個參數資料
# say("Hello","I'm","groot")

#參數的預設資料
# def power(base,exp=0):
#     print(base**exp) #**平方
# power(3,2)
# power(4)

#使用參數名稱對應
# def divide(n1,n2):
#     print(n1/n2)
# divide(2,4)
# divide(n2=2,n1=4)

#無限/不定 參數資料
def avg(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns)) #len(ns)列表的長度，ns是一個Tuple
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)