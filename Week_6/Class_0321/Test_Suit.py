import unittest
#import HTMLTestRunner
from Week_6.Class_0321.Class_0321 import *
#存储用例的容器suite 套件

##1存储用例   把要执行的用例加载进来
suite=unittest.TestSuite()  ##TestSuite是一个类，创建一个对象
suite.addTest(TestMathMethod("test_001"))##添加用例   创建实例  调用类   addtest是testsuite里面的方法  ---用例是测试列的实例
suite.addTest(TestMathMethod("test_002"))
##（第一中方法，第一个一个的执行）


##2第二种方法，用loder来加载用例,通过模块来加载用例
from Week_6.Class_0321 import Class_0321
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(Class_0321))


##3第3中方法，通过loader来加载用例，通过测试类名来加载用例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))##类名

###2.1执行用例，
runner=unittest.TextTestRunner()##创建一个对象来执行用例
runner.run(suite)

###2.2执行测试用例，放到某一个地方

#verbosity=0,1,2   详细程度
#0很简单
#1比0多了几个点，执行成功不成功

# #2详细显示每一个用例的结果  ----unittest版本
# with open('test.text','w') as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=0)##创建一个对象来执行用例 执行测试用例并生成报告
#     runner.run(suite)
#3执行并生成测试报告，---HTMLTestRunner   存放在lib下
# with open('test.txt','wb')as file:




###执行的状态：
#.通过一条用例   100个用例，100个点
#E 代表出错
#F 用例执行失败