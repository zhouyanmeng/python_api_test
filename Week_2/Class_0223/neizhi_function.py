####内置函数
# print()
# type()
# len()
# input()

####字符串
s='python'
#1首字母大写
s.capitalize()
print(s.capitalize())##首字母大写，其他的全部小写
#2大写
s.upper()
print(s.upper())
#3小写
s.lower()
print(s.lower())
#4count   找某一个字符串出现几次
# s.count()
print(s.count("s"))
#5find   找搜索字符第一个出现的索引位置，，找不到返回-1,
#6index   寻找子字符串第一次出现的索引位置，返回索引位置，没找到报错
#7islower  判断字符串是否是小写，返回值是boolen
#8ispper
#9 isdigit   返回值boolen   判断是纯数字
#10 join   插入
s='python'
res='@'.join(s)
print(res)