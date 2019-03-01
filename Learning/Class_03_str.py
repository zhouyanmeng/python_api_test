'''
字符串方法

1索引取值  函数名[索引]
2切片：[m,n,k]
3格式化输出：占位符%s,    {}.format
4函数：
upper()
lower()
swapcase()::切换大小写
split()
replace()::替换
find（）：查找
'''


####1字符串string str
a='hello python13'
print(type(a))
print(a)
print('1*****************************')
####2常规用法::字符串的取值，切片
#1）字符串里面的元素：单个字符算一个元素（数字，字母，符号，中文）
a='hello python13'#14个字符
#2）统计字符串长度len()
a='hello python13'#14个字符
print(len(a))
print(len('hello python13'))
print('2*****************************')
#3)如何取值：：字符串取值是根据索引来的，索引是什么呢：：：是字符串元素的编号，从0开始，用[]
#取值方式  变量名[索引]
#从前往后编号是0123456（正序，从左往右）
#从后往前编号是-1，-2，-3（反序，从右往左）
a='hello python13'#14个字符
print(a[13])####打印hello python13字符串里面的3     从前往后
print(a[-1])####打印hello python13字符串里面的3     从后往前
print(a[-14])####打印hello python13字符串里面的3     从后往前
#print(a[-15])####打印hello python13字符串里面的3     从后往前  抛错 string index out of range
print(a[6])####打印hello python13字符串里面的p
print('3*****************************')
#4)切片：：取部分：：：变量名[m:n:k]::开始，结束，步长   m从哪个位置（位置就是索引）开始切  n到哪里结束   k隔几个切一刀
#m从哪里开始取值的索引位置  n取值结束的位置n-1，取值不包含  k 取值隔开的距离   取左不取右
a='hello python13'#14个字符
print(a[0:13:1])#hello python1
print(a[0:14:1])#hello python13
print(a[0:14:3])#hlph1
print('4*****************************')
print('4*****************************')

#####实例###############
##1请把偶数的元素打印出来
print(a[0:14:2])
print(a[0:13:2])
print('5*****************************')
a='hello python13y'#15个字符
##2请把偶数的元素打印出来
print(a[0:15:2])
print(a[::2])###从头去到尾
print('6*****************************')
##3请把a字符串利用切片，实现倒叙输出
a='hello python13y'#15个字符
print(a[::-1])
print(a[14::-1])
print(a[-1:-16:-1])
print('7*****************************')
####3格式化输出::::占位符%d   %s  %f
##%d 整型  %s str  %f  浮点型  %0.2f 2位小数输出
##任何地方都可以放%s,但是如果数据类型是str的时候，只能是%s,,,,%d,%f是绝对不行的
S_1="hello"
S_2="World"
S_3=30
print(S_1+S_2)
print((S_1+S_2+str(S_3)))###str转换类型
print(S_1+S_2,S_3)###用逗号链接不同的数据类型
print('8*****************************')

age=22
height=170.34
hobby='睡觉'
print(type(age))
print(type(height))
print(type(hobby))
#--------格式化输出方法1，，，%s+逗号(占位符)，万能的是%s--------------
print('''年龄:%d,身高:%f,爱好%s'''%(age,height,hobby))
print('''年龄:%d,身高:%0.2f,爱好%s'''%(age,height,hobby))###2位小数
print('''年龄:%d,身高:%0.9f,爱好%s'''%(age,height,hobby))###9位小数
print('''年龄:%s,身高:%0.9f,爱好%s'''%(age,height,hobby))###整型的可以放str
print('''年龄:%s,身高:%d,爱好%s'''%(age,height,hobby))###取整
print('''年龄:%s,身高:%s,爱好%s'''%(age,height,hobby))###通杀
print('*****************************')
#--------格式化输出方法2::{}.format--------------要不全部编号，要不全部不编号
print('''年龄:{},身高:{},爱好{}'''.format(age,height,hobby))###按照顺序取值
print('''年龄:{0},身高:{1},爱好{2}'''.format(age,height,hobby))
print('''年龄:{0},身高:{0},爱好{0}'''.format(age,height,hobby))###编号是几，就去后面的第几个值
print('年龄:{},身高:{},爱好{}'.format(age,height,hobby))###按照顺序取值
print('9*****************************')
###''''''三个单引号有换行的作用
####4函数
##1）切换大小写upper()，lower()
a='hello python13'
print(a.upper())##大写
print(a.lower())##小写
print('10*****************************')
##2)大小写互换 swapcase()
s=''
b='Hello PytHon13'
print(b.swapcase())
print('11*****************************')
########将某一个字符变成大写
for i in range(len(b)):
    if i==11:
        s+=b[i].upper()
    else:
        s+=b[i]
print(b)
print('12*****************************')
######replace()替换的方法
s=''
c='Hello PytHon13'
s=c.replace('y','@')
print(s)
print('13*****************************')
##3)replace()替换的方法   ####只找有的，找到所有的全部替换，找不到的不替换，不报错
####不写数字，全部替换，写数字就替换几次，从左往右开始替换
c='Hello PytHon13'
s=c.replace('o','T')####全部替换
print(s)
print('14*****************************')

c='Hello PytHon13'
s=c.replace('o','U',1)###按照顺序替换，输入数字字，替换几次
print(s)
print('15*****************************')
#4）find查找元素：：：单个字符如果找到了，返回的是遇到的第一个元素的所有的值，后面的不管
##子字符串  长度大于1，如果找到了，就返回子字符串所在第一个元素的索引的位置
c='Hello PytHon13'
print(c.find('l'))###找到，返回的是索引的值，，返回遇到的第一个索引的值
print(c.find('W'))###没找到，返回-1
print(c.find('Hello'))####单个字符，，，，遇到的第一个元素的索引值
print(c.find('Pggg'))####没找到
print('16*****************************')
#5）数据类型：布尔值：：：True   False
#6)其他函数
c='Hello PytHon13'
print(c.capitalize())##首字母大写
print(c.count('o'))###字符出现几次
print(c.index('l'))###第一次遇到的元素的索引
#print(c.index('W'))###找不到###substring not found
print(c.isdigit())####判断否是数字
d='1'
print(d.isdigit())####判断否是数字,但是这个d的类型还是str，只是判断里面的内容是不是纯数值

print(c[0].isupper())###True
print(c[0].islower())###False
print('@'.join(a))####每隔一个插入一个@####h@e@l@l@o@ @p@y@t@h@o@n@1@3
print('16*****************************')
#7）切割 split
c='Hello PytHonh13'
print(c.split(' '))###['He', '', 'o PytHonh13']
print(c.split('P'))###切割的元素不打印出来###['He', '', 'o PytHonh13']
print(c.split('l'))###切割的元素不打印出来####['He', '', 'o PytHonh13']
print(c.split('h',2))###指定切割的次数，不够切不报错['Hello PytHon', '13']
print('17*****************************')

##切片与切割的区别
#切片：返回字符串，切割返回：列表