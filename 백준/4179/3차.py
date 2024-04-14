from collections import deque

r, c = map(int, input().split())
arr = []
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

via_f = [[-1 for _ in range(c)] for _ in range(r)]
via_j = [[-1 for _ in range(c)] for _ in range(r)]

for i in range(r):
    temp = list(map(str, input()))
    for j in range(c):
        if temp[j] == "F":
            queue.append((i, j))
            via_f[i][j] = 0
        if temp[j] == "J":
            j_x, j_y = i, j
            via_j[i][j] = 0
    arr.append(temp)

# 불
while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue

        if arr[nx][ny] != "#" and via_f[nx][ny] == -1:
            via_f[nx][ny] = via_f[x][y] + 1
            queue.append((nx, ny))

# 지훈
queue.append((j_x, j_y))
while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            print(via_j[x][y] + 1)
            exit()

        if arr[nx][ny] != "#" and via_j[nx][ny] == -1:
            if via_f[nx][ny] == -1 or via_j[x][y] + 1 < via_f[nx][ny]:
                via_j[nx][ny] = via_j[x][y] + 1
                queue.append((nx, ny))

print("IMPOSSIBLE")
