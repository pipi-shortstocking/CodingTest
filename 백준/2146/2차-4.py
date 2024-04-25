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
                    temp.append((x,y,0))
    edge.append(set(temp))

mark = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not via[i][j]:
            island(i,j)
            mark += 1

ans = 2000
for i in range(mark-1):
    queue = deque(edge[i])
    visited = [[False for _ in range(n)] for _ in range(n)]

    while queue:
        x, y, cnt = queue.popleft()
        visited[x][y] = True

        if arr[x][y] != 0 and arr[x][y] != i + 1:
            ans = min(ans, cnt)
        
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] != i+1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny, cnt + 1))

print(ans-1)