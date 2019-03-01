import unittest
from InterfaceTest.common.http_requests import HTTPRequest2
from InterfaceTest.common import do_excel
from InterfaceTest.common import contants
from InterfaceTest.common.config import config
from InterfaceTest.common import context
from InterfaceTest import data
from ddt import ddt,data
@ddt
class AddTest(unittest.TestCase):
    excel = do_excel.Do_Excel(contants.case_file, 'add')
    cases = excel.get_cases()##实例化对象   列表里面放case实例
    @classmethod##类方法，每一个类只执行一次
    def setUpClass(cls):
        cls.http_request=HTTPRequest2()##实例化
    @data(*cases)
    def test_add(self,case):###对象迭代里面的属性值
            print(type(case.data),case.data)
            ##请求之前，替换参数化的值
            case.data=context.replace(case.data)
            resp = self.http_request.request(case.method, case.url, case.data)
            try:
                self.assertEqual(str(case.expected), resp.json()['code'])
                self.excel.Write_excel(case.case_id+1,resp.text,'PASS')
            except AssertionError as e:
                self.excel.Write_excel(case.case_id+1,resp.text,'FAIL')
                raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()


