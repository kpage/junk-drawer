
import unittest, prob014, math

class TestProb014(unittest.TestCase):
    def test_prob014(self):
        actual = prob014.estimate_pi(10000000)
        print(f"Estimate of pi is: {actual}")
        error_margin = 0.001
        self.assertTrue(actual > (math.pi - error_margin) and actual < (math.pi + error_margin))

if __name__ == '__main__':
    unittest.main()
