class BoyFriend:
    '''这是一个男朋友类，主要是来用来描述男朋友这一类人'''
    #属性
    sex='boy'
    height='170'
    #方法--->90%的相似度与函数
    @staticmethod###静态方法跟函数100%相同
    ###如果有这样一个方法，它跟类里面的属性，函数没有任何关联的时候，用不到他们的时候，可以定义为静态方法
    def Coding(language):##language是位置参数，如果说是language='python’此时language就是默认参数
        print('男朋友都会写{}代码'.format(language))##1>类有self，占坑的，2>方法属于类   在类里面的叫类，不在类里面的叫方法
    def Cooking(self,*args):##动态参数
        dish_name=''##初始化
        for item in args:##遍历args这个元组
            dish_name+=item
            dish_name+=','
        print('会做饭，而且擅长{}'.format(dish_name))



    @classmethod
    def Play_Basketball(cls):##调用这个方法的时候，会把类作为参数传进来--->@classmethod。cls类方法的特征
        print('最喜欢打篮球')
        print('我男朋友的性别是：{}'.format(cls.sex))
        cls.Coding()###不行类不能调用对象方法
        cls.Play_Basketball()
        cls().Coding()##行，现在据说对象调用了
    def print_self(self):###对象方法，只能对象来调用
        print('self:',self)##<__main__.BoyFriend object at 0x0352DE10>
#self？？
#在类外面，类里面的属性和方法，谁可以调用--->类实例化的对象
# x=BoyFriend()
# x.print_self()###self调用这个方法的对象本身
# print(x)


##对象方法L必须有对象来进行调用
##类方法：类可以调用，对象也可以调用  @classmethod，参数：cls
BoyFriend.Play_Basketball()####类调用
BoyFriend().Play_Basketball()####对象调用
##静态方法：类可以调用，对象也可以调用  @statemethod在装饰
BoyFriend.Coding('Python')
BoyFriend().Coding('JAVA')


###对象方法，类方法，静态方法
###为什么会有对象方法
###什么时候使用

###有什么区别
#1>对象可以调用所有的方法：：：对象方法，静态方法，类方法
#2>类只能调用类方法，静态方法
#3>修饰符不同：
#4>对象方法里面可以调用所有类的方法，属性，可以调用类方法，静态方法
#5>类方法可以调用属性，使用cls.来调用
#6>静态方法不能调用类的属性，方法，因为没有属性，没有对象，，，一定要调用可以通过类