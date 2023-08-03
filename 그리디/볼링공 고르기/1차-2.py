import sys

input = sys.stdin.readline

n, m = map(int, input().split())
k = list(map(int, input().split()))

arr = [0] * 11

for i in k:
    arr[i] += 1

result = 0
for i in range(1, m + 1):
    n -= arr[i]
    result += arr[i] * n

print(result)
