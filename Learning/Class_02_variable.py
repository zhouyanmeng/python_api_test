####1变量名：：标识符里面的一种：：自己命名一个标识符，存储一个数据，就叫变量名
x=1
y=x*5
print(y)###x是变量，y是因变量
print('********************')
##数字，字符串，列表，元组，字典，集合 等都是各种类型的数据
#数字：int long float complex（整型int，浮点型float）
#字符串：str：string：：成对的单引号，双引号，三引号括起来的内容都是字符串
a=1
b=1
print(id(a))
print(id(b))##id判断内存地址
print('********************')

a=1
a=2
print(id(a))
print('********************')

##整型int,浮点型float  type()：判断数据类型
a=5
print(a)
print(type(a))##int
print('********************')
a=1.2
print(a)
print(type(a))##float
print('********************')

##字符串string
a='10'
b="asd"
c='''12.00000'''
d="""asdsd"""
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(a)
print(b)
print(c)
print('********************')

#如果你的字符串必须包含单引号，最外层用双引号， 同理，如果你的字符串必须包含双引号，最外层用单引号
x='"Hello"'
print(type(x))
print(x)####打印“hello”