import sys

input = sys.stdin.readline

t = int(input())
dp = [[0, 0, 0] for _ in range(100001)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for _ in range(t):
    n = int(input())

    for i in range(4, n + 1):
        for j in range(1, 3):
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 1000000009
            dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % 1000000009
            dp[i][2] = (dp[i - 3][1] + dp[i - 3][0]) % 1000000009

    print(sum(dp[n]))
