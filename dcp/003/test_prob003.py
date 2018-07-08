
import unittest
from prob003 import Node, deserialize, serialize

class TestProb003(unittest.TestCase):
    def test_prob003_given(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        assert deserialize(serialize(node)).left.left.val == 'left.left'

    def test_prob003_escaping(self):
        node = Node('root', Node('left', Node('Node("\'')), Node('right'))
        assert deserialize(serialize(node)).left.left.val == 'Node("\''

if __name__ == '__main__':
    unittest.main()
