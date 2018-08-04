# Dynamic programming solution
def largest_non_adj_sum(arr):
    # incl: max sum including the previous element
    # excl: max sum excluding the previous element
    incl, excl = 0, 0
    for x in arr:
        incl, excl = max(excl, excl+x), max(incl, excl)
    return max(incl, excl)

