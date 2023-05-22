import sys, math

input = sys.stdin.readline


def primary(x):
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):  # 약수는 대칭이므로 중간까지만 구하면 됨
            if x % i == 0:
                return False
        return True


testcase = int(input())

for _ in range(testcase):
    n = int(input())

    while primary(n) == False:
        n += 1
    print(n)
