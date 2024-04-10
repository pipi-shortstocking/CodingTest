from collections import deque

n = int(input())
paint = []
for _ in range(n):
    paint.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()


def bfs(via, a, b, color):
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= len(paint[0]):
                continue
            if via[nx][ny] == 0 and paint[nx][ny] == color:
                via[nx][ny] = 1
                queue.append((nx, ny))


via1 = [[0 for _ in range(len(paint[0]))] for _ in range(n)]
via2 = [[0 for _ in range(len(paint[0]))] for _ in range(n)]
cnt1 = 0
cnt2 = 0

for color in ["R", "G", "B"]:
    for i in range(n):
        for j in range(len(paint[0])):
            if paint[i][j] == color and via1[i][j] == 0:
                via1[i][j] = 1
                bfs(via1, i, j, color)
                cnt1 += 1

# 방법2) 그림의 초록색을 빨간색으로 교체
for i in range(n):
    for j in range(len(paint[0])):
        if paint[i][j] == "G":
            paint[i][j] = "R"

for color in ["R", "B"]:
    for i in range(n):
        for j in range(len(paint[0])):
            if paint[i][j] == color and via2[i][j] == 0:
                via2[i][j] = 1
                bfs(via2, i, j, color)
                cnt2 += 1

print(cnt1, cnt2)
