import  requests
# class HTTPRequest:
    #使用这类的request方法完成不同的HTTP请求，并且返回响应结果
    # def request(self,method,url,data=None,json=None,cookies=None):
    #     method=method.upper()##将method强制转为大写
    #     if type(data)==str:
    #         data=eval(data)
    #     if method=='GET':
    #         resp=requests.get(url,params=data,cookies=cookies)#url,params
    #
    #     elif method=='POST':
    #         if json is not None:
    #         #if json：
    #             resp=requests.post(url,json=json,cookies=cookies)
    #         else:
    #             resp=requests.post(url,data=data,cookies=cookies)
    #     else:
    #         print("输入的请求方法不支持")
    #
    #     return resp

class HTTPRequest2:
    # 使用这类的request方法完成不同的HTTP请求，并且返回响应结果    不传cookies
    def __init__(self):
        self.session=requests.sessions.session()##打开一个session    实例化
        ##实例变量
    def request(self,method,url,data=None,json=None):
        method=method.upper()
        if method=='GET':
            resp=self.session.get(url,params=data)
        elif method == 'POST':
            if json is not None:
                # if json：
                resp = self.session.post(url,json=json)
            else:
                resp = self.session.post(url,data=data)
        else:
            print("输入的请求方法不支持")
        return resp

    def close(self):
       self.session.close()


if __name__ == '__main__':
    # #登录：
    # params = {'mobilephone': '13915411434', 'pwd': '123456'}
    # http_request=HTTPRequest()
    # resp1=http_request.request('POST','http://test.lemonban.com/futureloan/mvc/api/member/login',data=params)
    # print(resp1.cookies)
    # print(resp1.status_code)
    # print(resp1.text)
    # #调用充值
    # params = {'mobilephone': '13915411434', 'amount': '500'}
    # http_request=HTTPRequest()
    # resp2=http_request.request('POST','http://test.lemonban.com/futureloan/mvc/api/member/recharge',data=params,cookies=resp1.cookies)
    # print(resp2.cookies)
    # print(resp2.status_code)
    # print(resp2.text)

    http_request2 = HTTPRequest2()
    params = {'mobilephone': '13915411434', 'pwd': '123456'}
    resp2=http_request2.request('POST','http://test.lemonban.com/futureloan/mvc/api/member/login',params)
    print(resp2.text)
    params = {'mobilephone': '13915411434', 'amount': '500'}
    resp3 = http_request2.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', params)
    http_request2.close()
    print(resp3.status_code)
    print(resp3.text)