# 3-16 定义一个配置类，实现配置文件的数据读取。
# 如题。利用configParser类来实现自己的功能封装。
#
# 可参考课堂上的类定义。也可以再扩展。
from configparser import ConfigParser
class MyConfig:
    def __init__(self,con_fileparth):
        #打开配置文件
        self.cf=ConfigParser()#
        self.cf.read(con_fileparth,encoding='utf-8')
    def get_sections(self):##获取section
        return self.cf.sections()

    def get_options(self,section):#获取option
        return self.cf.options(section)

    def getint_Value(self,section,option):#获取值int类型
        return self.cf.getint(section,option)

    def getfloat_Value(self,section,option):
        return self.cf.getfloat(section,option)

    def getboolean_Value(self,section,option):
        return self.cf.getboolean(section,option)

    def get_str(self,section,option):
        return self.cf.get(section,option)

if __name__ == '__main__':
    mycon=MyConfig("class_config.cfg")
    print(mycon.get_sections())##获取section
    print(mycon.get_options("login"))##获取section下login的option

    #getin password=123456
    mypassword=mycon.getint_Value("login","password")
    print(type(mypassword))##int
    print(mypassword)

    ##getfloat hiht=165.54
    myhight=mycon.getfloat_Value("student","hight")
    print(type(myhight))
    print(myhight)

    #getBoolen    ##excel
    mybool=mycon.getboolean_Value("hobby","excel")
    print(type(mybool))
    print(mybool)

    # #getvalue
    myvalue=mycon.get_Value("login","password")
    print(type(myvalue))
    print(myvalue)
