import unittest
from Week_6.Class_0321.HM_Testcase import *
suite=unittest.TestSuite()##1创建对象

#2加载用例
##1一个一个把测试用例加载进来
suite.addTest(TestLogin("test_001"))##添加测试集
suite.addTest(TestLogin("test_002"))
suite.addTest(TestLogin("test_003"))
suite.addTest(TestLogin("test_004"))

#2添加模块
from Week_6.Class_0321 import HM_Testcase
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(HM_Testcase))


#3添加测试类名
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestLogin))

#3执行用例
runner=unittest.TextTestRunner()
runner.run(suite)
