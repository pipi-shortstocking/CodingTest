from collections import deque


def bfs(arr, a, b):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = 0


t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                arr[i][j] = 0
                bfs(arr, i, j)
                cnt += 1

    print(cnt)
