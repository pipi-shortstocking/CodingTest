import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = []
cnt = []

for _ in range(n):
    board.append(input().rstrip())

for i in range(n-7):
    for j in range(m-7): # 8x8로 나눌 square의 시작점 제한
        index1, index2 = 0, 0 # index1은 시작점이 W, index2은 시작점이 B

        for row in range(i, i+8): # 8x8만 순회하기 위한 square 범위 제한
            for col in range(j, j+8):
                if (row + col) % 2 == 0: # 짝수는 시작점과 일치해야 함
                    if board[row][col] != 'W':
                        index1 += 1 # W 시작 체스판 규칙에 맞지 않아, 채색 횟수 +1
                    if board[row][col] != 'B':
                        index2 += 1 # B 시작 체스판 규칙에 맞지 않아, 채색 횟수 +1
                else: # 홀수는 시작점과 달라야 함
                    if board[row][col] != 'B':
                        index1 += 1 # W 시작 체스판 규칙에 맞지 않아, 채색 횟수 +1
                    if board[row][col] != 'W':
                        index2 += 1 # B 시작 체스판 규칙에 맞지 않아, 채색 횟수 +1
        
        cnt.append(min(index1, index2))

print(min(cnt))