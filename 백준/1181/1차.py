import sys

input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    arr.append(str(input().rstrip()))

arr.sort()  # 알파벳 순서

for i in range(n):
    min_index = i
    min = len(arr[i])
    for j in range(i + 1, n):
        if min > len(arr[j]):
            min = len(arr[j])
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)
