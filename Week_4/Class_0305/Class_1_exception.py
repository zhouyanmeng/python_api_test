####异常处理
##1什么是异常？
##2为什么要处理异常？
##3怎么处理？？

##1什么是异常？----代码出错了就是异常
##2为什么要处理异常？---防止程序停止运行
##3怎么处理？？

#print(a)##NameError: name 'a' is not defined--错误类型

# s=[1,2,3]
# print(s[4])##IndexError: list index out of range
# d={'name':"zhouzhou","age":28}
#print(d('name'))##TypeError: 'dict' object is not callable
#print(d(['name'])##SyntaxError: unexpected EOF while parsing
#print(d['value'])##KeyError: 'value'
# print(d['name'])

#test()##NameError: name 'test' is not defined

##代码从上往下顺序执行，上面报错了，报错以后的就不会再执行

####(1)try...except     except里面的代码一定会执行
# try:##里面存放重点关注代码
#     print(a)##需要处理代码
# except:
#     print("print:a")

#(2)try...except..具体error类型...as e##捕捉到错误信息   错误指定类型的异常
# try:##里面存放重点关注代码
#     print(a)##需要处理代码
# except NameError as e:##as 后面随便写，一般是error，可以不写
#     print("print:{}".format(e))###错误类型

# try:
#     s=[1,2,3]
#     print(s[4])
# except IndexError as e:
#     print("print:{}".format(e))


###同时处理多条
# try:
#     d={'name':'zhouzhou','hobby':'IT'}
#     print(d['agead'])
# except Exception as e:
#     print("print:{}".format(e))

####3BaseException   Exception
##BaseException>Exception 范围
# try:
#     print(a)
# except BaseException as e:
#     print("print:{}".format(e))


###AssertionError   AttributeError     IndexError
###TypeError  Keyerror   ValueError  NameError   IndentationError


####4try...except...finially
try:
    s=[1,2,3]
    print(s[4])
    print(s)
except Exception as e:
    print('error is {}'.format(e))
finally:###不管try下面的代码是否报错，finially里面的代码一定会执行
    print(s)

####5try...except...else...如果try下面的没有任何异常，执行else，如果有问题，不执行ealse
try:
    s=[1,2,3]
    print(s[4])
except Exception as e:
    print('error is{}'.format(e))
else:##如果try未出现任何异常，就执行else的代码
    print(s)