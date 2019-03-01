import unittest
import json
from Week_92_Interface_before_wk.Http_req_OK_ddt import HttpRequest

class Test_request_faile(unittest.TestCase):##get请求
    def test_001(self):
        print('登录成功')
        expected="登录成功"
        res=HttpRequest('18688773467','123456').http_request('get')
        self.assertEqual(expected,json.loads(res)['msg'])
    def test_002(self):#post
        print('登录成功')
        exected='登录成功'
        res=Interface_Request('18688773467','123456').http_request('post')
        self.assertEqual(exected,json.loads(res)['msg'])

class Test_request_success(unittest.TestCase):
    def test_001(self):#利用get传参，用户名正确，密码错误，预期："msg":"用户名或者密码错误"
        print("用户名或密码错误")
        expected='用户名或密码错误'
        res=Interface_Request('2345','123456').http_request('get')
        #断言
        self.assertEqual(expected, json.loads(res)['msg'])
    def test_002(self):
        print('手机号不能为空')
        expected='手机号不能为空'
        res=Interface_Request('','123456').http_request('get')
        self.assertIn(expected,res)