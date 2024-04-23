# pypy3로 통과
# python3로 시간 초과

from collections import deque

n, m = map(int, input().split())
queue1 = deque()
arr = []

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] > 0:
            queue1.append((i, j, 1))
    arr.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs1(yr_check, via, flag):
    while queue1 and flag:
        x, y, year = queue1.popleft()
        if yr_check != year:
            flag = False
            queue1.appendleft((x, y, year))
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and arr[x][y] > 0:  # 바다일 경우
                    if not via[nx][ny]:  # 바다인 곳에 직전에 방문한 곳이 아닐 경우
                        arr[x][y] -= 1
                        via[x][y] = True  # 방문 표시
            if i == 3 and arr[x][y] > 0:  # 4면을 모두 확인한 후
                queue1.append((x, y, year + 1))


def bfs2(via):
    while queue2:
        x, y = queue2.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] != 0 and not via[nx][ny]:
                    queue2.append((nx, ny))
                    via[nx][ny] = True


yr_check = 1
while True:
    via1 = [[False for _ in range(m)] for _ in range(n)]
    # yr_check = i
    flag = True
    bfs1(yr_check, via1, flag)

    cnt = 0
    via2 = [[False for _ in range(m)] for _ in range(n)]
    zero_cnt = 0
    for j in range(n):
        for k in range(m):
            queue2 = deque()
            if arr[j][k] != 0 and not via2[j][k]:
                queue2.append((j, k))
                via2[j][k] = True
                bfs2(via2)
                cnt += 1
            elif arr[j][k] == 0:
                zero_cnt += 1

    if zero_cnt == n * m:
        print(0)
        exit()
    elif cnt >= 2:
        print(yr_check)
        exit()
    yr_check += 1
