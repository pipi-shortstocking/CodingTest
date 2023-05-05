import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr_final = arr[0:n]
arr_final = sorted(list(set(arr_final)))
count = {}

for i in range(len(arr_final)):
    count[arr_final[i]] = i

for i in arr:
    print(count[i], end=" ")
