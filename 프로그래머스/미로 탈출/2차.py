from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    start_x, start_y = 0, 0
    lever_x, lever_y = 0, 0
    end_x, end_y = 0, 0
    new_maps = []
    for i in range(n):
        m_list = list(maps[i])
        new_maps.append(m_list)

        if 'S' in m_list:
            start_x = i
            start_y = maps[i].index('S')

        if 'L' in m_list:
            lever_x = i
            lever_y = maps[i].index('L')

        if 'E' in m_list:
            end_x = i
            end_y = maps[i].index('E')

    def bfs(start, end):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        queue = deque()
        queue.append(start)
        visited = [[-1] * m for _ in range(n)]
        visited[start[0]][start[1]] = 0

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if visited[nx][ny] == -1 and new_maps[nx][ny] != 'X':
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))

                if nx == end[0] and ny == end[1]:
                    return visited[nx][ny]

        return -1

    route1 = bfs((start_x, start_y), (lever_x, lever_y))
    route2 = bfs((lever_x, lever_y), (end_x, end_y))

    if route1 == -1 or route2 == -1:
        return -1
    else:
        return route1 + route2