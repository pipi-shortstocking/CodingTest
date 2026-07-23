def solution(land):
    N = len(land)
    dp = [[0] * 4 for _ in range(N)]
    dp[0] = land[0]

    for i in range(1, N):
        for j in range(4):
            dp[i][j] = land[i][j] + max(dp[i-1][k] for k in range(4) if k != j)

    return max(dp[N-1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))