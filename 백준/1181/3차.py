import sys
input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    arr.append(str(input().rstrip()))

arr_sort = set(arr)  # 중복제거
arr = list(arr_sort)
arr.sort()
arr.sort(key=len)

for i in range(len(arr)):
    print(arr[i])
