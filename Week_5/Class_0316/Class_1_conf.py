from configparser import ConfigParser
#你这个类要提供什么功能
#前提：打开配置文件
#读取想要的数据：：sections  options   字符串  整数，布尔值 float值
class MyConfig:
    def __init__(self,con_fileparth,encoding='utf-8'):
        #打开配置文件
        self.cf=ConfigParser()
        self.cf.read(con_fileparth)
    def get_sections(self):
        return self.cf.sections()
    def get_options(self,section):
        return self.cf.options(section)
    def getint_Value(self,section,option):
        return self.cf.getint(section,option)
    def getfloat_Value(self,section,option):
        return self.getfloat_Value(section,option)
    def getboolean_Value(self,section,option):
        return self.getboolean_Value(section,option)
    def get_Value(self,section,option):
        return self.get_Value(section,option)

cf=ConfigParser()##对象实例化
##1读取cnf文件：文件路径，文件编码
cf.read("class_config.cfg",encoding='utf-8')
##2读取所有section  返回的是列表
secs=cf.sections()
print(secs)
##3获取某一个section下面option的值
cf.options(secs[0])###方法1
print(cf.options(secs[0]))
print(cf.options("student"))###方法2：取section名

##4获取某一个section下面，某一个option的值   get
print(cf.get("student","name"))####拿出来的都是字符串
#获取int类型
oldage=cf.get("student","age")
print(type(oldage))
print(oldage)

age=cf.getint("student","age")
print(type(age))
print(age)

##获取布尔值类型
resbool=cf.getboolean("hobby","excel")
print(type(resbool))
print(resbool)


##获取float类型值  student hight=165.54
hight=cf.getfloat("student","hight")
print(type(hight))
print(hight)


sex=cf.get("student","sex")
print(eval(sex))###保持原来的列表类型


#写成类
#打开配置文件
#读取当前的数据
#