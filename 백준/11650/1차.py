import sys
input = sys.stdin.readline

arr = []

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort()

print(arr)
