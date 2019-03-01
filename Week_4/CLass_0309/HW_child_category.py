# 2:写一个子类，继承1 这个父类，且添加函数：discount 打折扣用的
# pay_money 支付餐，重写 open_restaurant() ，并完成子类完成调用
from Week_4.CLass_0309.HomeWork import Restaurant
class rest(Restaurant):
    def Discont(self):
        print("就餐可以打9.5折")
    def Pay_Money(self):
        print("新建支付还是支付宝，或者微信都可以")
    def Open_Restaurant(self):
        print('餐厅正在营业！！！,今日至营业到9点！！！')

if __name__ == '__main__':
    t=rest('王小二的烧烤店','烧烤')###初始化参数，未单独初始化参数，全部调用的父类
    print(t.restaurant_name)##调用父类的属性
    print(t.cooking_type)##调用父类的属性
    t.Describe_Restaurant()###调用父类的方法
    t.Open_Restaurant()###调用重写的方法，调用的是自己的方法，不在调用父类的方法
    t.Pay_Money()###调用子类自己的方法