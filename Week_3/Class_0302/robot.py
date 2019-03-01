##如果全局变量和局部变量同名
##1>如果全局变量和局部变量同时存在的话，那么函数优先调用自己上网的局部变量
##2>如果不存在局部变量，那么函数就调用全局变量
#3>global 变量名   声明是一个全局变量
# def robot(name,msg):
#     print("{}您有一条信息：{}".format(name,msg))
#
# language='c#'   ###全局变量
# # print(id(language))
#
# def coding():
#     ##global language  在函数内部全局变量
#     language='python'###局部变量   只能在当前函数内部生效
#     # print(id(language))
#     print('我最喜欢的代码是:{}'.format(language))
# def automation_testing(type):
#     print("{}测试，用{}代码比较合适公司的框架".format(type,language))
#
# coding()
# automation_testing('app')
# a=2
# print(id(a))
# a=4
# print(id(a))


###函数内部声明全局变量
def robot(name,msg):
    print("{}您有一条信息：{}".format(name,msg))

def coding():
    global language  #在函数内部全局变量
    language='python'###局部变量   只能在当前函数内部生效
    # print(id(language))
    print('我最喜欢的代码是:{}'.format(language))
    language='ruby'
def automation_testing(type):
    print("{}测试，用{}代码比较合适公司的框架".format(type,language))

coding()####取python
automation_testing('app')####取ruby



if __name__ == '__main__':####代码执行的主入口  执行当前文件的时候才会被调用，不然其他模块调用都不执行
   ###测试代码会写在里面，
    robot('001','今天一起吃午餐吧！！！')###调用函数