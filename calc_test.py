import unittest
import calc

class CalcTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(calc.add(""), 0)

    def test_one(self):
        self.assertEqual(calc.add("1"), 1)

    def test_two(self):
        self.assertEqual(calc.add("2,3"), 5)
