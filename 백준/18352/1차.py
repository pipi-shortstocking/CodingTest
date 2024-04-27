from collections import deque

n, m, k, x = map(int, input().split())
# 도시 수, 도로 수, 최단 거리, 출발 도시

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


via = [[0, 0] for _ in range(n + 1)]

ans = []

queue = deque()
queue.append((x, 0))
via[x] = [1, 0]
while queue:
    cur, dis = queue.popleft()

    if dis == k:
        ans.append(cur)

    for i in graph[cur]:
        if via[i][0] == 0:
            queue.append((i, dis + 1))
            via[i] = [1, dis + 1]

    # print(queue)
    # print(via)

if ans:
    for i in sorted(ans):
        print(i)
else:
    print(-1)
