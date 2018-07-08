
import unittest, prob002

class TestProb002(unittest.TestCase):
    def test_prob002_given1(self):
        arr = [1, 2, 3, 4, 5]
        expected = [120, 60, 40, 30, 24]
        self.assertEqual(prob002.calc_with_division(arr), expected)
        self.assertEqual(prob002.calc_no_division(arr), expected)

    def test_prob002_given2(self):
        arr = [3, 2, 1]
        expected = [2, 3, 6]
        self.assertEqual(prob002.calc_with_division(arr), expected)
        self.assertEqual(prob002.calc_no_division(arr), expected)

    def test_prob002_non_monotonic(self):
        arr = [22, 42, 6, 7, -3]
        expected = [-5292, -2772, -19404, -16632, 38808]
        self.assertEqual(prob002.calc_with_division(arr), expected)
        self.assertEqual(prob002.calc_no_division(arr), expected)

    def test_prob002_no_overflow(self):
        arr = [10000, 20000, 30000, 40000, 50000]
        expected = [1200000000000000000, 600000000000000000, 400000000000000000, 300000000000000000, 240000000000000000]
        self.assertEqual(prob002.calc_with_division(arr), expected)
        self.assertEqual(prob002.calc_no_division(arr), expected)
    
    def test_prob002_empty(self):
        arr = []
        expected = []
        self.assertEqual(prob002.calc_with_division(arr), expected)
        self.assertEqual(prob002.calc_no_division(arr), expected)

    def test_prob002_one_item(self):
        arr = [3]
        expected = [1]
        self.assertEqual(prob002.calc_with_division(arr), expected)
        self.assertEqual(prob002.calc_no_division(arr), expected)

    def test_prob002_two_item(self):
        arr = [3, 2]
        expected = [2, 3]
        self.assertEqual(prob002.calc_with_division(arr), expected)
        self.assertEqual(prob002.calc_no_division(arr), expected)

if __name__ == '__main__':
    unittest.main()
