from functools import lru_cache

# A recursive implementation from the recurrence relation.
#
# Computational complexity is O(2**n), or O(n) with O(n) memory if naively
# memoized.  To decrease memory usage of memoization to constant space or
# O(1), we can also take advantage of the property that the recursive calls
# use the same substring as input only a few times, so we can use a small
# fixed-size memoization cache that quickly discards least recently used
# values.  This is also limited by Python's stack depth of about 1000, so
# will stack overflow for inputs longer than about 300 chars
def calc_num_decodings_recursive(coded):
    # uses cache on internal function so that concurrent calls to the outer
    # function are independently cached
    @lru_cache(maxsize=4)
    def f(s):
        if len(s) == 0:
            return 1
        elif len(s) == 1:
            return 1

        if s[-1] != '0':
            if 10 <= int(s[-2:]) <= 26:
                return f(s[:-1]) + f(s[:-2])
            else:
                return f(s[:-1])
        elif 10 <= int(s[-2:]) <= 26:
            return f(s[:-2])
        else:
            return 0
    return f(coded)

# O(n), constant space, iteratively calculating from the beginning of the string on:
def calc_num_decodings(coded):
    # pc is the number of decodings of the substring up to 2 digits ago
    # cc is the number of decodings of the substring up to 1 digit ago (until last run of the loop)
    # d is the current digit
    # p is the previous digit
    pc = 0
    cc = 1
    p = ''
    for d in coded:
        temp = get_curr_num_decodings(pc, cc, d, p)
        pc, cc, p = cc, temp, d
    return cc

def get_curr_num_decodings(pc, cc, d, p):
    num = 0
    if d != '0': 
        num += cc
    if 10 <= int(p+d) <= 26: 
        num += pc
    return num