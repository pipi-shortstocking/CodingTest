import sys

sys.setrecursionlimit(10**8)


def hanoi(a, b, n):
    # if n == 1:
    #     print(a, b)
    #     return
    if n == 0:
        return

    hanoi(a, 6 - a - b, n - 1)
    print(a, b)
    hanoi(6 - a - b, b, n - 1)


n = int(input())

print(2**n - 1)
hanoi(1, 3, n)
