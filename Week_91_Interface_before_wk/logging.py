import logging
from Week_91_Interface_before_wk.cfg_work import MyConfig
class mylog(object):
    def __init__(self,cfg_file,cfg_section,cfg_option,lv_sec,lv_opt):
        self.cfg_file=cfg_file
        self.cf=MyConfig(self.cfg_file)
        self.cfg_section=cfg_section
        self.cfg_option=cfg_option
        self.fm=self.cf.get_str(cfg_section,cfg_option)
        self.lv=self.cf.get_str(lv_sec,lv_opt)
    def my_logging(self,logname1,logname2,level,msg):
        #设置自己的日志收集器
        my_logger=logging.getLogger(logname1)##新建收集器
        my_logger.setLevel("DEBUG")
        #设置日志输出格式
        fmt=self.fm
        formatter=logging.Formatter(fmt)
        #设置控制台输出渠道
        kh=logging.StreamHandler()
        kh.setLevel(self.lv)
        kh.setFormatter(formatter)

        #设置指定文件输出渠道
        fh=logging.FileHandler(logname2,encoding='utf-8')
        fh.setLevel(self.lv)
        fh.setFormatter(formatter)

        #日志收集器与渠道对接
        my_logger.addHandler(kh)
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)
    def debug(self,msg):
        self.my_logging('DEBUG',msg)

    def info(self,msg):
        self.my_logging('INFO',msg)

    def warning(self, msg):
        self.my_logging('WARNING', msg)

    def error(self, msg):
        self.my_logging('ERROR', msg)

    def critical(self,msg):
        self.my_logging('CRITICAL',msg)

if __name__ == '__main__':
    log=mylog('log.conf','format_info','formatter','level','lv_2')
    log.debug('一条debug信息')
    log.info('一条info信息')
    log.warning('一条warning信息')
    log.error('一条error信息')
    log.critical('一条critical信息')