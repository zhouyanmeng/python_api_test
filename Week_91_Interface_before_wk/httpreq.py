#1：作业安排：
#写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
#每个请求要求有请求参数
#登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
#请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码
import  requests
class Http_Request():
    '''初始化参数'''
    def __init__(self,url,method,data):
        self.url=url
        self.method=method
        self.data=data

    def http_request(self):
        '''判断请求方式是get还是post'''
        if self.method.lower() == 'get':
            res=requests.get(self.url,params=self.data)
            return res
        elif self.method.lower() == 'post':
            res=requests.post(self.url,data=self.data)
            return res
        else:
            print('你输入的请求方式错误')
if __name__ == '__main__':

    url='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    data={'mobilephone':'18688773467','pwd':'123456'}
    #发送一个get请求方式
    res=Http_Request(url,'get',data).http_request()
    print(res.headers)
    print(res.status_code)
    print(res.text)
    #发送一个post请求方式
    res=Http_Request(url,'Post',data).http_request()
    print(res.headers)
    print(res.status_code)
    print(res.text)