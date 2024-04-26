from collections import deque

n, k = map(int, input().split())
via = [-1 for _ in range(200001)]

queue = deque()
queue.append(n)
via[n] = 0

while queue:
    x = queue.popleft()

    if x == k:
        break

    if 2 * x < 200001 and via[2 * x] == -1:
        via[2 * x] = via[x]
        # 순간 이동 경우를 먼저 수행하기 위해 큐의 우선순위로 배치
        queue.appendleft(2 * x)

    for nx in [x - 1, x + 1]:
        if 0 <= nx < 200001 and via[nx] == -1:
            via[nx] = via[x] + 1
            queue.append(nx)

print(via[k])
