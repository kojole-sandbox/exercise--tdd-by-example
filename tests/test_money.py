import unittest

from money.dollar import Dollar


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        self.assertEqual(five.times(2), Dollar(10))
        self.assertEqual(five.times(3), Dollar(15))

    def test_equality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(6))
