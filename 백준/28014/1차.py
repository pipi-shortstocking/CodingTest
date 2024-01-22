import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

for i in range(0, n - 1):
    if arr[i] > arr[i + 1]:
        n -= 1

print(n)
