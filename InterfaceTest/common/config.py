import configparser
from InterfaceTest.common import contants
class ReadConfig:##完成配置文件的读取
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(contants.global_file)
        switch=self.config.getboolean('switch','on')##section option
        if switch:
            self.config.read(contants.online_file,encoding='utf-8')
        else:
            self.config.read(contants.test_file,encoding='utf-8')
    def get(self,section,option):
        return self.config.get(section,option)
config=ReadConfig()##实例化
# if __name__ == '__main__':
#     config=ReadConfig()
#     print(config.get('api','pre_url'))