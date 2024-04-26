from collections import deque

k = int(input())
w, h = map(int, input().split())
arr = []

for _ in range(h):
    arr.append(list(map(int, input().split())))

queue = deque()

h_dx = [-2, -2, -1, -1, 1, 1, 2, 2]
h_dy = [-1, 1, -2, 2, -2, 2, -1, 1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue.append((0, 0, 0))
arr[0][0] = -1
while queue:
    x, y, cnt = queue.popleft()

    if cnt < k:
        for i in range(8):
            nx = x + h_dx[i]
            ny = y + h_dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.appendleft((nx, ny, cnt + 1))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w:
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.appendleft((nx, ny, cnt))

print(arr)
if arr[h - 1][w - 1] == 0:
    print(-1)
else:
    print(arr[h - 1][w - 1] + 1)
