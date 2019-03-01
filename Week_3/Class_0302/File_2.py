##已经学习：识别路径，新建文件夹/目录/拼接路径
#1>只读，文件一定要存在，不存在不能读，不能新建文件
#2>只读，有中文，编码格式utf-8
#3>r+,可以进行读写文件，但是读写的前提，这个文件一定要存在，写入的内容一定是显示在最后面
#4>r+,不读，直接写，覆盖写在最前面，逐字覆盖写，把之前的文字覆盖掉
#5>r+,读写，写在最后，不覆盖任何文字，类似拼接
#6>写在指定位置：tell(）获取光标当前的位置)   seek(offset偏移量，where偏移位置)  偏移光标/位置
#offset  0  3 6 9   偏移几个位置
#where 0头部  1当前位置   2尾部
#7>只写w 没有读权限，只能写，是清空写，如果文件存在，清空写，如果文件不存在，新建文件，在写
#8>w+,可以读，但是打开文件的那一刻就全部删除了，只能写完之后再读，可以写，但是清空写，如果文件存在，清空写，如果文件不存在，新建文件，在写
#9>  a只写不读，，写不清空，写在最后，文件存在就写，不存在新建在写


####1文件的新建
##open()##新建文件的操作   txt  log   配置文件使用较多   文本文件
##获取文件的操作权限，然后进行读或者写的操作
##1获取当前模块同级下的文件
# file=open('python15.txt',encoding='utf-8')
# res=file.read()
# print(res)

##获取不同文件下的文件
# file=open('../Class_0228/python15.txt',encoding='utf-8')
# #绝对路径
# #file=open('E:\Pythontesting\python_15\Week_3\Class_0228\python15.txt',encoding='utf-8')
# res=file.read()
# print(res)
##file.write('888')###io.UnsupportedOperation: not writable

# file=open('python15.txt',encoding='utf-8')
# #file=open('python16.txt',encoding='utf-8')  FileNotFoundError: [Errno 2] No such file or directory: 'python16.txt'
# #res=file.read(10)##读取前多少个字符（长度）
# res=file.readline()###读取某一行
# print(res)
# file.close()
#file.write('888')###io.UnsupportedOperation: not writable
####2读取
####3写入数据
#r   只读  只读，如果我们要进行读或者写的文件里面有中文，那么就要设置编码为utf-8
#r+  读写
# file=open('python16.txt','r+',encoding='utf-8')
# #file=open('python16.txt',encoding='utf-8')  FileNotFoundError: [Errno 2] No such file or directory: 'python16.txt'
# res=file.read(10)##读取前多少个字符（长度）
# print(res)
# res=file.write('小明，小明，呼叫小明！！！')###写在最后
# file.close()

##不读直接写：：：：写在开头，覆盖写
# file=open('python15.txt','r+',encoding='utf-8')
# #file=open('python16.txt',encoding='utf-8')  FileNotFoundError: [Errno 2] No such file or directory: 'python16.txt'
# res=file.write('小明，小明，呼叫小明！')###写在最后
# file.close()

##写在指定位置
# file=open('python15.txt','r+',encoding='utf-8')
# res=file.read(10)##读取前多少个字符（长度）
# print(file.tell())##光标位置：：：：汉字占3位，其他占1位
# print(res)
# file.write('小明，小明，呼叫小明！')
# file.seek(0,0)
# print(file.tell())##光标在最后
# print(file.read())
##偏移
# file=open('python15.txt','r+',encoding='utf-8')
# res=file.read(10)##读取前多少个字符（长度）
# print(file.tell())##光标位置：：：：汉字占3位，其他占1位
# print(res)
# # file.write('小明，小明，呼叫小明！')
# #file.seek(2,0)####如果是2的话报错，，##UnicodeDecodeError: 'utf-8' codec can't decode byte 0x97 in position 0: invalid start byte
# file.seek(3,0)
# print(file.tell())
# print(file.read(1))###从外开始读取
# file.close()
#w   只写  清空写
#file=open('python15.txt','w',encoding='utf-8')
# print(res)
# res=file.write('小明，小明，呼叫小明！')
# file.close()
###如果文件不存在，新建文件写
# file=open('python16.txt','w',encoding='utf-8')
# # res=file.read()##io.UnsupportedOperation: not readable
# # print(res)
# res=file.write('小明，小明，呼叫小明！')
# file.close()

#w+  读写
# file=open('python15.txt','w+',encoding='utf-8')
# file.write('小明虾米')
# file.seek(0,0)##写完了光标就在最后了，所以要偏移才能读取到内容
# print(file.read())
# file.close()

#a   追加   只能写，不能读，但是不能把已经有的内容清空，写在最后
# file=open('python15.txt','a',encoding='utf-8')
# file.write('---小明虾米')
# # file.seek(0,0)##写完了光标就在最后了，所以要偏移才能读取到内容
# #print(file.read())##io.UnsupportedOperation: not readable
# file.close()

#a+  读追加
file=open('python15.txt','a+',encoding='utf-8')
file.write('---小明虾米')
# file.seek(0,0)##写完了光标就在最后了，所以要偏移才能读取到内容
#print(file.read())##io.UnsupportedOperation: not readable
file.close()


##rb,rb+,wb，wb+,ab,ab+,##文件流的形式去写入文件的时候，binary











