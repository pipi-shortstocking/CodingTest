import sys
input = sys.stdin.readline

arr = []

for i in range(9):
    height = int(input())

    arr.append(height)
    arr.sort()

num = sum(arr) - 100

for i in range(9):
    for j in arr[i+1:]:
        if arr[i] + j == num:
            if arr[i] == j:
                continue
            arr.remove(arr[i])
            arr.remove(j)
            break

for i in arr:
    print(i)