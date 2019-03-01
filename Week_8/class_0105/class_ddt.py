# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 9:36
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_ddt.py

#动态参数 关键字参数
#*args   **kwargs

def student_name(*args):
    print('args的类型',type(args))
    print(args)
    print('args的长度',len(args))
# t=('好呀','小陈','月亮的味道','差不多先生')
# student_name(t)
# #t=(('好呀','小陈'),('月亮的味道','差不多先生'))
# t=[['好呀','小陈'],['月亮的味道','差不多先生']]
# #t={'name_1':'好呀','name_2':'月亮的味道'}
# student_name(*t)


import unittest
from ddt import ddt,data,unpack


# t=('好呀','小陈','月亮的味道','差不多先生')
# t=(('好呀','小陈'),('月亮的味道','差不多先生','醉里簪花'))

t=[{'name_1':'好呀','name_2':'月亮的味道'},{'name_1':'差不多','name_2':'河畔'}]
@ddt#装饰测试类  继承unittest.TestCase
class TestAdd(unittest.TestCase):
    @data(*t)#data解包之后 有几个参数 下面就运行几次用例
    @unpack#把上面data解包的数据 再次根据逗号去拆分,有几个变量 那么我们的测试方法就要用几个参数来接接收值
    def test_001(self,name_1,name_2):#ddt 装饰测试方法 在测试类里面 test开头的
        print('test_001下面开始打印参数')
        # print(item)
        # print(args)
        print('test_001参数值name_1:',name_1)
        print('test_001参数值name_2:',name_2)
        # print('test_001参数值c:',c)
        print('test_001下面结束打印参数')
        print()

    @data(t)
    def test_002(self,item):
        print('test_002下面开始打印参数')
        print('test_002参数值:',item)
        print('test_002下面结束打印参数')
        print()

