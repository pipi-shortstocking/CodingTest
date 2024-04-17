from collections import deque

m, n, k = map(int, input().split())
arr = [[-1 for _ in range(n)] for _ in range(m)]
width = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    a, b = m - y1, x1
    if a > 0:
        a -= 1
    c, d = m - y2, x2
    if d > 0:
        d -= 1

    for i in range(c, a + 1):
        for j in range(b, d + 1):
            arr[i][j] = 1


def bfs(queue, cnt):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == -1:
                arr[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    width.append(cnt + 1)


queue = deque()

for i in range(m):
    for j in range(n):
        if arr[i][j] == -1:
            cnt = 0
            queue.append((i, j))
            arr[i][j] = 0
            bfs(queue, cnt)

print(len(width))
print(*sorted(width))
