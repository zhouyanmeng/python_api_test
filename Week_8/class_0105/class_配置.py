# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 10:20
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_配置.py

from configparser import ConfigParser#ConfigParser 配置类 专门来读取配置文件的

#配置文件：结尾 .ini、 .conf 、.config 、.properties .xml

#配置文件一般是什么样的
#section 片段/区域  [区域名]
#option  相当于字典里面key 一个一个的配置选项
#value  相当于字典里面value

#怎么用呢？
# cf=ConfigParser()
# cf.read('case.conf',encoding='utf-8')#open()
# value=cf.get('TeacherInfo','t4')
# # value=cf['TeacherInfo']['t4']#一层一层的去定位
# print(value)

#注意的点：读取出来的值 都是字符串 对值去进行处理 可以用eval()
# cf=ConfigParser()
# cf.read('case.conf',encoding='utf-8')#open()
# # value=eval(cf.get('TeacherInfo','grade'))
# # value=cf.getfloat('TeacherInfo','grade')
# # value=cf.getint('TeacherInfo','avg_age')
# value=cf.getboolean('TeacherInfo','age')
# # value=cf['TeacherInfo']['t4']#一层一层的去定位
# print(value)
# print('值的类型',type(value))


#写一个类  缺点：如果是列表类型或者是字典类型 或者是字符串类型 怎么做呢？？
from configparser import ConfigParser
class ReadConfig:

    def __init__(self,file):
        self.cf=ConfigParser()#为什么要赋值给self.cf 方面后面的方法调用
        self.cf.read(file,encoding='utf-8')

    def get_value(self,section,option):
        return self.cf.get(section,option)

    def get_int(self,section,option):
        return self.cf.getint(section,option)

    def get_float(self,section,option):
        return self.cf.getfloat(section,option)

    def get_boolean(self,section,option):
        return self.cf.getboolean(section,option)

if __name__ == '__main__':
    res=ReadConfig('case.conf').get_boolean('TeacherInfo','age')
    print(res)
