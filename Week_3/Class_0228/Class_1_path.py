####路径处理
#1文件的位置
#2新建文件夹
##相对路径 绝对路径
#相对路径：比较而言
#绝对路径：路径唯一

##相对路径   参照物就是自己
file=open('pyhton_15.txt')##打开一个文件
print(file.read())
##相对路径   ..向上走一级
file=open('../pyhton_15.txt')##打开一个文件
print(file.read())
##向上多级
file=open('../../pyhton_15.txt')##打开一个文件
print(file.read())

##绝对路径   转义：：r/R 在引号外面
##\t \n \r  需要转义(r/R) 或者加上\
file=open('E:\Pythontesting\python_15\Week_3\Class_0228\pyhton_15.txt')##打开一个文件
file=open(r'E:\Pythontesting\python_15\Week_3\Class_0228\pyhton_15.txt')##打开一个文件
print(file.read())
print("1**********************************")

##获取路径
#1>右键点击copy path
#2>import os 导入
import os
# path_1=os.getcwd()##获取当前路径，不会具体到模块名
# path_2=os.path.realpath(__file__)###_file_指的是当前文件本身
# path_3=os.path.basename(__file__)###只获取本身文件的文件名
# print(path_1)
# print(path_2)
# print(__file__)
# print(path_3)
# print("2****************************")

###在括号里面写其他文件名
path_2=os.path.realpath(__file__)###_file_指的是当前文件本身
print(path_2)
##可以滴路径进行切割os.path.split(path)  path是路径字符串
#os.mkdir(path)path是路径字符串，新建一个文件夹
##创建一个文件夹
os.mkdir(os.path.join(os.path.split(path_2)[0],'test'))

