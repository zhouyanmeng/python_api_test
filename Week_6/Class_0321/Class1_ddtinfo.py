import unittest
from ddt import ddt,data,unpack
@ddt##装饰类
class TestAdd(unittest.TestCase):

    @data(1,2,3,4,56) ##装饰方法
    def test_001(self,a):
        print(a)