#1函数额参数个数大于等于0个都行
#2为什么要加参数，就是为了提高代码的复用性，参数通过函数的参数列表传递进来
def count_number(x,y):
    count=0
    for i in range(x,y):
        count=count+i
    print("计算结果是:{}".format(count))
    return count
# count_number(101)###计算1-100之间的和
count_number(1,101)###计算1-100之间的和
count_number(1,101)###计算1-100之间的和
print("1********************8")

##步长
def count_number(x,y,z):
    count=0
    for i in range(x,y,z):
        count=count+i
    print("计算结果是:{}".format(count))
    return count
# count_number(101)###计算1-100之间的和
count_number(0,101,2)###计算1-100之间的偶数和
count_number(1,101,2)###计算1-100之间的奇数和
count_number(20,5,2)###不满足不报错，不进入循环计算