import requests
import json
class loginAPI:
    def login(self, method, url, params):
        if method.lower() == 'get':
            try:
                return requests.post(url, data=params)
            except Exception as e:
                print('get请求出错：{}'.format(e))
        else:
            try:
                return requests.post(url, data=params)
            except Exception as e:
                print('post请求出错：{}'.format(e))
if __name__ == '__main__':
    login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    param = {'mobilephone': '13915411434', 'pwd': '123456'}
    loginres = loginAPI().login('post',login_url, param)
    print(loginres)
    print(loginres.cookies)
    print(loginres.json())
    print("登录成功")


