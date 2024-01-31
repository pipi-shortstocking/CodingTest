import sys

input = sys.stdin.readline

n = int(input())


def cnt(i):
    ex_cnt = 0
    while i != 0:
        i = i // 5
        ex_cnt += i

    return ex_cnt


print(cnt(n))
