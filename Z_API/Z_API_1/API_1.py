import requests

#1构造请求：请求方式  请求地址  请求参数
#2发起请求
#3返回响应
#4判断响应码，响应体


##注册接口：{"mobilephone"}   构造请求
# params={"mobilephone":"15810047878","pwd":"123456"}
# resp=requests.get("http://test.lemonban.com/futureloan/mvc/api/member/register",params=params)#url params  **kwargs
# #get(url,params,**kwargs)  url位置参数
# #params:::字典类型,list,byte   get是有返回值的，使用一个变量去接收   resp是一个response class类的对象
# print(resp)
#
# print("响应码",resp.status_code)
# print("响应文本",resp.text)
# print("响应json",resp.json())
# print("响应头",resp.headers)
# print(resp.content)
# print("响应的cookies",resp.cookies)##响应的cookies <RequestsCookieJar[]>  []list cookie信息有多个
# print(resp.request._cookies)##请求里面有没有cookies   实例化一个request对象   私有属性._
# print(resp.request)##请求里面请求详情

#get使用params传参
#post使用data传参
##登录接口
params={"mobilephone":"15810447878","pwd":"123456"}
resp=requests.post("http://test.lemonban.com/futureloan/mvc/api/member/login",data=params)#url params  **kwargs
#post(url,data,json,**kwargs)  url位置参数   data 是关键字传参
#params:::字典类型,list,byte   post是有返回值的，使用一个变量去接收   resp是一个response class类的对象
print(resp)
print("响应码",resp.status_code)
print("响应文本",resp.text)
print("响应cookie",resp.cookies)
print("请求的cookie",resp.request._cookies)

##url,pparams,data,headers,cookies,files,cookies,auth,proxies,verify

##cookies::对象，字典
##充值接口
params={"mobilephone":"15810447878","amount":"100"}
resp=requests.post("http://test.lemonban.com/futureloan/mvc/api/member/recharge",
                   data=params,cookies=resp.cookies)#url params  **kwargs

print(resp)
print("响应码",resp.status_code)
print("响应文本",resp.text)
print("响应cookie",resp.cookies)
print("请求的cookie",resp.request._cookies)