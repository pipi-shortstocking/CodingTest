from collections import deque

## 인접 리스트형
def bfs_list(start, graph, N):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)

## 격자형
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_grid(start_x, start_y, graph):
    n = len(graph) # 행
    m = len(graph[0]) # 열

    queue = deque()
    queue.append((start_x, start_y))
    visited = [[False] * m for _ in range(n)]
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

        # 범위 벗어나면 무시
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 이미 방문했으면 무시
        if visited[nx][ny]:
            continue
        # 벽이면 무시 (0이 벽인 경우)
        if graph[nx][ny] == 0:
            continue

        visited[nx][ny] = True
        queue.append((nx, ny))