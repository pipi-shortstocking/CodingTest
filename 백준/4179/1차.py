from collections import deque

r, c = map(int, input().split())
arr = []
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

via_f = [[0 for _ in range(r)] for _ in range(c)]
via_j = [[0 for _ in range(r)] for _ in range(c)]

for i in range(c):
    temp = list(map(str, input()))
    for j in range(r):
        if temp[j] == "F":
            queue.append((i, j))
        if temp[j] == "J":
            j_x, j_y = i, j
    arr.append(temp)

# 불
while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= c or ny >= r:
            continue

        if arr[nx][ny] != "#" and via_f[nx][ny] == 0:
            via_f[nx][ny] = via_f[x][y] + 1
            queue.append((nx, ny))

# 지훈
queue.append((j_x, j_y))
while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= c or ny >= r:
            print(via_j[x][y] + 1)
            exit()

        if arr[nx][ny] != "#" and via_j[nx][ny] == 0:
            if via_j[nx][ny] < via_f[nx][ny]:
                via_j[nx][ny] = via_j[x][y] + 1
                queue.append((nx, ny))
print("IMPOSSIBLE")
