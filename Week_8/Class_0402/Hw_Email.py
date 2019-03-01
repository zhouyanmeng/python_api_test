import ssl
from smtplib import SMTP,SMTP_SSL

class myEmail:##发送邮件的类
    #email_name: zhouyanmeng@163.com   server:smtp.163.com,port:25
    # email_name: zhouyanmeng@qq.com   server:smtp.qq.com,port:45
    server=SMTP('smtp.163.com',25)
    #email_pwd:
    def __init__(self,email_name,email_pwd):
        self.email_name=email_name
        self.email_pwd=email_pwd
        pass
#登录
        server.login(email_name,email_pwd)
    def send_email(self,to,msg,attachment=None,subject=""):
        pass

#使用  用户名密码登录，send_email(to,msg,attachments,subject)
