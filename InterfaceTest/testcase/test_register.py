import unittest
from InterfaceTest.common.http_requests import HTTPRequest2
from InterfaceTest.common import do_excel
from InterfaceTest.common import  contants
from InterfaceTest import data
from ddt import ddt,data
from InterfaceTest.common import do_mysql
@ddt
class RegisterTest(unittest.TestCase):
    excel = do_excel.Do_Excel(contants.case_file, 'register')
    cases = excel.get_cases()##实例化对象   列表里面放case实例
    @classmethod##类方法，每一个类只执行一次
    def setUpClass(cls):
        cls.http_request=HTTPRequest2()##实例化
        cls.mysql=do_mysql.DoMysql()
    @data(*cases)
    def test_register(self,case):###对象迭代里面的属性值
        if case.data.find('register_mobile') > -1:  ##字符串的查找
            sql = 'select max(mobilephone) from future.member'  ##查询最大手机号码
            max_phone = self.mysql.fetch_one(sql)[0]  ##返回最近的一条数据   最大的手机号    元组类型
            # 最大手机号码+1，  原来是元组类型，转成int
            max_phone = int(max_phone) + 1
            ##replace方法替换之后重新返回一个新的字符串，有返回值，要接受
            case.data=case.data.replace('register_mobile', str(max_phone)) ###字符串的替换   replace(old,new)
            resp = self.http_request.request(case.method, case.url, case.data)
            try:
                self.assertEqual(case.expected,resp.text)
                self.excel.Write_excel(case.case_id+1,resp.text,'PASS')
            except AssertionError as e:
                self.excel.Write_excel(case.case_id+1,resp.text,'FAIL')
                raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()
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
