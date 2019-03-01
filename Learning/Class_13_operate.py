####上下文处理器 with...as...



file=open('test15.txt',"w+",encoding='utf-8')
file.write('如懿传')

##文件是否关闭？？
# print(file.closed)
# file.close()
# print(file.closed)

####上下文处理器
##with...as:主要：后面的执行了，就自动关闭（文件的处理都用with...as...）
with open('test15.txt',"w+",encoding='utf-8')as file:
    file.write('如懿传')

print(file.closed)##只是用来查看是否关闭