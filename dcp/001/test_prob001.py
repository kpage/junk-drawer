import unittest, prob001

class TestSumsToK(unittest.TestCase):
    def test_sums_to_k_given_example(self):
        l = [10, 15, 3, 7]
        k = 17
        expected = True
        self.assertEqual(prob001.sums_to_k(l, k), expected)

    def test_sums_to_k_list_empty(self):
        l = []
        k = 1
        expected = False
        self.assertEqual(prob001.sums_to_k(l, k), expected)

    def test_sums_to_k_list_single(self):
        l = [1]
        k = 1
        expected = False
        self.assertEqual(prob001.sums_to_k(l, k), expected)

    def test_sums_to_k_simple(self):
        l = [1, 2]
        k = 3
        expected = True
        self.assertEqual(prob001.sums_to_k(l, k), expected)

    def test_sums_to_k_last(self):
        l = [1, 22, 13, 54, 42]
        k = 43
        expected = True
        self.assertEqual(prob001.sums_to_k(l, k), expected)
    
    def test_sums_to_k_negatives(self):
        l = [2, 22, -3, 54, 42]
        k = 39
        expected = True
        self.assertEqual(prob001.sums_to_k(l, k), expected)
    
    def test_sums_to_k_duplicates(self):
        l = [2, 2]
        k = 4
        expected = True
        self.assertEqual(prob001.sums_to_k(l, k), expected)

    def test_sums_to_k_dont_add_with_self(self):
        l = [2, 6, 7, 8]
        k = 4
        expected = False
        self.assertEqual(prob001.sums_to_k(l, k), expected)

if __name__ == '__main__':
    unittest.main()