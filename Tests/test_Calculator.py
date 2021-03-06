import unittest
from Day1.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_find_two(self):
        a = [1721, 979, 366, 299, 675, 1456]
        result = Calculator.find_two(a)
        self.assertEqual(result, 514579, "Should be the same.")

    def test_find_three(self):
        a = [1721, 979, 366, 299, 675, 1456]
        result = Calculator.find_three(a)
        self.assertEqual(result, 241861950, "Should be the same.")


if __name__ == '__main__':
    unittest.main()
