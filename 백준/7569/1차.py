from collections import deque
import sys

input = sys.stdin.readline

m, n, h = map(int, input().split())
box = []
queue = deque()

# 전후상하좌우
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


# 3차원 배열 입력 방법
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
        for k in range(m):
            # 처음에 1인 정보를 전부 넣어야 함
            if temp[j][k] == 1:
                queue.append((i, j, k))
    box.append(temp)

while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= n or nz >= m:
            continue
        if box[nx][ny][nz] == 0:
            box[nx][ny][nz] = box[x][y][z] + 1
            queue.append((nx, ny, nz))

max = box[0][0][0]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print(-1)
                exit(0)
            if max < box[i][j][k]:
                max = box[i][j][k]

print(max - 1)
