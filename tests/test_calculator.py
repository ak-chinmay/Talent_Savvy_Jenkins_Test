import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
from calculator_utils.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.cal = Calculator()

    def test_add(self):
        self.assertEqual(self.cal.add(2, 3), 5)
        self.assertEqual(self.cal.add(-1, 1), 0)
    def test_add_invalid_value(self):
        self.assertEqual(self.cal.subtract(13, None), None)

    def test_subtract(self):
        self.assertEqual(self.cal.subtract(5, 3), 2)
        self.assertEqual(self.cal.subtract(10, 20), -10)

    def test_subtract_invalid_value(self):
        self.assertEqual(self.cal.subtract(5, None), None)

    def test_multiply(self):
        self.assertEqual(self.cal.multiply(4, 3), 12)
        self.assertEqual(self.cal.multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(self.cal.divide(10, 2), 5)
        self.assertEqual(self.cal.divide(9, 3), 3)
        with self.assertRaises(ValueError):
            self.cal.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
