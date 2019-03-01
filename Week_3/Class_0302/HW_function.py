# 1：人和机器进行猜拳游戏写一段程序，首先选择角色：
# 1 曹操 2张飞 3 刘备，然后选择的角色进行猜拳：
# 1剪刀 2石头 3布 玩家输入一个1-3的数字,
# 然后电脑出拳 随机产生1个1-3的数字，
# 提示电脑出拳结果（ 1剪刀 2石头 3布 ） ，双方出拳完毕后：角色和机器出拳对战，
# 对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？
# 按y继续，按n退出。最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
#
# s=input('''1----曹操
# 2----张飞
# 3----刘备
# 请通过输入1,2,3选择一个角色：''')
# print()
import random
role_dict={'1':"曹操",'2':"张飞",'3':"刘备"}
fist_dict={'1':'剪刀','2':"石头",'3':"布"}
##选择角色
while 1:
    role_num=input("请选择角色：1曹操，2张飞，3刘备::")
    if role_num in ['1','2','3']:
        role_name=role_dict[role_num]
        print("您选择的角色是:{}".format(role_name))
        break
    else:
        print("输入的数字只能是1,2,3")
        continue
#玩家出拳
pc_win = 0
human_win = 0
pingju = 0
while 1:
    while 1:
        human_fist_num=input("请选择你的次轮出拳值：1剪刀，2石头，3布::")
        if human_fist_num in ['1','2','3']:
            human_fist_value=fist_dict[human_fist_num]
            print("{}您次轮出拳：{}".format(role_name,human_fist_value))
            break
        else:
            print("输入的数字只能是1,2,3")
            continue
        #pc出拳
    pc_fist_num=random.randint(1,3)
    print("PC出拳为：{}".format(fist_dict[str(pc_fist_num)]))
    #human_fist_num  1  ->PC  2
    #human_fist_num  2  ->PC  3
    #human_fist_num  3  ->PC  1
    if int(human_fist_num) - pc_fist_num in [-2, 1]:
                # human赢
        human_win = human_win+1
        print("{}赢了！".format(role_name))
    elif int(human_fist_num) - pc_fist_num in [-1, 2]:
        pc_win =pc_win+ 1
        print('pc赢了！')
    else:
        pingju =pingju+ 1
        print('双方平局！')
    chose=input("是否要继续出拳：n退出，其他键继续")
    if chose=='n' or chose=='N':
        print("游戏结束")
        break
    else:
        continue

print("{}一共赢了{}局，PC赢了{}局，平局{}局".format(role_name,human_win,pc_win,pingju))























