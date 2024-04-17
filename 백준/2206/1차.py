from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

queue = deque()
queue.append((0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag1 = False
flag2 = False

while queue:
    x, y = queue.popleft()

    if flag1:
        flag2 = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m or (nx == 0 and ny == 0):
            continue

        if arr[nx][ny] == 0:
            arr[nx][ny] = arr[x][y] + 1
            queue.append((nx, ny))
        if arr[nx][ny] == 1 and (not flag1 or not flag2):
            arr[nx][ny] = arr[x][y] + 1
            queue.append((nx, ny))
            flag1 = True

if arr[n - 1][m - 1] != 0:
    print(arr[n - 1][m - 1] + 1)
else:
    print(-1)

print(arr)
