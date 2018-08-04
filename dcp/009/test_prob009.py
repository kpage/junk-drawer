
import unittest, prob009

class TestProb009(unittest.TestCase):
    def test_prob009_given1(self):
        expected = 13
        actual = prob009.largest_non_adj_sum([2, 4, 6, 2, 5])
        self.assertEqual(actual, expected)

    def test_prob009_given2(self):
        expected = 10
        actual = prob009.largest_non_adj_sum([5, 1, 1, 5])
        self.assertEqual(actual, expected)

    def test_prob009_odds_oddlength(self):
        expected = 6
        actual = prob009.largest_non_adj_sum([2, 1, 2, 1, 2])
        self.assertEqual(actual, expected)

    def test_prob009_odds_evenlength(self):
        expected = 4
        actual = prob009.largest_non_adj_sum([2, 1, 2, 1])
        self.assertEqual(actual, expected)

    def test_prob009_evens_evenlength(self):
        expected = 4
        actual = prob009.largest_non_adj_sum([1, 2, 1, 2])
        self.assertEqual(actual, expected)

    def test_prob009_evens_oddlength(self):
        expected = 4
        actual = prob009.largest_non_adj_sum([1, 2, 1, 2, 1])
        self.assertEqual(actual, expected)

    def test_prob009_odds_evenoutlier(self):
        expected = 8
        actual = prob009.largest_non_adj_sum([2, 6, 2, 1, 2])
        self.assertEqual(actual, expected)

    def test_prob009_evens_oddoutlier(self):
        expected = 5
        actual = prob009.largest_non_adj_sum([1, 2, 4, 2])
        self.assertEqual(actual, expected)

    def test_prob009_odds_oddlength_negative(self):
        expected = 4
        actual = prob009.largest_non_adj_sum([2, 1, 2, 1, -1])
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
