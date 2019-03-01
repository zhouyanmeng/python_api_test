import requests
import json
#注册
login_url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
param = {'mobilephone': '13915411434', 'pwd': '123456'}
registerres=requests.post(login_url,data=param)
print(registerres)
print(registerres.cookies)
print(registerres.json())
print("注册成功")
#登录
login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
param = {'mobilephone': '13915411434', 'pwd': '123456'}
registerres=requests.post(login_url,data=param)
print(registerres)
print(registerres.cookies)
print(registerres.json())
print("登录成功")
#充值

login_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
param = {'mobilephone': '13915411434', 'amount': 500}
registerres=requests.post(login_url,data=param,cookies=registerres.cookies,)
print(registerres)
print(registerres.cookies)
print(registerres.json())
print("充值成功")