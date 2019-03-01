import unittest
from Week_92_Interface_before_wk.test_http_reqest import *
import HTMLTestRunnerNew###测试报告模块
suite=unittest.TestSuite()##1创建对象
loader=unittest.TestLoader()#用例的加载器
suite=unittest.TestSuite()#创建了一个对象
#加载测试用例
suite.addTest(loader.loadTestsFromTestCase(Test_request_success))
suite.addTest(loader.loadTestsFromTestCase(Test_request_faile))

#执行用例
# runner=unittest.TextTestRunner()#创建一个对象来执行用例
# runner.run(suite)

#执行生成报告
with open('test.html','wb')as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,##详细程度
        title='2019年单元测试报告',
        tester='吃肉的小妖'
    )
    runner.run(suite)