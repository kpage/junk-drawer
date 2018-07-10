
import unittest
from prob005 import car, cdr, cons

class TestProb005(unittest.TestCase):
    def test_car(self):
        expected = 3
        actual = car(cons(3, 4))
        self.assertEqual(actual, expected)

    def test_cdr(self):
        expected = 4
        actual = cdr(cons(3, 4))
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
