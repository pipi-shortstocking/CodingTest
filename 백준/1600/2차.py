from collections import deque

h_dx = [-2, -2, -1, -1, 1, 1, 2, 2]
h_dy = [-1, 1, -2, 2, -2, 2, -1, 1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
via = [[[0 for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]


queue = deque([(0, 0, 0)])
via[0][0][0] = 1

ans = 20000
while queue:
    x, y, cnt = queue.popleft()

    if (x, y) == (h - 1, w - 1):
        if ans > via[x][y][cnt]:
            ans = via[x][y][cnt]
        break

    if cnt < k:  # 말의 움직임을 먼저 수행했을 때 시간복잡도가 크게 줄어듦
        for i in range(8):
            nx = x + h_dx[i]
            ny = y + h_dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if via[nx][ny][cnt + 1] == 0 and arr[nx][ny] == 0:
                    via[nx][ny][cnt + 1] = via[x][y][cnt] + 1
                    queue.append((nx, ny, cnt + 1))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w:
            if via[nx][ny][cnt] == 0 and arr[nx][ny] == 0:
                via[nx][ny][cnt] = via[x][y][cnt] + 1
                queue.append((nx, ny, cnt))

if via[h - 1][w - 1].count(0) == k + 1:
    print(-1)
else:
    print(ans - 1)
