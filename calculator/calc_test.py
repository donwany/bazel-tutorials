import unittest
from calc import Calculator


class TestSum(unittest.TestCase):

    def test_sum(self):
        calculator = Calculator.add(a=1, b=2)
        self.assertEqual(calculator, 3)

    def test_sum_negative(self):
        calculator = Calculator.add(a=-4, b=-11)
        self.assertEqual(calculator, -15)

    if __name__ == "__main__":
        unittest.main()
