# bfs는 최단 거리를 찾을 때 사용되는 느낌
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
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 주어진 범위를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물인 경우 무시
            if arr[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return arr[n-1][m-1]


# BFS를 수행한 결과 출력
print(bfs(0, 0))
