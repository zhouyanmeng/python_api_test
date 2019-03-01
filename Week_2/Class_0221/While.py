####while循环
###什么时候用到循环：：：重复的操作

##1 while循环
#while 条件表达式：  ###条件表达句：同if：布尔值，逻辑，比较，成员，各种数据类型（非空，0，1，其他非空数据）
    ##循环体
##判断，执行，再判断，执行，在判断，执行，

##while循环的风险：容易进入死循环   那是一个bug
##如果要避免进入死循环：
#1>while后面不要是永真式，那么while后面的表达式的值要变化，不能一直是False，也不能一直是True
#2>while后面是用真式，可以用break,continue组合的方式来防止进入死循环

# while 1:
#     print("python是世界上最优美的语言！！！")
#1>while后面的值是变化的
a=0
while a<5:
    a+=1
    print("python是世界上最优美的语言！！！")###5次

a=0
while a<5:
    print("python是世界上最优美的语言！！！")###5次
    a += 1
print("1******************！！！")
#2>while后面是用真式，可以用break,continue组合的方式来防止进入死循环
#break是终止循环 continue 是结束本轮循环 继续下一轮循环
while 1:
    print("python是世界上最优美的语言！！！")
    break
print("2******************！！！")
a=0
while 1:
    a+=1
    if a<3:
        print("python是世界上最优美的语言！！！")
        continue####从while重新开始
    else:
        break##########打印2次
print("3******************！！！")

a=0
while 1:
    if a<3:
        a += 1
        print("python是世界上最优美的语言！！！")
        continue####从while重新开始
    else:
        break##########打印3次
print("4******************！！！")


####有一个空列表s=[],利用while循环，循环5次，每次询问一个人的名字，并且把名字加到列表中
###列表增加元组，可以用这个方法  列表名.append(值)
###方法1
# a=0
# s=[]
# while 1:
#     if a<5:
#         Dear=input("请输入一个名字：")
#         s.append(Dear)
#         # print(s)
#         a=a+1
#         continue
#     else:
#         break
# print(s)

# ###方法2
# a=0
# s=[]
# while a<5:
#     Dear = input("请输入一个名字：")
#     s.append(Dear)
#     a=a+1
# print(s)

###方法3
s=[]
while len(s)<5:
    Dear = input("请输入一个名字：")
    s.append(Dear)
print(s)














