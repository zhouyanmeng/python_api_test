####字符串的内置函数
s='pytHonyy'
# s.lower()##小写
# s.maketrans()##翻译函数
# s.join('a')
####replace   替换
###3个参数：第一个参数是目标字符串，第二个是替换的字符串，最后显示什么，第二个是替换次数，默认是全部替换
###替换次数不限制，超过存在的字符就是全部替换，不报错
# res=s.replace('y','@')
# print(res)
#
# res=s.replace('y','@',2)##替换次数
# print(res)

####split切割  返回一个列表，列表里面是字符串类型
#第一个参数，根据指定的字符串进行切割，第二个参数，切割次数,默认全部切割（-1就是默认不切割）
# res=s.split('y')
# print(res)
#
# res=s.split('y',2)
# print(res)
####strip去除
# s='   pytHonyy   '
# res=s.strip()##默认去除头和尾的空格
# print(res)
# print(len(res))
# s='@@@pytHonyy@@@'
# res=s.strip()##默认去除头和尾的空格
# print(res)
# print(len(res))

####swapcase大小写互换
res=s.swapcase()
print(res)

###自己了解函数
s.translate()
s.swapcase()



s.isdigit()##是否为数字