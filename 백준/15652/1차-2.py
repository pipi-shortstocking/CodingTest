from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

ans = list(combinations_with_replacement(arr, m))

for a in ans:
    print(*a)
