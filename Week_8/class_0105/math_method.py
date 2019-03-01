# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 20:06
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : math_method.py
class MathMethod:

    # def __init__(self,a,b):#注释掉了
    #     self.a=a
    #     self.b=b

    def add(self,a,b):#对象
        return a+b

    def sub(self,a,b):
        return a-b

    def a_b_s(self,a,b):#返回差的绝对值
        return abs(a-b)

    @staticmethod
    def send_msg(content):
        print('Python13的人真是6666啊，自己不好好听课，专要老师重复讲，{}'
              .format(content))

class SuperMathMethod(MathMethod):
    def count_sale(self):
        print('该方法可以计算销售额')


if __name__ == '__main__':
    MathMethod.send_msg('下次要打手板！')
    # MathMethod(1,2,3,4,5,6,7,8).add()

    t=SuperMathMethod(4,5)
    print(t.add())
    print(t.sub())
