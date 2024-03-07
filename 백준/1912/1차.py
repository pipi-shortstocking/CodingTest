import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = []

for i in range(1, n):
    for j in range(n):
        if j + i <= n:
            # print(j, j + i)
            # ans.append(arr[j : j + i])
            ans.append(sum(arr[j : j + i]))

print(max(ans))
