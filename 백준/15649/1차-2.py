from itertools import permutations

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

ans = list(permutations(arr, m))

for a in ans:
    print(*a)
