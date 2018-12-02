# O(n)
def longest_k_substr(s, k):
    if len(s) == 0:
        return 0
    l = 0
    i = 0
    j = 0
    m = {}
    while j < len(s):
        # advance end of window
        #print(f"l: {l}, i: {i}, j: {j}, m: {m}, s[i]: {s[i]}, s[j]: {s[j]}")
        if s[j] in m:
            m[s[j]] = m[s[j]] + 1
        else:
            m[s[j]] = 1
        while i != j and len(m) > k:
            # advance start of window as this window is now invalid
            m[s[i]] = m[s[i]] - 1
            if m[s[i]] == 0:
                m.pop(s[i])
            i += 1
        if len(m) <= k:
            l = max(l, j-i+1)
        j += 1
    return l

# O(n^2)
def longest_k_substr_naive(s, k):
    l = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr = s[i:j]
            if (len(set(substr)) <= k):
                l = max(l, len(substr))
    return l