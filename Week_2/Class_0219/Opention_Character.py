#######在python中非0非空数据，true  1；；；零空数据  False

####运算符
##1算术运算符    + - *  /  % 取余（模运算）  //地板除（不要小数，只要整数）
a=10
b=3
print(a/b)##浮点   为啥是16位小数？？
print(a//b)##3
print(a%b)##1   余数
print("1.1*************************")
a=0.1
b=0.3
c=0.2
print(a+b-c)##0.2
print(a+b-c+a)##0.30000000000000004  #Python是动态语言，运算的精确度不确定##建议不用浮点数
##想使用，格式化输出
print(round(a+b-c+a,1))##目标数字，精确位数
#round(目标数值，精确的小数位数)
print("1.2*************************")

##判断奇偶数，会用到%
#x%2==0,x是偶数
#x%2!=0,x是奇数

##2赋值运算符::=  +=,-+
x=3
print(x)
print("2.1*************************")
x+=-2##x=x+2
print(x)##1
print("2.2*************************")

x=2
x+=2##x=x+2
print(x)##5
print("2.3*************************")
x=3
x-=2##x=x-2
print(x)##1
print("2.4*************************")
##python从上往下运行，上一个的输出可以作为下一个的输入

##3比较运算符：：6种：：== 、!=、 > 、<、 >=、 <=   python中没有约等于
#运算结果是布尔值  True False
x=5
y=2
print(x>=y)#True
print(x<y)#False
print(x==y)#False
print("3.1*************************")
x='GET'
y='get'
print(x==y)#False  字符串区分大小写 字符串可以比较的
print(x.lower()==y)##True
print(x==y.upper())##True
print("3.2*************************")
##赋值是=   比较==

##4逻辑运算符：：and  or  not
###计算优先级：：not>and>or
#运算结果是布尔值   True False
##and  两边为真才为真  真真为真，一假则假
##or 一边为真就为真    假假为假，一真则真

a=5
b=0
print(a>0 and b>0)##0 Flase
print(a>0 and b==0) ##0 True
print(a>=5 and b==0) ##0 True
print(a>=5 or b==0) ##0 True
print("4.1*************************")
print(a>=5 or not b==0) ##0 True   not b==0
print(a>5 or not b==0) ##0 False   not b==0
print(a>5 and not b==0) ##0 False   not b==0
print("4.2*************************")
##5成员运算符::;in  not in   用于 字符串，元组，列表，字典
#运算结果是布尔值   True False
s='python'
print('p' in s)#True
print('p' not in s)#False
print('P' in s)#False
print('P' not in s)#True
print("5.1*************************")
s=('python',9,0.33)
print('p' not in s)#True
print('p' in s)#False
print('p' in s[0])#True
print("5.2*************************")

d={'age':20,'name':'七月'}####字典默认判断的是通过key
print(20 in d)##False
print('age' in d)##True
print('age' in d.keys())##True
print(20 in d.values())##True
print(d['age'])#20
#print(20 in d['age'])##TypeError: argument of type 'int' is not iterable

print("5.3*************************")
print(d.values())
print(d.keys())
print("5.4*************************")

##非空非零数据，#空 0 False
###a=0就是false  1就是True

##and关联的左右，，and的左边是假的，那结果就是假的
##or关联的左右，or左边的值是假的，那结果就看右边


a=5
b=10
print(a and b)##10

a=0
b=10
print(a and b)##0

a=1
b=10
print(a and b)##10

a=20
b=10
print(a and b)##10

a=5
b=10
print(a>0 and b<0)##False