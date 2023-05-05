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

for i in range(m):
    for j in range(n):
        if arr[i] == sets[j]:
            count += 1

print(count)
