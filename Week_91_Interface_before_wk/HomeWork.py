#写一个日志类
#结合配置文件 完成 输出的格式 输出的级别的配置
import logging
from Week_6.Class_0319.CONF import MyConfig
#新建日志收集器
class logger:
    def logger_catalogter(self,logname1,logname2):
        my_logger=logging.getLogger(logname1)##新建收集器
        my_logger.setLevel("DEBUG")#设置收集器级别
            
        #指定格式
        fmt=logging.Formatter('%(asctime)s-%(levelno)s-%(levelname)s-%(filename)s-%(lineno)d-%(threadName)s-%(message)s')
        #指定输入渠道(1)
        output=logging.StreamHandler()##指定输出到控制台
        output.setLevel("DEBUG")
        output.setFormatter(fmt)
        #指定输出到文本(2)
        file_handler=logging.FileHandler(logname2,encoding='utf-8')
        file_handler.setFormatter(fmt)
        #配合关系(关联输入输出)
        my_logger.addHandler(output)##控制台
        my_logger.addHandler(file_handler)#文件
        #收集日志
        my_logger.info("This is a info msg")
        my_logger.debug("This is a debug msg")
        my_logger.warning("This is a warning msg")
        my_logger.error("This is a error msg")
        my_logger.critical("This is a critical msg")
if __name__ == '__main__':
    logger_new=logger()
    logger.logger_catalogter("py15","py15.log","DEBUG")
    print( logger.logger_catalogter("py15","py15.log","DEBUG"))

