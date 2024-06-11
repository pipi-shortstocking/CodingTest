from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

ans = list(combinations_with_replacement(arr, m))

for a in ans:
    print(*a)
