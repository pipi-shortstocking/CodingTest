import sys, math

input = sys.stdin.readline


# 소수 판별
def pri(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def out(n):
    for num in range(2, n):
        if pri(num) and pri(n - num):
            print(str(n) + " = " + str(num) + " + " + str(n - num))
            return


while True:
    n = int(input())

    out(n)

    if n == 0:
        break
