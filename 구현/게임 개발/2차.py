n, m = map(int, input().split())  # 세로 크기, 가로 크기
a, b, d = map(int, input().split())  # 시작 위치, 방향(0:북,1:동,2:남,3:서)

arr = []  # 맵
count = 1  # 방문한 칸 수
visited = [[0]*m for _ in range(n)]  # 방문 표시(0으로 초기화)
visited[a][b] = 1  # 현재 있는 곳 방문 표시
cnt_turn = 0

# 북,동,남,서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    arr.append(list(map(int, input().split())))  # 바다(1), 육지(0) 지정


def turn_left():  # 좌회전 함수
    global d

    d -= 1
    if d == -1:
        d = 3


while True:
    turn_left()

    nx = a + dx[d]
    ny = b + dy[d]

    # 육지일 경우, 방문한 적 없는 경우
    if arr[nx][ny] == 0 and visited[nx][ny] == 0:
        cnt_turn = 0
        count += 1
        a, b = nx, ny
        visited[a][b] = 1
    else:
        cnt_turn += 1

    # 네 방향 모두 가봄
    if cnt_turn == 4:
        # 뒤로 이동
        nx = a - dx[d]
        ny = b - dy[d]

        # 뒤로 이동
        if arr[nx][ny] == 0:
            a, b = nx, ny
            cnt_turn = 0
        # 네 방향 모두 바다
        else:
            break

print(count)
