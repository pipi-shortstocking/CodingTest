import sys

input = sys.stdin.readline

n = int(input())

dp = [[0 for _ in range(9)] for _ in range(n + 1)]

dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1]

if n > 1:
    dp[2] = [2, 2, 2, 2, 2, 2, 2, 2, 1]

for i in range(3, n + 1):
    dp[i][0] = ((i - 2) + dp[i - 1][1]) % 1000000000
    for j in range(1, 8):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000
    dp[i][8] = dp[i - 1][7] % 1000000000

print(sum(dp[n]) % 1000000000)
