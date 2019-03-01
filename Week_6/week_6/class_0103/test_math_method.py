# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 20:18
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : test_math_method.py

import unittest
from week_6.class_0103.do_excel import DoExcel
from week_6.class_0103.math_method import MathMethod#数学类


class TestAdd(unittest.TestCase):#继承TestCase

    #超继承：super
    def __init__(self,case_id,title,a,b,expected,methodName):#重写 override 覆盖掉
        #超继承：既有子类的方法 也会执行父类
        super(TestAdd,self).__init__(methodName)#关键的就在这里 调用父类的init方法
        self.case_id=case_id#用例的序号
        self.title=title#用例的标题
        self.a=a
        self.b=b
        self.expected=expected

    def setUp(self):
        self.t=DoExcel('python13.xlsx','add')#创建的对象
        print('-----开始执行第{}条用例：{}------'.format(self.case_id,self.title))

    def tearDown(self):
        print('----用例执行完毕------')

    '测试我们自己写的数学类 MathMethod'
    def test_add(self):#测试加法
        result=MathMethod().add(self.a,self.b)
        try:
            self.assertEqual(self.expected,result)#断言
            TestResult='Pass'#如果代码进入到try了里面 那么用例就通过
        except AssertionError as e:
            TestResult='Failed'#如果代码进入到except了里面 那么用例就不通过
            print('断言出错了，错误是：{}'.format(e))
            raise e
        finally:
            #写回结果
            self.t.write_back(self.case_id+1,6,result)#写回 测试的实际结果
            self.t.write_back(self.case_id+1,7,TestResult)#写回 测试的结论，到底是通过还是没通过

if __name__ == '__main__':#
    unittest.main()#会自动的在当前文件里面加载test_开头的用例
