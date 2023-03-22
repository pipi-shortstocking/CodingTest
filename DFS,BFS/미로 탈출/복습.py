from collections import deque

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    # 큐에 좌표값 할당
    queue.append((x, y))

    # 큐가 빌 때까지
    while queue:
        # 큐의 맨 아래에 있는 요소 꺼내기
        x, y = queue.popleft()

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로를 벗어났을 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물이 존재하는 경우
            if arr[nx][ny] == 0:
                continue
            # 제대로 된 길인 경우
            if arr[nx][ny] == 1:
                # 다음으로 이동할 곳에 현재 값의 + 1을 하여 움직인 칸 수 저장하기
                arr[nx][ny] = arr[x][y] + 1
                # 큐에 다음 좌표 할당
                queue.append((nx, ny))
    # 종점의 값 반환
    return arr[n-1][m-1]


# 시작 좌표 할당
print(bfs(0, 0))
