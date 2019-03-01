from Z_API.Z_API_1 import *
loader=unittest.TestLoader()#用例的加载器
suite=unittest.TestSuite()#创建了一个对象
# 第一种方法
# suite.addTest(loader.loadTestsFromModule(test_case))
# 第二种方法
suite.addTest(loader.loadTestsFromTestCase(Test_register))
suite.addTest(loader.loadTestsFromTestCase(Test_login))
suite.addTest(loader.loadTestsFromTestCase(Test_recharge))
# 第三种方法
# suite.addTest(Test_request_success('test_001'))
# suite.addTest(Test_request_success('test_002'))
# suite.addTest(Test_request_faile('test_001'))
# suite.addTest(Test_request_faile('test_002'))

#执行用例
runner=unittest.TextTestRunner()#创建一个对象来执行用例
runner.run(suite)
