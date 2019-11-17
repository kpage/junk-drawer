import random

# s is a stream
def sample(s):
    sampled_el = None
    for i, e in enumerate(s):
        if sampled_el is None or random.randint(1, i + 1) == 1:
            sampled_el = e
    return sampled_el