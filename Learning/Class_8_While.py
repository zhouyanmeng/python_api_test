####while循环用来重复执行某个操作：当条件为真时，执行代码，未假时，退出循环
#语法 while 条件表达式：
#           执行代码

#猜数字
# number=23
# count=5
# while count>0:
#     guess=int(input("请输入一个整数："))
#     if guess==number:
#         print("恭喜你猜对啦！！")
#     elif guess>number:
#         print("您猜的太大了。。。")
#     else:
#         print("您猜的太小了。。。")
#     count=count-1####关键

# j=3
# i=3
# while j>0:
#     if i>0:
#         print("*****")
#         i=i-1
#     j=j-1


for i in range(0,5):
    for y in range(0,5-i):
        w = ' '
        print(w,end="")
    s = '* ' * i
    print(s)



#1输出0-100累计和
s=0
for i in range(0,101):
    s=i+s
print(s)

#2打印a=[5,7,8,10,23,45]
a=[5,7,8,10,23,45]
print(a[::-1])

#3if

# price=int(input("请输入一个价格："))
#
# if price>100:
#     print("给您的折扣是20%")
#     price1=price*(1-0.2)
#     print("折扣后的价格是%d"%(price1))
# elif 50<=price<=100:
#     print("给您的折扣是10%")
#     price1 = price * (1-0.1)
#     print("折扣后的价格是%d" % (price1))
# else:
#     print("无折扣")
#     price1 = price
#     print("折扣后的价格是%d" % (price1))

#
# sex = input("请输入您的性别：")
#
# if sex=='女':
#     age=int(input("请输入您的年龄："))
#     if age>=12 and age<=10:
#         print("您符合我们的条件，您被录取了")
#         i=i+1
#     else:
#         print("")
# else:
#     print("不符合")

# sex = input("请输入您的性别：")
# if sex == '女':
#     age =int(input("请输入您的年龄："))
#     if age<=12 and age>=10:
#         print("您符合我们的条件，您被录取了")
#         # i = i + 1
#     else:
#         print("抱歉，您不符合我们的条件。")
# else:
#     print("抱歉，您不符合我们的条件。")

#
# #4 while
count=10
i=0
while count>0:
    sex=input("请输入您的性别：")
    if sex=='女':
        age=int(input("请输入您的年龄："))
        if age<=12 and age>=10:
            print("您符合我们的条件，您被录取了")
            i = i + 1
        else:
            print("抱歉，您不符合我们的条件。")
    else:
        print("抱歉，您不符合我们的条件。")
    count-=1
    print("符合条件的孩子有：%s"%i)
