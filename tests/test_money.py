import unittest

from money.dollar import Dollar


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(product.amount, 10)
        product = five.times(3)
        self.assertEqual(product.amount, 15)

    def test_equality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(6))
