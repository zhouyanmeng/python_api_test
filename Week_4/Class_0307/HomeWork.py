# 1：创建一个名为 Restaurant 的类，其方法 init ()设置两个属性：
# restaurant_name 和 cooking_type。创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，
# 其中前者打印前述两项信息，而后者打印一条消息， 指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
class Restanrant:
    restaurant_name = '二货家美食餐馆'
    cooking_type = '蒸煮'
    def __init__(self,restaurant_name,cooking_type):###也可以默认赋值，这样在调用的时候可以使用默认赋值
        self.restaurant_name=restaurant_name
        self.cooking_type=cooking_type
    def Describe_Restaurant(self,restaurant_name,cooking_type):
        print('这家餐馆的名字是:',restaurant_name)
        print('这家餐馆的主要制作方法是:', cooking_type)

    def Open_Restaurant(self):
        print('餐厅正在营业')
rest=Restanrant('二货家美食餐馆','炒菜')
rest.Describe_Restaurant('二货家美食餐馆','蒸煮')
rest.Open_Restaurant()
# 2:建一个名为 User 的类，其中包含属性 first_name 和 last_name，
# 还有用户简介通常会存储的其他几个属性。
# 在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；再定义一个名为 greet_user()的方法，
# 它向用户发出个性化的问候。
class user:
    first_name='zhou'
    last_name='xiaoyao'
    sex='女'
    age='18'
    work='tester'
    def Describe_User(self,first_name,last_name,sex,age,work):
        print('''这是我的基本信息:'''
              '我姓{}'.format(self.first_name),
              '我叫{}'.format(self.last_name),
              '我是{}'.format(self.sex),
              '我今年{}'.format(self.age),
              '我的工作是：{}'.format(self.work))
    def Greet_User(self):
        print("祝您今天愉快")
user1=user()
user1.Describe_User('zhou', 'xiaoyao', '女', '18', 'tester')
user1.Greet_User()

##   *args代替太多的参数
#     def Describe_User(self, *args):
#         print('我姓；{}，我叫：{}，我是个{}生，我今年{}岁了，我做的工作是{}'.format(*args))
# user2 = user()
# user2.Describe_User('zhou', 'xiaoyao', '女', '18', 'tester')



# 3：思考问题：
#
# #为什么会有对象方法 类方法 静态方法？我什么时候写什么类型的方法呢？
#存在即合理把，类里面的基本属性3个方法
#定义不同，使用的参数，调用的方法都不同

##跟后面学习类的一些属性也有关系，继承，多态，，重写，他们的调用都有关系

# #什么时候用？
#对象方法：有对象的时候使用
##类方法：类方法可以通过类直接调用，所以可以直接通过类调用，不通过对象这个实例

# #写成不同的方法类型 有啥用呢？对我来说有啥用?
##静态方法:只是写在类里面，方便调用，并不调用类里面的任何属性跟方法
##类方法：比对象方法调用领灵活点

# #他们有什么区别呢？ #自己总结一波。
#对象方法：：leiming(self)      对象调用
#类方法：：@classmethod（cls）  类调用，对象调用
#静态方法::@staticmethod()      类调用，对象调用   没有参数