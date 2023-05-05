import sys

input = sys.stdin.readline

n, m = map(int, input().split())
sets = []
arr = []
count = 0

for _ in range(n):
    sets.append(input().rstrip())

for _ in range(m):
    arr.append(input().rstrip())

# print(arr.count(sets[1]))

for i in range(n):
    count += arr.count(sets[i])

print(count)
