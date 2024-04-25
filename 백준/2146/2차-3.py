# pypy3 통과
# python3 시간 초과

from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
via = [[False for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

edge = []

def island(i,j):
    queue = deque()
    queue.append((i,j))
    arr[i][j] = mark
    via[i][j] = True

    temp = []

    while queue:
        x,y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1 and not via[nx][ny]:
                    arr[nx][ny] = mark
                    via[nx][ny] = True
                    queue.append((nx,ny))
                if arr[nx][ny] == 0 and arr[x][y] == mark:
                    temp.append((x,y))
    edge.append(set(temp))

mark = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not via[i][j]:
            island(i,j)
            mark += 1

cnt = []
for i in range(mark-1):
    queue = deque(edge[i])
    dis = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] != i + 1 and via[nx][ny]:
                    cnt.append(dis[x][y])
                if not via[nx][ny] and arr[nx][ny] == 0 and not visited[nx][ny]: # 방문한 적 없고, 바다이고, 거리 탐색에서도 간 적 없을 때
                    queue.append((nx,ny))
                    dis[nx][ny] = dis[x][y] + 1
                    visited[nx][ny] = True

print(min(cnt))
