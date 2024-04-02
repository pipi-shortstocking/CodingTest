import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
orders = list(map(int, input().split()))

arr = deque([i for i in range(1, n + 1)])


def one(arr):
    arr.popleft()
    return arr


def two(arr):
    num = arr.popleft()
    arr.append(num)
    return arr


def three(arr):
    num = arr.pop()
    arr.appendleft(num)
    return arr


cnt = 0

for order in orders:
    while arr[0] != order:
        loc = arr.index(order)  # order의 현재 위치

        if loc <= len(arr) // 2:
            arr = two(arr)
            cnt += 1
            # print(arr)
        else:
            arr = three(arr)
            cnt += 1
            # print(arr)

    arr = one(arr)
    # print(arr)

print(cnt)
