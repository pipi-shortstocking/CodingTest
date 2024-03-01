import sys

input = sys.stdin.readline

dp = [[0 for _ in range(9)] for _ in range(101)]

dp[1] = [9, 0, 0, 0, 0, 0, 0, 0, 0]
dp[2] = [2, 2, 2, 2, 2, 2, 2, 2, 1]

for i in range(3, 101):
    dp[i][0] = ((i - 2) + dp[i - 1][1]) % 1000000000
    for j in range(1, 8):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000
    dp[i][8] = dp[i - 1][7] % 1000000000

n = int(input())

print(sum(dp[n]) % 1000000000)
