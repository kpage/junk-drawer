
import unittest, prob016

class TestProb016(unittest.TestCase):
    def test_prob016_overflow(self):
        items = range(10)
        expected = [7, 8, 9]
        log = prob016.OrderLog(3)
        for x in items:
            log.record(x)
        actual = [log.get_last(2), log.get_last(1), log.get_last(0)]
        self.assertEqual(actual, expected)

    def test_prob016_unfilled_buffer(self):
        items = [1, 2, 3]
        expected = 2
        log = prob016.OrderLog(10)
        for x in items:
            log.record(x)
        actual = log.get_last(1)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
