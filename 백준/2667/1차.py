from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

queue = deque()
apart = []


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                arr[nx][ny] = 4
                queue.append((nx, ny))
                cnt += 1
    apart.append(cnt + 1)


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            queue.append((i, j))
            arr[i][j] = 4
            bfs()

print(len(apart))
for a in sorted(apart):  # 오름차순 주의!
    print(a)

# print(arr)
