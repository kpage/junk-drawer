a = set(input().split())
num_tests = int(input())
print(all(a > set(input().split()) for _ in range(num_tests)))