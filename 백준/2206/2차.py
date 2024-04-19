from collections import deque

n, m = map(int, input().split())
arr = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    arr.append(list(map(int, input())))

via1 = [[0 for _ in range(m)] for _ in range(n)]  # 벽을 하나도 부시지 않았을 경우


def bfs(arr, via):
    queue = deque()
    queue.append((0, 0))
    ans = 2000

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and via[nx][ny] == 0:
                    via[nx][ny] = via[x][y] + 1
                    queue.append((nx, ny))
    # print("arr : ", arr)
    # print("via : ", via)
    if via[n - 1][m - 1] != 0:
        ans = via[n - 1][m - 1]
    return ans


result = 2000
# 벽을 하나도 부셔보지 않은 경우
if bfs(arr, via1) < result:
    result = bfs(arr, via1)


# 모든 벽을 하나씩 부셔본 후
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            check_i, check_j = i, j
            arr[i][j] = 0  # 벽 하나 부시기

            via2 = [[0 for _ in range(m)] for _ in range(n)]
            if bfs(arr, via2) < result:
                result = bfs(arr, via2)
            arr[check_i][check_j] = 1

if result == 2000:
    print(-1)
else:
    print(result + 1)
