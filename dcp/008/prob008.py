class Node:
    def __init__(self, val, l=None, r=None):
        self.v = val
        self.l = l
        self.r = r

# Computational complexity: O(n) where n is number of nodes in tree
# Max stack depth: O(log(n))
def count_unival_subtrees(root):
    def f(n):
        if n is None:
            return (0, None)
        (lcount, lval) = f(n.l)
        (rcount, rval) = f(n.r)
        is_unival = (n.l is None and n.r is None) or (lval == rval and lval == n.v and lval != 'NOT_UNIVAL')
        return (lcount + rcount + (1 if is_unival else 0), n.v if is_unival else 'NOT_UNIVAL')
    return f(root)[0]