from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while True:
    l, r, c = map(int, input().split())
    if (l, r, c) == (0, 0, 0):
        exit()

    building = []
    queue = deque()
    flag = True

    for i in range(l):
        temp2 = []
        for j in range(r):
            temp1 = list(map(str, input()))
            for k in range(c):
                if temp1[k] == "S":  # 시작
                    s_x, s_y, s_z = i, j, k
                    queue.append((s_x, s_y, s_z))
                if temp1[k] == "E":  # 출구
                    goal_x, goal_y, goal_z = i, j, k
            temp2.append(temp1)
        building.append(temp2)
        input()
    # print(building)

    building[s_x][s_y][s_z] = 0
    while queue and flag:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if building[nx][ny][nz] == "." or building[nx][ny][nz] == "E":
                    building[nx][ny][nz] = building[x][y][z] + 1
                    queue.append((nx, ny, nz))

            if (nx, ny, nz) == (goal_x, goal_y, goal_z):
                flag = False
                continue

    if not flag:
        print("Escaped in " + str(building[goal_x][goal_y][goal_z]) + " minute(s).")
    else:
        print("Trapped!")
