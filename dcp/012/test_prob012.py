
import unittest, prob012

class TestProb012(unittest.TestCase):
    def test_prob012_min(self):
        expected = 1
        actual = prob012.num_unique_steps([1, 2], 1)
        self.assertEqual(actual, expected)

    def test_prob012_min2(self):
        expected = 2
        actual = prob012.num_unique_steps([1, 2], 2)
        self.assertEqual(actual, expected)

    def test_prob012_given(self):
        expected = 5
        actual = prob012.num_unique_steps([1, 2], 4)
        self.assertEqual(actual, expected)

    def test_prob012_given2(self):
        expected = 5
        actual = prob012.num_unique_steps([1, 3, 5], 5)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
