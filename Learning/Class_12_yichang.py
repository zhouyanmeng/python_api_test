####异常处理
#1>try...except
#2>try...except 错误类型  as a
#3>tyr...except  finally
#4>try...except...else
#5>with...open...as...上下文管理器




##异常::程序运行的过程中出现的问题错误，都可以称之为异常
#出错的文件，行数，具体的代码，错误类型，错误信息
#print(a)#NameError: name 'a' is not defined

# file=open('test.txt','w')
# # res=file.read()
# # print(res)##io.UnsupportedOperation: not readable

#代码从上往下运行，程序一旦报错，就不在往下执行

##异常处理：当程序运行出现异常的时候，对异常进行处理
# file=open('test.txt','w')
# try:
#     res=file.read()
# except:
#     pass
# print("晚上好")

####1try: ...except:
#try:
    #监控的代码块
#except：
    #如果监控的代码块出现问题，怎么处理，，处理方法

####2try:....except:... 错误类型 as e....
# print(a)##NameError: name 'a' is not defined
##错误类型：：基类  BaseException，exception常规错误额基类
##BaseException所有异常的基类
##Exception常规错误的基类
##BaseException Exception  万能的 缺点：逢错必抓，有内耗   优点：绝对不会放过一个问题，会把所有问题全部抓住
#定位异常，处理什么类型的异常，明确你的错误类型，方便定位问题
#BaseException
# try:
#     file=open('test.txt','w',encoding='utf-8')
#     print("读操作之前")
#     res=file.read()
#     print("读操作之后")
#     print('读操作获取的结果：{0}'.format(res))
# except BaseException as e:###错误类型：BaseException
#     file.write('读取操作报错啦::{0}'.format(e))###写到file里面去 ，错误信息
#     print('读操作报错啦')
# print("晚上好")

#Exception
# try:
#     file=open('test.txt','w',encoding='utf-8')
#     print("读操作之前")
#     res=file.read()
#     print("读操作之后")
#     print('读操作获取的结果：{0}'.format(res))
# except Exception as e:###错误类型：BaseException
#     file.write('读取操作报错啦::{0}'.format(e))###写到file里面去 ，错误信息
#     print('读操作报错啦')
# print("晚上好")

#NameError  住不到，运行还错误，
# try:
#     file=open('test.txt','w',encoding='utf-8')
#     print("读操作之前")
#     res=file.read()
#     print("读操作之后")
#     print('读操作获取的结果：{0}'.format(res))
# except NameError as e:###错误类型：BaseException
#     file.write('读取操作报错啦::{0}'.format(e))###写到file里面去 ，错误信息
#     print('读操作报错啦')
# print("晚上好")


#IOError  住不到，运行还错误，
# try:
#     file=open('test.txt','w',encoding='utf-8')
#     print("读操作之前")
#     res=file.read()
#     print("读操作之后")
#     print('读操作获取的结果：{0}'.format(res))
# except IOError as e:###错误类型：BaseException
#     file.write('读取操作报错啦::{0}'.format(e))###写到file里面去 ，错误信息
#     print('读操作报错啦')
# print("晚上好")



#try...except...finally（finially里面的一定会执行，写到文件里）
##无论你是运行try还是except，最后一定会运行finally
##什么时候用？？
# try:
#     file=open('test.txt','w',encoding='utf-8')
#     print("读操作之前")
#     res=file.read()
#     print("读操作之后")
#     print('读操作获取的结果：{0}'.format(res))
#     TestResult=':Pass'
# except IOError as e:###错误类型：BaseException
#     TestResult = ':Fail'
#     file.write('读取操作报错啦::{0}'.format(e))###写到file里面去 ，错误信息
#     print('读操作报错啦')
# finally:##一定要执行 写到文件里
#     file.write(TestResult)
#     file.write('我执行完毕了，我是finally')###写到file里面去 ，错误信息
# print("晚上好")

#try...except...else
#else  try跟else一起的，，，try不出错的时候执行，try出错的时候不执行
try:
    file=open('test.txt','w+',encoding='utf-8')
    print("读操作之前")
    res=file.read()
    print("读操作之后")
    print('读操作获取的结果：{0}'.format(res))
    TestResult=':Pass'
except IOError as e:###错误类型：BaseException
    TestResult = ':Fail'
    file.write('读取操作报错啦::{0}'.format(e))###写到file里面去 ，错误信息
    print('读操作报错啦')
else:##一定要执行 写到文件里
    file.write(TestResult)
    file.write('我执行完毕了，我是finally')###写到file里面去 ，错误信息
print("晚上好")


##try...except..else  与try....except....finally的区别
#else不能不写，不写里面的代码就会是finally，一定会执行写入到文件中
#else里面可以没有代码



