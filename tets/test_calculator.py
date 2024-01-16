import unittest
from simplecalculator.simplecalculator.calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
