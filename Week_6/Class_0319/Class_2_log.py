####日志 logging   记录程序代码运行 操作
###主要目的，写一个我们自己的日志类
#logging来写日志类
##等级：debug  info  warming  error  critical/fatal  越来越严重

import logging
##日志:收集 输出

##日志：收集5条，输出3条，debug，info的日志不见了
#日志分收集，输出2块，，收集，什么都收，输出，有区别，只输出info级别以上，（此处不包含info）

#收集-->日志收集器：root默认
#输出-->输出渠道 1》控制台console 2》指定文件file  默认的是console  默认输出info级别以上的logging

logging.debug('this is a debug msg')
logging.info('this is a info msg')
logging.warning("this is a warming msg")
logging.error("this is a error msg")
logging.critical("this is a crirical msg")

###新建日志收集器@@输出渠道@@凭借addHandler  my_logger-->handler 里面

#新建一个日志收集器：getlogger()
#新建指定的输出渠道：
my_logger=logging.getLogger('py15')#名为py15的日志收集器
my_logger.setLevel("DEBUG")

##指定格式
fmt=logging.Formatter()

#指定输出渠道
#指定输出渠道StreamHandler
ch=logging.StreamHandler()##指定输出到conolse控制台
ch.setLevel("DEBUG")#设置级别

ch.setFormatter(fmt)
##指定输出到文本渠道  FileHandler‘##也需要设置级别
file_handler=logging.FileHandler("py15.log",encoding='utf-8')##文件
file_handler.setFormatter(fmt)
##指定格式

#配合关系
my_logger.addHandler(ch)#添加渠道   my_logger收集的全部给ch
my_logger.addHandler(file_handler)
##收集日志
my_logger.debug('this is a debug msg')
my_logger.info('this is a info msg')
my_logger.warning("this is a warming msg")
my_logger.error("this is a error msg")
my_logger.critical("this is a crirical msg")

