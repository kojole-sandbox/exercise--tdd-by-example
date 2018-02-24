import unittest

from money.dollar import Dollar


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEqual(five.amount, 10)
