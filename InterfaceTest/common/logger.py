import logging
from InterfaceTest.common import contants
def get_logger(name):
    #logger=logging.getLogger()###默认输出渠道控制台，默认级别：error以上
    logger=logging.getLogger(name)
    logger.setLevel('DEBUG')###设置级别  大开关

    fmt="%(asctime)s- %(name)s -%(levelname)s -%(message)s - [%(filename)s:%(lineno)d]"
    formatter=logging.Formatter(fmt=fmt)##输出格式


    console_handler=logging.StreamHandler()##控制台
    ##把日志级别放到配置文件去，去配置
    console_handler.setLevel("DEBUG")###设置
    console_handler.setFormatter(formatter)

    file_handler=logging.FileHandler(contants.log_dir+"/case.log",encoding='utf-8')##文件
    file_handler.setLevel("DEBUG")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
logger=get_logger("case")
logger.info("测试开始了")
logger.error("测试报错了")
logger.debug("测试数据")
logger.info("测试结束")






