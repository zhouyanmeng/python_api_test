# 1：作业安排：
# 写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
# 每个请求要求有请求参数
# 登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
# 请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码

import requests
class HttpRequest:
    def http_request(self,method):
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        params1 = {"mobilephone": "18688773467", "pwd": "123456"}
        if method.lower()=='get':
            reqs=requests.put(url,params=params1)
            print("响应报文：",reqs.text)
        else:
            reqs = requests.post(url, data=params1)
            print("响应报文：", reqs.text)
        return reqs

if __name__ == '__main__':
    rsp=HttpRequest().http_request('get')
    print("发出的请求是：{}".format(rsp.text))