import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x,y):
    graph[x][y] = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                dfs(nx, ny)

t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())

    graph = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    for i in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    
    print(cnt)