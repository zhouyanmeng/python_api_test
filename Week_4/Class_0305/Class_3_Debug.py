####debug

# def add(a,b):
#     c=a+b
#     print(c)
# if __name__ == '__main__':
#     add(1,2)


# 将txt里面的文件按照格式输出
file=open('test_data.txt')
resp=file.readlines()
print(resp)
# l=[]
# for value in resp:
#     value_1=value.strip('\n')
#     value_2=value_1.split('@')
#     # print(value_2)
#     d={}
#     for item in value_2:
#         item=item.split(':',1)
#         print(item)
#         d[item[0]]=item[1]
#     l.append(d)
#     print(l)

s='url:http://XXX.XXX.XXX.XXX:8080/futureloan/mvc/api/member/login@mobilephone:13760246701@pwd:123456'
file=open('test_data.txt')
resp=file.readlines()
# print(resp)
# print(resp[0])
r_1=resp[0].strip('\n')
r_2=r_1.split('@')
# print(r_1)
print(r_2)###列表
# for item in r_2:
#     value=item.