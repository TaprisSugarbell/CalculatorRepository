"""
Unit tests for the calculator library
"""

import main
import unittest


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(main.add(2, 2), 4)

    def test_subtraction(self):
        self.assertEqual(main.subtract(4, 2), 2)

    def test_multiplication(self):
        self.assertEqual(main.multiply(10, 10), 100)


if __name__ == '__main__':
    unittest.main()
