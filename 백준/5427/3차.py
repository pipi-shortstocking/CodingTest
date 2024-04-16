from collections import deque

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    board = []
    via_f = [[-1 for _ in range(w)] for _ in range(h)]
    via_s = [[-1 for _ in range(w)] for _ in range(h)]
    f_queue = deque()
    s_queue = deque()
    flag = False

    for i in range(h):
        temp = list(map(str, input()))
        for j in range(w):
            if temp[j] == "@":  # 상근 위치
                s_queue.append((i, j))
                via_s[i][j] = 0
            if temp[j] == "*":  # 불 위치
                f_queue.append((i, j))
                via_f[i][j] = 0
        board.append(temp)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 불
    while f_queue:
        x, y = f_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if via_f[nx][ny] == -1 and board[nx][ny] != "#":
                    via_f[nx][ny] = via_f[x][y] + 1
                    f_queue.append((nx, ny))

    while s_queue:
        x, y = s_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                # print(via_s[x][y] + 1)
                # exit()  # 무조건 프로그램이 끝남
                flag = True
                # print(x,y, ",", nx,ny)
                ans = via_s[x][y] + 1
                s_queue = deque() # 큐 초기화
                continue
            # if via_s[nx][ny] == -1 and board[nx][ny] != "#" and board[nx][ny] != "*":
            if via_s[nx][ny] == -1 and board[nx][ny] == ".":
                if via_f[nx][ny] == -1 or via_s[x][y] + 1 < via_f[nx][ny]:
                    via_s[nx][ny] = via_s[x][y] + 1
                    s_queue.append((nx, ny))

    if flag:
        print(ans)
    else:
        print("IMPOSSIBLE")

    # print(via_f)
    # print(via_s)