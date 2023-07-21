import sys

input = sys.stdin.readline

n = int(input())
arr = [1 for i in range(n + 1)]

# print(arr[1:])

for i in range(2, n + 1):
    j = 1
    while i * j <= n:
        if arr[i * j] == 1:
            arr[i * j] = 0
            j += 1
        else:
            arr[i * j] = 1
            j += 1
    # print(arr[1:])

print(arr[1:].count(1))
