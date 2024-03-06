import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
dp_arr = [[num] for num in a]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            if dp[i] < dp[j] + 1:
                dp_arr[i].append(a[j])

            dp[i] = max(dp[i], dp[j] + 1)

max_len = max(dp)
max_idx = dp.index(max_len)
arr = dp_arr[max_idx]
arr.sort()

print(max_len)
print(*arr)
