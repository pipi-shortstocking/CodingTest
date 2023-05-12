import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = []

for _ in range(n):
    board.append(input().rstrip())

print(board[0])
print(type(board[0])) # str