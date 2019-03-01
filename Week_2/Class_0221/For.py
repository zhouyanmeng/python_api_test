####for循环   永远不会进入死循环
#for循环的语法
#for 变量名 in 数据：
#   循环体
####1遍历循环  每个挨个去访问
L=['angelbaby','cindy','sunny','jolin']
for item in L:##按顺序访问L里面的数据，有几个就访问几个
    print("鬼迷心窍！！！！")
    print('item的值{}'.format(item))
print("1**************")

###打印L里面的每一个元素
L=['angelbaby','cindy','sunny','jolin']
for item in L:##按顺序访问L里面的数据，有几个就访问几个
    print(item)
print("1**************")

###到底用哪个循环？？
#如果确定循环次数，用for
#如果不确定循次数，而是要达到某个指定的条件后才停止，用while
##in 后面的数据类型：字符串，字典，元组，列表

##字典的key要求：不可变，不可重复
##不可变：数字，元组，字符串
# s=[]
# for item in '12345':
#     sir=input("请输入你的名字：")
#     s.append(sir)
# print(s)
# print("2**************")

for item in '12345':
    print(item)
print("3**************")

d={"name":'lisa','age':24,'salary':'12K'}
for item in d.values():###拿到字典里面的values
    print(item)
print("4**************")
d={"name":'lisa','age':24,'salary':'12K'}
for item in d.items():###拿到字典里面的values
    print(d[item])
print("5**************")

d={'name':'lisa','age':24,'salary':'12K'}
for item in d.items():###拿到字典里面的values
    print(item)
print("5**************")


###嵌套循环
