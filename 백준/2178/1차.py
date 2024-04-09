from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

queue = deque()

# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if maze[nx][ny] == 0:
            continue
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))

print(maze[n - 1][m - 1])
