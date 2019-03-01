
# 1. 给定一个列表 [1,4,5,3,"a",3]，去除其中的重复元素。

# 命令式
a = [1,4,5,3,"a",3]

b = []
for i in a:
    if i not in b:
        b.append(i)

#
def del_repeat(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

# 如果您能用尽量少的代码完成，
print(list(set(a)))


# 2. 列表和字符串的相互转换

a = ['t', "2", '6', 'a']
a_str = ""
for i in a:
    a_str += str(i)

print("".join(a))

b_str = "sfowoeoofwfsf"
# 定义一个空列表，遍历。。。

# list(), split() ["sfowoeoofwfsf"]


# 字符串去重，加排序
a = "sofwoeofoweofiosfmsosf"

# 列表里，sort()


# 你的代码遇到 BUG 你是如何处理？ 你在工作中遇到的最困难的事，你是怎么解决的。 自己解决问题的问题，能不能解决根本性问题。

# 百度。企业==》面向搜索引擎编程不会招。技术社区 GitHub, stackoverflow, infoQ.
# 你对问题的本质能有自己的理解。能够独立处理问题。
# 文档，看源码
# 定位问题。 断点调试。。。print()

# 怎么拷贝列表, 默认参数不能为可变类型

a = ['3']
print(id(a))
b = a  # 指向的是通一个对象
print(id(b))
# a[:]
c = a[:]   # 拷贝一个新的对象
print(id(c))

a.append(10)

print(a)  # [3, 10]
print(b)    # ["3“”， 10]
print(c)   # 3，10


# 单例模式的实现：只能生成一个对象的。 2个对象，3对象， 4个对象

class A:
    # 计划生育  只能生一个孩子。==》你这个家庭之前有孩子
    a_intance = []

    def __new__(cls):
        #
        if cls.a_intance is None:
            # 没有对象生成的时候，生成一个新对象
            cls.a_intance = super().__new__(cls)
            return cls.a_intance
        else:
            # 已经有对象了，
            return cls.a_intance

    def __init__(self):
        pass


# 模块导入
from a import my_a

my_a















