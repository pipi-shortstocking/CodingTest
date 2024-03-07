import sys, math

input = sys.stdin.readline

n = int(input())
dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        # print(dp[i], dp[i - j**2] + 1, min(dp[i], dp[i - j**2] + 1))
        dp[i] = min(dp[i], dp[i - j**2] + 1)
        # print(dp)

print(dp[n])
