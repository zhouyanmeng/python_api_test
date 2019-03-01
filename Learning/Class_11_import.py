####模块的导入
 ##导入到当前模块中py来（py就是模块文件）
####import

####from..import
####from..import..as
####from..import *
####import as

##除了顶级目录，要拿到你的目标函数或者文件  需要一层一层的剥开（导入你要引用的文件）
####1 import
import Learning.Class_9
#调用eat函数  也要一层一层
Learning.Class_9.eat('胡萝卜','老坛酸菜')

####2 import as  取别名
##当你导入的文件路径超长的时候：：什么时候适合用
##当你导入的模块名超长的时候
import Learning.Class_9 as python_15
python_15.eat('胡萝卜','老坛酸菜')

####3from ..import..
##import可以具体到函数名以及类名，但是至少要到模块名
from Learning.Class_9 import eat
eat('胡萝卜','老坛酸菜111')
####4from ..import *   模块名里面的函数全部可以调用
from Learning.Class_9 import *
eat('胡萝卜AAA','老坛酸菜AAA')
stuent_info('sd','20','99.99')


####5from ..import as
from Learning.Class_9 import stuent_info as s1####函数名取别名
s1('01','shaiz','9.99')