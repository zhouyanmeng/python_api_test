import ssl
from smtplib import SMTP, SMTP_SSL

from conf import emailname, emailpwd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication




class MyEmail:

    def __init__(self, email_name, email_pwd):
        # email_name : wanyuze@163.com  ==> server: smtp.163.com , port:25
        # email_name : wanyuze@qq.com  ==> server: smtp.qq.com , port:465

        server = SMTP('smtp.163.com', 25)

        pass


    def send_email(self, to, msg, attachments=None, subject=""):
        pass


# 使用。 用户名和密码， send_email(to, msg, attachments, subject)
