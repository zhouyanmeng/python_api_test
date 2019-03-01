# 有两行数据，存在txt文件里面：
# url:http://47.107.168.87:8080/futureloan/mvc/api/member/register@mobile:18688773467@pwd:123456
# url:http://47.107.168.87:8080/futureloan/mvc/api/member/recharge@mobile:18688773467@amount:1000
# 请利用上课所学知识，把txt里面的两行内容，写一个函数，返回如下格式的数据：
# [{'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/register','mobile':'18688773467','pwd':'123456'},
#
# {'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge','mobile':'18688773467','amount':'1000'}]
# 请自行copy数据到Python里面，进行完整的分析后，再进行程序的编写！！！！

def fileOpen(file):
    files=open(file)
    res=files.readlines()
    result_list=[]##空列表
    for data_line in res:
        result_dict={}##空字典
        for data_str in data_line.strip('\n').split('@'):
            result_dict[data_str.split(':', 1)[0]] = data_str.split(':', 1)[1]
        result_list.append(result_dict)
    print(result_list)
    files.close()
fileOpen('python_file.txt')









