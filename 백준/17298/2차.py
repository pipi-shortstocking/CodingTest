import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = []

for i in range(n):
    result = []
    for j in arr[i + 1 :]:
        if arr[i] < j:
            result.append(j)
    if result:
        ans.append(result[0])
    else:
        ans.append(-1)

for j in ans:
    print(j, end=" ")
