####if
##1 if else必须要加条件表达式 lese不能加任何条件
##2什么情况擦会执行if elif的子代码？？只有当条件满足为True时
##3非0 和非空数据表示True，为0和为空的数据表述False（非常重要）
#3.1只要返回的值是True或者False都可以作为if或者elif后面的条件表达式
##4嵌套循环：第一层判断结束再进入第二层

##练习：从控制台获取一个成绩，根据成绩判断
#如果>80 优秀 >70良好  >=60及格   <60不及格
#数据的范围是0-100
# score=input("请输入小明的成绩：")###利用intput从控制台获取的都是字符串类型的数据
# print(type(score))
# print(score)
# score=float(input("请输入小明的成绩："))#强制转换类型
# # print(type(score))
# if score>100 or score<0:
#     print("输入的数据不在1-100之间")
# elif score>80 and score<=100:
#     print("优秀")
# elif score>70 and score<=80:
#     print("良好")
# elif score>=60and score<=70:
#     print("及格")
# else:
#     print("不及格")
#print("1********************")
# score1=input("请输入小明的成绩：")  # 强制转换类型
# if score1.isdigit():
#     score1=float(score1)
#     if score1 > 100 or score1 < 0:
#         print("输入的数据不在1-100之间")
#     elif score1 > 80 and score1 <= 100:
#         print("优秀")
#     elif score1 > 70 and score1 <= 80:
#         print("良好")
#     elif score1 >= 60 and score1 <= 70:
#         print("及格")
#     else:
#         print("不及格")
# else:
#     print("输入的数据类型有错")
#     print("2********************")



###看书
###1猜数字
number=50
Guess=int(input("请输入一个数值"))
if  Guess>number:
    print("您猜的值太大了！！！")
elif Guess<number:
    print("您猜的值太小了！！！")
elif Guess==number:
    print("您猜对了")
else:
    print("空")



