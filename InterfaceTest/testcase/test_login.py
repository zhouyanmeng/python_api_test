import unittest
from InterfaceTest.common.http_requests import HTTPRequest2
from InterfaceTest.common import do_excel
from InterfaceTest.common import  contants
from InterfaceTest import data
from ddt import ddt,data
from InterfaceTest.common import logger

logger=logger.get_logger(__name__)

@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.Do_Excel(contants.case_file, 'login')
    cases = excel.get_cases()##实例化对象   列表里面放case实例
    @classmethod##类方法，每一个类只执行一次
    def setUpClass(cls):
        logger.info("准备测试前置")
        cls.http_request=HTTPRequest2()##实例化
    @data(*cases)
    def test_login(self,case):###对象迭代里面的属性值
            logger.info("开始测试：{0}".format(case.title))
            resp = self.http_request.request(case.method, case.url, case.data)
            try:
                self.assertEqual(case.expected,resp.text)
                self.excel.Write_excel(case.case_id+1,resp.text,'PASS')
            except AssertionError as e:
                self.excel.Write_excel(case.case_id+1,resp.text,'FAIL')
                logger.error("测试报错了：{0}".format(e))
                raise e
    @classmethod
    def tearDownClass(cls):
        logger.info("测试后置处理")
        cls.http_request.close()


# class LoginTest(unittest.TestCase):##继承
#     def setUp(self):#单个，每个测试用例
#         self.http_request=HTTPRequest2()##实例化一个session
#     def test_login(self):
#         excel=do_excel.Do_Excel(contants.case_file, 'login')
#         cases=excel.get_cases()
#
#         for case in cases:
#             try:
#                 resp=self.http_request.request(case.method,case.url,case.data)
#                 self.assertEqual(case.expected,resp.text)
#                 excel.Write_excel(case.case_id+1,resp.text,'PASS')
#             except AssertionError as e:
#                 excel.Write_excel(case.case_id + 1, resp.text, 'FAIL')
#                 raise e
#
#     def tearDown(self):
#         self.http_request.close()
