# rotate 함수 사용(로직 동일) -> 시간 및 메모리가 약간 향상됨

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
orders = list(map(int, input().split()))

arr = deque([i for i in range(1, n + 1)])
cnt = 0

for order in orders:
    while arr[0] != order:
        loc = arr.index(order)

        if loc <= len(arr) // 2:
            arr.rotate(-1)
            cnt += 1
        else:
            arr.rotate(1)
            cnt += 1

    arr.popleft()

print(cnt)
