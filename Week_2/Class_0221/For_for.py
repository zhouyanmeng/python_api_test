####嵌套循环
##把s里面的每一个元素都打印出来
s=['summer','saber','sadness','fillico','megan','cherry','allen','cooper']
for item in s:
    print(item)

##把s里面的每一个元素都打印出来,把item这个字符串里面的每一个元素打印出来
s=['summer','saber','sadness','fillico','megan','cherry','allen','cooper']
for item in s:
    print(item)####item一定是可迭代的  字符串，元组，列表
    for element in item:
        print(element)


##冒泡算法：
