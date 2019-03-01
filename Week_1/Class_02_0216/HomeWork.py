'''
1：把字符串 元组 列表 字典的数据类型特征画一个思维导图，并提交作业
Excel总结
2：观察这个数据，输出到控制台，说出你发现的问题并且给出合理的解释

d={"name":'华华',
'hobby':'学Python',
'age':18,
'score':{'en':120,'math':99.99,'ch':'A'},
 'friend':['bay max','小CC','如意'],
 True:'good_man',
 0.02:'python',
False:'这个value对应的key是布尔值',
(1,2,3):'我就是元组大大！！！',
0:'这是真爱呀', 1:'socre is 99.9'}

3：拓展：利用input函数（自行去拓展该函数的用法），获取一个日期，日期格式如下所示：20190216，然后针对输入的这个日期，进行一些处理后，输出：2019年2月16日   这个字符串到控制台


'''

#2
# d={"name":'华华',
# 'hobby':'学Python',
# 'age':18,
# 'score':{'en':120,'math':99.99,'ch':'A'},
#  'friend':['bay max','小CC','如意'],
#  True:'good_man',
#  0.02:'python',
# False:'这个value对应的key是布尔值',
# (1,2,3):'我就是元组大大！！！',
# 0:'这是真爱呀', 1:'socre is 99.9'}
# print(d)

#2.1字典的存储方式： key,value组成
#2.2字典的标识：{}
#2.3字典key类型：数值，浮点，字符串，布尔型，元组，，，，value支持常用的7种类型：数值，浮点，字符串，布尔型，元组，列表，字典
#2.4字典的输出是无序的
#2.5,当同时出现key值是0/True.1/False的时候，key取值取第一个出现的key值，values值取后出现的key对应的value值：：原因：：True=0，False=1



#3：拓展：利用input函数（自行去拓展该函数的用法），获取一个日期，日期格式如下所示：20190216，
# 然后针对输入的这个日期，进行一些处理后，输出：2019年2月16日   这个字符串到控制台


import time
# print(time.strftime("%Y%M:%D"))
# print(time.strftime("%H:%M:%S"))
##localtime = time.localtime(time.time())
#>1控制台输入输出
a=input("请在控制台输入一个日期并且打印出来：")
# print(a)
# # #>2个书画处理输出：2019年2月16日
# # print(a[0:4:1])
# # print(a[4:6:1])
# # print(a[4:8:1])
print('{}年{}月{}日'.format(a[0:4:1],a[4:6:1],a[6:8:1]))
print('%s年%s月%s日'%(a[0:4:1],a[4:6:1],a[6:8:1]))

print()
input()##input函数获取到的数据类型：：字符串










