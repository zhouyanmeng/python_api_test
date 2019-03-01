####参数类型：位置参数  默认参数 动态参数*args  关键字参数**kwargs
##1位置参数
####有几个位置参数，传参的时候就要传几个，多不行，少不行
####一定要穿参数
def add():
    return 3+4
res=add()
print("add函数的计算结果是{}".format(res))

def add(x,y):##形参/位置参数：不需要给值 ##调用函数的时候传参
    return x+y
##位置参数
res=add(9,6)##调用函数的时候传的参数---实参--默认是按顺序赋值
##res=add(y=9,x=5)###指定赋值，不关注顺序###
##res=add(x=9,y=5)###指定赋值###
print("add函数的计算结果是{}".format(res))
print("1*****************************")

##2默认参数：在定义函数的时候，给某个参数设置默认值
###传参的时候,默认参数可以穿，也可以不传，，如果传值的话覆盖默认值，取最新的值
##注意点
#>1位置参数必须在默认参数之前：：默认参数写在最后
#>2有几个位置参数，就必须要穿几个参数
def add(x,y=9):
   '''加法，求任何2个参数的和，并返回计算接轨

    return x+y'''
res=add(9)
print("add函数的计算结果是{}".format(res))
print("2******************")

###3动态参数 *args  argument参数们----不定长参数
def add(*args):####参数传递到函数内部，会变成一个元组来存储所有的参数
    print(type(args))
    sum=0
    for item in args:
        sum+=item
    print(sum)

add(1,2,3,4,5)

print("3******************")
##4关键字参数**kwards key word arguments
##参数传递进去后变成一个字典，kwargs指明key  value
##可以不传，就是空字典
def student_info(**kwargs):
    print(kwargs)

student_info(name='妞妞',age=19)

print("4******************")

def add(*args):
    print(*args)####调用的时候，将元组或者列表解包成不同的参数
add(1,2,3,4,5,6)

def add(*args):
    print(args)###元组，收集成一个新的函数给元组
add(1,2,3,4,5,6)












