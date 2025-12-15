from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    dist[0][0] = 1

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    
    if visited[n-1][m-1] == False:
        answer = -1
    elif visited[n-1][m-1] == True:
        answer = dist[n-1][m-1]

    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
print()
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))