def solution(land):
    N = len(land)
    dp = [[0] * 4 for _ in range(N)]
    dp[0] = land[0]

    for i in range(1, N):
        prev = dp[i-1]
        sorted_prev = sorted(prev, reverse=True)
        first, second = sorted_prev[0], sorted_prev[1]
        first_idx = prev.index(first)

        for j in range(4):
            if j == first_idx:
                dp[i][j] = land[i][j] + second
            else:
                dp[i][j] = land[i][j] + first

    return max(dp[N-1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))