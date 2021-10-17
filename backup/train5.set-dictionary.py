#集合的運算
#s1={3,4,5}
#print(3 in s1)
#print(10 not in s1)

#s1={3,4,5}
#s2={4,5,6,7}
#s3=s1&s2 #交集:取兩個集合中. 相同的資料
#s3=s1|s2 #聯集:取兩個集合中的所有資料. 但不重複
#s3=s1-s2 #差集:從s1中減去和s2重複的資料
#s3=s1^s2 #反交集:取兩個集合中. 不重複的資料
#print(s3)

#s=set("Hello") #把字串中的字母拆解成集合:set(字串)
#print(s)
#print("h" in s)

#字典的運算:key-value配對
#dic={"apple":"蘋果","bug":"蟲"}
#dic["apple"]="小蘋果"
#print(dic["apple"])

#print("apple" in dic) #判斷key是否存在，判斷的對象為key
#print("bug" not in dic)

#dic={"apple":"蘋果","bug":"蟲"}
#print(dic)
#del dic["apple"] #刪除字典中的key-value pair
#print(dic)

dic={x:x*2 for x in [3,4,5]} # 從列表的資料產生字典
print(dic)