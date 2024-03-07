import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

temp = []
result = 0

for i in range(1, n):
    for j in range(n):
        if j + i <= n:
            temp.append(sum(arr[j : j + i]))
    # ans.append(max(temp))
    # print(temp)
    if max(temp) > result:
        result = max(temp)
    # print(result)
    temp = []

print(result)
