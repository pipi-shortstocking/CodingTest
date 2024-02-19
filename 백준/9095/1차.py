import sys
input = sys.stdin.readline

t = int(input())
dp = [0,1,2,4] + [0] * 7

for i in range(t):
    n = int(input())
    for j in range(4,n+1):
        dp[j] = dp[j-3] + dp[j-2] + dp[j-1]
    print(dp[n])