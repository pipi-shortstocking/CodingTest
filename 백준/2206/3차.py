from collections import deque

n, m = map(int, input().split())
arr = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    arr.append(list(map(int, input())))

queue = deque()

via = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
# via[x][y][0] : 안 부순 경로
# via[x][y][1] : 부순 경로
flag = True

queue.append((0, 0, 0))
while queue and flag:
    x, y, check = queue.popleft()

    if (x, y) == (n - 1, m - 1):
        flag = False
        ans = via[x][y][check]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            # 벽이 아니고 방문한 기록이 없을 때
            if arr[nx][ny] == 0 and via[nx][ny][check] == 0:
                via[nx][ny][check] = via[x][y][check] + 1
                queue.append((nx, ny, check))
            # 벽인데, 벽을 부순 기록이 없을 때
            elif arr[nx][ny] == 1 and check == 0:
                via[nx][ny][1] = via[x][y][0] + 1
                queue.append((nx, ny, 1))

if not flag:
    print(ans + 1)
else:
    print(-1)
