import sys

input = sys.stdin.readline

n = int(input())

dp = [[0, 0] for _ in range(91)]

dp[1] = [0, 1]
dp[2] = [1, 0]

for i in range(3, n + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    dp[i][1] = dp[i - 1][0]

    # print(i, dp[i])

print(sum(dp[n]))
