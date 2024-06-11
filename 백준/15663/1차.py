from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = sorted(list(set(permutations(arr, m))))

for a in ans:
    print(*a)
