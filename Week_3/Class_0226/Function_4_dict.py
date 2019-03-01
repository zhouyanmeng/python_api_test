####字典内置函数

d={'name':'lemon','age':22,'score':99.99}
####增  赋值运算  key：唯一不可变
##字典名[key]=value,如果key是已经存在的，那就是修改，
##如果key不存在，那就是新增
d['sex']='男'
print(d)
####改   key是唯一的
d['name']='summer'
print(d['name'])
print(d)

d={'name':'lemon','age':22,'score':99.99}
####删
#1>pop   删除键值对，通过key
d.pop('name')
print(d)

#2>随机删除
d.popitem()##随机删除

#3>clear  清空，变成空子点
# d.clear()

####查 字典名[key]


####copy

d={'name':'lemon','age':22,'score':99.99}
####items  返回键值对
res=d.items()
print(res)

####get  根据key取值，里面穿的参数是key,,输出的是对应的key的value值
res=d.get('name')
print(res)


####update
d.update()
print(d)