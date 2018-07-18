
import unittest, prob007
from timeit import default_timer as timer

class TestProb007(unittest.TestCase):
    def test_prob007_given(self):
        expected = 3
        self.assertEqual(prob007.calc_num_decodings('111'), expected)
        self.assertEqual(prob007.calc_num_decodings_recursive('111'), expected)

    def test_prob007_blank(self):
        expected = 1
        self.assertEqual(prob007.calc_num_decodings(''), expected)
        self.assertEqual(prob007.calc_num_decodings_recursive(''), expected)

    def test_prob007_one_digit_nonzero(self):
        expected = 1
        self.assertEqual(prob007.calc_num_decodings('1'), expected)
        self.assertEqual(prob007.calc_num_decodings_recursive('1'), expected)

    def test_prob007_two_digits_one_decoding(self):
        expected = 1
        self.assertEqual(prob007.calc_num_decodings('10'), expected)
        self.assertEqual(prob007.calc_num_decodings_recursive('10'), expected)

    def test_prob007_two_digits_two_decodings(self):
        expected = 2
        self.assertEqual(prob007.calc_num_decodings('22'), expected)
        self.assertEqual(prob007.calc_num_decodings_recursive('22'), expected)

    def test_prob007_three_digits_one_encoding(self):
        expected = 1
        self.assertEqual(prob007.calc_num_decodings('103'), expected)
        self.assertEqual(prob007.calc_num_decodings_recursive('103'), expected)

    def test_prob007_four_digits_one_encoding(self):
        expected = 1
        self.assertEqual(prob007.calc_num_decodings('1103'), expected)
        self.assertEqual(prob007.calc_num_decodings_recursive('1103'), expected)

    def test_prob007_five_digits_two_encodings(self):
        expected = 2
        self.assertEqual(prob007.calc_num_decodings('11011'), expected)
        self.assertEqual(prob007.calc_num_decodings_recursive('11011'), expected)

    def test_prob007_zero_in_middle(self):
        expected = 6
        self.assertEqual(prob007.calc_num_decodings('1112011'), expected)
        self.assertEqual(prob007.calc_num_decodings_recursive('1112011'), expected)

    def test_prob007_perf(self):
        time_it("Avg time in ms for iterative algorithm: {}", prob007.calc_num_decodings)
        time_it("Avg time in ms for recursive algorithm: {}", prob007.calc_num_decodings_recursive)

def time_it(s, f):
    start = timer()
    n = 300
    for i in range(0, n):
        f('1'*i)
    end = timer()
    print(s.format((end - start) * 1000 / n))

if __name__ == '__main__':
    unittest.main()
