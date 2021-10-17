#break example
# print("break example :")
# n=0
# while n<5:
#     if n==3:
#         break #符合 if 條件跳出迴圈
#     print(n) #印出迴圈中的n
#     n+=1
# print("最後的 n:",n) # 印出迴圈結束後的n

#continue example
# print("continue example :")
# n=0
# for x in [0,1,2,3]:
#     if x%2==0: # %:取餘數，x是偶數
#         continue  #符合餘數=0直接回到for，進下一個迴圈不會跑下去
#     print(x) #印出奇數
#     n+=1  #會執行兩次
# print("最後的n:",n) #印出 2 因為n只加了兩次

#whlie else example
# print("whlie else example :")
# n=1
# while n<5:
#     print("變數n的資料式:",n)
#     n+=1
# else:
#     print(n) #結束迴圈之前，印出5 

#for else example
# print("for else example :")
# for c in "Hello":
#     print("逐一取得字串中的字元",c)
# else:
#     print(c) #結束迴圈之前，印出o

#else simple example
# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum) #印出0+1+2+....+10=sum

#綜合範例:找出整數平方根
#輸入9 得到3
#輸入11 得到"沒有"整數的平方根
n=input("輸入一個正整數:")
n=int(n) #input轉成數字   #47&48合併 n=int(input("輸入一個正整數"))
for i in range(n): # i 從0~n-1
    if i*i==n: #1*1 2*2 3*3 從0~n-1一個一個判斷有沒有符合條件，有符合print
        print("整數平方根",i)
        break #用 break 強制結束迴圈，不會執行 else 區塊
else:
    print("沒有整數平方根")