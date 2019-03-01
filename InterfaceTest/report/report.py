import unittest
from InterfaceTest.common import HTMLTestRunnerNew
from InterfaceTest.common import contants
from InterfaceTest.testcase import test_register

# suite=unittest.TestSuite()
# loader=unittest.TestLoader()
# suite.addTests(loader.loadTestsFromModule(test_register))##一个一个加载进来

discover=unittest.defaultTestLoader.discover(contants.case_dir,"test_*.py")##正则表达

with open(contants.report_dir+'/report.html','wb+')as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            title='python api test report',
                                            description='xs api',
                                            tester='xiaoyao')
    runner.run(discover)

