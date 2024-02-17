import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 1000001
# dp = [0] * 11

for i in range(2, n + 1):
    # n-1을 1로 만들기 위한 최소 개수 + 1
    dp[i] = dp[i - 1] + 1

    # 2나 3으로 나눠지면, 나눠지고 남은 몫의 경우 연산 + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

# print(dp)
print(dp[n])
