import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(4, 2), 6)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(7, 3), 4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)
        self.assertEqual(self.calc.multiply(3, 3), 9)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(2, 2), 1)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 3), 2)
        self.assertEqual(self.calc.modulo(7, 2), 1)

if __name__ == '__main__':
    unittest.main()