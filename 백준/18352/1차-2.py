from collections import deque

n, m, k, x = map(int, input().split())
# 도시 수, 도로 수, 최단 거리, 출발 도시

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dis = [-1 for _ in range(n + 1)]
dis[x] = 0

queue = deque()
queue.append(x)
while queue:
    cur = queue.popleft()

    for i in graph[cur]:
        if dis[i] == -1:
            dis[i] = dis[cur] + 1
            queue.append(i)

ans = []
for i in range(1, n + 1):
    if dis[i] == k:
        ans.append(i)

if ans:
    for i in sorted(ans):
        print(i)
else:
    print(-1)
