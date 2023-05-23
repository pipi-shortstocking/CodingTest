# pypy3로 통과

import sys, math

input = sys.stdin.readline


def pri(x):
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True


cnt = 0

while True:
    n = int(input())

    if n == 0:
        break

    for i in range(n + 1, 2 * n + 1):
        if pri(i):
            cnt += 1
    print(cnt)
    cnt = 0
