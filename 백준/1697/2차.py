import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
via = [-1 for _ in range(100001)]

via[n] = 0
queue.append(n)
while queue:
    x = queue.popleft()

    for i in [x - 1, x + 1, x * 2]:
        nx = i
        if 0 <= nx < 100001 and via[nx] == -1:
            queue.append(nx)
            via[nx] = via[x] + 1

    if x == k:
        break

print(via[k])
