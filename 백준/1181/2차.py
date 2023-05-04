import sys
input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    arr.append(str(input().rstrip()))

arr.sort()

for i in range(n):
    for j in range(i, 0, -1):
        if len(arr[j]) < len(arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

print(arr)
