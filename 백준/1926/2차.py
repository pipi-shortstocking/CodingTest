import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())  # 세로, 가로
paints = []
for _ in range(n):
    paints.append(list(map(int, input().split())))

queue = deque()
via = [[False for _ in range(m)] for _ in range(n)]  # 방문 기록

width_max = 0
width = 1
cnt = 0

# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if paints[i][j] == 1 and via[i][j] == False:
            via[i][j] = True
            queue.append((i, j))
            width = 1
            cnt += 1

            while queue:
                x, y = queue.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    # 공간을 벗어나면 무시
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    # 방문한 적이 있고, 그림이 없는 경우
                    if via[nx][ny] or paints[nx][ny] != 1:
                        continue
                    width += 1
                    via[nx][ny] = True
                    queue.append((nx, ny))

        if width_max < width:
            width_max = width

print(cnt)
print(width_max)
