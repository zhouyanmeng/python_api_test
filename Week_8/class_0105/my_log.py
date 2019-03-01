# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 15:21
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : my_log.py
#自己写的日志类
import logging

class MyLog:

    def my_log(self,level,msg):
        #写一个属于自己的日志系统
        #收集器---创建一个日志收集器 getLogger 函数
        my_logger=logging.getLogger('python13')#创建一个日志收集器
        my_logger.setLevel('DEBUG')#给这个日志收集器 setLevel()


        #格式：规定日志输出的格式
        formatter = logging.Formatter('%(asctime)s-'
                                      '[%(levelname)s]-'
                                      '[line:%(lineno)d]-'
                                      '[日志信息]:%(message)s')
        #输出渠道--指定输出渠道
        ch=logging.StreamHandler()#创建一个输出到控制台的渠道
        ch.setLevel('DEBUG')#渠道设置级别
        ch.setFormatter(formatter)

        #输出到之指定的文件  文件路径 绝对路径 相对路径 都可以用
        fh=logging.FileHandler('python13.log',encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)


        #对接 日志收集器与输出渠道 进行对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        if level=='DEBUG':
          my_logger.debug(msg)
        elif level=='INFO':
          my_logger.info(msg)
        elif level=='WARNING':
          my_logger.warning(msg)
        elif level=='ERROR':
          my_logger.error(msg)
        else:
            my_logger.critical(msg)

        #去掉日志的重复 每次收集完毕之后 记得移除掉日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):#输出一条debug级别的信息
        self.my_log('DEBUG',msg)

    def info(self,msg):
        self.my_log('INFO',msg)

    def warning(self,msg):
        self.my_log('WARNING',msg)

    def error(self,msg):
        self.my_log('ERROR',msg)

    def critical(self,msg):
        self.my_log('CRITICAL',msg)

if __name__ == '__main__':
    my_logger=MyLog()
    my_logger.debug('我叫娟娟')
    my_logger.error('不交作业的同学太危险了！！！')