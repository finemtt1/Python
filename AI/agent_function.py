import numpy as np


# def function suck
def suck(area_size,livetime):

    # move & suck 
    # start form (0,0)
    for i in range(area_size):
        for j in range(area_size):
            print("suck on")

    print("suck off & clean")  
    livetime += 1
    return livetime 


# def function right
def right():

    # 紀錄移動次數
    move_right = 0
    # 與Area_B的距離 假設為2 (需偵測自身的位置)
    distance = 2

    # move right to Area_B
    for x in range(distance):
        move_right += 1
    
    print("move stop")


# def function left
def left():

    # 紀錄移動次數
    move_left = 0
    # 與Area_B的距離 假設為2 (需偵測自身的位置)
    distance = 2

    # move right to Area_B
    for x in range(distance):
        move_left += 1
    
    print("move stop")


# 定義 area 資訊，簡單假設A、B一樣大
area_size = int(input("area_size:"))
Area_A = np.zeros((area_size, area_size))
Area_B = np.zeros((area_size, area_size))

# 定義 livetime strat form 0 ,
livetime = 0
livetime_end = 1000


# 建立Percept squence
Pecept_sequence = {"A_Clean":right,"A_Dirty":suck,"B_Clean":left,"B_Dirty":suck}

# 輸入Percept

A_Clean = input("True or False:")
# 判斷式 # Pecept_sequence 有偵測到東西即開始suck
if A_Clean is False:
    suck(area_size,livetime)
else:
    right()

B_Clean = input("True or False:")

if B_Clean is False:
    suck(area_size,livetime)
else:
    left()



