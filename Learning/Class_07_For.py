##for in::字符，元组，列表，字典
##for in range::字符，元组，列表
##嵌套for循环

####for循环
#for 元素 in 数据集合：
#    执行代码

##遍历字符串
str1='Hello  World'
for i in str1:
    print(i)
print("1**********************")

##编辑列表
list=[1,2,3,4,'lemon']
for i in list:
    print(i)
print("2**********************")

##遍历元组
t=(1,2,3,4)
for i in t:
    print(i)
print("3**********************")

##遍历字典
#根据key去遍历
#根value去遍历
d={'age':18,'sex':'男'}
for i in d.keys():
    print(i)
print("4.1**********************")
for i in d.values():
    print(i)
print("4.2**********************")

####range for
#range(m,n,k)  shengc cong m--n且步长为1的整数序列
##遍历字符串
str1='Hello  World'
for i in range(len(str1)):
    print(str1[i])###遍历str1里面的每一个字符串
    print(str1)###遍历str1里的长度
print("5.1**********************")
str1 = 'Hello  World'
for i in range(len(str1)):
    print(str1)  ###str1的长度，打印这么多次str1字符串
print("5.2**********************")


##编辑列表
list=[1,2,3,4,'lemon']
for i in range(len(list)):
    print(list[i])
print("6**********************")

##遍历元组
t=(1,2,3,4)
for i in range(len(t)):
    print(t[i])
print("7**********************")

##数据范围
for i in range(1,5):###不取右值
    print(i)
print("8**********************")


####嵌套循环

list=[[1,2,3,4],[5,6,7,8]]
for i in range(len(list)):
        print(list[i])
print("9**********************")

list=[[1,2,3,4],[5,6,7,8]]
for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j])
print("10**********************")