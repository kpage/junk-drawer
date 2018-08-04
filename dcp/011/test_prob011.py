
import unittest, prob011

class TestProb011(unittest.TestCase):
    def test_prob011_given(self):
        arr = ["dog", "deer", "deal", "cat"]
        expected = ["deer", "deal"]
        actual = prob011.autocomplete_naive(arr, "de")
        self.assertEqual(actual, expected)
        trie = prob011.create_autocomplete_trie(["dog", "deer", "deal"])
        actual = trie.autocomplete("de")
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
