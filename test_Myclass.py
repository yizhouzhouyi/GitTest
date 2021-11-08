import unittest   #单元测试模块
from BeautifulReport import BeautifulReport as bf  #导入BeautifulReport模块，这个模块也是生成报告的模块
from multify import multi, add


class TestCalc(unittest.TestCase):

    def testcc(self):
        '''这是第一个测试用例'''
        self.assertEqual(1, 1)
        print('第一个用例')

    def testaa(self):
        '''这是第二个测试用例'''
        self.assertEqual(1, 1)
        print('第二个用例')

    def testdd(self):
        '''这是第三个测试用例'''
        self.assertEqual(1, 9)
        print('第三个用例')

    def testbb(self):
        '''这是第四个测试用例'''
        print('第四个用例')

    def testmulti23(self):
        '''这是第五个测试用例'''
        self.assertEqual(multi(2, 3), 6)

    def testmulti34(self):
        '''这是第六个测试用例'''
        self.assertEqual(multi(3, 4), 10)

    def testadd23(self):
        '''这是第七个测试用例'''
        self.assertEqual(add(2,3), 4)

    def testadd78(self):
        '''这是第八个测试用例'''
        self.assertEqual(add(7,8), 15)

    def testadd19(self):
        '''这是第九个测试用例'''
        self.assertEqual(add(1, 9), 10)


suite = unittest.TestSuite()  #定义一个测试集合
suite.addTest(unittest.makeSuite(TestCalc))  #把写的用例加进来（将TestCalc类）加进来
run = bf(suite) #实例化BeautifulReport模块
run.report(filename='test', description='这个描述参数是必填的')