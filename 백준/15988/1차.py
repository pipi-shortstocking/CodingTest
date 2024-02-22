import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0, 1, 2, 4] + [0] * (n + 1)
    for i in range(4, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

    print(dp[n] % 1000000009)
