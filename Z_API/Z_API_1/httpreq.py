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
    login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'
    param = {'mobilephone': '18688773467', 'pwd': '123456'}
    #param = {'mobilephone': '18688773467','pwd': ''}
    result = HttpRequest().http_request('post', login_url, param)
    print('结果是：{}'.format(result.json()))
    print(result.json())
    print(result.json()["msg"])