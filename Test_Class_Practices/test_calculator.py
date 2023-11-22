import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    # "setup" fixed-name funcyion
    # a method inherited from unittest, Testcae
    def setUp(self): #when running, this will always run first
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(7, 3), 4)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(8, 2), 4)

    def test_divide_by_zero(self):  #improtant to test for error
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()