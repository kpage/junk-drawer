
import unittest, prob015
# pip3 install scipy
from scipy import stats

# Probabalistic test: it might fail, but usually it should pass if the sample function is choosing uniformly 
class TestProb015(unittest.TestCase):
    def test_prob015(self):
        ks_acceptable_error = 0.05
        num_trials = 100000
        items = range(1, 20)
        samples = []
        for _ in range(num_trials):
            samples.append(prob015.sample(items))
        (statistic, p) = stats.kstest(samples, 'uniform', args=(min(items), max(items)))
        expected = 1/len(items)
        min_expected = expected * (1 - ks_acceptable_error)
        max_expected = expected * (1 + ks_acceptable_error)
        self.assertTrue(min_expected < statistic and statistic < max_expected, f"Expected K-S statistic {statistic} to be between {min_expected} and {max_expected}")

if __name__ == '__main__':
    unittest.main()
