def solution(triangle):
    height = len(triangle)
    dp = [[0] * height for _ in range(height)]
    dp[0][0] = triangle[0][0]

    for i in range(1, height):
        for j in range(i + 1):
            temp = dp[i-1][j-1] if j > 0 else 0 # 파이썬의 삼항연산자, j = 0일 경우 -1이 들어감
            dp[i][j] = triangle[i][j] + max(temp, dp[i-1][j])

            # dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])

    return max(dp[-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))