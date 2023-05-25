import sys, math, itertools

input = sys.stdin.readline


def pri(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0

    pri_arr = [i for i in range(2, n) if pri(i)]

    for i in range(2, n // 2 + 1):
        if i in pri_arr:
            if n - i in pri_arr:
                cnt += 1

    print(cnt)
