import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
graph = []

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
# visited = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().strip())))

def bfs(x,y):
    q = deque()
    q.append((x,y))
    # visited[x][y] = True
    dist[x][y] = 1

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == 0 and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1

bfs(0,0)
print(dist[n-1][m-1])
