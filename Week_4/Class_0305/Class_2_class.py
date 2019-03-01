####上下文管理器with open() as file:

file=open('python15.txt','w+',encoding='utf-8')
file.write('今天热老公生气了，怎么哄都哄不好，哎')
file.close()

with open('python15.txt','w+',encoding='utf-8') as file:
    file.write('今天热老公生气了，怎么哄都哄不好，哎')
    ##作用域：在：后面
print(file.close())