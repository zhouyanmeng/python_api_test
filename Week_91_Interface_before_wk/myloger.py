
import logging

from Week_91_Interface_before_wk.cfg_work import MyConfig
# mycfg=fcc_Config('mycfg.conf')
# lv=mycfg.get_option('level')
class my_Log:
    def __init__(self,cfg_file,f_section,f_option,lv_sec,lv_opt,):
        self.cfg_file=cfg_file
        self.cf=MyConfig(self.cfg_file)
        self.fm=self.cf.get_str(f_section,f_option)
        self.lv=self.cf.get_str(lv_sec,lv_opt)
    def my_logging(self,level,msg):
        #设置自己的日志收集器
        my_log=logging.getLogger('myroot')
        my_log.setLevel('DEBUG')
        #设置日志输出格式
        fmt = self.fm
        formatter = logging.Formatter(fmt)
        #设置控制台输出渠道
        kh=logging.StreamHandler()
        kh.setLevel(self.lv)
        kh.setFormatter(formatter)
        #设置指定文件输出渠道
        fh=logging.FileHandler('mylog.log',encoding='utf-8')
        fh.setLevel(self.lv)
        fh.setFormatter(formatter)
        #日志收集器与渠道对接
        my_log.addHandler(kh)
        my_log.addHandler(fh)


        if level == 'DEBUG':
            my_log.debug(msg)
        elif level == 'INFO':
            my_log.info(msg)
        elif level == 'WARNING':
            my_log.warning(msg)
        elif level == 'ERROR':
            my_log.error(msg)
        else:
            my_log.critical(msg)

        #去重
        # my_log.removeHandler(kh)
        # my_log.removeHandler(fh)
    def debug(self,msg):
        self.my_logging('DEBUG',msg)

    def info(self,msg):
        self.my_logging('INFO',msg)

    def warning(self,msg):
        self.my_logging('WARNING',msg)

    def error(self,msg):
        self.my_logging('ERROR',msg)

    def critical(self,msg):
        self.my_logging('CRITICAL',msg)

# logging.debug()
if __name__ == '__main__':
    log=my_Log('mycfg.conf','format_info','format_1','level','lv_2')
    log.error('一条error信息')
    log.debug('一条debug信息')
    log.info('一条info信息')
    log.warning('一条warning信息')
    log.critical('一条critical信息')



