####if条件判断语句
#语法
###1非常简单的条件语句
#if后面可以放：逻辑/比较/成员  各类数据类型 就是不能放赋值
'''###语句的层级，用冒号来进行控制， 层级用缩进控制 tab
if  条件：#if后面的条件运算结果是布尔值，并且成立
    代码###只有当if后面的条件成立的时候，才会执行if里面的代码块
'''
age=10
if age==10:##比较运算，运算值都是布尔值
    print("小丫头今年10岁")
print("1*********************")
age=10
if 1:##比较运算，运算值都是布尔值
    print("小丫头今年10岁")
print("2*********************")
if 9:##比较运算，运算值都是布尔值
    print("小丫头今年10岁")##执行，非0非空表示true
print("3*********************")
#######在python中非0非空数据，true  1；；；零空数据  False
s=[]
if s:
    print("小丫头今年10岁")###不执行
print("4*********************")

###2 if  else
age=18
if age>=18:
    print("恭喜你成年啦")
else:
    print("你还是个孩子")
print("5*********************")

#嵌套
age=18
if age>=18:
    print("恭喜你成年啦")
    if age>=40:
        print("中年大叔")
    else:
        print("小鲜肉")
else:
    print("你还是个孩子")
print("5*********************")

###3 多重判断语句  if  elif  else
##if是必须要有的  elif  else可有可无，，else一定是最后的
#1>elif的个数不限定
#2>他的分支顺序一定是  if...elif...else,,else一定在最后

# score=int(input("请输入整数类型的数值："))
# if score>100:
#     print("总分就100，怎么得的分数？？")
# elif 90<=score<=100:
#     print("优秀")
# elif 80<=score<90:
#     print("良好")
# elif 70<= score <80:
#     print("中")
# elif 60<=score<70:
#     print("及格")
# else:
#     print("不及格")



#####
n=int(input("请输入一个数值："))
if n%3==0:
    if(n%5==0):
        print("这个数{}".format(n),"可以同时被3和5整除")
    else:
        print("这个数只能被3整除")
elif (n%5==0):
    print("这个数能被5整除")
else:
    print("这个数既不能被3整除，也不能为5整除")
