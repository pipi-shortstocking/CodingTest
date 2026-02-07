def solution(triangle):
    n = len(triangle)
    dp = [[0 for _ in range(n)] for _ in range(n)] # dp[[0] * (i + 1) for i in range(n)] 가능

    dp[0][0] = triangle[0][0]
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]

    for i in range(2, n):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    return max(dp[n-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
