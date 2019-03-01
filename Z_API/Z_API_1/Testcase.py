import unittest
import requests
from Z_API.Z_API_1 import HttpRequest
class Test_register(unittest.TestCase):
    def test_001(self):##注册新用户
        login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'
        param = {'mobilephone': '13295211118', 'pwd': '123456'}
        expected = "注册成功"
        res = HttpRequest().http_request('post', login_url, param)
        self.assertEqual(expected, res.json()["msg"])
    def test_002(self):##注册手机号码已经被注册
        login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'
        param = {'mobilephone': '13295211112', 'pwd': '123456'}
        expected = "手机号码已被注册"
        res = HttpRequest().http_request('post', login_url, param)
        self.assertEqual(expected, res.json()["msg"])
class Test_login(unittest.TestCase):
    def test_001(self):##登录存在的用户
        login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
        param = {'mobilephone': '13295211112', 'pwd': '123456'}
        expected = "登录成功"
        res = HttpRequest().http_request('post', login_url, param)
        self.assertEqual(expected, res.json()["msg"])
        # print(res.json())
        # print(res.cookies)
    def test_002(self):##登录不存在的用户
        login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
        param = {'mobilephone': '1329521111', 'pwd': '123456'}
        expected = "用户名或密码错误"
        res = HttpRequest().http_request('post', login_url, param)
        self.assertEqual(expected, res.json()["msg"])
class Test_recharge(unittest.TestCase):
    def test_001(self):##登录存在的用户充值
        login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
        param = {'mobilephone': '13295211112', 'pwd': '123456'}
        res = HttpRequest().http_request('post', login_url, param)
        # print(res.cookies)

        login_url_2 = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
        param_2 = {'mobilephone': '13915411434', 'amount': 500}
        cookies=res.cookies
        rechargeres = HttpRequest().http_request("post",login_url_2,param_2)
        expected = "充值成功"
        # res = HttpRequest().http_request(login_url_2, data=param_2, cookies=loginres.cookies)
        rechargeres = requests.post(login_url_2, data=param_2, cookies=res.cookies)
        self.assertEqual(expected, rechargeres.json()["msg"])
        print("充值余额：",rechargeres.json()["data"]["leaveamount"])