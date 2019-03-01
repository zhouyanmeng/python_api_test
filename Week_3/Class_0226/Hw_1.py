# 1、请编程实现字符串的转换：将”sdSdsfdAdsdsdfsfdsdASDSDFDSFa”字符串大写变小写，小写变大写。
# 并且将字符串变为镜像字符串。 例如：字符串里面的’A’变为’Z’,’b’变为’y’ ，镜像的意思就是照镜子，对比了解下。
s='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
inpstr='adcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
outstr='zyxwvutsrqponmlkjihgfedcdaZYXWVUTSRQPONMLKJIHGFEDCBA'
new = s.maketrans(inpstr,outstr)
s2 = s.swapcase() 
s3 = s2.translate(new)
print('原字符串是：'+s)
print('大小写对换后是：'+s2)
print('镜像字符是：'+s3)


# 2：搜索引擎中会对用户输入的数据进行处理，
# 第一步就是词法分析，分离字符串中的数字、中文、拼音、符号。
# 比如这个字符串： 我的是名字是lemon,今年5岁。
# 语法分析后得到结果如下：
# 数字：5
# 中文：我的名字是、今年、岁
# 拼音：lemon
# 符号：，。 请编写程序实现该词法分析功能。
import string
s=input('请输入数据：')
new_english=new_number=new_kong=new_str=new_biao=' '
for i in s:
    if i in string.ascii_letters:
        new_yinwen=new_english+i
    elif i.isdigit():
        new_number =new_number+i
    elif i.isspace():
        new_kong=new_kong+i
    elif i.isalpha():
        new_str=new_str+i
    else:
        new_biao=new_biao+i
print('''英文有:{}
数字有:{}
空格有:{}
汉字有:{}
标点符号有:{}'''.format(new_english,new_number,new_kong,new_str,new_biao))