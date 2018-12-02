
import unittest, prob013

class TestProb013(unittest.TestCase):
    def test_prob013_given(self):
        s = "abcba"
        k = 2
        expected = 3
        self.assertEqual(prob013.longest_k_substr(s, k), expected)
        self.assertEqual(prob013.longest_k_substr_naive(s, k), expected)

    def test_prob013_k0(self):
        s = "abcba"
        k = 0
        expected = 0
        self.assertEqual(prob013.longest_k_substr(s, k), expected)
        self.assertEqual(prob013.longest_k_substr_naive(s, k), expected)

    def test_prob013_s_empty(self):
        s = ""
        k = 2
        expected = 0
        self.assertEqual(prob013.longest_k_substr(s, k), expected)
        self.assertEqual(prob013.longest_k_substr_naive(s, k), expected)

    def test_prob013_s_all_one_char(self):
        s = "aaaa"
        k = 2
        expected = 4
        self.assertEqual(prob013.longest_k_substr(s, k), expected)
        self.assertEqual(prob013.longest_k_substr_naive(s, k), expected)
    def test_prob013_s_all_different_chars(self):
        s = "abcd"
        k = 2
        expected = 2
        self.assertEqual(prob013.longest_k_substr(s, k), expected)
        self.assertEqual(prob013.longest_k_substr_naive(s, k), expected)

    def test_prob013_longest_substr_at_end(self):
        s = "aaabbbccccd"
        k = 1
        expected = 4
        self.assertEqual(prob013.longest_k_substr(s, k), expected)
        self.assertEqual(prob013.longest_k_substr_naive(s, k), expected)

    def test_prob013_7(self):
        s = "abbccbbebbccbba"
        k = 3
        expected = 13
        self.assertEqual(prob013.longest_k_substr(s, k), expected)
        self.assertEqual(prob013.longest_k_substr_naive(s, k), expected)

    def test_prob013_8(self):
        s = "abbccbbebbccbbacacacacab"
        k = 3
        expected = 16
        self.assertEqual(prob013.longest_k_substr(s, k), expected)
        self.assertEqual(prob013.longest_k_substr_naive(s, k), expected)

if __name__ == '__main__':
    unittest.main()
