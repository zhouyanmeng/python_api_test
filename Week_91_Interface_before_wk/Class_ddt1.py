# -*- coding: utf-8 -*-
# @Time    : 2019/3/22/022 14:23
# @Author  : bing
# @File    : test_case.py
# @Software: PyCharm

import unittest
import json
from ddt import ddt,data,unpack
from Week_6.Class_0323.TestAdd import Test_add

@ddt
class TestAdd(unittest.TestCase):
    print("1234567")
    @data(*[[1,2],[3,4]])
    @unpack
    def test_001(self,a,b):
        print(a)
        print(b)
        print(a+b)
    #元组--》1个元素--》加*，元组里面2个元素
    #unpack是对字典进行拆分，（针对每一条的数据进行拆分，3条）
    # @data(*[{'a': 0, "b": 0, 'expect': '0'}, {'a': 1, "b": 1, 'expect': '2'}])
    # @unpack  # 拆分字典
    # def test_001(self, a, b, expected):  # 利用'get'方式传参，用户名正确，密码错误    预期："msg":"用户名或密码错误"
    #     print(a)
    #     print(b)
    #     print(expected)


