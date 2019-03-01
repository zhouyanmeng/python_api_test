##函数的调用,,从上往下顺序执行
def stuent_info(name,classname,offer):
    print("{}期的{}同学拿到了{}K的offer！！！！恭喜恭喜" .format(classname,name,offer))
    eat("玉米",'可乐','周黑鸭')
# def eat(*food_name):##动态参数
#     # print('参数的格式',food_name)###元组，tuple
#     food_name_str=''
#     for item in food_name:
#         food_name_str+=item
#         food_name_str+='，'
#     food_name_str=food_name_str.strip('，')
#     print('最喜欢吃：{}'.format(food_name_str))
# eat('煎饼','火锅','烧烤')
def eat(*food_name):##动态参数
    # print('参数的格式',food_name)###元组，tuple
    food_name_str=''
    for i in range(len(food_name)):
        food_name_str+=food_name[i]
        if i!= len(food_name)-1:
         food_name_str+='，'
    print('最喜欢吃：{}'.format(food_name_str))
#eat('煎饼','火锅','烧烤')

##测试代码会放在这里
##不想影响别的模块调用这个文件，执行代码就放在main下面
if __name__ == '__main__': ###代码执行的入口  只在当前模块文件中运行的时候，执行下面的代码
    stuent_info('13', 'W.', '22')