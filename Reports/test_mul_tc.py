import unittest
from calc import CalcClass


# 测试乘法
class TestMulClass(unittest.TestCase):

    def setUp(self):
        self.run = CalcClass()

    def test_mul_success_001(self):
        data = self.run.mul(1, 2)
        self.assertEqual(data, 1)

    def test_mul_success_002(self):
        data = self.run.mul(3, 2)
        self.assertEqual(data, 6)