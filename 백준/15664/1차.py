from itertools import combinations

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

ans = sorted(set(list(combinations(arr, m))))

for a in ans:
    print(*a)
