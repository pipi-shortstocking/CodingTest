from itertools import product

n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = sorted(set(list(product(arr, repeat=m))))

for a in ans:
    print(*a)
