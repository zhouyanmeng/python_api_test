####导入模块的学习
##除了顶级目录，一层一层的去丁文，相对于当前模块，当前模块就是正在写代码的模块：Class_2_import
import os##导入，为什么要导入呢？？
#.py结尾的可以叫做python文件，也可以叫做模块  模块跟模块之间是独立的


##导入的方式1： import 模块名
##具体到模块名，不需要.py这个后缀  除了顶级项目名称，一层一层的去定位你要用的模块
##到那时python_15以外的不能导入，python_15下的全部都能导入
import Week_3.Class_0228.Add
Week_3.Class_0228.Add.addfunction(1,3)

# import Week_2.Class_0221.Function

##导入的方式2： import 模块名  as newname
import Week_3.Class_0228.Add as AT
AT.addfunction(1,3)


##导入的方式3： from..import ..   import后面可以具体到模块名以及函数名以及类名
from Week_3.Class_0228.Add import  addfunction
addfunction(5,6)
from Week_3.Class_0228 import Add
Add.addfunction(5,6)
Add.sub_funcrion(7,5)
##导入的方式4： from..import *   import后面可以具体到模块名以及函数名以及类名
from Week_3.Class_0228.Add import  *
addfunction(5,6)
sub_funcrion(7,3)

from Week_3.Class_0228.Add import addfunction as ad
ad(12,12)  #调用addfunction方法