import unittest
import calc

class CalcTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(calc.add(""), 0)

    def test_one(self):
        self.assertEqual(calc.add("1"), 1)

    def test_two(self):
        self.assertEqual(calc.add("2,3"), 5)

    def test_ten(self):
        self.assertEqual(calc.add("4,5,6,7,8,9,0,11,915,45"), 1010)

    def test_newlines(self):
        self.assertEqual(calc.add("333\n666\n999"), 1998)

    def test_mixed(self):
        self.assertEqual(calc.add("9,10\n11\n12\n13,14"), 69)

    def test_doubledelimiter(self):
        with self.assertRaises(ValueError):
            calc.add("1\n,2")
