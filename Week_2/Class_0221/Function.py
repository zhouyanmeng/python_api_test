####函数的定义：为了实现某个功能而写的代码段
#如果这个功能是需要重复使用的，提高复用性
# def add(a,b):
#     print(a+b)
##函数的语法：
#def 函数名(参数1，参数2，参数3)：####小写子目录，不同的字母或者数字之间用下划线隔开
    ###'''解释文档'''
    ###代码段/函数体
    ###return

#参数：位置参数，默认参数，动态参数*args，关键字参数**args
#参数个数：0--正无穷
#函数体：实现什么功能
#return  函数是否有返回值

def say_hello():
    print("早上好！！！")
    return [1, 2, 3], {'name': '1212'}, '31232'

res=say_hello()###函数的调用  函数名()
print("函数返回的值是：",res)

#请对say_hello()这个函数的结果进行遍历
for item in res:
     print(item)

###return作用：：：当你调用这个函数的时候，返回给你一个值，这个值就是return后面的值

##1.1>函数里面没有return python会隐形的给你添加一个return None
##1.2>韩式里面有return，但是return后面啥都没有，等同于return None
##1.3>函数里面有return，但是return后面加的是None,最后结果还是返回None

##2.1如果return后面只有一个值的时候，是什么类型的数据就会返回什么类型的数据
#比如return后面是正数，返回的就是整数类型
#如果return后面的是字符串，返回的就是字符串类型
##3如果return后面多个值的时候，是以元组的类型返回()
##4return表示函数的结束，return后面的代码都不会再执行



# def say_hello():
#     print("早上好！！！")
#     return [1,2,3],{'name':'1212'},'31232'
# res=say_hello()###函数的调用  函数名()
# print("函数返回的值是：",res)

# def add(a,b,c):
#     res=a+b+c
#
#
# result=add(4,5,6)
# print(result+100)###TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# ##此时add里面的返回值就是None  那么None+100根据就不行


def add(a,b,c):
    res=a+b+c
    return res

result=add(4,5,6)
print(result)
































