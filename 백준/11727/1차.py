import sys
input = sys.stdin.readline

n = int(input())
dp = [0,1,3] + [0] * 998

for i in range(3, n+1):
    dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[n]%10007)