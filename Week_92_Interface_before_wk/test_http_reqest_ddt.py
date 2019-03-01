# -*- coding:utf-8 -*-
# @datetime:2019/3/22 16:36
# @author:1111
# @email:123@sina.com
# @File:test_request_suite.py

import unittest
import json
from ddt import ddt,data,unpack
from Week_92_Interface_before_wk.requrst_login import Interface_Request
# from Week_92_Interface_before_wk.Http_req_OK_ddt import HttpRequest
# 登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
# 请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码
@ddt###执行必须从这里开始执行
class Test_request_faile(unittest.TestCase):##get请求
    @data(*[{"url":"http://47.107.168.87:8080/futureloan/mvc/api/member/login","mobilephone": "18688773467", "pwd": "123456"}])
    @unpack
    def test_001(self,url,mobilephone,pwd):
        expected="登录成功"
        res=Interface_Request(18688773467,123456).http_request('get')
        # print("res:"+res)
        self.assertEqual(expected,json.loads(res)['msg'])

    @data(*[{"url": "http://47.107.168.87:8080/futureloan/mvc/api/member/login", "mobilephone": "18688773467",
                 "pwd": "123456"}])
    @unpack
    def test_002(self,url,mobilephone,pwd):
        expected="登录成功"
        res=Interface_Request(18688773467,123456).http_request('post')
        self.assertEqual(expected,json.loads(res)["msg"])


@ddt
class Test_request_success(unittest.TestCase):
    @data(*[{"url": "http://47.107.168.87:8080/futureloan/mvc/api/member/login", "mobilephone": "688773467",
             "pwd": "123456"}])
    @unpack
    def test_001(self,url,mobilephone,pwd):
        expected = "用户名或密码错误"
        res=Interface_Request(688773467,123456).http_request("post")
        self.assertEqual(expected,json.loads(res)["msg"])

    @data(*[{"url": "http://47.107.168.87:8080/futureloan/mvc/api/member/login", "mobilephone": "",
             "pwd": "123456"}])
    @unpack
    def test_002(self,url,mobilephone,pwd):
        expected='手机号不能为空'
        res=Interface_Request("",123456).http_request('get')
        self.assertEqual(expected,json.loads(res)["msg"])
















#     def test_002(self):#post
#         print('登录成功')
#         exected='登录成功'
#         res=Interface_Request('18688773467','123456').http_request('post')
#         self.assertEqual(exected,json.loads(res)['msg'])
# class Test_request_success(unittest.TestCase):
#     def test_001(self):#利用get传参，用户名正确，密码错误，预期："msg":"用户名或者密码错误"
#         print("用户名或密码错误")
#         expected='用户名或密码错误'
#         res=Interface_Request('2345','123456').http_request('get')
#         #断言
#         self.assertEqual(expected, json.loads(res)['msg'])
#     def test_002(self):
#         print('手机号不能为空')
#         expected='手机号不能为空'
#         res=Interface_Request('','123456').http_request('get')
#         self.assertIn(expected,res)