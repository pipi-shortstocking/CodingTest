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
    pri_arr = []
    cnt = 0

    for i in range(2, n):
        if pri(i):
            pri_arr.append(i)

    result = list(itertools.combinations(pri_arr, 2))

    if int(n / 2) in pri_arr:
        cnt += 1

    for j in range(len(result)):
        if sum(result[j]) == n:
            cnt += 1

    print(cnt)
