import unittest

from money.dollar import Dollar
from money.franc import Franc


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        self.assertEqual(five.times(2), Dollar(10))
        self.assertEqual(five.times(3), Dollar(15))

    def test_equality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(6))
        self.assertEqual(Franc(5), Franc(5))
        self.assertNotEqual(Franc(5), Franc(6))
        self.assertNotEqual(Dollar(5), Franc(5))

    def test_franc_multiplication(self):
        five = Franc(5)
        self.assertEqual(five.times(2), Franc(10))
        self.assertEqual(five.times(3), Franc(15))
