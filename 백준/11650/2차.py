import sys
input = sys.stdin.readline

arr = []

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort()

for j in range(len(arr)):
    for k in range(2):
        print(arr[j][k], end=' ')
    print()
