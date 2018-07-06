def sums_to_k(l, k):
    "Given a list of numbers l and a number k, return whether any two numbers from the list add up to k."
    wanted = set()
    for n in l:
        if n in wanted:
            return True
        wanted.add(k - n)
    return False