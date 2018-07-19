
import unittest
from prob008 import count_unival_subtrees, Node

class TestProb008(unittest.TestCase):
    def test_prob008_given(self):
        #    0
        #   / \
        #  1   0
        #     / \
        #    1   0
        #   / \
        #  1   1
        expected = 5
        root = Node(0, Node(1), 
                       Node(0, Node(1, Node(1), 
                                       Node(1)),
                               Node(0)))
        actual = count_unival_subtrees(root)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
