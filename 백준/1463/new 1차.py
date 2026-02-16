import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)

for i in range(2, n + 1):
    # -1
    dp[i] = dp[i-1] + 1

    # // 2
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1) # -1 연산과 // 2 연산 중 최솟값 저장

    # // 3
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])