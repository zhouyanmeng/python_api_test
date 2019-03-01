####反射
'''
类的发射可以动态的查看，增加，删除，更改类或者实例的属性
getattr（Context,'normal_user'）获取类属性的值
setattr(Context,'admin_user','abc')添加属性
hasattr(Context,'admin_user')判断是否有这个额属性
delattr(Context,'admin_user')删除这个属性
'''
class People:
    number_eye=2
    def __init__(self,name,age):
        self.name=name
        self.age=age

if __name__ == '__main__':
    print(People.number_eye)###类属性，不定义对象可以调用
    p=People('xiaoyao',12)
    print(p.number_eye)
    print(p.name)
    print(p.age)
    #添加属性
    print("是否有腿属性",hasattr(People,'number_leg'))##没有返回Fasle，有返回True
    print("是否有眼睛属性",hasattr(People,'number_eye'))##没有返回Fasle，有返回True
    setattr(People,"number_leg",2)###添加属性
    print("是否有腿属性",hasattr(People, 'number_leg'))
    print("新属性：有几条腿:",People.number_leg)###直接使用类调用

    setattr(p,"dance",True)
    print(p.dance)


    getattr(People,"number_leg")###获取嘞属性
    getattr(p, "dance")#获取实例属性

    # delattr(p,"dance")##删除
    # getattr(p, "dance")##在获取，找不到就报错


    setattr(p,"number_eye",3)
    print(p.number_eye)
    print(getattr(p,"number_eye"))
