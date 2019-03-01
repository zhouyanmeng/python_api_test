####单元测试
#类：属性 方法
#属性 类属性 对象属性
#方法 类方法 静态方法 对象方法

##单元测试谁做？  开发可以做，测试也可以做
##单元测试时做什么呢？？-->对某个功能去做测试-->每一个功能都是封装在类里面-->类：属性+方法
##-->单元测试测试什么？？-->测试方法-->创建对象，调用方法 传参-->通过传递多组数据，来额测试不同的情况

##框架-->unittest-->pytest(更高级)
#python unittest 单元测试
#loader   result runner suite  case  5大类  5个文件夹
#case：TestCase：SetUp()  teaarDown()  run(result)
#suite:TestSuite:self._tests=[]   run(result)   收集测试用例  从TestCase收集
#loader：TestLoader：测试加载:::case,suite  加载用例   2个路径加载用例
#runner：Test TestRunner  TestTestResult
#result:TestResult::出测试报告


#写用例case TestCase用来写用例
import unittest
from Week_6.Class_0321.math_MathMethod import MathMethod
class TestMathMethod(unittest.TestCase):#测试类   继承unittest.TestcCase类
    #没有测试用例，测试用例需要测试自己加
    #测试用例标注：test开头
    def test_001(self):##1test开头
        expect=0##2预期值
        respect=MathMethod().add(0,0)##3实际值      ##类调用方法 类名().方法
        #断言
        self.assertEqual(expect,respect)##4断言比较

    def test_002(self):
        expect=-1
        respect=MathMethod().add(1,-2)
        self.assertEqual(expect,respect)