from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def burn():
    for _ in range(len(f_queue)):
        x, y = f_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= h and 0 <= ny <= w:
                if board[nx][ny] != "#" and board[nx][ny] != "*":
                    board[nx][ny] = "*"
                    f_queue.append((nx, ny))


def move():
    isgo = False
    for _ in range(len(s_queue)):
        x, y = s_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= h and 0 <= ny <= w:
                if via[nx][ny] == 0 and board[nx][ny] != "#" and board[nx][ny] != "*":
                    isgo = True
                    via[nx][ny] = via[x][y] + 1
                    s_queue.append((nx, ny))
            else:
                return via[nx][ny]
    if not isgo:
        return "IMPOSSIBLE"


t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    board = []
    via = [[0 for _ in range(w)] for _ in range(h)]
    f_queue = deque()
    s_queue = deque()

    for i in range(h):
        board.append(list(map(str, input().rstrip().split())))
        for j in range(w):
            if board[i][j] == "@":  # 시작 위치
                s_queue.append((i, j))
            if board[i][j] == "*":  # 불 위치
                f_queue.append((i, j))

    via[s_queue[0][0]][s_queue[0][1]] = 1

    result = 0
    while True:
        burn()
        result = move()

        if result:
            break

    print(result)
