import sys
input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    age, name = map(str, input().rstrip().split())
    age_int = int(age)
    arr.append((age_int, name))

for i in range(n):
    for j in range(i, 0, -1):
        if arr[j][0] < arr[j-1][0]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

for k in range(n):
    print(arr[k][0], arr[k][1])
