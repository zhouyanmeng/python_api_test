'''
字典dict{}   dictionary
#>1空字典d={}
#>2字典里面元素存储的方式是key:value  键值对
#key:不可变，唯一::int float,str,tuple,True,False:一般常用类型：str ''  ""     在后期的接口测试中，使用""
#value：数据类型不限制：int,float,boolen，str,tuple,list,sirt
#根据key，value用douhao逗号区分
#字典里面的元素类型可以是任意类型，不同的数据类型之间用逗号隔开
#1:true  0:false
#>3取值方式：：无序数据（根据key取值）  字典名[key]
字符串，列表，元组：：有序元组（根据索引值取值）
##嵌套取值：d[][]
#>4字典是无序的，列表是不可变类型,是有序的
#>5字典支持增删改    d[key]  d.pop(key)    d.popitem()
'''
#>1空字段d={}
d={}
print(type(d))
print("1**************************")
#2>字典的组成 key:value  键值对  不同的键值对之间用douhao逗号隔开
#key:不可变数据  list不可用：：：int folat boolen str tuple
##一般key都是使用字符串，  ''  ""
#value::可以是任意类型：int folat boolen str tuple list dict

##key是不会被覆盖的，Value会被覆盖
d={1:'我',0.02:'爱',True:'罗','age':22,(1,2,3):'tuple'}
print(d)###我不见了，1就是True   ##{1: '罗', 0.02: '爱', 'age': 22, (1, 2, 3): 'tuple'}
d={1:'我',0.02:'爱',False:'罗','age':22,(1,2,3):'tuple'}
print(d)###{1: '我', 0.02: '爱', False: '罗', 'age': 22, (1, 2, 3): 'tuple'}
#d={1:'我',0.02:'爱',True:'罗','age':22,(1,2,3):'tuple',[1,2,3]:'list',{1,2,3}:'dict'}
##TypeError: unhashable type: 'list'
d={1,2,'ths',True,('sfv','vsdfv')}
print(d)##3{1, 2, ('sfv', 'vsdfv'), 'ths'}
print("2.1**************************")

d={True:'我',1:'罗'}
print(d)##{True: '罗'}
d={1:'罗',True:'我'}
print(d)##{1: '我'}
print("2.2**************************")
#key:不可变数据  list不可用：：：int folat boolen str tuple
d1={"name":'zhouzhou',
   2:'int',
   4.00:'folat',
   'str':"string1",
   "str1":'string2',
    True:'Yes',
    False:'No',
    (1,2,3):'我就是元组'
}
print(d1)
print(len(d1))
print("2.3**************************")
d2={
   "name":'zhouzhou',
   "hobby":'玩',
   "score":{'en':90,'math':99.99,'ch':'A'},
   "friend":['bay max','xiaoC','如意'],
   'good_man':True
}
print(d2)
print(d2["friend"])
print(d2["friend"][0])##取名字最长的

print(d2["score"]['en'])#英语成绩取出来
print("2.4**************************")
#>3字典取值  字典名[key]
d={"name":"lemon",
   "Class_name":"Pyhon",
   "Score":[90,99,100],
   "hight":{'A':180,'B':122}}
print(d["Score"])
print("3**************************")
#>4嵌套取值，层级定位
print(d["hight"]["A"])
print("4**************************")
#>4dict也是可变数据类型，但是是无序的
d={"name":"lemon",
   "Class_name":"Pyhon",
   "Score":[90,99,100],
   "hight":{'A':180,'B':122}}
#>5支持增删改
#>5.1增加  d[key]是不存在字典里面，就是新增
#>5.2修改  d[key]是存在字典里面，就是修改
#>5.3删除  根据key去删除 pop(指定删除)
#随机删除 popitem


#新增
d['salary']='20K'
print(d)
#编辑
d["name"]='jojo'
print(d)
# #删除：指定删除
# d.pop('hight')
# print(d)
#删除，随机删除
d.popitem()
print(d)
print("5**************************")

print(d.keys())##获取字典的所有的key
print(d.values())##获取字典的所有的value


