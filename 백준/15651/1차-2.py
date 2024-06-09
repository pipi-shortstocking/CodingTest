from itertools import product

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

ans = list(product(arr, repeat=m))

for a in ans:
    print(*a)
