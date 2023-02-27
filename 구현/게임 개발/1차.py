n, m = map(int, input().split())  # 세로 크기, 가로 크기
a, b, d = map(int, input().split())  # 시작 위치, 방향(0:북,1:동,2:남,3:서)

# 확인
#check = 1

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
    #print('d:', d)

    nx = a + dx[d]
    ny = b + dy[d]

    # 육지일 경우, 방문한 적 없는 경우
    if arr[nx][ny] == 0 and visited[nx][ny] == 0:
        # print('순서 ', check)
        # print('d는 ', d)
        # print('count는 ', count)
        cnt_turn = 0
        count += 1
        a, b = nx, ny
        visited[a][b] = 1
        #check += 1
    else:
        # print('순서 ', check)
        # print('d는 ', d)
        # print('count는 ', count)
        cnt_turn += 1
        #check += 1
        #print('count_turn:', cnt_turn)

    if cnt_turn == 4:
        break

print(count)
