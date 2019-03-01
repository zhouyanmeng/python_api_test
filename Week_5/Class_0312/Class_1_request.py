import requests

login_url="http://47.107.168.87:8080/futureloan/mvc/api/member/login"
param={'monile':"18688773467",'pwd':'123456'}
#发送一个get请求::如果要求有参数的话，就要以地点的形式传递过去
resp1=requests.get(login_url,params=param)
print("响应报文：",resp1.text)##响应报文

##发送一个post请求
resp2=requests.post(login_url,data=param)##响应结果消息实体
print("响应报文：",resp2.text)
# def http_request(self,mobilephone,pwd):
#     params1={"mobilephone":"18688773467","pwd":"123456","data":None}
#     url='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
#     reqs=requests.get(url,params=params1)
#     print(reqs)
#     print(reqs.headers)
#     print(reqs.text)
#     print(reqs.status_code)

