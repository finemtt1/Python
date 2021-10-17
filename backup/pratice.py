# #問答程式 引入方法1
from question import Question #從question.py引入class:Question 其他不引入
#import question #question.py全部引入

test = [
    "1+3=?\n(a) 2 \n(b) 3 \n (c) 4 \n",
    "1公尺等於幾公分?\n(a) 10 \n(b) 100 \n (c) 1000 \n",
    "香蕉是甚麼顏色?\n(a) 黑色 \n(b) 黃色 \n (c) 白色\n\n"
    ]
questions=[
    Question(test[0],"c"),
    Question(test[1],"b"),
    Question(test[2],"b")
]

def run_test(questions):
    score=0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score+=1
    print("get "+str(score)+"分","共"+str(len(questions))+"題")
run_test(questions)

#問答程式 引入方法2
import question as qq #question.py全部引入

test = [
    "1+3=?\n(a) 2 \n(b) 3 \n (c) 4 \n",
    "1公尺等於幾公分?\n(a) 10 \n(b) 100 \n (c) 1000 \n",
    "香蕉是甚麼顏色?\n(a) 黑色 \n(b) 黃色 \n (c) 白色\n\n"
]
#呼叫 question.py裡面的Question類別
questions=[qq.Question(test[0],"c"),
    qq.Question(test[1],"b"),
    qq.Question(test[2],"b")
]
def run_test(questions):
    score=0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score+=1
    print("get "+str(score)+"分","共"+str(len(questions))+"題")
run_test(questions)

#用import question 呼叫時需把question.py加上，qq.Question
#用from question import Question，已經指定question.py裡面的Question類別呼叫，因此只要Question