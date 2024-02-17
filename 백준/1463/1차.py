import sys

input = sys.stdin.readline

n = int(input())


def three(n):
    return n // 3


def two(n):
    return n // 2


def one(n):
    return n - 1


cnt = 0

while True:
    print(n, cnt)
    if n % 2 != 0 and n % 3 != 0:
        n = one(n)
        cnt += 1
        print("-1")
    if n % 2 == 0:
        n = two(n)
        cnt += 1
        print("//2")
    if n % 3 == 0:
        n = three(n)
        cnt += 1
        print("//3")

    if n == 1:
        break

print(cnt)
