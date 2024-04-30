import sys

sys.setrecursionlimit(10**8)


def cal(a, b, c):
    if b == 1:
        return a % c

    val = cal(a, b // 2, c)
    val = val * val % c

    if b % 2 == 0:
        return val
    else:
        return val * a % c


a, b, c = map(int, input().split())
print(cal(a, b, c))
