####运算符
####1算术运算符：：+-*/%
#%取余运算：：无法整除的时候取余
##用来做啥呢：：判断一个数，是否是奇数，还是偶数
a=7
if a%2==0:
    print('a是偶数')
else:
    print('a是奇数')
print('1。1***************************')
print(1+2)#3
print(1-2)#-1
print(1*2)#2
print(1/2)#0.5
print(1%2)#1
print('1.22***************************')
##我们在哪里还用过+  （1）字符串拼接，（2）列表的合并
####2赋值运算符：：=,+=,-=
###+=,-=在if，for循环中大量使用
a=1##1存在内存里面，a相当于1的引用
b=2
c=a+b
print(a)
print(c)

a=1
a=2
print(a)##2
print('2.1***************************')
a=3
a+=3####等同于  a=a+3
print(a)###6

a=3
a-=1
print(a)###2
print('2.2***************************')

####3比较运算符：：>,<,==,>=,<=,!=
##运算结果是boolen：True/False
###==判断==左右2边的值是否相等
print(3==4)##False
print(3==3)##True
print(3!=4)##True
print(3>4)##False
print(3<4)##True
print(3>=4)##False
print(3<=4)##True
print('get'=='GET')##False  str区分大小写
print('get'.upper()=='GET')##True
print('get'=='GET'.lower())##True
print('3.1***************************')
print()
####4逻辑运算符：：and  or  not
#and 且   左右两边同时满足才为真
# or 或   左右两边有一边满足即可
###and的优先级高于or，，，出现多个比较，先and再or，再算not
a=10
b=-5
c=0
print(a>0 and b>0)##False
print(a>0 or b>0)##True
print(a>0 and b>0 and c>0)##False
print(a>0 and b>0 or c>0)##False
print(a>0 or b>0 and c>0)##True
print(a>0 or b>0 or c>0)##True
print('4.1***************************')
####5成员运算符：：in  not in
##运算结果：：布尔值；True/False
##使用与
str1='Hello'
print('H' in str1)##True
print('h' in str1)#False   字符串
print('5.1***************************')
t=[1,0.0089,'Hello',666,9.09]
print('h' in t)#False   列表   元素元素，列表用,区分
print('H' in t[2])#True   列表   元素元素，列表用,区分
print('5.2***************************')
d={'name':'xiaoxx','age':22}###字典里面判断的是key不是value
print(22 in d)#False
print(22 not in d)#True
print('age' in d)#True
print('age' not in d)#False
print('5.3***************************')