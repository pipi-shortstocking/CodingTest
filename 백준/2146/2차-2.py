from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def marking(i, j, mark):
    queue = deque()
    queue.append((i, j))
    arr[i][j] = mark
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    arr[nx][ny] = mark
                    visited[nx][ny] = True
                    queue.append((nx, ny))


# 섬을 나누는 과정
# 0이 아닌 좌표 발견 시, 그 좌표와 연결된 값을 전부 mark로 변경
mark = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:  # 섬이고, 아직 방문한 적 없음
            marking(i, j, mark)
            mark += 1


def getDist(i, j, now):  # now는 현재 위치값
    queue = deque()
    queue.append((i, j, 0))

    while queue:
        x, y, cnt = queue.popleft()

        if arr[x][y] != 0 and arr[x][y] != now:
            return cnt

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] != now:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cnt + 1))
    return 2000


# 각 좌표에서 가장 가까운 섬의 거리를 구함
ans = 2000
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:  # 바다일 경우
            visited = [[False] * n for _ in range(n)]
            ans = min(ans, getDist(i, j, arr[i][j]))  # 최솟값 갱신
