import sys

input = sys.stdin.readline

arr = []

for i in range(9):
    height = int(input())

    arr.append(height)
    arr.sort()

sum = sum(arr)

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if sum - arr[i] - arr[j] == 100:
            for k in range(len(arr)):
                if k == i or k == j:  # arr[i], arr[j] 값을 제외해야 함
                    continue
                else:
                    print(arr[k])
            exit()
