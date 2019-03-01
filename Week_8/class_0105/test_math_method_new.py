# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 20:18
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : test_math_method.py

import unittest
from ddt import ddt,data  # pip install ddt
from week_6.class_0105.do_excel import DoExcel
from week_6.class_0105.my_log import MyLog
from week_6.class_0105.math_method import MathMethod#数学类

my_logger=MyLog()#创建的一个日志对象

#测试是数据
cases=DoExcel('python13.xlsx','add').get_data()#列表,列表里面的值 是一个个的对象

@ddt#装饰器 ddt装饰测试类  类与测试方法同步装饰
class TestAdd(unittest.TestCase):#继承TestCase

    def setUp(self):
        my_logger.info('----------开始执行用例--------')
        self.t=DoExcel('python13.xlsx','add')#创建的对象

    def tearDown(self):
        my_logger.info('----用例执行完毕------')

    @data(*cases)#装饰我们的测试方法的/测试用例  类与测试方法同步装饰
    def test_add(self,case):#测试方法 用一个变量来接收data传递的数据  data有几个数据 就执行几次用例
        my_logger.info('-----开始执行第{}条用例：{}------'.format(case.case_id,case.title))
        result=MathMethod().add(case.a,case.b)
        try:
            self.assertEqual(case.expected,result)#断言
            TestResult='Pass'#如果代码进入到try了里面 那么用例就通过
        except AssertionError as e:
            TestResult='Failed'#如果代码进入到except了里面 那么用例就不通过
            my_logger.error('断言出错了，错误是：{}'.format(e))
            raise e
        finally:
            #写回结果
            self.t.write_back(case.case_id+1,6,result)#写回 测试的实际结果
            self.t.write_back(case.case_id+1,7,TestResult)#写回 测试的结论，到底是通过还是没通过


if __name__ == '__main__':#
    unittest.main()#会自动的在当前文件里面加载test_开头的用例
