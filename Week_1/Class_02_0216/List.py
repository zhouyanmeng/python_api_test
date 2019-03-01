'''
#>1空列表t=()
#>2列表里面的元素类型可以是任意类型，不同的数据类型之间用逗号隔开
#>3列表是有下标的，正序/反序编号都支持，取值方式同字符串
#>3.1单个取值  元组名[索引号]  索引从0开始
#>3.2切片  元组名[m:n:k]  [索引头:索引尾：步长]
#>4嵌套取值，字段里面还有字典:::层级定位
#4.1元组，元素可以包含列表，字典
1>不能变动元组的值
2>不能变动元组里面元素的值
3>可以变换元组里列表里面元素的值
4>不能变动元组里面列表的值
#4.2列表：元素可以包含元组，列表，字典，
1>可以变动元组的值
2>可以变动列表的值
3>不可以变动列表元组的元素值
4>可以变动列表元素的值
#>5列表是不可变类型,是有序的
'''
t=((1,2,3),['JAVA','python'])
#t[0]='b'#TypeError: 'tuple' object does not support item assignment
print(t)
# t[1]='JDBC'#TypeError: 'tuple' object does not support item assignment
print(t)
# t[0][-1]='aa'###TypeError: 'tuple' object does not support item assignment
print(t)
t[-1][-1]='JDBC'
print(t)

l=[(1,2,3),['JAVA','python']]
# l[0]='asdv'
# print(l)
# l[0][0]='abs'#TypeError: 'tuple' object does not support item assignment
# print(l)
# l[1]='hahahah'
# print(l)
l[1][1]='woquni'
print(l)






#>1空列表list[]
l=[]
print(type(l))
print("1*******************************")
#>2元组里面的元素类型可以是任意类型，不同的数据类型之间用逗号隔开
l=[1,0.01,True,'Hello',(1,2,3),[1,2,3]]
print("2*******************************")
#>3列表是有下标的，有索引，正序/反序编号都支持，取值方式同字符串
l=[1,0.01,'Hello',True,(1,2,3),[1,2,3]]
#  0   1    2       3       4       5
#  -6  -5   -4     -3     -2      -1
#>3.1单个取值  元组名[索引号]  索引从0开始
print(l[-1])
print(l[3])#True
print("3*******************************")
#>3.2切片  元组名[m:n:k]  [索引头:索引尾：步长]
l=[1,0.01,'Hello',True,(1,2,3,666,'python'),['python','JAVA','ruby']]
s=(l[-1])
print(s)##['python', 'JAVA', 'ruby']
print(s[::-1])##['ruby', 'JAVA', 'python']

s=(l[-1])
print(s[-2][::-1])##['python', 'JAVA', 'ruby']
print("4*******************************")

#>4可以重新赋值,是有序的
###列表与元组并不是绝对的不能修改


l=[1,0.01,'Hello',True,(1,2,3,666,'python'),['python','JAVA','ruby']]
l[2]='周艳朦'
print(l)
print("5*******************************")

###修改列表里面的元组
t=(1,0.01,'Hello',True,(1,2,3,666,'python'),['python','JAVA','ruby'])
print(t[-2])
print(t[-1])
# t[4]='helloworld'
print(t)
print("6*******************************")

###列表里面改列表的值
l=[1,0.01,'Hello',True,(1,2,3,666,'python'),['python','JAVA','ruby']]
# print(t[4])
# print(t[4][::1])
print(t)
t[-1][-1]='shadow'
# print(t)
print("7*******************************")

##列表可以删除，元组不可以删除，是绝对的吗？？？不是绝对的
l=[1,0.01,'Hello',True,(1,2,3,666,'Hello'),['python','JAVA','ruby']]

l[4]='柠檬茶'
print(l)####列表里面的元素是可以修改的
###可以修改列表里面的元素，但是不能修改列表里面的元组内部的元素
# l[4][0]='柠檬茶'
print(l)###TypeError: 'str'/’tuple' object does not support item assignment
print("8*******************************")

###元组里面可以放列表
t=(1,0.01,'Hello',True,(1,2,3,666,'python'),['python','JAVA','ruby'])
print(t)
print(t[-1])

##元组里面的元素值不能修改，无论是列表还是字典
#t[-1]=9###TypeError: 'tuple' object does not support item assignment
##元组里面的字典/列表的具体元素的值可以修改
t[-1][-1]='JBCD'
print(t)
print("9*******************************")


###为什么有的数据能直接输出，有的数据不能直接输出？？？？

t=[1,0.01,'Hello',True,(1,2,3,666,'Hello'),['python','JAVA','ruby']]
print(t.index('Hello'))###Hello所在的索引位置
t.reverse()###倒叙
print(t)
# print(t.reverse())#函数以及函数的返回值

print("10*******************************")


