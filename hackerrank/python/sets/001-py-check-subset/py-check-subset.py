num_tests = int(input())
for x in range(num_tests):
    input() # Num items in set A, don't care
    a = set(input().split())
    input() # Num items in set B, don't care
    b = set(input().split())
    print(a.issubset(b))