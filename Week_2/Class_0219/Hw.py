# 1.根据你输入的数据，来进行判断学生的成绩。输入数据函数：input()
# score=input("请输入学生成绩：")
# while True:
#     try:
#         score=int(score)
#         break
#     except:
#         score=input("输入错误，成绩只能为数字，请输入成绩：")
# if 90<score<=100:
#     print("优秀")
# elif score>100:
#     print("100分总分，您输入的成绩有误！！！")
# elif 80<score<=90:
#     print("良好")
# elif 70<score<=80:
#     print("一般")
# elif 60<=score<=70:
#     print("及格")
# elif score<60:
#     print("不及格，加油啦！！！")
# else:
#     print("您输入的成绩类型不合法！！！")


# 2、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
# #如果购买金额大于100元会给20%折扣。
# 编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格
# price=input("请输入购买金额：")
# while True:
#     try:
#         price=float(price)
#         break
#     except:
#         price=input("输入错误，单价只能为数字，请输入单价：")
# if 50<=price<=100:
#     price=price-price*0.1
#     print("折扣是10%")
#     print("折扣以后您应付的总价是：{}".format(round(price,2)))
# elif price>100:
#     price = price - price * 0.2
#     print("折扣是20%")
#     print("折扣以后您应付的总价是：{}".format(round(price, 2)))
# elif price<50:
#     print("无折扣，再去买点吧！！")
#     print("折扣以后您应付的总价是：{}".format(round(price, 2)))




# 3、输入一个数，判断一个数n能同时被3和5整除

# n=input("请输入一个数字：")
# while True:
#     try:
#         n=float(n)
#         break
#     except:
#         n=input("请输入一个数字！！！")
# if n%3==0:
#     #print("这个数能被3整除 ！")
#     if (n%5==0):
#         print("这个数既能被3整除，也能被5整除 ！")
#     else:
#         print("这个数能被3整除，但是不能被5整除 ！")
# else:
#     if (n%5==0):
#         print("这个数能被5整除，但是不能被3整除！")
#     else:
#         print("这个数既不能被3整除也能被5整除 ！")

# 4、输入一个年份，输出是否为闰年，
# 闰年条件：能被4整除但不能被100整除，或者能被400整除的年份都是闰年
# year=input("请输入一个年份：")
# while True:
#     try:
#         year=int(year)
#         break
#     except:
#         year=input("请输入一个年份！！！")
# if year%4==0 and year%100!=0:
#     print("您输入的年份：{}是闰年".format(year))
# elif year%400==0:
#     print("您输入的年份：{}是闰年".format(year))
# else:
#     print("您输入的年份：{}不是闰年".format(year))

# 5、一个 5 位数，判断它是不是回文数。
# 即 12321 是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息。01210
# number=input("请输入一个5位数：")
# while True:
#     try:
#         number=int(number)
#         break
#     except:
#         number=input("请输入一个5位数：！")
# # for number in range(10000,100000):
# a=number//10000
# b=(number%10000)//1000
# c=(number%1000)//100
# d=(number%100)//10
# e=number%10
# # print(a)
# # print(b)
# # print(c)
# # print(d)
# # print(e)
# if a==e and b==d and a!=0:
#         print("您输入的数:{}是回文数".format(number))
#     #print("您输入的数:{}不是回文数".format(number))
# else:
#     print("您输入的数:{}不是回文数".format(number))

##切片
number=input("请输入一个数字：")
if number[0]==number[4] and number[1]==number[3]:
    print()
else:
    print()
# 6、利用random函数生成随机整数，
# 从1-9取出来。然后输入一个数字，来猜，如果大于，则打印bigger。
# 小了，则打印less。如果相等，则打印equal
# #
# import random
# a=random.randint(1,10)
# # print(a)
# number=input("请输入一个数字：")
# while True:
#     try:
#         number=int(number)
#         break
#     except:
#         number=input("请输入一个数字：")
# if a>number:
#     print("bigger!")
# elif a<number:
#     print("less!")
# elif a==number:
#     print("equal!")


# 拓展题：
# 登录功能：用户名和密码存在{'name':'huahua','pwd':'123456'}字典中，
# 通过控制台输入用户名和密码判读是否正确，然后给出对应的提示消息：
# 登录成功 OR 用户名或密码错误
# d={'name':'huahua','pwd':'123456'}
# # print(d['name'])
# # print(d['pwd'])
# name=input("用户名：")
# pwd=input("请输入密码：")
# if name==d['name']:
#     if pwd==d['pwd']:
#         print("用户名密码正确，登录成功！")
#     else:
#         print("密码错误，请重新输入！")
# else:
#     print("用户名错误，请重新输入！")