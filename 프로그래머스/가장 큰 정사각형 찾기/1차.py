def solution(board):
    n = len(board)
    m = len(board[0])
    dp = [[0] * m for _ in range(n)]
    max_dp = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                dp[i][j] = 0
            elif i < 1 or j < 1:
                dp[i][j] = board[i][j]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1

    return max_dp * max_dp

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
# board = [[0,0,1,1],[1,1,1,1]]
# board = [[1]]
print(solution(board))