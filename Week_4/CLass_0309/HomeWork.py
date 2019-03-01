# 1：创建一个名为 Restaurant 的类，
# 其方法 init ()设置两个属性： restaurant_name 和 cooking_type。
# 创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，
# 其中前者打印前述两项信息，而后者打印一条消息， 指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
class Restaurant:

    def __init__(self,restaurant_name,cooking_type):
        self.restaurant_name=restaurant_name
        self.cooking_type=cooking_type
    def Describe_Restaurant(self):
        print("餐馆名称:{}".format(self.restaurant_name))
        print("餐馆的烹饪方法是:{}".format(self.cooking_type))
    def Open_Restaurant(self):
        print('餐厅正在营业！！！')
if __name__ == '__main__':
    restaurant=Restaurant('二货小吃','炸')
    print(restaurant.restaurant_name)
    print(restaurant.cooking_type)
    restaurant.Describe_Restaurant()
    restaurant.Open_Restaurant()

#
#
# 2:写一个子类，继承1 这个父类，且添加函数：discount 打折扣用的
# pay_money 支付餐费用，重写 open_restaurant() ，并完成子类完成调用
#
# 至于怎么做？可以自由发散，另0307的第一题不用做了，做这一题就OK！

