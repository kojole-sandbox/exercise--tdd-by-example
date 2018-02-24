import unittest

from money.dollar import Dollar


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(product.amount, 10)
        product = five.times(3)
        self.assertEqual(product.amount, 15)
