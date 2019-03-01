# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 14:31
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_日志.py

#1：为什么要学习-->日志是什么？为什么要学习？
#在哪一行 哪个文件 错误级别 错误发生的时间
#记录软件/应用程序/代码 的运行日志
#方便我们后期去定位复查问题

#日志里级别有哪几种：
#5种 debug info warning error critical
#从左往右 越来越严重

#2：学好了之后怎么用
#学完了之后再来问

#Python 有一个自带的日志系统 logging
import logging


#root logger 收集日志的容器  如果你不定义一个logger  那么就默认使用root logger
#收集warning以上级别的信息

#handlers   渠道 两种：控制台 console  文本 file_handler  默认渠道就是console
#pre-defined format 按照提前设置好的格式进行输出 --> 级别:日志收集器的名字:日志信息
# logging.debug('这个是一个debug的信息')
# logging.info('这个是一个info的信息')
# logging.warning('这个是一个warning的信息')
# logging.error('这个是一个error的信息')
# logging.critical('这个是一个critical的信息')

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
ch.setLevel('ERROR')#渠道设置级别
ch.setFormatter(formatter)

#输出到之指定的文件  文件路径 绝对路径 相对路径 都可以用
fh=logging.FileHandler('python13.log',encoding='utf-8')
fh.setLevel('INFO')
fh.setFormatter(formatter)


#对接 日志收集器与输出渠道 进行对接
my_logger.addHandler(ch)
my_logger.addHandler(fh)

my_logger.debug('这个是一个debug的信息')
my_logger.info('这个是一个info的信息')
my_logger.warning('这个是一个warning的信息')
my_logger.error('这个是一个error的信息')
my_logger.critical('这个是一个critical的信息')
