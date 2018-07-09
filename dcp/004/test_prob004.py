import unittest, prob004

class TestProb004(unittest.TestCase):
    def test_prob004_given1(self):
        expected = 2
        self.assertEqual(prob004.find_missing_int_naive([3, 4, -1, 1]), expected)
        self.assertEqual(prob004.find_missing_int_fast([3, 4, -1, 1]), expected)

    def test_prob004_given2(self):
        expected = 3
        self.assertEqual(prob004.find_missing_int_naive([1, 2, 0]), expected)
        self.assertEqual(prob004.find_missing_int_fast([1, 2, 0]), expected)

    def test_prob004_complete(self):
        expected = 4
        self.assertEqual(prob004.find_missing_int_naive([1, 2, 3]), expected)
        self.assertEqual(prob004.find_missing_int_fast([1, 2, 3]), expected)

    def test_prob004_empty(self):
        expected = 1
        self.assertEqual(prob004.find_missing_int_naive([]), expected)
        self.assertEqual(prob004.find_missing_int_fast([]), expected)

    def test_prob004_multiple_missing(self):
        expected = 4
        self.assertEqual(prob004.find_missing_int_naive([-4, 1, 3, 2, 5, 7, 0, -3]), expected)
        self.assertEqual(prob004.find_missing_int_fast([-4, 1, 3, 2, 5, 7, 0, -3]), expected)

    def test_prob004_signed_zero(self):
        expected = 2
        self.assertEqual(prob004.find_missing_int_naive([-1, 0, 1, 3]), expected)
        self.assertEqual(prob004.find_missing_int_fast([-1, 0, 1, 3]), expected)

    def test_prob004_array_bounds(self):
        expected = 2
        self.assertEqual(prob004.find_missing_int_naive([234, 0, 1]), expected)
        self.assertEqual(prob004.find_missing_int_fast([234, 0, 1]), expected)

if __name__ == '__main__':
    unittest.main()
