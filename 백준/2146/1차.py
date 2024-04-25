from collections import deque

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

queue1 = deque()
edge = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

edge = []


def findisland():
    temp = []
    while queue1:
        x, y = queue1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1 and via[nx][ny][0] == 0:
                    queue1.append((nx, ny))
                    via[nx][ny] = [1, start]
                if arr[nx][ny] == 0 and via[x][y][1] == start:
                    temp.append((x, y))
    edge.append(list(set(temp)))


via = [[[0] * 2 for _ in range(n)] for _ in range(n)]
start = 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and via[i][j][0] == 0:
            queue1.append((i, j))
            findisland()
            start += 1

cnt = []

for i in range(start - 1):
    queue2 = deque(edge[i])
    dis = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    while queue2:
        x, y = queue2.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < n and 0 <= ny < n:
                if via[nx][ny][0] == 1 and via[nx][ny][1] != i + 1:
                    cnt.append(dis[x][y])

                if (
                    via[nx][ny][0] == 0
                    and via[nx][ny][1] != i + 1
                    and not visited[nx][ny]
                ):
                    queue2.append((nx, ny))
                    dis[nx][ny] = dis[x][y] + 1
                    visited[nx][ny] = True
    # print(visited)
    # print(dis)
    # print(cnt)

print(min(cnt))
