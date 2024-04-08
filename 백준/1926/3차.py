import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())  # 세로, 가로
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0  # 방문한 위치는 그림 지우기
    cnt = 1  # 그림 크기

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 공간을 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 그림이 있는 경우
            if graph[nx][ny] == 1:
                cnt += 1
                queue.append((nx, ny))
                graph[nx][ny] = 0  # 방문한 위치는 그림 지우기
    return cnt


paint = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:  # 그림이 그려져 있다면
            paint.append(bfs(graph, i, j))

print(len(paint))
if len(paint) == 0:
    print(0)
else:
    print(max(paint))
