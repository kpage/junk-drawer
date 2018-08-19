def num_unique_steps(step_sizes, n):
    if n == 0: # we've successfully hit all the steps
        return 1
    count = 0
    for s in step_sizes:
        if s <= n:
            count += num_unique_steps(step_sizes, n - s)
    return count