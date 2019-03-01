# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 20:43
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : math_sutie.py

import unittest
import HTMLTestRunnerNew
from week_6.class_0103.do_excel import DoExcel#导入doexcel模块 获取测试数据
from week_6.class_0103.test_math_method import TestAdd #模块的方式加载用例
#suite:集合套件  TestSuite测试套件 存储加载用例

suite=unittest.TestSuite()#对象
cases=DoExcel('python13.xlsx','add').get_data()#列表

for case in cases:
    suite.addTest(TestAdd(case.case_id,case.title,case.a,case.b,case.expected,'test_add'))

with open('py13.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='python13的第一份报告',
                                            description='测试我们的数学类里的加法和减法',
                                            tester='华华')#测试者的名字
    runner.run(suite)#执行测试集里面的用例