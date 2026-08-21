def solution(n):
    board = [0 for _ in range(n)]

    def dfs(board, row):
        count = 0

        if row == n: # 끝까지 탐색 완료
            return 1

        for col in range(n):
            board[row] = col

            for i in range(row):
                if board[i] == board[row]: # board에 col 값을 저장하므로 동일하면 세로상 위치
                    break
                if abs(board[i] - board[row]) == row - i:
                    break
            else: # break 없이 for문이 끝나면
                count += dfs(board, row + 1)

        return count

    answer = dfs(board, 0)

    return answer

n = 4
print(solution(n))