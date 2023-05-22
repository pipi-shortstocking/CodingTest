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


m, n = map(int, input().split())

# for i in range(m, n + 1):
#     if pri(i) == True:
#         print(i)

for i in range(m, n + 1):
    # print(i, pri(i))
    if pri(i) == True:
        print(i)
