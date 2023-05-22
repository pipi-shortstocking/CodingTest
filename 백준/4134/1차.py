import sys

input = sys.stdin.readline


def primary(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


testcase = int(input())

for _ in range(testcase):
    n = int(input())
    if primary(n) == True:
        print(n)
    else:
        while primary(n) == False:
            n += 1
        print(n)
