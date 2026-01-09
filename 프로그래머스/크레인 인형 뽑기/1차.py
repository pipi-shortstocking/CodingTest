def solution(board, moves):
    cnt = 0
    stack = []
    n = len(board[0])

    for move in moves:
        for a in range(n):
            if board[a][move-1] != 0:
                doll = board[a][move-1]
                board[a][move-1] = 0

                # print("move = ", move)
                # print("doll = ", doll)

                if len(stack) != 0 and stack[-1] == doll: # if stack and stack[-1] == doll 로 작성 가능
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(doll)

                break
        
        # print("board = ", board)
        # print("stack = ", stack)
    
    return cnt




board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))