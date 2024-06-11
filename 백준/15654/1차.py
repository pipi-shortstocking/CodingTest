from itertools import permutations

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
# arr = list(map(int, input().split()))

# ans = sorted(list(permutations(arr, m)))
ans = list(permutations(arr, m))

for a in ans:
    print(*a)
