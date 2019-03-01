##相对路径
import os

# base_dir=os.path.abspath(__file__)##当前文件的绝对路径
# base_dir=os.path.dirname(os.path.abspath(__file__))##common的地址
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))##Interface的地址
print(base_dir)


##取data下面的Testcase
case_file=os.path.join(base_dir,'data','Testcase.xlsx')##
print(case_file)

global_file=os.path.join(base_dir,'config','global.conf')
print(global_file)

online_file=os.path.join(base_dir,'config','online.conf')
print(online_file)

test_file=os.path.join(base_dir,'config','test.conf')
print(test_file)

log_dir=os.path.join(base_dir,'log')
print(log_dir)
case_dir=os.path.join(base_dir,'testcase')
print(case_dir)
report_dir=os.path.join(base_dir,'report')
print(report_dir)