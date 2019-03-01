#####为什么要写file
##存储测试数据
##写入结果
##写日志logging


# def add(a,b):
# #     print(a+b)
# # ##存数据
# # file=open('python16.txt','r')
# # # resp1=file.readline()##读取一行内容，返回字符串形式的数据
# # resp2=file.readlines()##读取所有行，每一行数据是列表一个字符串元素
# # # print(resp1)
# # print(resp2)
# #
# # for item in resp2:
# #     item=item.strip('\n')##返回的是字符串
# #     # print(type(item))
# #     # print(item)
# #     date = item.split(',')
# #     print(date)
# #     add(int(date[0]),int(date[1]))


import requests
file=open('python17.txt','w',encoding='utf-8')
resp=requests.get('http://www.baidu.com')
file.write(resp.text)
file.close()