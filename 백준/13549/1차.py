from collections import deque

n, k = map(int, input().split())
via = [-1 for _ in range(200001)]
queue = deque()

queue.append(n)
via[n] = 0
cnt = 0

while queue:
    x = queue.popleft()

    if x == k:
        break

    for i in [x + 1, x - 1, 2 * x]:
        if 0 <= i < 200001 and via[i] == -1:
            queue.append(i)
            if i == 2 * x:
                via[i] = via[x]
            else:
                via[i] = via[x] + 1

print(via[k])
