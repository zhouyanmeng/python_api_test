###解析正则表达式---查找替换
import re
from InterfaceTest.common.config import config
data = '{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'

# 原本字符,元字符
# p = "#(.*?)#"  # 正则表达式
# p='normal_user'
# p='#(.*?)#'###(开始结束)#（）#  （里面的返回，括号代表组的开始于结束）
# m=re.search(p,data)##从任意位置开始找，找到一个就返回，这样就找不到所有的
# print(type(m),m.group(1))##返回   #开始，#结束 p='#.*#'
# print(m.group())#返回表达式和组里面的内容
# print(m.group(1))#返回指定组的内  group第一个组里面的内容
# g=m.group(1)
# v=config.get('data',g)##拿到参数化的key，根据key取配置文件的值
# print(v)
# ms=re.findall(p,data)###获取全部返回列表
# data=re.sub(p,v,data,count=1)###查找替换
# # 如果要匹配多次，替换多次，使用循环来解决

p = "#(.*?)#"  # 正则表达式
while re.search(p, data):
    print(data)
    m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
    g = m.group(1)  # 拿到参数化的KEY
    v = config.get('data', g)  # 根据KEY取配置文件里面的值
    print(v)
    # 记得替换后的内容，继续用data接收
    data = re.sub(p, v, data, count=1)  # 查找替换,count查找替换的次数

print('最后替换后的data', data)