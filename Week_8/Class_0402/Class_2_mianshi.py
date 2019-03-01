##1给定一个列表，去除其中的重复元素
#[1,4,5,3,"a",3]
a=[1,4,5,3,"a",3]
def del_repeat(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b
if __name__ == '__main__':
    b=del_repeat([1,4,5,3,"a",3])
    print(b)


print(list(set(a)))###set去重复元素，

##2列表和字符串的相互转换
a=['t','2','6','a']
a_str=""
for i in a:
    a_str+=str(i)
print(a_str)


print(" ".join(a))

b_str="sdfgbfnfvbh3455432"
#3定义一个空列表，遍历

##字符串转列表：list(),split()
new_list=[]
for i in b_str:
    new_list.append(i)
print(new_list)


##4字符串去重，加排序
a="sdvbejfjfjfnvndnvjkdn4567890765dsh"
#列表里，sort()

##5遇到bug如何处理？
##6怎么拷贝列表,,默认参数   ###列表是可变参数
a=['3']
b=a
c=a[:]
a.append(10)##['3', 10]
print(a)##['3', 10]
print(b)##['3', 10]
print(c)##['3']##拷贝一个新的对象
print(id(a))##打印内存地址id

##7单例模式的实现：：只能生产一个对象
class A:
    a_intance=None

    def __new__(cls):##用来生成对象
        if cls.a_intance is None:##cls就是class A这个类
            cls.a_intance=super().__new__(cls)
            return cls.a_intance
        else:
            return cls.a_intance
print(A())###对象是一个，对应的一个内存地址
print(A())

##8模块导入


