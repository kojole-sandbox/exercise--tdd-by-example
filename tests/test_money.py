import unittest

from money.money import Money
from money.franc import Franc


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(five.times(2), Money.dollar(10))
        self.assertEqual(five.times(3), Money.dollar(15))

    def test_equality(self):
        self.assertEqual(Money.dollar(5), Money.dollar(5))
        self.assertNotEqual(Money.dollar(5), Money.dollar(6))
        self.assertEqual(Money.franc(5), Money.franc(5))
        self.assertNotEqual(Money.franc(5), Money.franc(6))
        self.assertNotEqual(Money.dollar(5), Money.franc(5))

    def test_franc_multiplication(self):
        five = Money.franc(5)
        self.assertEqual(five.times(2), Money.franc(10))
        self.assertEqual(five.times(3), Money.franc(15))

    def test_currency(self):
        self.assertEqual(Money.dollar(1).currency(), 'USD')
        self.assertEqual(Money.franc(1).currency(), 'CHF')

    def test_differenct_class_equality(self):
        self.assertEqual(Money(10, 'CHF'), Franc(10, 'CHF'))
