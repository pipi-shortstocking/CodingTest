from itertools import product

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

ans = list(product(arr, repeat=m))

for a in ans:
    print(*a)
