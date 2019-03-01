# 写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
# 每个请求要求有请求参数
# 登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
# 请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码
import requests
import json
class HttpRequest:
    def http_request(self, method, url, param):
        """完成http的get请求或post请求
        :method 请求方法 可以是get or post
        :url 请求地址
        :param 请求参数，字典的格式 """
        if method.lower() == 'get':
            try:
                return requests.post(url, data=param)
            except Exception as e:
                print('get请求出错：{}'.format(e))
        else:
            try:
                return requests.post(url, data=param)
            except Exception as e:
                print('post请求出错：{}'.format(e))
if __name__ == '__main__':
    login_url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    param = {'mobilephone': '18688773467', 'pwd': '123456'}
    #param = {'mobilephone': '18688773467','pwd': ''}
    result = HttpRequest().http_request('post', login_url, param)
    print('结果是：{}'.format(result.json()))


