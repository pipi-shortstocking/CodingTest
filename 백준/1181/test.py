import sys
input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    arr.append(str(input().rstrip()))

arr_sort = set(arr)  # 중복제거
arr = list(arr_sort)
arr.sort()

for i in range(len(arr)):
    for j in range(i, 0, -1):
        if len(arr[j]) < len(arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

for i in range(len(arr)):
    print(arr[i])
