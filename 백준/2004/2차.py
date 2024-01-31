import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def cnt(i, j):  # j에는 2 또는 5
    ex_cnt = 0
    while i != 0:
        i = i // j
        ex_cnt += i

    return ex_cnt


two = cnt(n, 2) - cnt((n - m), 2) - cnt(m, 2)
five = cnt(n, 5) - cnt((n - m), 5) - cnt(m, 5)

print(min(two, five))
