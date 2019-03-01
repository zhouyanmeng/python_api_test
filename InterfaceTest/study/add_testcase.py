import unittest
from InterfaceTest.common.http_requests import HTTPRequest2
from InterfaceTest.common import do_excel
from InterfaceTest.common import  contants
from InterfaceTest.common.config import config
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
    def test_longin(self,case):###对象迭代里面的属性值
            case.data = eval(case.data)  ##变成一个字段
            print(type(case.data),case.data)
            if case.data.__contains__('mobilephone') and case.data['mobilephone']=='normal_user':
                case.data['mobilephone']=config.get('data','normal_user')##拿到 值赋值给data
            if case.data.__contains__('pwd') and case.data['pwd'] == 'normal_pwd':
                case.data['pwd'] = config.get('data', 'normal_pwd')  ##拿到 值赋值给data
            if case.data.__contains__('member_id') and case.data['member_id'] == 'loan_member_id':
                case.data['member_id'] = config.get('data', 'loan_member_id')  ##拿到 值赋值给data
            # case.data=contants.replace(case.data)
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


