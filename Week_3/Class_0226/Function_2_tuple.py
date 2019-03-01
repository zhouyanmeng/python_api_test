#####元组的内置函数  不可变元素，所有方法特别少
t=('rigth','sadness','灰灰的','柠檬','sadness','sadness')
####count统计数量的作用
res=t.count('A')###寻找元素出现的次数，在元组里面去找
print(res)

####index   找某个元素索引（位置）  找不到报错  默认1开始，可以指定个数
res=t.index("rigth")
print(res)###0
res=t.index("sadness",3)
print(res)###4
