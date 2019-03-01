import unittest
from Week_6.Class_0323.HM_Testcase import *
import HTMLTestRunnerNew###测试报告模块
suite=unittest.TestSuite()##1创建对象

#2加载用例
##1一个一个把测试用例加载进来

# suite.addTest(Test_request_faile("test_001"))##添加测试集
# suite.addTest(Test_request_faile("test_002"))
suite.addTest(Test_request_success("test_001"))
# suite.addTest(Test_request_success("test_002"))
#2添加模块
from Week_6.Class_0321 import HM_Testcase
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(HM_Testcase))


#3添加测试类名
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(Test_request_success))

# #3。1执行用例
# runner=unittest.TextTestRunner()
# runner.run(suite)

# #3.2执行用例---unittest版本
# with open('test.txt','w')as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=2)##创建一个对象来执行用例
#     runner.run(suite)

##3。3执行测试用例---生成测试报告
with open('test.html','wb')as file:###wb文件流的写入
    runner=HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title='2019单元测试报告',
        tester='chirou'
        )##创建一个对象来执行用例
    runner.run(suite)