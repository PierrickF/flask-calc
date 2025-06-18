import unittest
from app import add, subtract, multiply, divide

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(add(2, 3), 5, "The sum is wrong.")

    def test_diff(self):
        self.assertEqual(subtract(3, 2), 1, "The difference is wrong.")

    def test_product(self):
        self.assertEqual(multiply(2, 3), 6, "The product is wrong.")

    def test_quotient(self):
        self.assertEqual(divide(6, 3), 2, "The quotient is wrong.")

if __name__ == "main":
    unittest.main()
