import unittest
from InterfaceTest.common.http_requests import HTTPRequest2
from InterfaceTest.common import do_excel
from InterfaceTest.common import  contants
from InterfaceTest import data
from ddt import ddt,data
from InterfaceTest.common.do_mysql import DoMysql
@ddt
class RechargeTest(unittest.TestCase):
    excel = do_excel.Do_Excel(contants.case_file, 'recharge')
    cases = excel.get_cases()##实例化对象   列表里面放case实例

    @classmethod##类方法，每一个类只执行一次
    def setUpClass(cls):
        cls.http_request=HTTPRequest2()##实例化
        cls.mysql=DoMysql()
    @data(*cases)
    def test_recharge(self,case):###对象迭代里面的属性值
        print(case.title)
        ##请求之前先判断是否需要执行sql
        if case.sql is not None:
            sql=eval(case.sql)['sql1']
            member=self.mysql.fetch_one(sql)
            print(member['leaveamount'])
            before=member['leaveamount']
        resp = self.http_request.request(case.method, case.url, case.data)
        resp_code=resp.json()['code']
        try:
            self.assertEqual(str(case.expected),resp_code)
            self.excel.Write_excel(case.case_id+1,resp.text,'PASS')
            ##成功之前先判断是否需要执行sql
            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                member = self.mysql.fetch_one(sql)
                # print(member['leaveamount'])
                after = member['leaveamount']
                recharge_amount=int(eval(case.data)['amount'])###st转字段，在转整型
                self.assertEqual(before + recharge_amount, after)
            #self.assertEqual(before+case.data['amount'],after)
        except AssertionError as e:
            self.excel.Write_excel(case.case_id+1,resp.text,'FAIL')
            raise e
    @classmethod
    def tearDownClass(cls):
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
