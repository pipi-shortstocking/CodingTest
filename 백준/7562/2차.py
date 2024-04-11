import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = int(input())
    board = [[0 for _ in range(l)]for _ in range(l)]
    start_x, start_y = map(int,input().split()) # 현재 있는 칸
    ans_x, ans_y = map(int,input().split()) # 목적지

    if (start_x, start_y) == (ans_x, ans_y):
        print(0)
        continue  

    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [-1,1,-2,2,-2,2,-1,1]
    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x,y = queue.popleft()
        
        # 시간 초과에 유의
        # 끝까지 구하지 않더라도, 목적지의 값이 정해졌다면 바로 출력
        if (x,y) == (ans_x,ans_y):
            print(board[x][y])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))
