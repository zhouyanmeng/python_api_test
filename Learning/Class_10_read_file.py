####file文件的处理
##file：：txt,日志，，，不包括mp4，excel，html
##处理
##什么时候用：：想用就用

##存储数据的操作
##第一步：打开这个文件open() file
file=open('python12.txt',encoding='UTF-8')##我打开的文件存在在file变量里面
# # print(file.read())##读取文件中的内容,默认把内容一次性读取出来（读取所有内容），，保持格式
# print("************************************")
# print(file.read(5))##读取指定长度的内容，前5个元素
print("************************************")
# print(file.readline())###每次只能读取一行的代码
# print(file.readlines())###按行读取，读完所有行---返回列表  每一行是列表的一个元素
##有中文的时候设置编码为UTF-8
###第一次全部读取，第二次去取部分，第二部分不执行

#读出前十行
# for i in range(1,10):
#     print(file.readline())

#读出前十行
# i=0
# while 1:
#     if i<10:
#         print(file.readline())
#         i+=1
#         continue
#     else:
#         break

#读出5--8行数据
# for i in range(10):
#     if 5<=i<=8:
#         print(file.readline())
#     else:
#         file.readline()


# print(file.read())###打印无换行

for item in file.readlines():###打印有换行
    print(item)