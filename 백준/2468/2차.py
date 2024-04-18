from collections import deque

n = int(input())
area = []
scale = set()  # area의 높이 기록 (중복 X)

for _ in range(n):
    temp = list(map(int, input().split()))
    scale.update(temp)
    area.append(temp)

scale = list(scale)
if len(scale) > 1:
    scale.pop()
else:
    print(1)
    exit()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

safe = []


def bfs(queue, water):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if area[nx][ny] > water and via[nx][ny] == 0:
                    via[nx][ny] = 1
                    queue.append((nx, ny))


for water in scale:
    queue = deque()
    via = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > water and via[i][j] == 0:
                queue.append((i, j))
                via[i][j] = 1
                bfs(queue, water)
                cnt += 1
    safe.append(cnt)

print(max(safe))
