import sys

input = sys.stdin.readline

t = int(input())
dp = [1, 2, 4]

for _ in range(t):
    n = int(input())
    for i in range(len(dp), n):
        dp.append((dp[-3] + dp[-2] + dp[-1]) % 1000000009)
    print(dp[n - 1])
