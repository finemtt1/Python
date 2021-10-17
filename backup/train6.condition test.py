name=input("使用者ID:")
password=input("密碼:")
print("哈囉"+name+"\n"+"你的密碼:"+password+" 請確認")
x=int(input("請輸第一個數字:")) #int 把字串轉成整數
y=int(input("請輸入第二個數字"))
z=input("請輸入運算符號+,-,*,/:")
if z=="+":
    print(x+y)
elif z=="-":
    print(x-y)
elif z=="*":
    print(x*y)
elif z=="/":
    print(x/y)
else:
    print(gg)