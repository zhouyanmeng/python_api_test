import requests
class HTTPRequest:
    def __init__(self):
        self.session=requests.sessions.session()
    def request(self,method,url,data=None,json=None):
        method=method.upper()
        if method=='GET':
            resp=self.session.get(url,params=data)
        elif method=='POST':
            if json is not None:
                resp=self.session.post(url,json=json)
            else:
                resp=self.session.post(url,data=data)

        else:
            print("输入的请求方式错误")
        return resp
    def close(self):
       self.session.close()

if __name__ == '__main__':
    rsp1=HTTPRequest()
    params = {'mobilephone': '13915411434', 'pwd': '123456'}
    resp1 = rsp1.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/login', params)
    print("resp1:",resp1.text)
    print("resp1:", resp1.cookies)
    params = {'mobilephone': '13915411434', 'amount': '500'}
    resp2 = rsp1.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', params)
    resp2.close()
    print(resp2.text)

