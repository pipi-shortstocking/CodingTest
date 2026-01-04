import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n = int(input())
graph = []
dist = []

for i in range(n):
    graph.append(list(map(int, input().strip())))

def dfs(x,y):
    graph[x][y] = 0
    cnt = 1

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                cnt += dfs(nx, ny)
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dist.append(dfs(i, j))

dist.sort()
print(len(dist))
for num in dist:
    print(num)