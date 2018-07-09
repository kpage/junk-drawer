def find_missing_int_naive(arr):
    arr.sort()
    positive_ints = (x for x in arr if x > 0)
    last_seen_int=0
    for x in positive_ints:
        if last_seen_int + 1 != x:
            return last_seen_int + 1
        last_seen_int = x
    return last_seen_int + 1

# modifies arr.  Uses out-of-band sign information to store state. A minus sign at array index n indicates presence 
# of positive int n+1 somewhere in the array.
def find_missing_int_fast(arr):
    # clear existing negatives to 0
    for i, x in enumerate(arr):
        arr[i] = max(x, 0)

    max_x = len(arr)
    for x in arr:
        if x != 0 and x != 'NEG_0' and x <= max_x:
            x = abs(x)
            if (arr[x-1] == 0):
                arr[x-1] = 'NEG_0' # need to set to special value because 0 has no sign
            else:
                arr[x-1] = -1*arr[x-1]

    # return index + 1 of first non-negative item, as this indicates absence of this int
    for i, x in enumerate(arr):
        if x != 'NEG_0' and x >= 0:
            return i + 1

    # if we haven't found anything yet, the given arr was a complete sequence and so the
    # next largest integer is considered the missing int
    return len(arr) + 1
