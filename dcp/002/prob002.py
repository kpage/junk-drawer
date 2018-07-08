import operator
from functools import reduce

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def calc_with_division(arr):
    return list(prod(arr) // x for x in arr)

def calc_no_division(arr):
    # This may be inefficient in python as + creates a new list each time
    accumer = lambda accum, next: accum + [(next * accum[-1])]
    # Calc cumulative product from left to right and right to left
    ltor = reduce(accumer, arr, [1]) # Seed both lists of cumulative products with [1]
    rtol = reduce(accumer, arr[::-1], [1])[::-1]
    # Shift the product lists to exclude the "current" factor and multiply pairwise
    shifted_tuples = zip(ltor[:-1], rtol[1:len(rtol)])
    return list(x[0] * x[1] for x in shifted_tuples)