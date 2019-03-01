import re
from InterfaceTest.common.config import config
import configparser
class Context:
    loan_id=None

def replace(data):
    p="#(.*?)#"
    while re.search(p,data):
        print(data)
        m=re.search(p,data)
        g=m.group(1)
        try:
            v=config.get('data',g)
        except configparser.NoOptionError as e:##如果配置文件里面没有，去context里面去取
            if hasattr(Context,g):
                v=getattr(Context,g)
            else:
                print("找不到参数化的值")
                raise e
        print(v)
        data=re.sub(p,v,data,count=1)##替换
    print(data)
    return data
