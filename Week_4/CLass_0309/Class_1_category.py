####类与对象
####初始化---封装

#对象方法最常用，一定要有的，对象方法依赖于对象
#静态方法，工具方法，与对象，类无任何关联，不会调用类里面的方法，属性

##对象方法与类方法的区别
##1对象方法一定要创建一个对象，类方法可以直接通过类去调用,类不能调用对象属性


###手机类
#属性
#方法：call  message  video
class phone:
    ##手机属性===>>类属性
    # color='pink'
    # price='4500'
    # brand='iPhone'
    # size='5.5'



    ###参数化--->>魔法方法---初始化方法====>>对象属性
    ##对象属性
    def __init__(self,color,price,brand,size):###我们是调用这个方法
        self.color=color
        self.price=price
        self.brand=brand
        self.size=size
        #cls.color=color###类属性
        ###类的范围大于对象
        ###类的东西，对象可以调用，对象与类都可以调用
        ###对象的东西，类不能调用，只能对象调用



    #方法
    @classmethod
    def Call(cls,tel_no):##打电话
        print('拨号：{}，开始打电话'.format(tel_no))
    def Message(self,tel_no,content):
        print('给{}发送信息：{}'.format(tel_no,content))
    def Watch_TV(self,*args):
        app=''
        for item in args:
            app+=item
            app+=','
        print('可以使用这些app进行看电视，比如：{}'.format(app))
    def Take_shoot(self):
        print('拍照')

    @staticmethod
    def add(a,b):
        print(a+b)
    def Phone_Info(self):###这时候就不用再self了，因为已经赋值给了对象变量了，
        print('颜色:{},品牌{}，价格：{}，尺寸{}'
              .format(self.color,self.brand,self.price,self.size))


if __name__ == '__main__':
    t=phone()##color,price,brand,size   初始化以后一定要传参
    t.add(4,5)###静态方法
    t.Take_shoot()
    t.Watch_TV('爱奇艺','腾讯','优酷')
    t.Message('139384755533','我要去卫生间，内急')
    t.Call('1495995959')
    t.Phone_Info()