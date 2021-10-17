#猜數字遊戲
name=input("挑戰者:")
print("歡迎來到我的旅店"+"  "+name)
guess= None
import random
secret_num=int(random.uniform(0,100))
sum=0
limit=6
out=False
while secret_num != guess and not(out):
    sum += 1
    if sum <= limit:
        guess=int(input("0~100猜一個數字:"))
        if guess > secret_num:
            print("更小")
        elif guess < secret_num:
            print("更大")
    else:
        out = True
if out:
    print("Your Losser "+name)
else:
    print("Victory"+"\n"+"Winner "+name+"\n"+"紀錄:"+str(sum)+" 次")