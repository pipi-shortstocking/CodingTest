import sys

input = sys.stdin.readline

n, k = map(int, input().split())
mod = 1000000000

dp = [[1 for _ in range(n + 1)] for _ in range(k + 1)]

for i in range(2, k + 1):  # k = 1이면, dp[k][n] = 1
    for j in range(1, n + 1):  # n = 1이면, dp[k][n] = 1
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod

print(dp[k][n])
