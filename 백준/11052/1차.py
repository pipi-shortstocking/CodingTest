import sys

input = sys.stdin.readline

n = int(input())
p_arr = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = p_arr[i]
    for j in range(1, i):
        dp[i] = max(dp[i], dp[i - j] + p_arr[j])
        # print(dp)

print(dp[-1])
