class OrderLog:
    def __init__(self, n):
        self.k = 0
        self.log = [None] * n
    
    # adds the order_id to the log
    def record(self, order_id):
        self.k += 1
        if self.k == len(self.log):
            self.k = 0
        self.log[self.k] = order_id

    # gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
    def get_last(self, i):
        return self.log[self.k-i]