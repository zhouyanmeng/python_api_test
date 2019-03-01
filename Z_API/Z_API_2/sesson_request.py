import requests
###同一个session，充值想要用登录的sessionid,,,,


"""
两种传递cookies的方式
1单独的session，把上一个请求的返回cookies，指定穿戴到下一个请求的入参cookie中
2使用同一个session，就会自动传递cookie
"""
session=requests.sessions.session()
#登录
params = {'mobilephone': '13915411434', 'pwd': '123456'}
resp1=session.request('POST',url='http://test.lemonban.com/futureloan/mvc/api/member/login',data=params)
print("登录状态：",resp1.status_code)
print("登录返回值：",resp1.text)
print("登录cookies:",resp1.cookies)
#充值
session2=requests.sessions.session()

params = {'mobilephone': '13915411434', 'amount': '500'}
resp2=session.request('POST','http://test.lemonban.com/futureloan/mvc/api/member/recharge',data=params)
print("充值状态：",resp2.status_code)
print("充值返回：",resp2.text)
session.close()