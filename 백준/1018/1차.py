import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
count = []

for _ in range(n):
    board.append(input().rstrip())

# print(board[0])
# print(type(board[0])) # str

for i in range(n - 7):
    for j in range(m - 7):  # row, col 탐색 시, 제한을 정해줘야 배열 탈출 X -> 즉, 8x8 보드로 제한해줌
        index1, index2 = 0, 0

        for row in range(i, i + 8):
            for col in range(j, j + 8):
                if (row + col) % 2 == 0:  # 짝수
                    if board[row][col] != "W":
                        index1 += 1
                    if board[row][col] != "B":
                        index2 += 1
                else:  # 홀수
                    if board[row][col] != "B":
                        index1 += 1
                    if board[row][col] != "W":
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))
