import requests
from Z_API.Z_API_1.login import loginAPI
class rechargeAPI:
    def recharge(self, method, url, params):
        if method.lower=='get':
            return requests.get(url,params=params)
        elif method.lower=='post':
            return requests.post(url, data=params)
        else:
            print("输入的请求方式错误！！！")
if __name__ == '__main__':
    login_url_1 = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    param_1 = {'mobilephone': '13915411434', 'pwd': '123456'}
    loginres = loginAPI().login('post', login_url_1, param_1)###实例化登录，获取登录的cookie

    login_url_2= "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
    param_2 = {'mobilephone': '13915411434', 'amount': 500}
    rechargeres = requests.post(login_url_2, data=param_2, cookies=loginres.cookies, )
    print(rechargeres)
    print(rechargeres.json())
    print(rechargeres.json()["data"]["leaveamount"])
    print("充值成功")


