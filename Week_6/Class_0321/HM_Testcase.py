import unittest
from Week_6.Class_0321.HttpRequestMethod import HttpRequest
class TestLogin(unittest.TestCase):
    def test_001(self):
        excep='{"status":1,"code":"10001","data":null,"msg":"登录成功"}'
        resp=HttpRequest().http_request('get')
        self.assertTrue(excep,resp)

    def test_002(self):
        excep = '{"status":1,"code":"10001","data":null,"msg":"登录成功"}'
        resp = HttpRequest().http_request('post')
        self.assertTrue(excep, resp)

    def test_003(self):
        excp = 200
        rsp = HttpRequest().http_request('get')
        self.assertNotEqual(excp, rsp)

    def test_004(self):
        excp = 200
        rsp = HttpRequest().http_request('post')
        self.assertNotEqual(excp, rsp)