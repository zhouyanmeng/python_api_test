def print_msg(*args):##动态参数，
        ##  *解包作用
    # print(args)##(1, 2, 'hello', [321, 123])
    print(args)##1 2 hello [321, 123]

# print_msg(1,2,'hello',[321,123])


a=[1,2,3]
print_msg(a)##([1, 2, 3],)
print(type(a))
print_msg(*a)##(1, 2, 3)
print(type(a))

a=[[1,2,3],[4,5,6]]
print_msg(a)##([[1, 2, 3], [4, 5, 6]],)
print(type(a))
print_msg(*a)##([1, 2, 3], [4, 5, 6])
print(type(a))