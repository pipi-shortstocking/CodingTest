import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr_final = arr[0:n]
arr_set = set(arr_final)
count = 0
arr_count = []

for i in range(len(arr_final)):
    for j in range(len(arr_set)):
        if arr_final[i] > arr_final[j]:
            count += 1
        else:
            continue
    arr_count.append(count)
    count = 0

for i in range(len(arr_count)):
    print(arr_count[i], end=" ")
