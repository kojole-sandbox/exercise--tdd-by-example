import unittest


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        cases = [
            [0, 0],
            [1, 1],
            [2, 1],
            [3, 2],
            [4, 3],
        ]
        for case in cases:
            self.assertEqual(fib(case[0]), case[1])
