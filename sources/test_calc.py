import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(calc.add2(1, 2), 3)

    def test_add_floats(self):
        self.assertEqual(calc.add2(2.5, 3.5), 6.0)

    def test_add_strings(self):
        self.assertEqual(calc.add2('abc', 'def'), 'abcdef')

    def test_add_string_and_number(self):
        self.assertEqual(calc.add2('abc', 5), 'abc5')

if __name__ == '__main__':
    unittest.main()
