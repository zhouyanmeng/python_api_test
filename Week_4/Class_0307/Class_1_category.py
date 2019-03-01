####类与对象
#万物皆对象，对象都是属于具体某个类

#猫类
#叫声 喵喵喵  有尾巴 猫科动物 有胡须 有爪子 抓老鼠  喜欢吃鱼
#爱干净

#男朋友类
#实际男朋友类


####1类的特征，函数没有。只有类有
#继承，封装，重写，多态---->复用性，可重写性，提高复用性

####2语法
class LeiMing:##class 类名：
        '''类的解释文档'''
        #1>类的方法：动作，行为，功能
        #2>类的属性：文字性的特征：身高，体重
##类名的规范：类名也是标识符：：数字，字母，下划线组成，不能以数字开头
##见名知意，不能使用关键字，驼峰命名：ZhouZhou
##怎么变成代码
class BoyFriend:
    '''这是一个男朋友类，主要是来用来描述男朋友这一类人'''
    #属性
    sex='boy'
    height='170'
    #方法--->90%的相似度与函数
    def Coding(self,language):##language是位置参数，如果说是language='python’此时language就是默认参数
        print('男朋友都会写{}代码'.format(language))##1>类有self，占坑的，2>方法属于类   在类里面的叫类，不在类里面的叫方法
    def Cooking(self,*args):##动态参数
        dish_name=''##初始化
        for item in args:##遍历args这个元组
            dish_name+=item
            dish_name+=','
        print('会做饭，而且擅长{}'.format(dish_name))
    def Play_Basketball(self):
        return '最喜欢打篮球'

####万物皆对象---对象肯定是属于 某个类--->类可以产生对象
####创建对象：类名()

t=BoyFriend()###对象  类名（）
##对象具有类的所有的数量跟方法   调用
##对象.属性
##对象.方法
print(t.sex)
print(t.height)
t.Coding('python')
t.Cooking('方便面','蛋炒饭','西红柿')
res=t.Play_Basketball()##有返回值，就用变量存储起来
print(res)
















