####列表的内置函数
L=[0.02,100,'Hello',(1,2,3),['python',0.02]]
####增 +拼接
#1>+，两个列表的元素合到一个列表里面
s=[3,4,5]
print(L+s)##[0.02, 100, 'Hello', (1, 2, 3), ['python', 0.02], 3, 4, 5]
print("1***************************")
#2>append()   给列表里面增加元素，增加在最后，每次只能加一个元素
L.append('cd')
print(L)
print("2***************************")
###想加几个，就多加几次
L.append('cd')
L.append('yogo')
L.append('yong')
print(L)
print("3***************************")
#3>insert给列表里面增加元素，可以增加在指定位置
#指定位数（索引位置），值
L.insert(0,"sdd")###不覆盖，只后移
print(L)
print("4***************************")

#4>extend一次性添加读个元素 ,,,添加在尾巴上
s=[6,66,666]
L.extend(s)
print(L)
print("5***************************")
####查  索引取值 ，切片取值
print(L[::])
print("6***************************")
####改
#1>直接赋值，按照索引位置去赋值
L=[0.02,100,'Hello',(1,2,3),['python',0.02]]
L[0]='newnew'
print(L)
print("7***************************")
####删除
#1>pop  默认删除最后一个参数-1，，，可以删除指定位置的值
# L.pop()
# print(L)
##被删除的元素
res=L.pop()
print("被删除的元素：",res)
L.pop(0)
print(L)

#2>del  直接从内存删除
# del L
# print(L)

# #3>clear
# L.clear()
# print(L)

#4>remove   删除第一个遇到的值,删除存在的值，从第一个开始删
##删除的值不存在，报错
L=[0.02,100,'Hello',(1,2,3),['python',0.02],0.02]
L.remove(0.02)##删除指定的值
print(L)
print("************************")
####range   生成指定范围的正数序列
#切片很相似
##1>三个参数，range(m,n,k) m索引头 n索引尾 k 步长，默认等于1
##2>取头不取尾
##3>传一个参数：默认从0开始，不取尾
##4>步长可以不传
range(1,6,1)##1,2,3,4,5, 取头不取尾
res=list(range(1,6,1))
print(res)##强制转换成list查看range的取值


res=list(range(1,6,2))
print(res)##1,3,5

res=list(range(1))
print(res)##0

res=list(range(0))
print(res)##[]空列表

res=list(range(-4,-2))
print(res)##[-4,-3]

res=list(range(0,-4,-1))
print(res)##[0,-1,-2,-3]


L=[0.02,100,'Hello',(1,2,3),['python',0.02],0.02]

for item in L:
    print(item)
print("*****************")
for i in range(len(L)):###rang(4)-->range(0,4,1)-->0,1,2,3
    print(L[i])
print("*****************")

for i in range(len(L)-1,-1,-1):###倒叙输出   range(3,-1,-1)-->3,2,1,0
    print(L[i])
print("range*****************")

L=[0.02,100,'Hello',(1,2,3),['python',0.02],0.02]
####count 有几个想要知道的字符的值
res=L.count(100)
print(res)###1
print("count*****************")
####clear  清楚
####copy  深copy 浅copy
res=L.copy()
print(res)
print("copy*****************")

L=[0.02,100,'Hello',(1,2,3),['python',0.02],0.02]
#### index  返回遇到第一个值的索引（第一个值的位置）
res=L.index(0.02)
print(res)###0
res=L.index(0.02,2)
print(res)###5
print("index*****************")

####reverse() 列表翻转
L.reverse()
print(L)##[0.02, ['python', 0.02], (1, 2, 3), 'Hello', 100, 0.02]
print("reverse*****************")

####sort  排序 数字类型的排序
L=[34,4]
L.sort()
print(L)###[4,34]

##冒泡排序
L=[1,7,4,89,34,2]
L.sort()
print(L)##[1, 2, 4, 7, 34, 89]

##sort+reverse组合使用
L.sort(reverse=True)
print(L)##[89, 34, 7, 4, 2, 1]
L.sort(reverse=False)
print(L)##[1, 2, 4, 7, 34, 89]