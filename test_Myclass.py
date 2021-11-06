import unittest
from Myclass_test import Myclass_test

class Test_Myclass(unittest.TestCase):

    def setUp(self):
        self.myclass = Myclass_test(12,12)

    def test_sum(self):
        sum = self.myclass.sum()
        self.assertEqual(24,sum)

    def test_sub(self):
        sub = self.myclass.sub()
        self.assertEqual(0,sub)